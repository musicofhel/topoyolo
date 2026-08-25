# Queue batch-003 — link-forge export, 2026-08-25

Machine-term-filtered export (lesson from batch-002's wrapper-heavy yield):
candidates matched on the atlas's own machine vocabulary (delay embedding,
persistent homology, optimal transport, transfer entropy, stability bounds,
surrogates, chain complexes). Deduped vs batches 001-002 and annotations/.
Dynamics×Matching (dyn-matching group) is the priority cell.
Consume per papers/INGESTION.md (≤3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [dyn-matching] — ANNOTATED as 2510.22002 (promote-on-encounter: already covered as a prose block in by-domain/dynamical_systems.md; block migrated verbatim to annotations/2510.22002.md, pass 19. Queue-group label 'dyn-matching' is a filter artifact — paper instantiates parameterized homology, stability, spectral matching; no optimal-transport matching.)

**Title:** 2510.22002v1

**URL:** file:///7d6f2be1827faa877e1ab6ab4dcfb879cbeae88a7cd78431d10143e9b06da786/2510.22002v1.pdf

**Description:** An introductory guide to Koopman learning that provides a unified account of rigorously convergent data-driven methods for analyzing nonlinear dynamical systems via their linear Koopman operator representations. The paper covers matrix approximations (EDMD/DMD), residual-based error control in finite and infinite dimensions, delay embeddings, generalized Laplace analysis for computing Koopman modes, and state-of-the-art methods for computing continuous spectra and spectral measures. It includes an elementary convergence proof for generalized Laplace analysis applicable to operators with continuous spectra and no spectral gaps.

**Content extract (≤6k chars):**

```
An Introductory Guide to Koopman Learning
Matthew Colbrook * Zlatko Drmaˇ c † Andrew Horning ‡
October 28, 2025
Abstract
Koopman operators provide a linear framework for data-driven analyses of nonlinear dynamical
systems, but their infinite-dimensional nature presents major computational challenges. In this article,
we offer an introductory guide to Koopman learning, emphasizing rigorously convergent data-driven
methods for forecasting and spectral analysis. We provide a unified account of error control via resid-
uals in both finite- and infinite-dimensional settings, an elementary proof of convergence for general-
ized Laplace analysis—a variant of filtered power iteration that works for operators with continuous
spectra and no spectral gaps—and review state-of-the-art approaches for computing continuous spec-
tra and spectral measures. The goal is to provide both newcomers and experts with a clear, structured
overview of reliable data-driven techniques for Koopman spectral analysis.
Keywords: Data-driven dynamics, Koopman operator, Dynamic Mode Decomposition, generalized
Laplace analysis, spectral measures
Contents
1 Introduction 2
1.1 The setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 Matrix approximations of the operator 3
2.1 Finite sections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 Data-driven approximations (a.k.a. EDMD) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.3 Further compressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.4 Transposes and the DMD connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.5 Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3 Controlling projection error from infinite dimensions 9
3.1 Infinite-dimensional residuals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2 Pseudospectra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3 Forecast errors and coherency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.4 Convergence theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.5 Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4 Delay embedding and Krylov subspaces 13
4.1 Invariant versus non-invariant subspaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.2 Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5 Koopman modes and Generalized Laplace Analysis 15
arXiv:2510.22002v1 [math.NA] 24 Oct 2025 5.1 Laplace averages for spectral operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
5.2 Consequence for Koopman operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
5.3 Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6 Computing spectral measures of Koopman operators 18
6.1 Spectral measures of unitary operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.2 Family I: Moment-based methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
6.3 Family II: Eigenvalue-based methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
6.4 Family III: Resolvent-based methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
6.5 Spectral analysis beyond measures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
7 Towards a classification theory 29
* Department of Applied Mathematics & Theoretical Physics, University of Cambridge, Cambridge, UK. (mjc249@cam.ac.uk)
† Department of Mathematics, University of Zagreb, Zagreb, Croatia. (drmac@math.hr)
‡ Department of Mathematical Sciences, Rensselaer Polytechnic Institute, Troy, New York, USA. (hornia3@rpi.edu)
1
1 Introduction
In this paper, we give an introductory guide to Koopman learning for studying data-driven spectral
problems for discrete-time dynamical systems of the form
x n +1 = F ( x n ) , n = 0 , 1 , 2 , . . . . (1.1)
Here, x ∈ X denotes the state of the system and the state space X is a metric space. The function
F : X → X , which governs the evolution of the state, is assumed to be continuous. Frequently, though
not always, X ⊂ R d and F is nonlinear.
For many modern systems, the function F is either unknown or too complex to analyze directly.
Instead, we rely on observations in the form of snapshot data :
n o
x ( m ) , y ( m ) M
⊂ X such that y ( m ) = F ( x ( m ) ) , m = 1 , . . . , M. (1.2)
m =1
Such data may come from a single long trajectory or from many shorter experiments or simulations.
Our aim is to show how this information can be used to study Koopman operators, which provide a
powerful linear framework for analyzing nonlinear dynamics. Namely, one studies functions (called
“observables”) g : X → C and the Koopman operator acts on g , yielding another observable K g defined
by
[ K g ]( x ) = g ( F ( x )) . (1.3)
The key features of K are that it is always linear on the space of observables and its spectral decom-
positions encode information about the state-space dynamics. Numerical approximations of K from
snapshot data allow nonlinear forecasting, and spectral computations uncover struct
```

## candidate-02 [dyn-matching] — ANNOTATED as 10.3390-electronics9050823 (promote-on-encounter: duplicate of existing prose-block coverage in dynamical_systems/filtrations/phase_transitions indices; block migrated verbatim to annotations/, pass 19)

**Title:** electronics 09 00823 v3

**URL:** file:///d3e16654ca4e01a8f9ebc45cb86e4d738704cfdd52e6373cb383e9c89af6431d/electronics-09-00823-v3.pdf

**Description:** This research paper proposes a novel method for detecting predictable segments within chaotic financial time series by integrating phase space reconstruction (PSR) with self-organizing map (SOM) neural networks. The approach clusters phase track segments to separate linear (predictable) from nonlinear (chaotic) components, then validates predictability using LSTM. The method is tested on the Dow Jones index, Nikkei index, China growth enterprise market index, and Chinese gold price, demonstrating the ability to mark unpredictable regions and evaluate risk from 1-dimensional time series data.

**Content extract (≤6k chars):**

```
electronics
Article
Detecting Predictable Segments of Chaotic Financial
Time Series via Neural Network
Tianle Zhou * , Chaoyi Chu, Chaobin Xu, Weihao Liu and Hao Yu
School of Computer Engineering, Jiangsu University of Technology, Changzhou 213001, China; ccy@jsut.edu.cn
(C.C.); xuchaobin123@hotmail.com (C.X.); lwh498321660@hotmail.com (W.L.); yuhaoprice@hotmail.com (H.Y.)
* Correspondence: ztl@jsut.edu.cn; Tel.: +86-180-1583-2822
 
Received: 16 April 2020; Accepted: 13 May 2020; Published: 16 May 2020 
Abstract: In this study, a new idea is proposed to analyze the financial market and detect
price fluctuations, by integrating the technology of PSR (phase space reconstruction) and SOM
(self organizing maps) neural network algorithms. The prediction of price and index in the financial
market has always been a challenging and significant subject in time-series studies, and the prediction
accuracy or the sensitivity of timely warning price fluctuations plays an important role in improving
returns and avoiding risks for investors. However, it is the high volatility and chaotic dynamics of
financial time series that constitute the most significantly influential factors affecting the prediction
effect. As a solution, the time series is first projected into a phase space by PSR, and the phase tracks are
then sliced into several parts. SOM neural network is used to cluster the phase track parts and extract
the linear components in each embedded dimension. After that, LSTM (long short-term memory) is
used to test the results of clustering. When there are multiple linear components in the m-dimension
phase point, the superposition of these linear components still remains the linear property, and they
exhibit order and periodicity in phase space, thereby providing a possibility for time series prediction.
In this study, the Dow Jones index, Nikkei index, China growth enterprise market index and Chinese
gold price are tested to determine the validity of the model. To summarize, the model has proven
itself able to mark the unpredictable time series area and evaluate the unpredictable risk by using
1-dimension time series data.
Keywords: financial time series; chaotic dynamics; SOM neural network; clustering; LSTM
1. Introduction
Recently, nonlinear models, such as LSTM and deep learning algorithms, have been widely used
and proven effective to train and predict time series [ 1 – 3 ]. However, it is the outstanding prediction
results which are contrary to the initial sensitivity law of chaotic system and the principle of long-term
immeasurability [ 4 ]. The fact is, the dynamic properties of a chaotic financial time series should be
restored first before it is analyzed. For example, by calculating the Hurst index with MF-DFA [ 5 ],
or using PSR technology to restore the dynamic system of time series, and calculate the Lyapunov
index and K entropy, the complexity of time series and the size of predictable range of time series needs
to be acquired [ 6 ]. The chaos degree of a time series system can be described with Lyapunov index,
which means that the more chaotic the system is, the more difficult it is to predict the time series.
Besides, the predictable range of a time series is reflected by the reciprocal of the Lyapunov index.
If the Lyapunov index is greater than 1, the prediction ability of the time series is less than one step,
which means that the data in the past is not highly correlated with the data to be generated in the
future [ 7 ]. It is meaningful to predict the time series only when the Lyapunov index is 0 < L < 1.
When the Hurst index is in the range of 0 < h < 0.5, it indicates that the time series has a long-term
correlation, although the future trend is opposite to the past trend [ 6 ]. The closer h is to 0, the stronger
Electronics 2020 , 9 , 823; doi:10.3390/electronics9050823 www.mdpi.com/journal/electronics
Electronics 2020 , 9 , 823 2 of 13
the negative correlation of price is. When h is close to 0.5, the time series is random or uncorrelated,
which means the past data will not affect the future data. Instead of directly fitting and predicting time
series with nonlinear models, the methods above should be considered as preconditions for predicting
time series, as they are the solutions to over-fitting.
In our past study, real financial data DJI, SSE, Nikkei and DAX were reconstructed and by PSR to
restore the dynamic properties of the time series [ 4 ]. The study concluded that a time series is a chaotic
system, and it cannot be predicted for a long time. Here are the two main points of our past study:
1. A time series can be predicted in the short term, and the prediction range is limited by the degree of
chaos. 2. Although time series show disorder and randomness in the time domain, the restored phase
points have ordered operation in the phase space as strange attractors.
However, there are still many problems remaining in the research of financial time series.
For example, although L index is able to estimate the average predictable step length, the predictable
area is uncertain. On the other hand, there is no reasonable mathematical explanation for the violent
fluctuations of the stock market. It is generally believed that violent fluctuations are caused by some
unexpected factors—take the Great Depression of the western economy in 1930, the Asian financial
crisis in 1997, the global financial crisis in 2007 and the outbreak of coronavirus in China at the
beginning of 2020—which means these fluctuations are caused by abnormal values and irrational
trading, and emotional panic [ 8 ]. However, black swan phenomenon also happens frequently when
the economy environment is stable.
In order to improve on the previous study, two main amendments and addenda in this manuscript
are proposed as follows:
1. Using a SOM neural network to cluster similar phase track segments after processing by PSR,
for L index cannot label the predictable range of time series precisely
```

## candidate-03 [filtration-ph] — REJECTED
CHIRPS precipitation dataset paper; zero atlas machines — the 'filtration' hit is a text-filter artifact, no persistent homology or filtration construction in the atlas sense (pass 20).

**Title:** The climate hazards infrared precipitation with stationsa new environmental reco

**URL:** file:///7e31dcedc6c5d9c6d05e8b48aaacdf513f5091d03682f0a34344e2d808f0eb3e/The_climate_hazards_infrared_precipitation_with_stationsa_new_environmental_reco.pdf

**Description:** This Nature Scientific Data paper introduces CHIRPS (Climate Hazards group Infrared Precipitation with Stations), a quasi-global 0.05° resolution daily precipitation dataset spanning 1981–present that blends satellite-derived Cold Cloud Duration estimates with station observations using smart interpolation techniques. Designed to fill the gap between high-latency gauge products and low-latency satellite-only estimates, CHIRPS enables near-real-time agricultural drought monitoring and climate trend analysis. Validation against GPCC and independent stations demonstrates strong performance, and a case study using the VIC hydrologic model shows CHIRPS can effectively forecast drought and quantify the combined impacts of declining precipitation and rising temperatures in the Greater Horn of Africa.

**Content extract (≤6k chars):**

```
www.nature.com/scientificdata
OPEN
The climate hazards infrared
SUBJECT CATEGORIES
» Climate-change impacts precipitation with stations — a new
» Hydrology
» Environmental sciences environmental record for monitoring
» Attribution
» Atmospheric dynamics extremes
Chris Funk 1,2 , Pete Peterson 2 , Martin Landsfeld 2 , Diego Pedreros 1 , James Verdin 1 ,
Shraddhanand Shukla 2 , Gregory Husak 2 , James Rowland 1 , Laura Harrison 2 , Andrew Hoell 3
& Joel Michaelsen 2
Received: 23 July 2015 The Climate Hazards group Infrared Precipitation with Stations (CHIRPS) dataset builds on previous
Accepted: 13 October 2015 approaches to ‘ smart ’ interpolation techniques and high resolution, long period of record precipitation
Published: 8 December 2015 estimates based on infrared Cold Cloud Duration (CCD) observations. The algorithm i) is built around a
0.05° climatology that incorporates satellite information to represent sparsely gauged locations,
ii) incorporates daily, pentadal, and monthly 1981-present 0.05° CCD-based precipitation estimates,
iii) blends station data to produce a preliminary information product with a latency of about 2 days and a
fi nal product with an average latency of about 3 weeks, and iv) uses a novel blending procedure
incorporating the spatial correlation structure of CCD-estimates to assign interpolation weights. We present
the CHIRPS algorithm, global and regional validation results, and show how CHIRPS can be used to
quantify the hydrologic impacts of decreasing precipitation and rising air temperatures in the Greater Horn
of Africa. Using the Variable In fi ltration Capacity model, we show that CHIRPS can support effective
hydrologic forecasts and trend analyses in southeastern Ethiopia.
Design Type(s) observation design • time series design • data integration objective
Measurement Type(s) atmospheric precipitation
Technology Type(s) meterological observation
Factor Type(s)
Sample Characteristic(s) atmospheric water vapour • Africa • Central America • Caribbean Region
• East Africa
1 US Geological Survey, Center for Earth Resources Observation and Science, 47914 252nd St., Sioux Falls, South
Dakota 57198, USA. 2 UC Santa Barbara Climate Hazards Group, Santa Barbara, California 93106, USA. 3 National
Oceanic and Atmospheric Administration Earth Systems Research Laboratory, Boulder, Colarodo 80305, USA.
Correspondence and requests for materials should be addressed to C.F. (email: cfunk@usgs.gov).
SCIENTIFIC DATA | 2:150066 | DOI: 10.1038/sdata.2015.66 1
www.nature.com/sdata/
Background & Summary
This paper describes the Climate Hazards group Infrared Precipitation with Stations (CHIRPS)
environmental record (Data Citation 1), a new quasi-global (50°S-50°N), high resolution (0.05°), daily,
pentadal, and monthly precipitation dataset. CHIRPS was developed to support the United States Agency
for International Development Famine Early Warning Systems Network (FEWS NET). Building on
approaches used in successful thermal infrared (TIR) precipitation products like the National Oceanic
and Atmospheric Administration ’ s (NOAA ’ s) Rainfall Estimate (RFE2) 1,2 and African
Rainfall Climatology 3 or the University of Reading ’ s TAMSAT African Rainfall Climatology And Time
series (TARCAT) 4 – 6 , CHIRPS uses the Tropical Rainfall Measuring Mission Multi-satellite Precipitation
Analysis version 7 (TMPA 3B42 v7) 7 to calibrate global Cold Cloud Duration (CCD) rainfall estimates.
Also building on approaches used in current state-of-the-science interpolated gauge products 8 – 12 ,
CHIRPS uses a ‘ smart interpolation ’ approach 13,14 , working with anomalies from a high resolution
climatology. CHIRPS incorporates station data in a two phase process, producing two unique products.
In the fi rst phase, which yields a preliminary rainfall product with 2-day latency, sparse World
Meteorological Organization ’ s Global Telecommunication System (GTS) gauge data are blended with
CCD-derived rainfall estimates at every pentad. There are six pentads in a calendar month, fi ve 5-day
pentads and one pentad with the remaining 3 to 6 days of the month. Stations from Mexico are also
included, because these data can be obtained in near real-time as well. In the second phase, which yields a
fi nal product with a ~3 week latency, the best available monthly (and pentadal) station data are combined
with monthly (and pentadal) high resolution CCD-based rainfall estimates to produce fi elds that are
similar to gridded monthly station products like those produced by the Global Precipitation Climatology
Centre (GPCC) 8,12 – 14 or University of East Anglia ’ s Climate Research Unit (CRU) 9,11 . Thus, the CHIRPS
falls somewhere between heavily curated interpolated gauge datasets like the GPCC and sparse gauge plus
satellite products like the RFE2.
At present, and on a global scale, there is an important gap in types of gridded precipitation datasets.
There are datasets with a long period of record with very long latency, like the GPCC 8,12 – 14 and CRU
products 9,11 , and there are low latency precipitation estimates based solely on satellite information, like the
TMPA 3B42 RT 7 , Climate Prediction Center MORPHing Technique (CMORPH) 15 , or Precipitation
Estimation from Remotely Sensed Information using Arti fi cial Neural Networks (PERSIANN) 16 products, or
on climate reanalysis systems, like the Coupled Forecast System (CFS) version 2 (ref. 17) or the European
Centre for Medium-Range Weather Forecasts (ECMWF) 18 . The shortage of low latency, long record gridded
data makes it challenging for scientists and analysts to place recent extremes in historic context. While one
product (the Climate Prediction Center Merged Analysis of Precipitation (CMAP) 2 blends station data and
satellite estimates to produce a continuous 1979-present time series, it has a coarse 2.5° resolution. CHIRPS
has been explicitly designed to fi ll this gap, providing blended gauge-satellite precipitation estimates that
cover most globa
```

## candidate-04 [filtration-ph] — ANNOTATED as 10.1007-s00521-024-10787-x (promote-on-encounter: already covered as a full prose block in by-domain/tda.md plus summary rows in by-structure/filtrations.md + phase_transitions.md — the dedup gap again, queue checked only annotations/; block migrated verbatim to annotations/, crossrefs repointed, pass 20)

**Title:** s00521 024 10787 x

**URL:** file:///ada86aacccb283616913701d9f4859ff220c0d363c1a0856c552fa86e8240ed8/s00521-024-10787-x.pdf

**Description:** This peer-reviewed paper investigates whether topological data analysis (TDA) features—persistent entropy, amplitude, and point counts from persistence diagrams—can enhance univariate financial time series forecasting when integrated into the N-BEATS neural network model. Using a sliding window approach to construct multiple point clouds preserving temporal dynamics, the authors evaluate their N-BEATS+TDA method across 32 datasets spanning six cryptocurrencies and four traditional financial instruments. The TDA-augmented model achieves the best mean performance and ranking across MAPE, MAE, and RMSE metrics with statistically significant improvements over baseline and alternative feature strategies.

**Content extract (≤6k chars):**

```
Neural Computing and Applications (2025) 37:6527–6545
https://doi.org/10.1007/s00521-024-10787-x (0123456789().,-volV) (0123456789().,-volV)
ORIGINAL ARTICLE
Enhancing financial time series forecasting through topological data
analysis
Luiz Carlos de Jesus Jr. 1 • Francisco Ferna ´ndez-Navarro 2 • Mariano Carbonero-Ruz 1
Received: 9 August 2024 / Accepted: 7 November 2024 / Published online: 17 January 2025
Ó The Author(s) 2024
Abstract
Topological data analysis (TDA) is increasingly acknowledged within financial markets for its capacity to manage
complexity and discern nuanced patterns and structures. It has been applied effectively to uncover intricate relationships
and capture non-linear dependencies inherent in market data. This manuscript presents a groundbreaking study that delves
into integrating features derived from TDA to improve the performance of forecasting models for univariate time series
prediction. The research specifically examines whether incorporating features extracted from TDA-such as entropy,
amplitude, and the number of points obtained from persistent diagrams can provide valuable supplementary information to
the baseline forecasting model. Thus, the aim is to determine if these TDA-derived features can boost forecasting accuracy
by offering additional insights that existing models might overlook. The N-BEATS model serves as the baseline fore-
casting model due to its robust generalization capabilities and flexibility in incorporating additional features into the model.
The proposed methodology is compared against a univariate N-BEATS model without additional features and other
strategies incorporating supplementary features such as temporal decomposition and time delay embeddings. The evalu-
ation includes forecasting for six cryptocurrencies across four distinct time scenarios and four traditional financial
instruments across two scenarios each, resulting in 32 datasets. The results obtained were promising, as the proposed
method, N  BEATS þ TDA , achieved the best results in mean performance and mean ranking for the three metrics considered
(MAPE, MAE, and RMSE). Significant differences were observed with the rest of the proposed methods using a signif-
icance level of a ¼ 0 : 10, highlighting the effectiveness of integrating TDA features to enhance forecasting models.
Keywords Topological data analysis  Time series forecasting  feature extraction
1 Introduction homology to unveil the underlying structure of data by
identifying and tracking features such as connected com-
Topological data analysis (TDA) utilizes concepts from ponents, loops, and voids across different scales [2]. Per-
algebraic topology to analyse the shape of data, making it a sistent homology, a cornerstone of TDA, systematically
pivotal tool for extracting meaningful insights from com- studies the multi-scale topological characteristics of data-
plex datasets [1]. At its core, TDA employs persistent sets. It constructs simplicial complexes at different scales
and tracks the evolution of features like connected com-
ponents, loops, and voids [3]. This method captures the
& Francisco Ferna ´ndez-Navarro
fafernandez@uma.es persistence of these features across scales, offering insights
into the robustness and significance of topological struc-
Luiz Carlos de Jesus Jr.
lluizcarlos@al.uloyola.es tures within the data [4].
Persistent homology results are typically visualized
Mariano Carbonero-Ruz
mcarbonero@uloyola.es using persistence diagrams or barcodes, which provide a
concise yet powerful representation of the topological
1 Department of Quantitative Methods, Universidad Loyola features and lifetimes inherent in a dataset [3]. These visual
Andalucı ´a, 41704 Co ´rdoba, Spain tools condense complex mathematical insights into acces-
2 Department of Computer Languages and Computer Science, sible formats, enabling researchers to discern persistent
Universidad de Ma ´laga, 29010 Ma ´laga, Spain
123
6528 Neural Computing and Applications (2025) 37:6527–6545
patterns across various scales of analysis [2]. By high- cryptocurrency markets. Gidea et al. (2020) [15] analysed
lighting enduring features amidst fluctuations and noise, the time series of four major cryptocurrencies: Bitcoin,
persistence diagrams facilitate the discovery of funda- Ethereum, Litecoin, and Ripple. They defined the C 1 norm
mental structures that may not be discernible through of persistence landscapes to identify critical transitions
conventional data analysis methods alone [5]. Moreover, preceding the cryptocurrency crash in January 2018.
these capabilities enhance the interpretability of intricate Additionally, they employed the k-means clustering algo-
datasets and support informed decision-making across rithm to discern patterns in price movements.
diverse scientific and practical domains, ranging from TDA has also been employed to manage risk and guide
biology and neuroscience to materials science and beyond. potential investment strategies. By understanding the
Finally, persistence diagrams yield metrics such as entropy, topological features of financial data, TDA can contribute
amplitude, and point counts, which can be instrumental in to more effective risk management strategies. Persistent
quantitative assessments and predictive modelling [6]. homology aids in identifying periods of increased market
Financial markets are complex systems where prices of turbulence, enabling investors to adjust their portfolios
assets evolve according to various factors, including eco- accordingly [16]. Additionally, researchers have developed
nomic indicators, market sentiment, and external events TDA-based indicators to enhance investment strategies.
[7]. Traditional financial analysis methods rely on time These indicators, derived from the persistence landscapes
series analysis, statistical models, and machine learning of financial time series, offer new insights into market
techniques [8–10]. However, these methods may fail to beha
```

## candidate-05 [filtration-ph] — REJECTED
TopP-S element-specific PH molecular descriptors + multitask DNN for logP/logS; one machine (parameterized homology only), a PH-as-descriptor application wrapper with no stability bound, null model, matching, or joint-vs-marginal content (pass 20).

**Title:** J Comput Chem   2018   Wu   TopP S  Persistent homology‐based multi‐task deep neural networks for simultaneous predictions

**URL:** file:///63a0ee348f64e247db1c21a75a1611e4e5b9def3eb1abaeb04fddccd7784540b/J Comput Chem - 2018 - Wu - TopP S  Persistent homology‐based multi‐task deep neural networks for simultaneous predictions.pdf

**Description:** Research paper introducing TopP-S, a method using element-specific persistent homology (ESPH) as a topological molecular descriptor combined with multi-task deep neural networks to simultaneously predict octanol-water partition coefficient (log P) and aqueous solubility (log S). The authors validate their approach across six datasets, showing ESPH provides a competitive, multiscale representation of small molecules. The shared feature representation between the two correlated properties enables more accurate predictions on small datasets via inductive bias.

**Content extract (≤6k chars):**

```
FULL PAPER WWW.C-CHEM.ORG
Top P – S : Persistent Homology-Based Multi-Task Deep
Neural Networks for Simultaneous Predictions of Partition
Coefficient and Aqueous Solubility
[a] [b] [c] [a,d,e]
Kedi Wu , Zhixiong Zhao, Renxiao Wang, and Guo-Wei Wei * 
Aqueous solubility and partition coefficient are important physi- interpretation. Fortunately, it is readily suitable for machine
cal properties of small molecules. Accurate theoretical prediction learning methods, rendering topological learning algorithms.
of aqueous solubility and partition coefficient plays an important Due to the inherent correlation between solubility and partition
role in drug design and discovery. The prediction accuracy coefficient, a uniform ESPH representation is developed for both
depends crucially on molecular descriptors which are typically properties, which facilitates multi-task deep neural networks for
derived from a theoretical understanding of the chemistry and their simultaneous predictions. This strategy leads to a more
physics of small molecules. This work introduces an algebraic accurate prediction of relatively small datasets. A total of six
topology-based method, called element-specific persistent datasets is considered in this work to validate the proposed
homology (ESPH), as a new representation of small molecules topological and multitask deep learning approaches. It is dem-
that is entirely different from conventional chemical and/or onstrated that the proposed approaches achieve some of the
physical representations. ESPH describes molecular properties in most accurate predictions of aqueous solubility and partition
terms of multiscale and multicomponent topological invariants. coefficient. Our software is available online at http://weilab.
Such topological representation is systematical, comprehensive, math.msu.edu/TopP-S/. V C 2018 Wiley Periodicals, Inc.
and scalable with respect to molecular size and composition var-
iations. However, it cannot be literally translated into a physical DOI: 10.1002/jcc.25213
methods, which was first proposed by Ghose and Crippen [7] 
Introduction is
essentially purely additive and effectively a table look-up per
The partition coefficient, denoted P and defined to be the atom. Later on, XLOGP3, a refined version of the atomic-based
ratio of concentrations of a solute in a mixture of two immisci- additive methods, was developed. [6] This approach considers
ble solvents at equilibrium, is of great importance in pharma- various atom types, contributions from neighbors, as well as
cology. It measures the drug-likeness of a compound as well correction factors which help overcome known difficulties in
as its hydrophobic effect on human body. The logarithm of
purely atomistic additive methods. However, additivity may fail
this coefficient, i.e., log P , has proved to be one of the key
in some cases, where unexpected contributions to log P occur,
parameters in drug design and discovery. Optimal log P along
especially for complicated structures. Fragment/compound-
with low molecular weight and low polar surface area plays an
based predictors, instead of employing information from a
important role in governing kinetic and dynamic aspects of
drug action. In particular, Hansch and coworkers [1] gave a
detailed description of how lipophilicity impacted pharmaco- [a] K. Wu, Guo-Wei Wei
Department of Mathematics, Michigan State University, East Lansing,
dynamics. This being said, surveys show that approximately Michigan, 48824
half of the drug candidates fail to reach the market due to E-mail: wei@math.msu.edu
unsatisfactory pharmacokinetic properties or toxicity, [2] which [b] Z. Zhao
indeed makes log P predictions even more important. School of Medicine, Foshan University, Foshan, Guangdong, 528000,
People’s Republic of China
The extent of existing reliable experimental log P data is [c] R. Wang
negligible compared to tremendous compounds whose log P State Key Laboratory of Bioorganic Chemistry, Shanghai Institute of
data are practically needed. Therefore, computational predic- Organic Chemistry, Chinese Academy of Sciences, Shanghai, 200032,
tion of partition coefficient is an indispensable approach in People’s Republic of China
modern drug design and discovery. Since the pioneering work [d] Guo-Wei Wei
of Hansch and coworkers, [3–5] Department of Electrical and Computer Engineering, Michigan State
a large variety of octanol–water University, Michigan, 48824
partition coefficient predictors has been developed over the [e] Guo-Wei Wei
past few decades. [6] Many methods are generally called as Department of Biochemistry and Molecular Biology, Michigan State
University, Michigan, 48824
quantitative structure–activity relationship (QSAR) models. In
Contract grant sponsor: NSF; Contract grant numbers: DMS-1721024
general, these models can be categorized into atomic-based and IIS-1302285; Contract grant sponsor: MSU Center for Mathematical
additive methods, fragment/compound-based methods, and Molecular Biosciences Initiative
property-based methods. One of the atomic-based additive V C 2018 Wiley Periodicals, Inc.
1444 Journal of Computational Chemistry 2018 , 39 , 1444–1454 WWW.CHEMISTRYVIEWS.COM
1096987x, 2018, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/jcc.25213 by University Of North Carolina Charlotte, Wiley Online Library on [27/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WWW.C-CHEM.ORG FULL PAPER
single atom, are built at compounds or fragments level. Com- Geometric descriptors are commonly used in machine learn-
pounds or fragments are then added up with correction fac- ing to represent small molecules. In fact, geometric represen-
tors. Popular fragment methods include KOWWIN, [8,9] tation of molecules, particularly macromolecules, often
CLOGP, [10,11] ACD/LOGP, [12,13] KLOGP. [14,15] A major c
```

## candidate-06 [filtration-ph] — REJECTED
PHOM/NPHOM — one-machine PH-descriptor wrapper: 1-dim PH on weight clique complexes used only as an overfitting scalar diagnostic, no atlas machine beyond the descriptor itself (pass 21).

**Title:** s41060 022 00332 1

**URL:** file:///70fc2d147ae5d8e7a8fe4bbb464bbac1c7bb6773998f6c0d2ad8f3464238c876/s41060-022-00332-1.pdf

**Description:** A peer-reviewed research paper proposing PHOM (Persistent Homology-based Overfitting Measure) and its normalized variant NPHOM to detect overfitting in convolutional neural networks using only trained network weights — without requiring access to training data. The method constructs clique complexes from network weights and applies one-dimensional persistent homology to investigate co-adaptations among neurons. Experimental results on CIFAR-10, SVHN, Tiny ImageNet, and CIFAR-100 demonstrate that PHOM/NPHOM can effectively indicate the degree of overfitting, enabling filtering of overfitted pretrained networks distributed without their training datasets.

**Content extract (≤6k chars):**

```
International Journal of Data Science and Analytics (2022) 14:261–278
https://doi.org/10.1007/s41060-022-00332-1
R E G U L A R P A P E R
Overfitting measurement of convolutional neural networks using
trained network weights
Satoru Watanabe 1 · Hayato Yamana 2
Received: 4 January 2022 / Accepted: 20 April 2022 / Published online: 12 May 2022
© The Author(s), under exclusive licence to Springer Nature Switzerland AG 2022
Abstract
Overfitting reduces the generalizability of convolutional neural networks (CNNs). Overfitting is generally detected by com-
paring the accuracies and losses of the training and validation data, where the validation data are formed from a portion of
the training data; however, detection methods are ineffective for pretrained networks distributed without the training data.
Thus, in this paper, we propose a method to detect overfitting of CNNs using the trained network weights inspired by the
dropout technique. The dropout technique has been employed to prevent CNNs from overfitting, where the neurons in the
CNNs are invalidated randomly during their training. It has been hypothesized that this technique prevents CNNs from over-
fitting by restraining the co-adaptations among neurons, and this hypothesis implies that the overfitting of CNNs results from
co-adaptations among neurons and can be detected by investigating the inner representation of CNNs. The proposed persis-
tent homology-based overfitting measure (PHOM) method constructs clique complexes in CNNs using the trained network
weights, and the one-dimensional persistent homology investigates co-adaptations among neurons. In addition, we enhance
PHOM to normalized PHOM (NPHOM) to mitigate fluctuation in PHOM caused by the difference in network structures. We
applied the proposed methods to convolutional neural networks trained for the classification problems on the CIFAR-10, street
view house number, Tiny ImageNet, and CIFAR-100 datasets. Experimental results demonstrate that PHOM and NPHOM
can indicate the degree of overfitting of CNNs, which suggests that these methods enable us to filter overfitted CNNs without
requiring the training data.
Keywords Convolutional neural network · Overfitting · Persistent homology · Topological data analysis
1 Introduction Overfitting of CNNs is generally detected by comparing
the accuracies and losses of the training and validation data,
Overfitting is defined as “the production of an analysis that where a portion of the training data is used to form the valida-
corresponds too closely or exactly to a particular set of data, tion data [2]. However, the detection method is ineffective for
and may therefore fail to fit additional data or predict future pretrained networks distributed without the associated train-
observations reliably [1].” Overfitting is a major contributor ing data. Due to the large amount of training data, trained
to reduced generalizability of data analytics methods, includ- networks are typically distributed without the training data
ing convolutional neural networks (CNNs). to reduce the data handling costs.
Srivastava et al. [3] previously proposed a dropout method
that prevents CNNs from overfitting. In this method, the
neurons in the CNNs are invalidated randomly during their
B Satoru Watanabe
satoru.watanabe.aw@hitachi.com training. They hypothesized that “for each hidden unit,
dropout prevents co-adaptation by making the presence of
Hayato Yamana
yamana@waseda.jp other hidden units unreliable.” This hypothesis implies that
the overfitting of CNNs is a result of co-adaptations among
1 Department of Computer Science and Communications neurons and can be detected by investigating the inner rep-
Engineering, Waseda University, 3-4-1, Okubo, Shinjuku-ku, resentation of CNNs.
Tokyo 169-8555, Japan
Persistent homology (PH) has been used to investigate
2 Faculty of Science and Engineering, Waseda University, the inner representation of CNNs [4–9]. PH is a prominent
3-4-1, Okubo, Shinjuku-ku, Tokyo 169-8555, Japan
123
262 International Journal of Data Science and Analytics (2022) 14:261–278
method in big data analysis due to its three advantages, i.e., its these encircled regions corresponds to the birth of homolo-
theoretical foundation, practical computability, and robust- gies. We then increase the radius of the circles further, which
ness against small perturbations [10]. PH has been applied in causes the encircled regions to disappear. The disappearance
various fields, including neuroscience [11–13], proteomics of the encircled region corresponds to the death of homolo-
[14,15], and materials science [16,17]. However, it can be gies.
difficult to obtain precise data in such fields; thus, PH is more Figure 1b shows the PH diagram of Fig. 1a. Here, the X
useful in the computational science including CNNs because and Y axes present the birth and death of the homologies,
their network structures and the activation of neurons can be respectively. The coordinate values on the axes are deter-
described mathematically. mined by the radius of the oblique lined circles. The two
In this paper, as an enhancement of our previous work points in Fig. 1b correspond to the two enlarged regions in
[18], we propose a PH-based overfitting measure (PHOM) Fig. 1a. Note that the small region in Fig. 1a is less stable
that uses trained network weights to measure the degree of than the large region. The stability of the regions is indicated
overfitting of CNNs. PHOM constructs clique complexes on by the distance from the diagonal line in Fig. 1b, i.e., the
trained CNNs using the network weights, kernel weights, distance from the diagonal line of the point corresponding to
and pooling sizes in the dense, convolution, and pooling the small region is shorter than that to the large region.
layers, respectively. The one-dimensional PH investigates A barcode diagram provides the same information as the
the co-adaptations among neurons; thus, PHOM does not PH diagram. The barcode dia
```

## candidate-07 [filtration-ph] — REJECTED
PHG-Net — application wrapper: cubical-PH features vectorized via a PointNet-style encoder and fused into a medical-image classifier, PH-as-feature-extractor only (pass 21).

**Title:** PHG Net Persistent Homology Guided Medical Image Classification

**URL:** file:///24c514f9b3c16e0ba4659310b2ae2dc756333a2ffeab652800190d1840f35e99/PHG-Net_Persistent_Homology_Guided_Medical_Image_Classification.pdf

**Description:** WACV 2024 paper introducing PHG-Net, a persistent homology guided approach for medical image classification that processes persistence diagrams as point clouds via a PointNet-inspired encoder. The extracted topological features are fused into multi-scale CNN or Transformer feature maps in an end-to-end fashion, rather than concatenated only at the final layer. Evaluated on three public medical datasets, PHG-Net shows considerable improvements over state-of-the-art classification methods.

**Content extract (≤6k chars):**

```
2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
PHG-Net: Persistent Homology Guided Medical Image Classification *
Yaopeng Peng Hongxiao Wang Milan Sonka
University of Notre Dame University of Notre Dame University of Iowa
ypeng4@nd.edu hwang21@nd.edu milan-sonka@uiowa.edu
Danny Z. Chen
University of Notre Dame
dchen@nd.edu
Abstract cies. However, these models tend to neglect key global and
robust anatomical structures (e.g., topological structures),
Modern deep neural networks have achieved great suc- such as connected components, loops, and voids. Medi-
cesses in medical image analysis. However, the fea- cal images commonly contain tissues, organs, and lesions
tures captured by convolutional neural networks (CNNs) or as connected components with specific patterns (e.g., loops
Transformers tend to be optimized for pixel intensities and and voids), but such structures and typologies are often
neglect key anatomical structures such as connected com- overlooked by deep learning (DL) models.
ponents and loops. In this paper, we propose a persistent In recent years, topological data analysis (TDA) [9] has
homology guided approach (PHG-Net) that explores topo- been applied as a powerful methodology to analyze data in
logical features of objects for medical image classification. chemistry [20], medicine [6], biology [29], and other fields.
For an input image, we first compute its cubical persistence Persistent homology (PH) is a most widely-used method of
diagram and extract topological features into a vector rep- TDA. It tracks topological changes of object dynamics dur-
resentation using a small neural network (called the PH ing the filtration process, where a lifespan is associated with
module). The extracted topological features are then incor- these changes in the form of entity birth or death. The col-
porated into the feature map generated by CNN or Trans- lection of such birth-death time pairs forms a persistence di-
former for feature fusion. The PH module is lightweight and agram (PD). But, effectively utilizing persistence diagrams
capable of integrating topological features into any CNN in machine learning is not straightforward due to the multi-
or Transformer architectures in an end-to-end fashion. We set nature of the persistent homology building process.
evaluate our PHG-Net on three public datasets and demon-
A technique was proposed to input topological signa-
strate its considerable improvements on the target classifi-
tures into DNNs for 2D object shape and social network
cation tasks over state-of-the-art methods.
classification [12]. Additionally, a readout operation to ag-
gregate node features into a graph representation was intro-
duced [11]. Persistent landscapes were presented [2] as a
1. Introduction
method to summarize topological data into vectors to use
Deep neural networks (DNNs) are capable of learn- in machine learning. In [1], persistent images were pro-
ing useful image features based on their potent represen- posed as a stable representation that converts a persistence
tations, and are widely used in medical image analysis. diagram into a finite-dimensional vector representation. A
From AlexNet [17], VGG [25], to DenseNet [26, 10, 15], framework in [3] first encoded a persistence diagram into a
many convolutional neural network (CNN) architectures vector and then learned the vectorization using a neural net-
have been proposed for rich feature representations. Due to work. Another method was developed in [16] to first encode
their nature, CNNs primarily focus on capturing local fea- a persistence diagram into a list of persistent landscapes and
tures. Vision Transformers [7, 21] have been proposed to then vectorize them for use in DL models
2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) | 979-8-3503-1892-0/24/$31.00 ©2024 IEEE | DOI: 10.1109/WACV57701.2024.00741 procure global dependencies and long-range relationships Medical images often exhibit intricate marked topolog-
by leveraging self-attention mechanism, which allows mod- ical structures/patterns of clinical targets, thereby render-
els to attend to different patches and learn their dependen- ing persistent homology (PH) a promising computational
* This research was supported in part by NIH NIBIB Grant R01- technique that provides supplementary topological informa-
EB004640. tion and insights alongside pixel-oriented CNNs [9]. More
2642-9381/24/$31.00 ©2024 IEEE 7568
DOI 10.1109/WACV57701.2024.00741
Authorized licensed use limited to: University of North Carolina at Charlotte. Downloaded on April 27,2026 at 22:02:23 UTC from IEEE Xplore. Restrictions apply.
…… … …… VisionLoss
Input
Stage 1 Stage 4 output Ground Truth
…… ……
FC block FC block FC block
TopoLoss
Persistent PD Encoder
Diagram
Figure 1. Illustrating the pipeline of our proposed PHG-Net. The details of the PD encoder are shown in Fig. 3(a). A fully connected block
(FC block) is a two-layer MLP shown in Fig. 3(b). The blue points in a persistence diagram denote the 0-dimensional persistent homology
(H0), and the orange points denote the 1-dimensional persistent homology (H1). VisionLoss and TopoLoss represent the vision loss and
topological loss, respectively.  denotes matrix multiplication. We use a CNN backbone for illustration.
specifically, cubical persistence leverages image intensity branch) inspired by PointNet [24]. Code is available at
values as filtration functions in its analytical process, which https://github.com/yaoppeng/TopoClassification
serves as a persistent homology tool that has been proven Our main contributions are three-fold:
to be highly useful for medical image analysis. For exam-
ple, in [13], it computed persistent curves and statistics, and 1. Inspired by PointNet [24], we develop a new approach
these features were integrated into ResNet for skin lesion to process persistence diagrams as point clouds rather
classification. In [18], the persistence of each regio
```

## candidate-08 [filtration-ph] — REJECTED
ATPGCN — application wrapper: PH features concatenated with GCN readouts for brain-disease classification plus adversarial training; zero atlas machines (pass 21).

**Title:** Adversarially Trained Persistent Homology Based Graph Convolutional Network for Disease Identification Using Brain Connectivity

**URL:** file:///4012365c1d8be749456f50cac1810dd8834f2233a792529aa4e29894e996e3e5/Adversarially_Trained_Persistent_Homology_Based_Graph_Convolutional_Network_for_Disease_Identification_Using_Brain_Connectivity.pdf

**Description:** IEEE Transactions on Medical Imaging paper proposing ATPGCN, an adversarially trained persistent homology-based graph convolutional network for brain disease identification from structural/functional connectivity. The method concatenates persistent homology topological features with GCN global pooling readouts, then uses adversarial perturbations targeting clinically prior risk ROIs to evaluate robustness. Experiments across three independent datasets show ATPGCN outperforms existing classifiers and remains robust to minor network perturbations.

**Content extract (≤6k chars):**

```
IEEE TRANSACTIONS ON MEDICAL IMAGING, VOL. 43, NO. 1, JANUARY 2024 503
Adversarially Trained Persistent Homology
Based Graph Convolutional Network for Disease
Identification Using Brain Connectivity
Chenyuan Bian , Nan Xia, Anmu Xie, Shan Cong, and Qian Dong
Abstract — Brain disease propagation is associated with to collaboratively learn the individual-level representation.
characteristic alterations in the structural and functional Finally, we simulate the adversarial perturbations by target-
connectivity networks of the brain. To identify disease- ing the risk ROIs from clinical prior, and incorporate them
specific network representations, graph convolutional net- into a training loop to evaluate the robustness of the model.
works (GCNs) have been used because of their powerful The experimental results on three independent datasets
graph embedding ability to characterize the non-Euclidean demonstrate that ATPGCN outperforms existing classifica-
structure of brain networks. However, existing GCNs gener- tion methods in disease identification and is robust to minor
ally focus on learning the discriminative region of interest perturbations in network architecture. Our code is available
(ROI) features, often ignoring important topological informa- at https://github.com/CYB08/ATPGCN.
tion that enables the integration of connectome patterns of
brain activity. In addition, most methods fail to consider the Index Terms — Adversarial training, brain connectiv-
vulnerability of GCNs to perturbations in network properties ity, classification, graph convolutional network, persistent
of the brain, which considerably degrades the reliability homology.
of diagnosis results. In this study, we propose an adver-
sarially trained persistent homology-based graph convolu- I. I NTRODUCTION
tional network (ATPGCN) to capture disease-specific brain
connectome patterns and classify brain diseases. First, TRUCTURAL impairment and functional reorganization
the brain functional/structural connectivity is constructed S are major hallmarks of brain disorders. Both show high
using different neuroimaging modalities. Then, we develop inter-individual variability, particularly with the progression
a novel strategy that concatenates the persistent homol- of disorders [1]. Further, pathophysiological models of brain
ogy features from a brain algebraic topology analysis with disorders have shifted from elucidating the pathology in spe-
readout features of the global pooling layer of a GCN model
cific brain regions to characterizing the functional/structural
communications among brain regions. Simultaneously, rapid
Manuscript received 5 July 2023; revised 14 August 2023 and 21 August
2023; accepted 26 August 2023. Date of publication 29 August 2023; date advances have occurred in brain connectomics, i.e., the science
of current version 2 January 2024. This work was supported in part by the of constructing and analyzing computer-generated maps of
National Natural Science Foundation of China under Grant 62206145, brain structural/functional connectivity [2]. The progress in
Grant 62103116, and Grant 81971192; and in part by the Natural
Science Foundation of Shandong Province under Grant ZR2022QH107. neuroimaging techniques has considerably facilitated research
(Corresponding author: Chenyuan Bian.) in these areas, as cost-effective in vivo assessments of struc-
This work involved human subjects or animals in its research. Approval tural and functional connectivity networks in the brain have
of all ethical and experimental procedures and protocols was granted
by the Ethics Committee of The Affiliated Hospital of Qingdao University become feasible [3]. Specifically, functional magnetic reso-
under Approval No. QYFYWZLL27552. nance imaging (fMRI) and diffusion tensor imaging (DTI)
Chenyuan Bian is with the Shandong Provincial Key Laboratory provide efficient and non-invasive solutions to map structural
of Digital Medicine and Computer-Assisted Surgery, The Affiliated
Hospital of Qingdao University, Qingdao 266000, China (e-mail: and functional connectivity, respectively. Previous fMRI stud-
biancy@qdu.edu.cn). ies revealed that brain functional connectivity is altered in
Nan Xia is with the Institute of Digital Medicine and Computer- patients with autism spectrum disorder (ASD) [4] and attention
Assisted Surgery, Qingdao University, Qingdao 266071, China (e-mail:
xianan@qdu.edu.cn). deficit hyperactivity disorder (ADHD) [5], showing reduced
Anmu Xie is with the Department of Neurology, The Affiliated short- and long-term functional connectivity. Additionally,
Hospital of Qingdao University, Qingdao 266000, China (e-mail: recent studies [6], [7] using DTI have shown that axonal
xieanmu@163.com).
Shan Cong is with the Qingdao Innovation and Development Cen- integrity and structural connectivity are affected in patients
ter, Harbin Engineering University, Qingdao 260000, China (e-mail: with mild cognitive impairment (MCI). The aforementioned
Shan.Cong@hrbeu.edu.cn). findings can serve as potential biomarkers for brain disorder
Qian Dong is with the Shandong Provincial Key Laboratory of Digital
Medicine and Computer-Assisted Surgery, The Affiliated Hospital of identification.
Qingdao University, Qingdao 266000, China, and also with the Shandong With brain connectivity data as input, many deep learning
College Collaborative Innovation Center of Digital Medicine Clinical methods [8], [9], [10] have been proposed to explore these
Treatment and Nutrition Health, Qingdao University, Qingdao 266003,
China (e-mail: 18661801885@163.com). informative biomarkers and produced promising results in
Digital Object Identifier 10.1109/TMI.2023.3309874 discriminating patients from healthy controls (HCs). Recently,
1558-254X © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: University of N
```

## candidate-09 [transport-matching] — REJECTED
QR-DQN — transport-as-tool: Wasserstein metric appears only as a training loss / contraction-metric for RL value distributions; no matching, filtration, or other atlas machine (pass 21).

**Title:** Distributional Reinforcement Learning with Quantile Regression

**URL:** file:///246188523f020902aef818ee3b1e6692f8fd9a654e6369c9aefd6b7047481b2f/Distributional_Reinforcement_Learning_with_Quantile_Regression.pdf

**Description:** This AAAI-18 paper introduces QR-DQN, a distributional reinforcement learning algorithm that uses quantile regression to minimize the Wasserstein distance between predicted and target return distributions. It closes the theory-practice gap left by C51 by proving contraction mapping results for approximate distributions and operating end-to-end under the Wasserstein metric. QR-DQN achieves a 33% median score improvement over C51 on the Atari 2600 benchmark suite.

**Content extract (≤6k chars):**

```
The Thirty-Second AAAI Conference
on Artificial Intelligence (AAAI-18)
Distributional Reinforcement
Learning with Quantile Regression
Will Dabney Mark Rowland Marc G. Bellemare R´ emi Munos
DeepMind University of Cambridge ∗ Google Brain DeepMind
Abstract the-art on the suite of benchmark Atari 2600 games (Belle-
mare et al. 2013).
In reinforcement learning (RL), an agent interacts with the One of the theoretical contributions of the C 51 work was
environment by taking actions and observing the next state a proof that the distributional Bellman operator is a contrac-
and reward. When sampled probabilistically, these state tran- tion in a maximal form of the Wasserstein metric between
sitions, rewards, and actions can all induce randomness in
the observed long-term return. Traditionally, reinforcement probability distributions. In this context, the Wasserstein
learning algorithms average over this randomness to estimate metric is particularly interesting because it does not suffer
the value function. In this paper, we build on recent work ad- from disjoint-support issues (Arjovsky, Chintala, and Bot-
vocating a distributional approach to reinforcement learning tou 2017) which arise when performing Bellman updates.
in which the distribution over returns is modeled explicitly Unfortunately, this result does not directly lead to a practical
instead of only estimating the mean. That is, we examine algorithm: as noted by the authors, and further developed by
methods of learning the value distribution instead of the value Bellemare et al. (2017), the Wasserstein metric, viewed as a
function. We give results that close a number of gaps between loss, cannot generally be minimized using stochastic gradi-
the theoretical and algorithmic results given by Bellemare, ent methods.
Dabney, and Munos (2017). First, we extend existing results This negative result left open the question as to whether it
to the approximate distribution setting. Second, we present
a novel distributional reinforcement learning algorithm con- is possible to devise an online distributional reinforcement
sistent with our theoretical formulation. Finally, we evaluate learning algorithm which takes advantage of the contraction
this new algorithm on the Atari 2600 games, observing that result. Instead, the C 51 algorithm first performs a heuristic
it significantly outperforms many of the recent improvements projection step, followed by the minimization of a KL di-
on DQN , including the related distributional algorithm C 51. vergence between projected Bellman update and prediction.
The work therefore leaves a theory-practice gap in our un-
derstanding of distributional reinforcement learning, which
Introduction makes it difficult to explain the good performance of C 51.
In reinforcement learning, the value of an action a in state s Thus, the existence of a distributional algorithm that oper-
describes the expected return, or discounted sum of rewards, ates end-to-end on the Wasserstein metric remains an open
obtained from beginning in that state, choosing action a , and question.
subsequently following a prescribed policy. Because know- In this paper, we answer this question affirmatively. By
ing this value for the optimal policy is sufficient to act opti- appealing to the theory of quantile regression (Koenker
mally, it is the object modelled by classic value-based meth- 2005), we show that there exists an algorithm, applicable in
ods such as SARSA (Rummery and Niranjan 1994) and Q- a stochastic approximation setting, which can perform distri-
Learning (Watkins and Dayan 1992), which use Bellman’s butional reinforcement learning over the Wasserstein metric.
equation (Bellman 1957) to efficiently reason about value. Our method relies on the following techniques:
Recently, Bellemare, Dabney, and Munos (2017) showed • We “transpose” the parametrization from C 51: whereas
that the distribution of the random returns, whose expecta- the former uses N fixed locations for its approxima-
tion constitutes the aforementioned value, can be described tion distribution and adjusts their probabilities, we assign
by the distributional analogue of Bellman’s equation, echo- fixed, uniform probabilities to N adjustable locations;
ing previous results in risk-sensitive reinforcement learning • We show that quantile regression may be used to stochas-
(Heger 1994; Morimura et al. 2010; Chow et al. 2015). In tically adjust the distributions’ locations so as to minimize
this previous work, however, the authors argued for the use- the Wasserstein distance to a target distribution.
fulness in modeling this value distribution in and of itself. • We formally prove contraction mapping results for our
Their claim was asserted by exhibiting a distributional rein- overall algorithm, and use these results to conclude that
forcement learning algorithm, C 51, which achieved state-of- our method performs distributional RL end-to-end under
∗ the Wasserstein metric, as desired.
Contributed during an internship at DeepMind.
Copyright c © 2018, Association for the Advancement of Artificial The main interest of the original distributional algorithm
Intelligence (www.aaai.org). All rights reserved. was its state-of-the-art performance, despite still acting by
2892
maximizing expectations. One might naturally expect that a
direct minimization of the Wasserstein metric, rather than its π π
q 1 T Z D KL (Φ T  Z ‖ Z )
heuristic approximation, may yield even better results. We
derive the Q-Learning analogue for our method ( QR - DQN ),
apply it to the same suite of Atari 2600 games, and find that it q 2 T π Z
achieves even better performance. By using a smoothed ver- π 
Φ T Z
sion of quantile regression, Huber quantile regression , we
gain an impressive 33% median score increment over the al- z   z   z
1 z z z
2
ready state-of-the-art C 51.
Figure 1: Projection used by C 51 assigns mass inversely
Distributional RL proportional to distance from nearest support. Update mini-
```

## candidate-10 [transport-matching] — REJECTED
Hawkes-process functional limit theorems — pure probability theory; Wasserstein distance used only to bound convergence rates, zero atlas machines ('matching' hit is a text-filter artifact) (pass 21).

**Title:** Functional Limit Theorems for Hawkes Processes

**URL:** file:///3787b529d8dcbe426f282306a063a610f08da0c52009dfbee6b39269a57a4ab9/Functional_Limit_Theorems_for_Hawkes_Processes.pdf

**Description:** A rigorous probability theory paper establishing functional laws of large numbers (FLLNs) and functional central limit theorems (FCLTs) for subcritical and critical Hawkes processes under minimal kernel conditions. The authors prove that long-run behavior is fully determined by the average offspring number and the dispersion of child events, with the precise form of limit theorems depending strongly on dispersion regime. Convergence rates are provided via Wasserstein distance bounds, and critical processes with heavily dispersed child events are shown to display long-range dependencies.

**Content extract (≤6k chars):**

```
Functional Limit Theorems for Hawkes Processes
Ulrich Horst ∗ and Wei Xu †
December 31, 2024
Abstract
We prove that the long-run behavior of Hawkes processes is fully determined by the average number
and the dispersion of child events. For subcritical processes we provide FLLNs and FCLTs under minimal
conditions on the kernel of the process with the precise form of the limit theorems depending strongly
on the dispersion of child events. For a critical Hawkes process with weakly dispersed child events,
functional central limit theorems do not hold. Instead, we prove that the rescaled intensity processes
and rescaled Hawkes processes behave like CIR-processes without mean-reversion, respectively integrated
CIR-processes. We provide the rate of convergence by establishing an upper bound on the Wasserstein
distance between the distributions of rescaled Hawkes process and the corresponding limit process. By
contrast, critical Hawkes process with heavily dispersed child events share many properties of subcritical
ones. In particular, functional limit theorems hold. However, unlike subcritical processes critical ones
with heavily dispersed child events display long-range dependencies.
MSC 2020 subject classifications: Primary 60F17, 60G55; secondary 60J80
Keywords and phrases: Hawkes process, functional limit theorem, regular variation, convergence rate.
1 Introduction
A Hawkes process N := { N ( t ) : t ≥ 0 } is a random point process that models self-exciting arrivals of
random events. Its intensity Λ := { Λ( t ) : t ≥ 0 } is usually of the form
∑ ∫
Λ( t ) := μ ( t ) + φ ( t − τ i ) = μ ( t ) + φ ( t − s ) N ( ds ) , (1.1)
0 <τ i <t (0 ,t )
for some immigration density μ ∈ L 1
loc ( R + ; R + ) that captures the immigration of exogenous events, and
arXiv:2401.11495v3 [math.PR] 29 Dec 2024
some kernel φ ∈ L 1 ( R + ; R + ) that captures the self-exciting impact of past events on the arrivals of future
events. The random variable τ i denotes the arrival time of the i -th event, for each i ∈ N .
A Hawkes process can be reconstructed as a Poisson cluster process associated to an age-dependent
branching process with an average offspring number m := ‖ φ ‖ L 1 . The criticality of branching processes
gives rise to three regimes. Depending on the average number of offsprings, a Hawkes process is called
subcritical/stationary ( m < 1), critical/quasi-stationary ( m = 1) or super-critical/non-stationary ( m > 1).
In this paper we analyse the asymptotic behavior of subcritical and critical Hawkes processes by estab-
lishing FLLNs and FCLTs (classical and non-clasical) for such processes. 1
∗ Department of Mathematics and School of Business and Economics, Humboldt-Universit¨ at zu Berlin, Unter den Linden
6, 10099 Berlin; email: horst@math.hu-berlin.de. Horst gratefully acknowledges support from DFG CRC/TRR 388 “Rough
Analysis, Stochastic Dynamics and Related Fields”, Project B02.
† School of Mathematics and Statistics, Beijing Institute of Technology, Beijing 100081, China; email: xuwei.math@gmail.com
1 Supercritical Hawkes processes grow to infinity exponentially fast in which case FLLNs and FCLTs cannot be established.
1
1.1 Literature review
First introduced by Hawkes in [ 36 , 37 ] to understand cross-dependencies between earthquakes and their
aftershocks, Hawkes processes have been generalized in many directions in recent years including marked
Hawkes processes and point measures [ 17 , 61 ], nonlinear Hawkes processes [ 16 , 64 ], infinite-dimensional
processes [ 11 , 40 ], and nearly unstable processes [ 49 , 50 , 71 ].
Hawkes processes and their generalizations have become a powerful tool to model a variety of phenomena
in biology and neuroscience [ 41 , 51 , 62 , 64 ], sociology and criminology [ 13 , 19 , 60 ], seismology [ 15 , 61 ] and,
in particular, finance. Applications in finance range from intraday transaction dynamics [ 10 , 14 ] to asset
price processes [ 6 , 7 ]and rough volatility modeling [ 25 , 42 , 49 , 50 ], and from limit order book modelling
[ 40 , 55 ] to financial contagion [ 3 , 32 , 52 ] and exchange rate dynamics [ 39 ]. We refer to [ 8 ] for a review of
Hawkes processes and their applications.
The more applied literature on Hawkes processes is accompanied by an increasing theoretical litera-
ture that studies microscopic and macroscopic properties of Hawkes processes and their generalizations.
Three well-known microscopic properties, including statistical characterization, cluster representation and
probability generating function were first established in [ 36 , 37 , 38 ] for subcritical Hawkes processes and
extended recently in [ 9 , 30 ] to general processes. The genealogy and event cascades of a Hawkes process
with exponential kernel were studied in [ 42 ] by exploring the intrinsic branching structure.
Macroscopic properties are usually established by proving scaling limit or laws of large numbers and
central limit theorems. Hawkes and Oakes [ 38 ] were the first to establish a central limit theorem (CLT) for ∫ ∞
stationary Hawkes processes whose kernels satisfy the integrability condition 0 t φ ( t ) dt < ∞ . Their result
was later generalized by Bacry et al. [ 7 ] who established a functional law of large numbers (FLLN) and a
functional central limit theorem (FCLT) under the weaker integrability condition
∫ ∞ √
t φ ( t ) dt < ∞ . (1.2)
0
A FCLT and a large deviation principle (LPD) for Hawkes processes with exponential kernel and large
exogenous density have been established by Gao and Zhu [ 28 , 29 ]. LDPs for nonlinear and mean-field limits
of Hawkes processes have been established in [ 76 , 77 ] and [ 26 , 27 ] respectively.
Limit theorems and LDPs for marked Hawkes processes have also been studied by many authors. LDPs
for marked Hawkes processes were first established in [ 70 , 75 ]; their results have recently been extended
to path-wise LDPs in [ 23 ]. CLTs for marked Hawkes processes were first established in [ 54 , 74 ]. Under
a light-tailed condition on t
```

## candidate-11 [transport-matching] — REJECTED
GWGAN — GAN wrapper around the existing Gromov-Wasserstein distance used as a differentiable loss; single-machine Matching instantiation already covered more deeply by annotations/2206.09398.md (FUGW) and s41468-022-00089-3.md (pass 21).

**Title:** Learning Generative Models across Incomparable Spaces

**URL:** file:///193e2bfd6afa53f0318828241d644925b4c17841c7355ebb95d28f17a34b89e2/Learning_Generative_Models_across_Incomparable_Spaces.pdf

**Description:** This ICML 2019 paper introduces GWGAN, a novel class of generative adversarial networks that can learn distributions across incomparable spaces—spaces of different dimensionality or data type—by using the Gromov-Wasserstein distance as a loss function. The key idea is to compare distributions relationally via pairwise intra-space distances rather than requiring a shared metric space, enabling applications such as learning from graph structures to Euclidean space, dimensionality reduction that preserves distributional structure, and stylistic modification of generated samples.

**Content extract (≤6k chars):**

```
Learning Generative Models across Incomparable Spaces
Charlotte Bunne 1 David Alvarez-Melis 2 Andreas Krause 1 Stefanie Jegelka 2
Abstract of 28 × 28 -pixel vectors for MNIST), and the generated dis-
Generative Adversarial Networks have shown re- tribution that minimizes the objective has the same support
markable success in learning a distribution that as the reference one. This is of course desirable when the
faithfully recovers a reference distribution in its goal is to generate samples that are indistinguishable from
entirety . However, in some cases, we may want to those of the reference distribution.
only learn some aspects (e.g., cluster or manifold Many other applications, however, require modeling only
structure), while modifying others (e.g., style, ori- topological or relational aspects of the reference distribution.
entation or dimension). In this work, we propose In such cases, the absolute location of the data manifold is
an approach to learn generative models across irrelevant (e.g., distributions over learned representations,
such incomparable spaces, and demonstrate how such as word embeddings, are defined only up to rotations),
to steer the learned distribution towards target or it is not available (e.g., if the data is accessible only as a
properties. A key component of our model is weighted graph indicating similarities among sample points).
the Gromov-Wasserstein distance, a notion of dis- Another reason for modeling only topological aspects is the
crepancy that compares distributions relationally desire to, e.g., change the appearance or style of the samples,
rather than absolutely. While this framework sub- or down-scale images. Divergences that directly compare
sumes current generative models in identically samples from the two distributions, and hence most current
reproducing distributions, its inherent flexibility generative models, do not apply to those settings.
allows application to tasks in manifold learning,
relational learning and cross-domain learning. In this work, we develop a novel class of generative mod-
els that can learn across incomparable spaces, e.g., spaces
of different dimensionality or data type. Here, the rela-
tional information between samples, i.e., the topology of
1. Introduction
the reference data manifold, is preserved, but other char-
Generative Adversarial Networks (GANs, Goodfellow et al. acteristics, such as the ambient dimension, can vary. A
(2014)) and its variations (Radford et al., 2016; Arjovsky key component of our approach is the Gromov-Wasserstein
et al., 2017; Li et al., 2017) are powerful models for learning ( GW ) distance (M emoli, 2011), a generalization of classic ´
complex distributions. Broadly, these methods rely on an Optimal Transport distances to incomparable ground spaces.
adversary that compares samples from the true and learned Instead of directly comparing points in the two spaces, the
distributions, giving rise to a notion of divergence between GW distance computes pairwise intra-space distances, and
them. The divergences implied by current methods require compares those distances across spaces, greatly increasing
the two distributions to be supported in sets that are identical the modeling scope. Figure 1 illustrates the new model.
arXiv:1905.05461v2 [cs.LG] 15 May 2019 or at the very least comparable ; examples include Optimal
To realize this model, we address several challenges. First,
Transport (OT) distances (Salimans et al., 2018; Genevay
we enable the use of the Gromov-Wasserstein distance in
et al., 2018) or Integral Probability Metrics (IPM) (M uller, ¨
various learning settings by improving its robustness and
1997; Sriperumbudur et al., 2012; Mroueh et al., 2017). In
ensuring unbiased learning. Similar to existing OT-based
all of these cases, the spaces over which the distributions are
generative models (Salimans et al., 2018; Genevay et al.,
defined must have the same dimensionality (e.g., the space
2018), we leverage the differentiability of this distance to
1 Department of Computer Science, Eidgen ossische Technische ¨ provide gradients for the generator. Second, for efficiency,
Hochschule (ETH), Z urich, Switzerland ¨ 2 Computer Science and we further parametrize it via a learnable adversary. The
Artificial Intelligence Laboratory (CSAIL), Massachusetts Insti- added flexibility of the GW distance necessitates to con-
tute of Technology (MIT), Cambridge, USA. Correspondence to: strain the adversary. To this end, we propose a novel or-
Charlotte Bunne < bunnec@ethz.ch > .
thogonality regularization, which might be of independent
Proceedings of the 36 th International Conference on Machine interest.
Learning , Long Beach, California, PMLR 97, 2019. Copyright
2019 by the author(s). A final challenge —which doubles as one of the main ad-
Learning Generative Models across Incomparable Spaces
intra-space distances intra-space distances
w 1 
GW GAN 0 d 21 … d 1n 0 sp 21 … sp 1n w w
3 2
… sp 2n w 4 w 6 w 7 data
z g d 12 0 … d 2n GW sp 12 0
θ w 5 w 8
… … … … loss … … … … P x
[ d n1 d n2 … 0 ] [ sp w 10
n1 sp n2 … 0 ] w 9
Figure 1. The Gromov-Wasserstein generative adversarial network (G W G AN ) learns across incomparable spaces, such as different
dimensions or data type (from graphs to Euclidean space). The key idea is that its learning objective is purely based on intra-space
distances (e.g., pairwise distances d or shortest paths sp ) in the generator and data space, respectively.
vantages of this approach— arises from the added flexibility neural network, maps random noise z ∈ Z to a generator
of the generator: it allows to freely alter superficial char- space Y that is independent of data space X .
acteristics of the generated distribution while still learning
the basic structure of the reference distribution. We show 2.1. Gromov-Wasserstein Discrepancy
examples how to steer these additional degrees of freedom
via regularization or adversaries in the model. The resulting Learning generative models 
```

## candidate-12 [transport-matching] — REJECTED
CDRL analysis — RL theory around the Cramér distance and projected Bellman operators; Wasserstein only invoked by analogy, zero atlas machines ('transport' hit is a text-filter artifact) (pass 21).

**Title:** An Analysis of Categorical Distributional Reinforcement Learning

**URL:** file:///a2b01c3263c1203a4067d202c1a63f3d67ca5408c80ab0309742e932f7f0da9c/An_Analysis_of_Categorical_Distributional_Reinforcement_Learning.pdf

**Description:** A theoretical analysis of categorical distributional reinforcement learning (CDRL), the foundation behind the C51 algorithm that achieved state-of-the-art Atari performance. The paper establishes a formal framework connecting CDRL to the Cramér distance, quantifies the approximation error from discrete distribution parametrisation, and provides the first convergence proofs for sample-based CDRL algorithms.

**Content extract (≤6k chars):**

```
An Analysis of Categorical Distributional Reinforcement Learning
Mark Rowland *1 Marc G. Bellemare † Will Dabney ‡ R´ emi Munos ‡ Yee Whye Teh ‡
* University of Cambridge, † Google Brain, ‡ DeepMind
Abstract et al., 2016]. Recently, Bellemare et al. [2017a] used
the distributional perspective to propose an algorithm,
C51 , which achieved state-of-the-art performance on
Distributional approaches to value-based re-
the Atari 2600 suite of benchmark tasks. C51 is a deep
inforcement learning model the entire dis-
RL algorithm based on categorical policy evaluation
tribution of returns, rather than just their
(for evaluation) and categorical Q-learning (for con-
expected values, and have recently been
trol), also introduced by Bellemare et al. [2017a], and
shown to yield state-of-the-art empirical per-
it is these latter two algorithms which are at the centre
formance. This was demonstrated by the re-
of our study. We refer to these approaches as categor-
cently proposed C51 algorithm, based on cat-
ical distributional reinforcement learning (CDRL).
egorical distributional reinforcement learn-
ing (CDRL) [Bellemare et al., 2017a]. How- Given a state x and action a , C51 approximates the
ever, the theoretical properties of CDRL al- distribution over returns using a uniform grid over a
gorithms are not yet well understood. In this fixed range, i.e. a categorical distribution with evenly-
paper, we introduce a framework to analyse spaced outcomes. Analogous to how value-based ap-
CDRL algorithms, establish the importance proaches such as SARSA [Rummery and Niranjan,
of the projected distributional Bellman oper- 1994] learn to predict, C51 also forms a learning target
ator in distributional RL, draw fundamental from sample transitions: reward, next state, and even-
connections between CDRL and the Cram´ er tually next-state distribution over returns. However,
distance, and give a proof of convergence for the parallel ends here: because C51 learns a distri-
sample-based categorical distributional rein- bution, it minimises the Kullback-Leibler divergence
forcement learning algorithms. between its target and its prediction, rather than the
usual squared loss. However, the support of the target
is in general disjoint from the approximation support;
1 INTRODUCTION to account for this, Bellemare et al. [2017a] further
introduced a projection step normally absent from re-
Reinforcement learning (RL) formalises the problems inforcement learning algorithms.
of evaluation and optimisation of an agent’s behaviour As a whole, the particular techniques incorporated
while interacting with an environment, based upon in C51 are not explained by the accompanying the-
feedback given through a reward signal [Sutton and ory. While the “mean process” which governs learning
arXiv:1802.08163v1 [stat.ML] 22 Feb 2018 Barto, 1998]. A major paradigm for solving these within C51 is described by a contractive distributional
problems is value-based RL, in which the agent pre- Bellman operator, there are not yet any guarantees
dicts the expected return – i.e. the expected discounted on the behaviour of sample-based algorithms. To put
sum of rewards – in order to guide its behaviour. The things in context, such guarantees in case of estimating
moments or distribution of the random return have expected returns require a completely different math-
also been considered in the literature, with a variety of ematical formalism [Tsitsiklis, 1994, Jaakkola et al.,
approaches proposing algorithms for estimating more 1994]. The effect of the discrete approximation and its
complex distributional information [Morimura et al., corresponding projection step also remain to be quan-
2010b,a, Prashanth and Ghavamzadeh, 2013, Tamar tified. In this paper we analyse these issues.
1 Contributed during an internship at DeepMind. At the centre of our analysis is the Cram´ er distance
Proceedings of the 21 st International Conference on Ar- between probability distributions. The Cram´ er dis-
tificial Intelligence and Statistics (AISTATS) 2018, Lan- tance is of particular interest as it was recently shown
zarote, Spain. PMLR: Volume 84. Copyright 2018 by the to possess many of the same properties as the Wasser-
author(s). stein metric, used to show the contractive nature of
An Analysis of Categorical Distributional Reinforcement Learning
the distributional Bellman operator [Bellemare et al., dom variable given by the sum of discounted rewards:
2017b]. Specifically, using the Cram´ er distance, we: (i) ∑ ∞ ∣
∣
quantify the approximation error arising from the dis- γ t R t ∣
∣ X 0 = x, A 0 = a , (1)
crete approximation in CDRL (see Section 4.2); and t =0
(ii) develop stochastic approximation results for the where γ ∈ [0 , 1) is the discount factor. We may im-
sample-based case (see Section 4.3). plicitly view the distribution of the returns as being
One of the main contributions of this paper is to estab- parametrised by π [Sutton et al., 1999]. Two common
lish a framework for the analysis of CDRL algorithms. tasks in RL are (i) evaluation , in which the expected
This framework reveals a space of possible alternative value of the return is sought for a fixed policy, and
methods (Sections 3 and 4). We also demonstrate (ii) control , in which a policy π ∗ which maximises the
that the fundamental property required for the con- expected value of the returns is sought.
vergence of distributional RL algorithms is contractiv- In the remainder of this paper, we will write the distri-
ity of a projected Bellman operator, in addition to the bution of the return of policy π and initial state-action
contractivity of the Bellman operator itself as in non- pair ( x, a ) ∈ X × A as
distributional RL (Proposition 2). This point has par- ( 
allels with the importance of the (distinct) projection ∑ ∞ ∣ )
∣
η ( x,a ) t
operator in non-tabular RL [Tsitsiklis and Van Roy, π = Law π γ R t ∣
∣ X 0 = x, A 0 = a . (2)
t =0
1997].
We write η π for the collection of distribution
```

## candidate-13 [transport-matching] — REJECTED
Cornulier commability of focal locally compact groups — pure geometric group theory (quasi-isometry classification); no optimal transport or matching in the atlas sense (pass 21).

**Title:** Commability and focal locally compact groups

**URL:** file:///381bc4277689ec3e63cb8f0c7b3e1e43291559b4c8e06d81e409264c199322f5/Commability_and_focal_locally_compact_groups.pdf

**Description:** A research paper by Yves Cornulier introducing commability—an equivalence relation on locally compact groups generated by cocompact inclusions and quotients by compact normal subgroups. The paper classifies focal hyperbolic locally compact groups up to commability across connected, totally disconnected, and mixed types, identifying type-dependent invariants including a real parameter in the mixed case shown to be a quasi-isometry invariant.

**Content extract (≤6k chars):**

```
COMMABILITY AND FOCAL LOCALLY COMPACT GROUPS
YVES CORNULIER
Abstract. We introduce the notion of commability between locally compact groups, namely
the equivalence relation generated by cocompact inclusions and quotients by compact normal
subgroups. We give a classification of focal hyperbolic locally compact groups up to comma-
bility. In the mixed case, it involves a real parameter, which is shown to be a quasi-isometry
invariant.
1. Introduction
Classically, two groups are called commensurable if they have isomorphic finite index sub-
groups, and commensurable up to finite kernel if they have finite index subgroups that are
isomorphic after modding out by a finite normal subgroup. It is easy to check that these are
transitive (and hence equivalence) relations. In the setting of locally compact groups, it is
natural to consider the same relations by only considering open finite index subgroups and
topological isomorphisms. However, another variant is to replace finite index open subgroups
by cocompact closed subgroups, and compact kernels. This is a natural setting, in view of
the fact that cocompact closed embeddings and quotients by compact normal subgroups are
coarse equivalences. A difference with the previous setting, however, is that the intersection
of two closed cocompact subgroups may not be cocompact: for instance consider the lattices √
Z and 2 Z in R . A consequence is that the proof that these relations are transitive falls
down, and they are actually not transitive (this follows from [MSW03, Corollary 10]). It is
still natural to consider the equivalence relations they generate.
We abbreviate locally compact group into LC-group . For a homomorphism between LC-
groups, write copci as a (pronounceable) shorthand for continuous proper with cocompact
image . A copci homomorphism f : G → H obviously factors as the composition G →
G/ Ker( f ) → H of the quotient map by a compact normal subgroup and an injective copci,
and the latter can be viewed as a topological isomorphism onto a cocompact closed subgroup.
Definition 1.1. Let us say that two LC-groups G, H are commable if there exist an integer
k and a sequence (called commability) of copci homomorphisms
(1.1) G = G 0 − − G 1 − − G 2 − − . . . − − G k = H,
where each sign − − denotes an arrow in either direction.
arXiv:1306.4194v4 [math.GR] 7 Dec 2017 If all the above homomorphisms are required to be injective, we call G and H strictly
commable . If all G i are required to belong to a certain class C of groups, we say that G and
H are commable (or strictly commable) within C .
For instance, for discrete groups, commensurability up to finite kernels (resp. commensu-
rability) is the same as commability (resp. strict commability) within discrete groups. On
the other hand, many discrete groups, including semidirect products Z 2 o Z occurring as
lattices in SOL, are commable but not commensurable.
Here are three (related) classical motivations for the study of commability:
Date : February 2, 2015 with incorporation of errata in § 2, December 6, 2017.
2010 Mathematics Subject Classification. Primary 20F67; Secondary 20E08, 20F65, 22D05, 22D45, 53C30,
57M07, 57S20, 57S30.
Key words and phrases. Compacting automorphisms, locally compact groups, Gromov-hyperbolic groups,
focal groups, commability, millefeuille spaces, quasi-isometric classification, topological FC-center.
1
2 YVES CORNULIER
• The quasi-isometric classification. Indeed, two commable locally compact groups
are always quasi-isometric, and many known examples of quasi-isometric groups are
actually commable by construction. A natural question, asked in an early version of
[C13] is to find two compactly generated locally compact groups (e.g., discrete) that
are quasi-isometric but not commable. Carette and Tessera checked that if Γ 1 , Γ 2
are non-commensurable cocompact lattices in, say SL 2 ( C ), then Γ 1 ∗ Z and Γ 2 ∗ Z
are not commable although they are quasi-isometric.
• The so-called study of “locally compact envelopes”. In the setting introduced by
Furman [Fu01], it consists, given some finitely generated group Γ, of classifying
locally compact groups in which Γ admits an embedding as a cocompact lattice.
However, in the setting of [Fu01], it seems that part of the methods essentially use
only the quasi-isometry class and might be modified to give a full classification of the
whole quasi-isometry class (within locally compact groups). In the realm of solvable
groups, further examples were recently obtained by Dymarz [Dy15].
• The study of “model spaces”. Indeed if G = Isom( X ) for some proper metric space
X with a cocompact isometry group, then a copci homomorphism H → G is the
same as a continuous proper cocompact isometric action of H on X . Thus two σ -
compact LC-groups H 1 , H 2 admit copci homomorphisms into the same LC-group if
and only if they have a common “model space”; this is a strong form of commability.
Certain quasi-isometry classes of groups can be described as those groups admitting
a continuous proper cocompact isometric action on a certain “model space” X . Here
we rather emphasize the group G , because the space X is sometimes less canonical
than the group itself.
Section 2 focuses on generalities about commability, especially related to the relevance of
the necessity of modding out by compact normal subgroups. It therefore involves a general
discussion on the polycompact radical W ( G ) of a locally compact group G , namely the union
of its compact normal subgroups. In many cases, this subgroup is compact, but it can also
fail to be compact, in which case its closure is also non-compact; it can also even fail to be
closed; however we use a difficult result of Trofimov to show:
Theorem 1.2. If G is a compactly generated locally compact group, then W ( G ) is a closed
subgroup.
Examples of compactly generated locally compact groups with W ( G ) not compact are easy
to exhibit (e.g., finitely generated groups with an infinite, locally finite cent
```

## candidate-14 [transport-matching] — REJECTED
CP-DRL — curriculum-learning application wrapper; optimal transport appears only inside a borrowed curriculum-optimization framework, single-machine-at-best tool usage (pass 21).

**Title:** Causal Paced Deep Reinforcement Learning

**URL:** file:///e6aaa09789da87bfbe0fc4eb11baa521bbafd91bb9cee6a6941dea1333ad6ca5/Causal-Paced_Deep_Reinforcement_Learning.pdf

**Description:** A research paper introducing Causal-Paced Deep Reinforcement Learning (CP-DRL), a curriculum learning framework that approximates Structural Causal Model (SCM) differences between tasks using only interaction data rather than requiring ground-truth causal structures. The method estimates causal misalignment via ensemble model disagreement across state, action, transition, and reward components, combining this with reward improvement signals within an optimal transport-based curriculum optimization framework. Experiments on Point Mass and Bipedal Walker benchmarks show faster convergence, higher returns, and reduced variance compared to existing curriculum methods.

**Content extract (≤6k chars):**

```
Causal-Paced Deep Reinforcement Learning
Causal-Paced Deep Reinforcement Learning
Geonwoo Cho Jaegyun Im Doyoon Kim Sundong Kim
{gwcho.public, jaegyun.public, dykim.research}@gmail.com,
sundong@gist.ac.kr
Gwangju Intsitute of Science and Technology
Abstract
Designing effective task sequences is crucial for curriculum reinforcement learning
(CRL), where agents must gradually acquire skills by training on intermediate tasks.
A key challenge in CRL is to identify tasks that promote exploration, yet are sim-
ilar enough to support effective transfer. While recent approach suggests compar-
ing tasks via their Structural Causal Models (SCMs), the method requires access to
ground-truth causal structures, an unrealistic assumption in most RL settings. In this
work, we propose Causal-Paced Deep Reinforcement Learning (CP-DRL), a curricu-
lum learning framework aware of SCM differences between tasks based on interac-
tion data approximation. This signal captures task novelty, which we combine with
the agent’s learnability, measured by reward gain, to form a unified objective. Empir-
ically, CP-DRL outperforms existing curriculum methods on the Point Mass bench-
mark, achieving faster convergence and higher returns. CP-DRL demonstrates re-
duced variance with comparable final returns in the Bipedal Walker-Trivial setting,
and achieves the highest average performance in the Infeasible variant. These results
indicate that leveraging causal relationships between tasks can improve the structure-
awareness and sample efficiency of curriculum reinforcement learning. We provide the
full implementation of CP-DRL to facilitate the reproduction of our main results at
https://github.com/Cho-Geonwoo/CP-DRL .
1 Introduction
Just as a child first learns to crawl before walking and running, intelligent behavior in complex
environments is rarely acquired in a single leap. Instead, learning unfolds through a gradual ac-
cumulation of simpler skills that scaffold more advanced capabilities. This principle underlies the
idea of curriculum learning in reinforcement learning (RL), where agents are trained on a structured
arXiv:2507.02910v1 [cs.LG] 24 Jun 2025 sequence of tasks that progressively increase in complexity (Narvekar et al., 2020; Florensa et al.,
2018; Klink et al., 2022). By mastering simpler subtasks before facing the target task, the agent can
avoid inefficient exploration and accelerate learning.
A core challenge in curriculum reinforcement learning (CRL) is to measure how tasks differ, iden-
tify what the agent has not yet learned, and expose it to novel yet transferable tasks (Hughes et al.,
2024). Existing approaches typically approximate task differences using agent-centric signals, such
as regret (Jiang et al., 2021) or value disagreement (Zhang et al., 2020), but these are inherently
policy-dependent and sensitive to noise. As a more principled alternative, Li et al. (2024) pro-
pose comparing tasks via differences in their Structural Causal Models (SCMs), enabling a policy-
independent and structure-aware measure of transferability.
While SCM-based comparison provides a principled way to quantify task differences, it relies on
access to the true causal structure, which is rarely available in realistic RL environments (Zanga
et al., 2022). In this work, we propose Causal-Paced Deep Reinforcement Learning (CP-DRL) , a
1
Causal-Paced Deep Reinforcement Learning
Task A Task B
Trajectory 1 Trajectory 1
Causal
Trajectory N Difference Trajectory K
Teacher Student
Curriculum
Figure 1: An overview of the CP-DRL. We estimate the causal difference between tasks based on
the observed trajectories in each task. This structural signal is used by the teacher to construct a
curriculum that gradually exposes the student to novel tasks.
framework that addresses this limitation by approximating the SCM difference between tasks using
only interaction data. Specifically, we estimate the differences in state, action, transition, and re-
ward components, the key constituents of SCM difference in deterministic reinforcement learning,
by measuring the disagreement across modular ensemble models. These component-wise disagree-
ments are then aggregated into a causal misalignment score, which serves to identify tasks whose
underlying causal structures remain unfamiliar to the agent. To balance novelty with learnability,
we combine the causal misalignment score with the agent’s reward improvement, yielding a unified
signal that characterizes both structural novelty and learning potential. This unified signal is then in-
corporated into an optimal transport-based curriculum optimization framework (Klink et al., 2022),
enabling the curriculum to prioritize tasks that are structurally informative yet learnable, and guide
training smoothly toward the target distribution. This process is conceptually illustrated in Figure 1.
We conduct experiments on two RL benchmarks, Point Mass (PM) and Bipedal Walker (BW),
demonstrating that CP-DRL effectively balances exploration and transfer through causal reason-
ing. In the PM environment, CP-DRL achieves the highest return and converges faster than baseline
methods. In the Bipedal Walker-Trivial setting, it achieves comparable final performance with re-
duced variance, and in the Infeasible setting, it achieves the highest mean return among all methods.
These results highlight CP-DRL’s potential to generate structure-aware curricula that enhance gen-
eralization and sample efficiency in complex reinforcement learning environments.
2 Preliminary
2.1 Markov Decision Process and Contextual RL for curriculum learning
We assume each task or environment can be modeled as a Markov Decision Process (MDP) M ,
defined by the tuple ⟨S , A , p, r, γ ⟩ , where S is the state space, A the action space, p ( s ′ | s, a )
with s, s ′ ∈ S and a ∈ A the transition probability function, r ( s, a ) the reward function, and
γ ∈ [0 , 1) the discount factor. The solution to an MDP is an optimal policy P π ( a |
```

## candidate-15 [info-machines] — ANNOTATED as 2305.18887 (promote-on-encounter: duplicate — full annotation already lived in the historical ledger cross_domain_bridges.md plus summary rows in four index files; block migrated verbatim to annotations/2305.18887.md, crossrefs repointed, pass 22)

**Title:** How Does Information Bottleneck Help Deep Learning

**URL:** file:///b0211af1f6ffea4585c53a0f02c2135039bbb66048fff3f46cccb3118cc8e160/How_Does_Information_Bottleneck_Help_Deep_Learning.pdf

**Description:** A theoretical machine learning paper that provides the first rigorous generalization bounds justifying why the information bottleneck principle helps deep learning. The authors prove that controlling mutual information between input and hidden representations bounds generalization error, resolving an open conjecture by Shwartz-Ziv et al. (2019) and extending it to the practical case where encoders are learned from training data. Experiments across multiple architectures validate that empirical estimates of their bound factors strongly predict generalization gaps.

**Content extract (≤6k chars):**

```
How Does Information Bottleneck Help Deep Learning?
Kenji Kawaguchi * 1 Zhun Deng * 2 Xu Ji * 3 Jiaoyang Huang 4
Abstract
Numerous deep learning algorithms have been
inspired by and understood via the notion of in-
formation bottleneck, where unnecessary infor-
mation is (often implicitly) minimized while task-
relevant information is maximized. However, a
rigorous argument for justifying why it is desir-
able to control information bottlenecks has been
elusive. In this paper, we provide the first rig-
orous learning theory for justifying the benefit
of information bottleneck in deep learning by Figure 1. Illustration of X , Y and Z . This paper studies the rela-
mathematically relating information bottleneck tionship between performances of deep neural networks and the
to generalization errors. Our theory proves that mutual information between X and Z . Our theory proves that
controlling information bottleneck is one way to controlling this mutual information is one way to control perfor-
control generalization errors in deep learning, al- mances in deep learning, although it is not the necessary way.
though it is not the only or necessary way. We
investigate the merit of our new mathematical
findings with experiments across a range of ar- minimal sufficient statistics for extracting information about
chitectures and learning settings. In many cases, target Y ∈ Y into representation Z = ϕ ( X ) ∈ Z from
generalization errors are shown to correlate with input X ∈ X . An information bottleneck imposes regu-
the degree of information bottleneck: i.e., the larization at representation Z by minimizing the mutual
amount of the unnecessary information at hidden information between X and Z , I ( X ; Z ) , while maximizing
layers. This paper provides a theoretical founda- the mutual information between Y and Z , I ( Y ; Z ) .
tion for current and future methods through the In practice I ( X ; Z ) is often minimized implicitly, e.g. as
lens of information bottleneck. Our new gener- a result of stochastic gradient descent (SGD) or an archi-
alization bounds scale with the degree of infor- tecture choice (Shwartz-Ziv & Tishby, 2017). An explicit
mation bottleneck, unlike the previous bounds minimization of I ( X ; Z ) has been also adopted in the ma-
that scale with the number of parameters, VC chine learning literature as a regularization technique (Alemi
dimension, Rademacher complexity, stability or et al., 2016; 2018), where the mutual information is either
robustness. Our code is publicly available at: estimated by averaging log probabilities of latent represen-
https://github.com/xu-ji/information-bottleneck tations over empirical samples or replaced by a tractable
arXiv:2305.18887v1 [cs.LG] 30 May 2023 upper bound (Kirsch et al., 2020; Kolchinsky & Tracey,
2017; Alemi et al., 2016). More generally, the notion of
1. Introduction bottlenecks on representation expressivity has been used in
The information bottleneck principle (Tishby et al., 1999; work on structural inductive biases (Goyal & Bengio, 2022).
Slonim & Tishby, 2000) has been a great concept in balanc- Consequently, understanding the connection between the
ing the trade-off between the complexity of representation information bottleneck regularizer I ( X ; Z ) and the general-
and the power of predicting. It is based on the notion of ization ability of machine learning models has become an
* active area of research. Given its importance, Shwartz-Ziv
Equal contribution. Author ordering determined by coin flip.
1 NUS 2 Columbia University 3 Mila 4 University of Pennsylvania. et al. (2019) provided the following conjecture:
Correspondence to: Kenji Kawaguchi < kenji@nus.edu.sg > . Conjecture 1. ( Informal version (Shwartz-Ziv et al., 2019))
Proceedings of the 40 th International Conference on Machine With probability at least 1 − δ over the training data
Learning , Honolulu, Hawaii, USA. PMLR 202, 2023. Copyright s = { ( x i , y i ) } n
i =1 drawn from the same distribution as a
2023 by the author(s). random variable pair ( X, Y ) , for the generalization error
1
How Does Information Bottleneck Help Deep Learning?
P n
∆( s ) = E X,Y [ ℓ ( f s ( X ) , Y )] − 1 s
n i =1 ℓ ( f ( x i ) , y i ) , there “ How does information bottleneck help deep learning from
is a bound obeys the following form: the perspective of statistical learning theory? ”
s
s
2 I ( X ; Z l ) + log 2 As our first contribution , we resolve this open question by
∆( s ) ≤ δ , (1) providing novel and complete proofs for end-to-end learn-
2 n 
ing of intermediate representations (Theorem 2). To the
where f s is the full model obtained by training and Z s
l = best of our knowledge, we provide the first rigorous gen-
ϕ s
l ( X ) is the output of the an intermediate l -layer encoder eralization bound for information bottleneck in the case of
ϕ s
l of the model, i.e. representation obtained after passing learning representations, showing that simplicity in both the
through the first l layers. representation and representation function are factors that
support generalization.
However, this appealing conjecture cannot be applied to
explain the success of information bottleneck principle in As our second contribution , an intermediate step and
practice. First, the proof of the bound in this conjecture is in- byproduct of our novel proof for Theorem 2 not only com-
complete . More importantly, as pointed out by Hafez-Kolahi pletes the proof of Conjecture 1, where Z is treated as fixed
et al. (2020), there is a critical drawback in the formulation random variable and independent of the training data s , it
of this conjecture: Shwartz-Ziv et al. (2019) implicitly as- also significantly improve the previous bound in the conjec-
sumes the independence of Z s
l and s in the arguments of ture. We show the generalization error roughly (with high
this conjecture, which means that they treated the encoder probability) as
ϕ s
l as fixed and independent of training data s . Indeed, r !
I ( X 
```

## candidate-16 [info-machines] — ANNOTATED as 10.3390-e24030403 (promote-on-encounter: duplicate — already covered as full prose block PID-01 in by-domain/information_theory.md; block migrated verbatim to annotations/, pass 22)

**Title:** A Novel Approach to the Partial Information Decomposition

**URL:** file:///88fc3bb6b3a2be3f3565cd91553a24379f3410efb668549fd4ebc26796092571/A_Novel_Approach_to_the_Partial_Information_Decomposition.pdf

**Description:** A peer-reviewed research paper proposing a principled framework for Partial Information Decomposition (PID), which decomposes the mutual information that source random variables provide about a target into redundant, synergistic, union, and unique components. The framework is grounded in a formal analogy with set-theoretic intersection and union, parameterized by an ordering relation over information sources, and is instantiated using the Blackwell order to yield operationally interpretable measures with connections to decision theory.

**Content extract (≤6k chars):**

```
entropy
Article
A Novel Approach to the Partial Information Decomposition
Artemy Kolchinsky
Santa Fe Institute, Santa Fe, NM 87501, USA; artemyk@gmail.com
Abstract: We consider the “partial information decomposition” (PID) problem, which aims to decom-
pose the information that a set of source random variables provide about a target random variable
into separate redundant, synergistic, union, and unique components. In the first part of this paper,
we propose a general framework for constructing a multivariate PID. Our framework is defined in
terms of a formal analogy with intersection and union from set theory, along with an ordering relation
which specifies when one information source is more informative than another. Our definitions
are algebraically and axiomatically motivated, and can be generalized to domains beyond Shannon
information theory (such as algorithmic information theory and quantum information theory). In the
second part of this paper, we use our general framework to define a PID in terms of the well-known
Blackwell order, which has a fundamental operational interpretation. We demonstrate our approach on
numerous examples and show that it overcomes many drawbacks associated with previous proposals.
Keywords: partial information decomposition; redundancy; synergy
1. Introduction
Understanding how information is distributed in multivariate systems is an important
problem in many scientific fields. In the context of neuroscience, for example, one may wish to
understand how information about an external stimulus is encoded in the activity of different
  brain regions. In computer science, one might wish to understand how the output of a logic

gate reflects the information present in different inputs to that gate. Numerous other examples
Citation: Kolchinsky, A. A Novel abound in biology, physics, machine learning, cryptography, and other fields [1–10].
Approach to the Partial Information
Formally, suppose that we are provided with a random variable Y which we call the
Decomposition. Entropy 2022 , 24 , 403.
“target”, as well as a set of n random variables X 1 , . . . , X
https://doi.org/10.3390/e24030403 n which we call the “sources”. The
partial information decomposition (PID), first proposed by Williams and Beer in 2010 [ 11 ], aims
Academic Editor: Eckehard Olbrich to quantify how information about the target is distributed among the different sources.
Received: 4 January 2022 In particular, the PID seeks to decompose the mutual information provided jointly by
Accepted: 23 February 2022 all sources into a set of nonnegative terms, such as redundancy (information present in
Published: 13 March 2022 each individual source), synergy (information only provided by the sources jointly, not
individually), union information (information provided by at least one individual source),
Publisher’s Note: MDPI stays neutral and unique information (information provided by only one individual source).
with regard to jurisdictional claims in As discussed in detail below, the PID is inspired by an analogy between information
published maps and institutional affil- theory and set theory. In this analogy, the information that the sources provide about the
iations.
target are imagined as sets, while PID terms such as redundancy, union information, and
synergy are imagined as the sizes of intersections, unions, and complements. While the
analogy between information-theoretic and set-theoretic quantities is suggestive, it does
Copyright: © 2022 by the author. not specify how to actually define the PID. Moreover, it has also been shown that existing
Licensee MDPI, Basel, Switzerland. measures from information theory (such as mutual information and conditional mutual
This article is an open access article information) cannot be used directly to construct the PID, since these measures conflate
distributed under the terms and contributions from different terms like synergy and redundancy [ 11 , 12 ]. In response, many
conditions of the Creative Commons proposals for how to define PID terms have been advanced [ 5 , 13 – 21 ]. However, existing
Attribution (CC BY) license (https:// proposals suffer from various drawbacks, such as behaving counterintuitively on simple
creativecommons.org/licenses/by/ examples, being limited to only two sources, or lacking a clear operational interpretation.
4.0/). Today there is no generally agreed-upon way of defining the PID.
Entropy 2022 , 24 , 403. https://doi.org/10.3390/e24030403 https://www.mdpi.com/journal/entropy
Entropy 2022 , 24 , 403 2 of 34
In this paper, we propose a new and principled approach to the PID which addresses
these drawbacks. Our approach can handle any number of sources and can be justified in
algebraic, axiomatic, and operational terms. We present our approach in two parts.
In part I (Section 4), we propose a general framework for defining the PID. Our
framework does not prescribe specific definitions, but instead shows how an information-
theoretic decomposition can be grounded in a formal analogy with set theory. Specifically,
we consider the definitions of “set intersection” and “set union” in set theory: the intersec-
tion of sets S 1 , S 2 , . . . is the largest set that is contained in all of the S i , while the union of
sets S 1 , S 2 , . . . is the smallest set that contains all of the S i . As we show, these set-theoretic
definitions can be mapped into information-theoretic terms by treating “sets” as random
variables, “set size” as mutual information between a random variable and the target Y ,
and “set inclusion” as some externally specified ordering relation < , which specifies when
one random variable is more informative than another. Using this mapping, we define
information-theoretic redundancy and union information in the same way that the sizes
of intersections and unions are defined in set theory (other PID terms, such as synergy
and unique information, can be computed in a straightforward way from redunda
```

## candidate-17 [info-machines] — ANNOTATED as 1801.04062 (promote-on-encounter: duplicate — MINE itself, already covered as full prose block in by-domain/information_theory.md; block migrated verbatim to annotations/1801.04062.md, pass 22)

**Title:** MINE Mutual Information Neural Estimation

**URL:** file:///ebf2a6df3db08df06f512f08cfe7d09715f746c5b6a82c4a3b8423138d031896/MINE_Mutual_Information_Neural_Estimation.pdf

**Description:** This ICML 2018 paper introduces MINE (Mutual Information Neural Estimator), a neural network-based approach for estimating mutual information between high-dimensional continuous random variables using dual representations of the KL-divergence (Donsker-Varadhan and f-divergence bounds). The estimator is linearly scalable in both dimensionality and sample size, trainable via backpropagation, and strongly consistent, with applications demonstrated in improving GANs against mode-dropping, enhancing Adversarially Learned Inference, and implementing the continuous Information Bottleneck for supervised classification.

**Content extract (≤6k chars):**

```
Mutual Information Neural Estimation
Mohamed Ishmael Belghazi 1 Aristide Baratin 1 2 Sai Rajeswar 1 Sherjil Ozair 1 Yoshua Bengio 1 3 4
Aaron Courville 1 3 R Devon Hjelm 1 4
Abstract trast to correlation, mutual information captures non-linear
We argue that the estimation of mutual informa- statistical dependencies between variables, and thus can act
tion between high dimensional continuous ran- as a measure of true dependence (Kinney & Atwal, 2014).
dom variables can be achieved by gradient descent Despite being a pivotal quantity across data science, mutual
over neural networks. We present a Mutual Infor- information has historically been difficult to compute (Panin-
mation Neural Estimator (MINE) that is linearly ski, 2003). Exact computation is only tractable for discrete
scalable in dimensionality as well as in sample variables (as the sum can be computed exactly), or for a
size, trainable through back-prop, and strongly limited family of problems where the probability distribu-
consistent. We present a handful of applications tions are known. For more general problems, this is not
on which MINE can be used to minimize or max- possible. Common approaches are non-parametric (e.g.,
imize mutual information. We apply MINE to im- binning, likelihood-ratio estimators based on support vector
prove adversarially trained generative models. We machines, non-parametric kernel-density estimators; see,
also use MINE to implement the Information Bot- Fraser & Swinney, 1986; Darbellay & Vajda, 1999; Suzuki
tleneck, applying it to supervised classification; et al., 2008; Kwak & Choi, 2002; Moon et al., 1995; Kraskov
our results demonstrate substantial improvement et al., 2004), or rely on approximate gaussianity of data
in flexibility and performance in these settings. distribution (e.g., Edgeworth expansion, Van Hulle, 2005).
Unfortunately, these estimators typically do not scale well
with sample size or dimension (Gao et al., 2014), and thus
1. Introduction cannot be said to be general-purpose. Other recent works
Mutual information is a fundamental quantity for measuring include Kandasamy et al. (2017); Singh & P oczos (2016); ´
the relationship between random variables. In data science Moon et al. (2017).
it has found applications in a wide range of domains and In order to achieve a general-purpose estimator, we rely
tasks, including biomedical sciences (Maes et al., 1997), on the well-known characterization of the mutual informa-
blind source separation (BSS, e.g., independent component tion as the Kullback-Leibler (KL-) divergence (Kullback,
analysis, Hyv arinen et al., 2004), information bottleneck (IB, ¨ 1997) between the joint distribution and the product of the
Tishby et al., 2000), feature selection (Kwak & Choi, 2002; marginals (i.e., I ( X ; Z ) = D KL ( P XZ || P X ⊗ P Z ) ). Re-
Peng et al., 2005), and causality (Butte & Kohane, 2000). cent work uses a dual formulation to cast the estimation of
Put simply, mutual information quantifies the dependence f -divergences (including the KL-divergence, see Nguyen
of two random variables X and Z . It has the form, et al., 2010) as part of an adversarial game between com-
∫ peting deep neural networks (Nowozin et al., 2016). This
arXiv:1801.04062v5 [cs.LG] 14 Aug 2021 d P XZ
I ( X ; Z ) = log d P XZ , (1) approach is at the cornerstone of generative adversarial net-
X ×Z d P X ⊗ P Z works (GANs, Goodfellow et al., 2014), which train a
where generative model without any explicit assumptions about
∫ P XZ is the joint probability distribution, and ∫ P X =
Z d P XZ and P Z = the underlying distribution of the data.
X d P XZ are the marginals. In con-
1 In this paper we demonstrate that exploiting dual optimiza-
Montr eal ´ Institute for Learning Algorithms (MILA),
University of Montr eal ´ 2 Department of Mathematics and tion to estimate divergences goes beyond the minimax ob-
Statistics, McGill University 3 Canadian Institute for Ad- jective as formalized in GANs. We leverage this strategy
vanced Research (CIFAR) 4 The Institute for Data Valorization to offer a general-purpose parametric neural estimator of
(IVADO). Correspondence to: Mohamed Ishmael Belghazi < ish- mutual information based on dual representations of the
mael.belghazi@gmail.com > . KL-divergence (Ruderman et al., 2012), which we show
Proceedings of the 35 th International Conference on Machine is valuable in settings that do not necessarily involve an
Learning , Stockholm, Sweden, PMLR 80, 2018. Copyright 2018 adversarial game. Our estimator is scalable, flexible, and
by the author(s). completely trainable via back-propagation. The contribu-
Mutual Information Neural Estimation
tions of this paper are as follows: 2.2. Dual representations of the KL-divergence.
A key technical ingredient of MINE are dual representa-
• We introduce the Mutual Information Neural Estimator
tions of the KL-divergence. We will primarily work with
(MINE), which is scalable, flexible, and completely
the Donsker-Varadhan rep
```

## candidate-18 [info-machines] — UNCONSUMED

**Title:** CCMI Classifier based Conditional Mutual Information Estimation

**URL:** file:///1fb249a1ca7c1aaef51bb24a7e29166e03dbb45bfee95e912243943b0aafb1b7/CCMI_Classifier_based_Conditional_Mutual_Information_Estimation.pdf

**Description:** This research paper introduces CCMI, a family of classifier-based estimators for Conditional Mutual Information (CMI) that leverage neural classifiers and conditional generative models (CGANs, CVAEs) to overcome the curse of dimensionality plaguing traditional k-nearest-neighbor and kernel-based methods. The authors propose both divergence-based and difference-based CMI estimation approaches, demonstrating that their estimators maintain accuracy up to 100 dimensions where the widely-used KSG estimator fails beyond 5, and achieve state-of-the-art conditional independence testing on synthetic and real datasets.

**Content extract (≤6k chars):**

```
CCMI : Classifier based Conditional Mutual Information Estimation
Sudipto Mukherjee, Himanshu Asnani, Sreeram Kannan
Department of Electrical and Computer Engineering,
University of Washington, Seattle, WA.
{sudipm, asnani, ksreeram}@uw.edu
Abstract conditional mutual information is defined as:
∫ ∫ ∫
p ( x, y, z )
I ( X ; Y | Z ) = p ( x, y, z ) log dxdydz
Conditional Mutual Information (CMI) is a p ( x, z ) p ( y | z ) 
measure of conditional dependence between
random variables X and Y, given another ran- assuming that the distributions admit the respective den-
dom variable Z. It can be used to quantify con- sities p ( · ) . One of the striking features of MI and CMI is
ditional dependence among variables in many that they can capture non-linear dependencies between
data-driven inference problems such as graph- the variables. In scenarios where Pearson correlation
ical models, causal learning, feature selec- is zero even when the two random variables are depen-
tion and time-series analysis. While k-nearest dent, mutual information can recover the truth. Like-
neighbor ( k NN) based estimators as well as wise, in the sense of conditional independence for the
kernel-based methods have been widely used case of three random variables X , Y and Z , conditional
for CMI estimation, they suffer severely from mutual information provides strong guarantees, i.e., X ⊥
the curse of dimensionality. In this paper, we Y | Z ⇐⇒ I ( X ; Y | Z ) = 0 .
leverage advances in classifiers and genera-
tive models to design methods for CMI esti- The conditional setting is even more interesting as de-
mation. Specifically, we introduce an estima- pendence between X and Y can potentially change based
tor for KL-Divergence based on the likelihood on how they are connected to the conditioning variable.
ratio by training a classifier to distinguish the For instance, consider a simple Markov chain where
observed joint distribution from the product X → Z → Y . Here, X ⊥ Y | Z . But a slightly dif-
distribution. We then show how to construct ferent relation X → Z ← Y has X  6 ⊥ Y | Z , even though
several CMI estimators using this basic diver- X and Y may be independent as a pair. It is a well known
gence estimator by drawing ideas from condi- fact in Bayesian networks that a node is independent of
tional generative models. We demonstrate that its non-descendants given its parents. CMI goes beyond
the estimates from our proposed approaches stating whether the pair ( X, Y ) is conditionally depen-
arXiv:1906.01824v1 [cs.LG] 5 Jun 2019 do not degrade in performance with increasing dent or not. It also provides a quantitative strength of
dimension and obtain significant improvement dependence.
over the widely used KSG estimator. Finally, 1.1 Prior Art
as an application of accurate CMI estimation,
The literature is replete with works aimed at apply-
we use our best estimator for conditional inde-
ing CMI for data-driven knowledge discovery. Fleuret
pendence testing and achieve superior perfor-
(2004) used CMI for fast binary feature selection to im-
mance than the state-of-the-art tester on both
prove classification accuracy. Loeckx et al. (2010) im-
simulated and real data-sets.
proved non-rigid image registration by using CMI as a
similarity measure instead of global mutual information.
1 Introduction
CMI has been used to infer gene-regulatory networks
Conditional mutual information (CMI) is a fundamental (Liang and Wang 2008) or protein modulation (Giorgi
information theoretic quantity that extends the nice prop- et al. 2014) from gene expression data. Causal discovery
erties of mutual information (MI) in conditional settings. (Li et al. 2011; Hlinka et al. 2013; Vejmelka and Paluš
For three continuous random variables, X , Y and Z , the 2008) is yet another application area of CMI estimation.
Despite its wide-spread use, estimation of conditional approach that is more stable and performs superior to the
mutual information remains a challenge. One naive recent neural methods (Belghazi et al. 2018).
method may be to estimate the joint and conditional den- Divergence Based CMI Estimation: We express CMI
sities from data and plug it into the expression for CMI. as the KL-divergence between two distributions p xyz =
But density estimation is not sample efficient and is of- p ( z ) p ( x | z ) p ( y | x, z ) and q xyz = p ( z ) p ( x | z ) p ( y | z ) , and
ten more difficult than estimating the quantities directly. explore candidate generators for obtaining samples from
The most widely used technique expresses CMI in terms q ( · ) . The CMI estimate is then obtained from the diver-
of appropriate arithmetic of differential entropy estima- gence estimator.
tors (referred to here as Σ H estimator): I ( X ; Y | Z ) = Difference Based CMI Estimation: Using the im-
h ( ∫ X, Z )+ h ( Y, Z ) − h ( Z ) − h ( X, Y, Z ) , where h ( X ) = proved MI estimates, and the difference relation
− p ( x ) log p ( x ) dx is known as the differential entropy. I ( X ; Y | Z ) = I ( X ; Y Z ) − I ( X ; Z ) , we show that es-
X timating CMI using a difference of two MI estimates
The differential entropy estimation problem has been performs best among several other proposed methods in
studied extensively by Beirlant et al. (1997); Nemen- this paper such as divergence based CMI estimation and
man et al. (2002); Miller (2003); Lee (2010); Le´ sniewicz KSG.
(2014); Sricharan et al. (2012); Singh and Póczos (2014) Improved Performance in High Dimensions: On both
and can be estimated either based on kernel-density linear and non-linear data-sets, all our estimators per-
(Kandasamy et al. 2015; Gao et al. 2016) or k -nearest- form significantly better than KSG. Surprisingly, our es-
neighbor estimates (Sricharan et al. 2013; Jiao et al. timators perform well even for dimensions as high as
2018; Pál et al. 2010; Kozachenko and Leonenko 1987; 100 , while KSG fails to obtain reasonable estimates even
Singh et al. 2003; Singh and Póczos 2016). Build- beyond 
```

## candidate-19 [info-machines] — UNCONSUMED

**Title:** Cauchy Schwarz Divergence Information Bottleneck for Regression

**URL:** file:///fa109b021a9651849606f31eea19df6477acfbb0ebd372199890b6893d7ab14d/Cauchy-Schwarz_Divergence_Information_Bottleneck_for_Regression.pdf

**Description:** This ICLR 2024 paper proposes CS-IB, a new parameterization of the information bottleneck principle for regression using Cauchy-Schwarz divergence instead of KL divergence. By replacing MSE loss with a CS-divergence prediction term and using closed-form CS quadratic mutual information for compression, the method avoids distributional assumptions and variational approximations. CS-IB achieves superior generalization, adversarial robustness, and optimal prediction-compression trade-offs on six benchmark regression datasets compared to five existing deep IB approaches.

**Content extract (≤6k chars):**

```
Published as a conference paper at ICLR 2024
C AUCHY -S CHWARZ D IVERGENCE I NFORMATION B OT -
TLENECK FOR R EGRESSION
Shujian Yu 1 , 3 Xi Yu 2 Sigurd Løkse 4 Robert Jenssen 3 , 6 Jose C. Principe 5
1 Vrije Universiteit Amsterdam 2 Brookhaven National Laboratory
3 UiT - The Arctic University of Norway 4 NORCE Norwegian Research Centre
5 University of Florida 6 University of Copenhagen
s.yu3@vu.nl ; xyu1@bnl.gov ; sigl@norceresearch.no
robert.jenssen@uit.no ; principe@cnel.ufl.edu
A BSTRACT
The information bottleneck (IB) approach is popular to improve the generaliza-
tion, robustness and explainability of deep neural networks. Essentially, it aims
to find a minimum sufficient representation t by striking a trade-off between a
compression term I ( x ; t ) and a prediction term I ( y ; t ) , where I ( · ; · ) refers to the
mutual information (MI). MI is for the IB for the most part expressed in terms of
the Kullback-Leibler (KL) divergence, which in the regression case corresponds
to prediction based on mean squared error (MSE) loss with Gaussian assumption
and compression approximated by variational inference. In this paper, we study
the IB principle for the regression problem and develop a new way to parameterize
the IB with deep neural networks by exploiting favorable properties of the Cauchy-
Schwarz (CS) divergence. By doing so, we move away from MSE-based regression
and ease estimation by avoiding variational approximations or distributional as-
sumptions. We investigate the improved generalization ability of our proposed
CS-IB and demonstrate strong adversarial robustness guarantees. We demonstrate
its superior performance on six real-world regression tasks over other popular deep
IB approaches. We additionally observe that the solutions discovered by CS-IB
always achieve the best trade-off between prediction accuracy and compression
ratio in the information plane. The code is available at https://github.com
/SJYuCNEL/Cauchy-Schwarz-Information-Bottleneck .
1 I NTRODUCTION
The information bottleneck (IB) principle was proposed by (Tishby et al., 1999) as an information-
theoretic framework for representation learning. It considers extracting information about a target
variable y through a correlated variable x . The extracted information is characterized by another
variable t , which is (a possibly randomized) function of x . Formally, the IB objective is to learn a
arXiv:2404.17951v1 [cs.LG] 27 Apr 2024 representation t that maximizes its predictive power to y subject to some constraints on the amount
of information that it carries about x :
max I ( y ; t ) s.t. I ( x ; t ) ≤ R, (1)
p ( t | x ) 
where I ( · ; · ) denotes the mutual information. By introducing a Lagrange multiplier β > 0 , t is found
by optimizing a so-called IB Lagrangian (Gilad-Bachrach et al., 2003; Shamir et al., 2010):
min − I ( y ; t ) + βI ( x ; t ) . (2)
p ( t | x ) 
Maximizing I ( y ; t ) ensures the sufficiency of t to predict y , whereas minimizing I ( x ; t ) encourages
the minimality (or complexity) of t and prevents it from encoding irrelevant bits. The parameter β
controls the fundamental tradeoff between these two information terms. In this sense, the IB principle
also provides a natural approximation of minimal sufficient statistic (Gilad-Bachrach et al., 2003).
Traditionally, the IB principle and its variants (e.g., (Strouse & Schwab, 2017; Creutzig et al.,
2009)) have found applications in document clustering (Slonim & Tishby, 2000), image segmen-
tation (Bardera et al., 2009), biomolecular modeling (Wang et al., 2019), etc. Recent studies have
1
Published as a conference paper at ICLR 2024
established close connections between IB and DNNs, especially in a supervised learning scenario.
In this context, x denotes input feature vectors, y denotes desired response such as class labels,
and t refers to intermediate latent representations or activations of hidden layers. Theoretically, it
was observed that the layer representation t undergoes two separate training phases: a fitting or
memorization phase in which both I ( x ; t ) and I ( y ; t ) increase, and a compression phase in which
I ( x ; t ) decreases while I ( y ; t ) continues to increase or remains consistent (see (Shwartz-Ziv &
Tishby, 2017; Saxe et al., 2018; Chelombiev et al., 2019; Yu et al., 2020; Lorenzen et al., 2022) for a
series of work in this direction; although the argument itself is still under a debate). The existence of
compression also provides new insights to the generalization behavior of DNNs (Wang et al., 2022;
Kawaguchi et al., 2023). Practically, the intermediate representations learned with the IB objective
have been demonstrated to be more robust to adversarial attacks (Wang et al., 2021; Pan et al., 2021)
and distributional shift (Ahuja et al., 2021). In a parallel line of research (Bang et al., 2021; Kim et al.,
2021), the IB approach has been leveraged to identify the most informative features (to a certain
decision) by learning a differentiable mask m on the input, i.e., t = x ⊙ m , in which ⊙ refers to
element-wise product.
Unfortunately, optimizing the IB Lagrangian remains a challenge due to its computational intractabil-
ity. Although scalable methods of IB are feasible thanks to variational bounds of mutual informa-
tion (Alemi et al., 2017; Kolchinsky et al., 2019b; Poole et al., 2019) as well as Gaussian or discrete
data assumptions (Chechik et al., 2003; Tishby et al., 1999), the choice of such bounds, the imposed
data distributional assumptions, as well as specific details on their implementations may introduce
strong inductive bias that competes with the original objective (Ngampruetikorn & Schwab, 2023).
In this paper, we propose a new method for performing nonlinear IB on arbitrarily distributed p ( x , y ) ,
by exploiting favorable properties of the Cauchy-Schwarz (CS) divergence (Principe et al., 2000;
Yu et al., 2023). We focus our attention on the regression setup, which is far less investigated tha
```

## candidate-20 [info-machines] — ANNOTATED as 1909.11396 (promote-on-encounter: duplicate — already covered as full prose block in by-domain/information_theory.md plus summary rows in composite_systems/filtrations indices; block migrated verbatim to annotations/1909.11396.md, crossrefs repointed, pass 22)

**Title:** Information Plane Analysis of Deep Neural Networks via Matrix Based Renyis Entro

**URL:** file:///38bf00819eb0e93b55441596bf92e45d276f59f28cd09dead9b243e43a0463b2/Information_Plane_Analysis_of_Deep_Neural_Networks_via_Matrix-Based_Renyis_Entro.pdf

**Description:** A research paper proposing a novel mutual information estimator based on matrix-based Rényi's entropy coupled with tensor kernels for analyzing deep neural networks in the information plane. The method overcomes dimensionality limitations of prior estimators, enabling the first comprehensive information plane analysis of large-scale architectures like VGG-16. Key findings indicate the compression phase is primarily observed on training data and is linked to overfitting, as early stopping typically halts training before compression occurs.

**Content extract (≤6k chars):**

```
I NFORMATION P LANE A NALYSIS OF D EEP N EURAL
N ETWORKS VIA M ATRIX –B ASED R ´ ENYI ’ S E NTROPY
AND T ENSOR K ERNELS
Kristoffer Wickstrøm ∗ , 1 , Sigurd Løkse 1 , Michael Kampffmeyer 1 , Shujian Yu 2 , Jose Principe 2 , and
Robert Jenssen 1
1 Department of Physics and Technology, UiT The Arctic University of Norway
2 Computational NeuroEngineering Laboratory, Department of Electrical and Computer
Engineering, University of Florida
A BSTRACT
Analyzing deep neural networks (DNNs) via information plane (IP) theory has
gained tremendous attention recently as a tool to gain insight into, among others,
their generalization ability. However, it is by no means obvious how to estimate
mutual information (MI) between each hidden layer and the input/desired output,
to construct the IP. For instance, hidden layers with many neurons require MI
estimators with robustness towards the high dimensionality associated with such
layers. MI estimators should also be able to naturally handle convolutional layers,
while at the same time being computationally tractable to scale to large networks.
None of the existing IP methods to date have been able to study truly deep Con-
volutional Neural Networks (CNNs), such as the e.g. VGG-16. In this paper, we
propose an IP analysis using the new matrix–based R´ enyi’s entropy coupled with
tensor kernels over convolutional layers, leveraging the power of kernel methods
to represent properties of the probability distribution independently of the dimen-
sionality of the data. The obtained results shed new light on the previous literature
concerning small-scale DNNs, however using a completely new approach. Im-
portantly, the new framework enables us to provide the first comprehensive IP
analysis of contemporary large-scale DNNs and CNNs, investigating the different
training phases and providing new insights into the training dynamics of large-
scale neural networks.
1 I NTRODUCTION
Although Deep Neural Networks (DNNs) are at the core of most state–of–the art systems in com-
puter vision, the theoretical understanding of such networks is still not at a satisfactory level
arXiv:1909.11396v1 [stat.ML] 25 Sep 2019 (Shwartz-Ziv & Tishby, 2017). In order to provide insight into the inner workings of DNNs, the
prospect of utilizing the Mutual Information (MI), a measure of dependency between two random
variables, has recently garnered a significant amount of attention (Cheng et al., 2018; Noshad et al.,
2019; Saxe et al., 2018; Shwartz-Ziv & Tishby, 2017; Yu et al., 2018; Yu & Principe, 2019). Given
the input variable X and the desired output Y for a supervised learning task, a DNN is viewed as
a transformation of X into a representation that is favorable for obtaining a good prediction of Y .
By treating the output of each hidden layer as a random variable T , one can model the MI I ( X ; T )
between X and T . Likewise, the MI I ( T ; Y ) between T and Y can be modeled. The quanti-
ties I ( X ; T ) and I ( T ; Y ) span what is referred to as the Information Plane (IP). Several works have
demonstrated that one may unveil interesting properties of the training dynamics by analyzing DNNs
in the form of the IP. Figure 1, produced using our proposed estimator, illustrates one such insight
that is similar to the observations of Shwartz-Ziv & Tishby (2017), where training can be separated
into two distinct phases, the fitting phase and the compression phase. This claim has been highly
∗ Corresponding author: kristoffer.k.wickstrom@uit.no. Wickstrøm, Løkse, Kampffmeyer and Jenssen are
all at the UiT Machine Learning Group (https://machine-learning.uit.no/)
1
debated as subsequent research has linked the compression phase to saturation of neurons (Saxe
et al., 2018) or clustering of the hidden representations (Goldfeld et al., 2019).
Contributions We propose a novel approach for estimating MI, wherein a kernel tensor-based
estimator of R´ enyi’s entropy allows us to provide the first analysis of large-scale DNNs as com-
monly found in state-of-the-art methods. We further highlight that the multivariate matrix–based
approach, proposed by Yu et al. (2019), can be viewed as a special case of our approach. How-
ever, our proposed method alleviates numerical instabilities associated with the multivariate matrix–
based approach, which enables estimation of entropy for high-dimensional multivariate data. Fur-
ther, using the proposed estimator, we investigate the claim of Cheng et al. (2018) that the entropy
H ( X ) ≈ I ( T ; X ) and H ( Y ) ≈ I ( T ; Y ) in high dimensions (in which case MI-based analysis
would be meaningless) and illustrate that this does not hold for our estimator. Finally, our results
indicate that the compression phase is apparent mostly for the training data, particularly for more
challenging datasets. By utilizing a technique such as early-stopping, a common technique to avoid
overfitting, training tends to stop before the compression phase occurs (see Figure 1). This may
indicate that the compression phase is linked to the overfitting phenomena.
Figure 1: IP obtained using our proposed estimator for a small DNN averaged over 5 training runs.
The solid black line illustrates the fitting phase while the dotted black line illustrates the compres-
sion phase. The iterations at which early stopping would be performed assuming a given patience
parameter are highlighted. Here, patience denotes the number of iterations that need to pass without
progress on a validation set before training is stopped to avoid overfitting. It can be observed that for
low patience values, training will stop before the compression phase. For the benefit of the reader,
the bottom right corner displays a magnified version of the first four layers.
2 R ELATED W ORK
Analyzing DNNs in the IP was first proposed by Tishby & Zaslavsky (2015) and later demonstrated
by Shwartz-Ziv & Tishby (2017). Among other results, the authors studied the evolution of the
IP during the training process of DNNs and not
```

## candidate-21 [stability-bounds] — UNCONSUMED

**Title:** PAC Bayes meta learning with implicit task specific posteriors

**URL:** file:///42fcc13ac01f78b7d961edf224ccfe88ccefcb4939c60b506a6c32e027cd046f/PAC-Bayes_meta-learning_with_implicit_task-specific_posteriors.pdf

**Description:** A research paper that extends the PAC-Bayes framework from single-task to meta-learning settings, deriving rigorous generalization bounds that upper-bound errors on arbitrary unseen tasks and samples. The authors propose implicit generative modeling of task-specific posteriors as a more expressive alternative to diagonal Gaussian variational distributions, achieving state-of-the-art calibration and classification accuracy on mini-ImageNet, tiered-ImageNet, and multi-modal regression benchmarks.

**Content extract (≤6k chars):**

```
1
PAC-Bayes Meta-learning with Implicit
Task-specific Posteriors
Cuong Nguyen , Thanh-Toan Do, and Gustavo Carneiro
Abstract —We introduce a new and rigorously-formulated PAC-Bayes meta-learning algorithm that solves few-shot learning. Our
proposed method extends the PAC-Bayes framework from a single task setting to the meta-learning multiple task setting to
upper-bound the error evaluated on any, even unseen, tasks and samples. We also propose a generative-based approach to estimate
the posterior of task-specific model parameters more expressively compared to the usual assumption based on a multivariate normal
distribution with a diagonal covariance matrix. We show that the models trained with our proposed meta-learning algorithm are well
calibrated and accurate, with state-of-the-art calibration and classification results on few-shot classification (mini-ImageNet and
tiered-ImageNet) and regression (multi-modal task-distribution regression) benchmarks.
Index Terms —PAC Bayes, meta-learning, few-shot learning, transfer learning.
F
1 I NTRODUCTION
NE unique ability of humans is to quickly learn new method) [16], or PLATIPUS [13], Amortised Bayesian Meta-
O tasks with only a few training examples. This is due learner (ABML) [17] and VERSA [18] that use variational
to the fact that humans tend to exploit prior experience inference (VI). However, these studies have not thoroughly
to facilitate the learning of new tasks. Such exploitation investigated the errors evaluated on arbitrary tasks (includ-
is markedly different from conventional machine learning ing seen and unseen) sampled from the same task distribu-
approaches, where no prior knowledge (e.g. training from tion and arbitrary samples generated from the same task.
scratch with random initialisation) [1], or weak prior knowl- This results in limited theoretical generalisation guarantees.
edge (e.g., fine tuning from pre-trained models) [2] are em- Moreover, most of these studies are based on variational
ployed to learn a new task. This motivates the development functions that may not represent well the richness of the
of novel learning algorithms that can effectively encode underlying distributions. For instance, a common choice for
the knowledge learnt from training tasks, and exploit that the variational distribution relies on a multivariate normal
knowledge to quickly adapt to future tasks [3]. distribution with a diagonal covariance matrix, which can
Prior knowledge can be helpful for future learning only potentially worsen the prediction accuracy given its limited
if all tasks are assumed to be distributed according to a representability.
latent task distribution. Learning this latent distribution is, In this paper, we address the two problems listed above
therefore, useful for solving an unseen task, even if the with the following technical novelties: (i) derivation of
task contains a limited number of training examples. Many a rigorous meta-learning objective that upper-bounds the
approaches have been proposed and developed to achieve errors evaluated on any tasks and any samples of few-
this goal, namely: multi-task learning [4], domain adaptation [5, shot learning setting based on the PAC-Bayes framework,
6] and meta-learning [7, 8]. Among these, meta-learning has and (ii) proposal of a novel implicit modelling approach to
flourished as one of the most effective methods due to its expressively represent the posterior of task-specific model
arXiv:2003.02455v3 [cs.LG] 30 Oct 2021 ability to leverage the knowledge learnt from many training parameter. Our evaluation shows that the models trained
tasks to quickly adapt to unseen tasks. with our proposed meta-learning algorithm is at the same
Recent advances in meta-learning have produced state- time well calibrated and accurate, with state-of-the-art re-
of-the-art results in many benchmarks of few-shot learning sults in few-shot classification (mini-ImageNet and tiered-
data sets [9–15]. Learning from a few training examples ImageNet) and regression (multi-modal task-distribution
is often difficult and easily leads to over-fitting, especially regression) benchmarks in terms of accuracy, Expected
when no model uncertainty is taken into account. This Calibration Error (ECE) and Maximum Calibration Error
issue has been addressed by several recent probabilistic (MCE).
meta-learning approaches that incorporate model uncer-
tainty into prediction, e.g., LLAMA (based on Laplace
2 R ELATED W ORK
Our paper is related to probabilistic few-shot meta-learning
• C. Nguyen and G. Carneiro are with the Australian Institute for Machine techniques that have been developed to incorporate un-
Learning, University of Adelaide, SA, Australia 5000.
certainty into model estimation. LLAMA [16] employs the
• T.-T. Do is with the Department of Data Science and AI, Faculty of Laplace method to extend the deterministic estimation as-
Information Technology, Monash University. sumed in MAML [13] to a multivariate normal distribution.
Work in progress. However, the need to estimate and invert the Hessian matrix
2
of a loss function makes this approach computationally 3 B ACKGROUND
challenging for large-scale models, such as deep neural 3.1 Data generation model of a task
networks. Variational inference (VI) addresses such scala-
A data point of a task indexed by i considered in this paper
bility issue – remarkable examples of VI-based methods are
consists of an input x
PLATIPUS [19], BMAML [20], ABML [17] and VERSA [18]. ij ∈ X ⊆ R d and a corresponding label
y
Although these VI-based approaches have demonstrated ij ∈ Y with j ∈ N . Such data points are generated in 2
steps. The first step is to generate the input x
impressive results in regression, classification as well as ij by sampling
from some probability distribution D
reinforcement learning, they do not provide any theoretical i . The second step is to
determine the label y
guarantee on the error induced by arbitrary or even unseen ij = f ( x ij ) ,
```

## candidate-22 [stability-bounds] — UNCONSUMED

**Title:** Separating Geometry from Probability in the Analysis of Generalization

**URL:** https://arxiv.org/abs/2604.19560

**Description:** A theoretical paper reframing generalization bounds through deterministic sensitivity analysis of optimization problems rather than probabilistic i.i.d. assumptions.

**Content extract (≤6k chars):**

```
Title: Separating Geometry from Probability in the Analysis of Generalization
Authors: Maxim Raginsky, Benjamin Recht
Year: 2026
Categories: cs.LG, math.OC, stat.ML
arXiv: 2604.19560

Abstract:
The goal of machine learning is to find models that minimize prediction error on data that has not yet been seen. Its operational paradigm assumes access to a dataset $S$ and articulates a scheme for evaluating how well a given model performs on an arbitrary sample. The sample can be $S$ (in which case we speak of ``in-sample'' performance) or some entirely new $S'$ (in which case we speak of ``out-of-sample'' performance). Traditional analysis of generalization assumes that both in- and out-of-sample data are i.i.d.\ draws from an infinite population. However, these probabilistic assumptions cannot be verified even in principle. This paper presents an alternative view of generalization through the lens of sensitivity analysis of solutions of optimization problems to perturbations in the problem data. Under this framework, generalization bounds are obtained by purely deterministic means and take the form of variational principles that relate in-sample and out-of-sample evaluations through an error term that quantifies how close out-of-sample data are to in-sample data. Statistical assumptions can then be used \textit{ex post} to characterize the situations when this error term is small (either on average or with high probability).
```

## candidate-23 [null-surrogate] — UNCONSUMED

**Title:** A temporal network version of Wattss cascade model

**URL:** file:///cee7897970992c36dc394dbdd8f0cfb0cd7b1e4799b1a9468adf22815ab66aeb/A_temporal_network_version_of_Wattss_cascade_model.pdf

**Description:** A research paper extending Duncan Watts's threshold cascade model to temporal interaction networks by introducing a sliding time window of influence. The authors test fractional and absolute threshold variants on six empirical human-interaction datasets (email, dating, conference, forums, prostitution) and compare results against null models. The key finding is that temporal structure and the time window parameter significantly affect cascade dynamics, enabling cascades at higher threshold values than the static-network version.

**Content extract (≤6k chars):**

```
A temporal network version of Watts’s cascade
model
Fariba Karimi and Petter Holme
Abstract Threshold models of cascades in the social sciences and economics explain the
spread of opinion and innovation due to social influence. In threshold cascade models, fads
or innovations spread between agents as determined by their interactions with other agents
and their personal threshold of resistance. Typically, these models do not account for struc-
ture in the timing of interaction between the units. In this work, we extend a model of so-
cial cascades by Duncan Watts to temporal interaction networks. In our model, we assume
friends and acquaintances influence agents for a certain time into the future. That is the in-
fluence of the past ages and becomes unimportant. Thus, our modified cascade model has
an effective time window of influence. We explore two types of thresholds—thresholds to
fractions of the neighbors or absolute numbers. We try our model on six empirical datasets
and compare them with null models.
1 Introduction
arXiv:2103.13604v1 [physics.soc-ph] 25 Mar 202
Threshold models of cascades have been studied extensively in the social-science litera-
ture. The examples of the phenomena they seek to explain include diffusion of innova-
tion, rumors, diseases, strikes, voting behavior, and migration. Diffusion models such as
Fariba Karimi
IceLab, Department of Physics, Ume˚ a University, 90187 Ume˚ a, Sweden
Petter Holme
IceLab, Department of Physics, Ume˚ a University, 90187 Ume˚ a, Sweden
e-mail: petter.holme@physics.umu.se
Department of Energy Science, Sungkyunkwan University, Suwon 440–746, Korea
e-mail: holme@skku.edu
Department of Sociology, Stockholm University, 10691 Stockholm, Sweden
1
2 Fariba Karimi and Petter Holme
Bass model [3] are canonical models. These assume that the individual choice of action is
independent of the individuals’ total number of interactions. However, sociologist Mark
Granovetter [9] proposed thresholds to influence as a rational action. This insight comes
from that there must be a point where the net benefits of acting exceed the net costs. This
also reflects the fact that many decisions need group size to be considered. For example,
the costs of joining a riot would probably decrease as the group size increases. Granovetter
further proposes two main factors that influence spreading in threshold scenarios—social
structure and timing of social action. In this chapter, we focus on the latter factor.
Social psychologist Bibb Latan´ e [16] proposed social impact theory to explain social in-
fluence as a multiplicative function of strength, immediacy (an inverse function of physical
distance), and the number of sources of influence. In the threshold model of cascades, we
only investigate the effects of the third factor (that the influence is proportional to the
number of people involved). The threshold itself corresponds to the individual’s persis-
tence to change his or her state. Threshold models have been studied for uniform or het-
erogeneous threshold values [22, 9]. Dodds and Watts [4] showed that minor manipula-
tion of individual thresholds could have a major impact on spreading phenomena. Here,
for simplicity (like in Ref. [24]), we assume an identical threshold value for all individuals.
This chapter is inspired by Watts’ threshold model of cascades in networks [24]. This
work explains, for example, how innovation can trigger a cascade of adaptation solely by
network interactions. Even though this approach does not represent the reality of inno-
vation adaptation, it estimates the importance of networks in the spreading process. In
threshold models, the agents’ decision of action is a binary choice, such as replacing an
old production method with a new one. In this model, the individuals’ choice of action
depends only on other neighbors’ choices. In Schelling’s words, we have a model of binary
choice with externalities.
We extend the work of Ref. [14] where we present a generalization of a threshold model
to temporal networks [11, 15]. Temporal networks, the theme of this book, are networks
that encode information about when things happen, not only about which nodes are in
contact. We contrast our generalized model to the behavior of the original, static-network
version. In our model (as in Watts’s model), all the agents initially have the same state,
and the thresholds are homogeneously distributed over the population. During the sim-
ulation, the agents change their states according to their interaction with their neighbor-
hood and the time of these interactions. We study two types of thresholds—fractional and
absolute—corresponding to whether the individual responds to the fraction of neighbors
with a deviating opinion or the absolute number of such neighbors. We note that while
fractional thresholds are most common in the social and economic literature, absolute
threshold models are used in bootstrap percolations and self-organized criticality, which
focus on local dependency [1, 7].
A temporal network version of Watts’s cascade model 3
2 Methods
We consider a system of vertices (agents) and edges (vertices that at some point are in contact
with each other). The system can be represented as a network G with a set of vertices V
and a set of edges E . Every edge is associated with a set of times of interaction events. These
interactions are bidirectional.
Each vertex or agent in the network has a state . The state can be either 0 or 1. We call ver-
tices with state 0 non-adopters . Vertices with state 1 correspond to adopters . Initially, all the
vertices in the network have state 0 (non-adopters). We start by randomly choosing a ver-
tex and assign the state to 1. This initial vertex with state 1 can, according to the diffusion-
of-innovation literature [22], be interpreted as an innovator advertising a new product.
Here, for simplicity, we only divide the population into adopters and non-adopters. We
thus study cascades of adoption from ado
```

## candidate-24 [null-surrogate] — UNCONSUMED

**Title:** Consistency of permutation tests for HSIC and dHSIC

**URL:** file:///6849fd4fd8da88c39f774bca0b63834dc958bd5b71d909c66e5ccf052ed66f05/Consistency_of_permutation_tests_for_HSIC_and_dHSIC.pdf

**Description:** This research paper proves the consistency (power converging to 1) of permutation tests for the Hilbert-Schmidt Independence Criterion (HSIC) and its d-variable extension dHSIC, answering an open question from Pfister et al. The authors use elementary techniques showing that under the alternative hypothesis the test statistic converges to a positive constant while its distribution under random permutation converges to zero, and additionally prove correct type 1 error rate for non-continuous data and provide guidance on selecting the number of permutations.

**Content extract (≤6k chars):**

```
Consistency of permutation tests for HSIC and dHSIC
David Rindt, Dino Sejdinovic and David Steinsaltz
Department of Statistics,
University of Oxford
Abstract
The Hilbert–Schmidt Independence Criterion (HSIC) is a popular measure of the dependency
between two random variables. The statistic dHSIC is an extension of HSIC that can be
used to test joint independence of d random variables. Such hypothesis testing for (joint)
independence is often done using a permutation test, which compares the observed data with
randomly permuted datasets. The main contribution of this work is proving that the power of
such independence tests converges to 1 as the sample size converges to infinity. This answers
a question that was asked in [8]. Additionally this work proves correct type 1 error rate of
HSIC and dHSIC permutation tests and provides guidance on how to select the number of
permutations one uses in practice. While correct type 1 error rate was already proved in [8],
we provide a modified proof following [1], which extends to the case of non-continuous data.
The number of permutations to use was studied e.g. by [7] but not in the context of HSIC
and with a slight difference in the estimate of the p -value and for permutations rather than
vectors of permutations. While the last two points have limited novelty we include these to
give a complete overview of permutation testing in the context of HSIC and dHSIC.
arXiv:2005.06573v1 [math.ST] 13 May 2020 1 Introduction
In [5] and [4] kernel methods were proposed for independence testing and two-sample testing.
Since then kernel based tests have been proposed for conditional independence testing and
joint independence testing [16],[8]. Such tests have been used in graphical modeling, among
other applications. Independence testing using reproducing kernel Hilbert spaces has also
been extended to right-censored data found in survival analysis [9, 2]. We study the tests
for joint independence proposed by [8] which includes the independence test between two
1
random variables.
These methods have several desirable properties. For appropriate choices of kernel, the
population value of the test statistic, called the Hilbert–Schmidt Independence Criterion
(HSIC), equals zero if and only if the two variables are independent. Similarly, the popula-
tion value of the statistic measuring joint independence — the d -variable HSIC, or dHSIC
— is zero if and only if the variables are indeed jointly independent. One thus does not
need to make assumptions about the form of the relationship among the variables. Fur-
thermore, under mild conditions the test statistic converges in probability to the population
value. Additionally, these tests may be applied to multidimensional random variables, and
even to variables that do not take values in the Euclidean domains, such as graphs or text [5].
In practice, one does not have access to the true sampling distribution. To perform
hypothesis testing one thus needs to approximate the null distribution or perform permuta-
tion tests or bootstrapping. These three methods were studied for dHSIC in [8] by Pfister,
B¨ uhlmann, Sch¨ olkopf, and Peters, where they established consistency of the bootstrap test
(power converging to 1 for every alternative hypothesis), correct type 1 error rate of the per-
mutation test, and pointwise asymptotic correct type 1 error rate of the bootstrap procedure.
One question that remained unanswered was the consistency of the permutation test.
See Table 1 of [8] and Section 3.2.1 and Remark 2 where they propose a proof strategy. The
main theoretical contribution of this work is to prove the consistency of the permutation test,
albeit not in the proposed way, but using more elementary techniques that can be traced
back at least to [6]: as we discuss in Section 2 the test statistic dHSIC, with appropriate
choice of kernel, converges to a positive constant for each fixed alternative hypothesis. The
main observation from which consistency will follow is that it suffices for the statistic’s dis-
tribution under random permutation of the data to converge to zero in probability (Theorem
3). The full proof of consistency may be found in Section 6.
We also present short proofs the permutation test has correct type 1 error rate (Section
5) and investigate the question of how many permutations are appropriate to use (Section
7). These last investigations are not new, and can be found elsewhere in the literature, e.g.
[8, 7, 1], as well as older literature, such as [6]. We review these ideas here for completeness,
and because we wish to give a more unified treatment. In particular, [7] studied the number
of permutations, but differs from our notation in considering individual permutations rather
2
than vectors of permutations, and their p -value estimate lacked a guarantee for the type 1
error rate of the test. In [8] correct type 1 error rate of the test was proved, but under the
additional assumption that the random variables had a density. For completeness we also
show here two correct ways of dealing with non-continuous data. Furthermore, we provide
a different proof, following [1], which appeared in the context of independence-testing using
mutual information.
2 Background
2.1 Reproducing Kernel Hilbert Spaces
This section reviews some relevant information about reproducing kernel Hilbert spaces
(RKHSs).
Definition 1. (Reproducing Kernel Hilbert Space)([11]) Let X be a non-empty set and H
a Hilbert space of functions f : X → R . Then H is called a reproducing kernel Hilbert
(RKHS) space endowed with dot product 〈· , ·〉 if there exists a function k : X × X → R with
the following properties.
1. k has the reproducing property
〈 f, k ( x, · ) 〉 = f ( x ) for all f ∈ H, x ∈ X . (1)
2. k spans H , that is, H = span { k ( x, · ) | x ∈ X } where the bar denotes the completion of
the space.
Let X be a measurable space and H k be an RKHS on X with kernel k . Let P be a
√
probability measure on X . If E P k ( X, X ) < ∞
```

## candidate-25 [null-surrogate] — UNCONSUMED

**Title:** Order patterns their variation and change points in financial time series and Br

**URL:** file:///fadeeb603fa42491308a9b30a8fe93fa15b63b7618426dd09bbd8ac2ef194973/Order_patterns_their_variation_and_change_points_in_financial_time_series_and_Br.pdf

**Description:** A peer-reviewed paper studying order patterns and permutation entropy in day-to-day financial time series, comparing pattern frequencies with Brownian motion as a null model. It demonstrates that pattern frequencies remain essentially constant for small lags (1–6 days) due to self-similarity properties, and develops rigorous statistical tests—including a modern version of a forgotten 1874 test by Bienaymé—for the turning rate and up-down balance parameters. The key finding is that up-down balance is the most effective order parameter for detecting change points in financial data.

**Content extract (≤6k chars):**

```
Statistical Papers (2020) 61:1565–1588
https://doi.org/10.1007/s00362-020-01171-7
R E G U L A R A R T I C L E
Order patterns, their variation and change points in
financial time series and Brownian motion
Christoph Bandt 1
Received: 21 October 2019 / Revised: 11 March 2020 / Published online: 20 March 2020
© The Author(s) 2020
Abstract
Order patterns and permutation entropy have become useful tools for studying biomed-
ical, geophysical or climate time series. Here we study day-to-day market data, and
Brownian motion which is a good model for their order patterns. A crucial point is that
for small lags (1 up to 6 days), pattern frequencies in financial data remain essentially
constant. The two most important order parameters of a time series are turning rate
and up-down balance. For change points in EEG brain data, turning rate is excellent
while for financial data, up-down balance seems the best. The fit of Brownian motion
with respect to these parameters is tested, providing a new version of a forgotten test
by Bienaymé.
Keywords Order pattern · Time series · Permutation entropy · Stock data
Mathematics Subject Classification 62M10 · 91B84 · 60G18
1 Overview
Given a finite series of data, time series analysis attempts to find laws of the mechanism
or process which generated the data. One tool to this end are frequencies of order
patterns, defined in Sect. 3. For a first impression, Fig. 1 shows the six order patterns
of length 3. Given a time series x 1 , . . . , x T , a point t represents the pattern π = 123 if
x t < x t + 1 < x t + 2 . The frequency p π of a pattern π is the number of time points which
represent π, divided by T − 2 . Such frequencies are estimates of probabilities of an
underlying random process. They can be combined in various ways. The permutation ∑
entropy − π p π log p π measures the variety of patterns (Bandt and Pompe 2001).
Applications to brain and heart data concern epilepsy (Bruzzo et al. 2008; Ferlazzo
2014), Alzheimer’s disease (Morabito et al. 2012), effect of anaesthesia (Olofsen et al.
B Christoph Bandt
bandt@uni-greifswald.de
1 Institute of Mathematics, University of Greifswald, 17487 Greifswald, Germany
123
1566 C. Bandt
Fig. 1 The six order patterns of length 3
2008), and cardiac dynamics (Parlitz et al. 2012; Chicote et al. 2016; McCullough
et al. 2017). For an overview of applications to physics, geophysics, environtmental
and climate data see Amigo et al. (2013), Amigo et al. (2015), and Zanin et al. (2012).
Moreover, probabilities of specific order patterns can give important information.
For chaotic dynamical systems, certain patterns will not appear (Amigo 2010). Differ-
ent versions of permutation entropy and the number of forbidden patterns were used
to quantify and monitor the efficiency of stock (Zunino et al. 2009) and bond markets
(Zunino et al. 2012, 2016). The probabilities of patterns can be combined to form
correlation functions (Bandt 2015, 2017). The dependence of economical time series
was studied in Schnurr (2014) by means of order patterns. Statistical theory of order
pattern estimators was developed recently by Schnurr and Dehling (2017) and Betken
et al. (2019), earlier work by Bandt and Shiha (2007) and Sinn and Keller (2011) was
restricted to Gaussian processes.
Several authors have studied change points and segmentation of time series by
means of order patterns (Sinn et al. 2013; Unakafov and Keller 2018). The interest-
ing approach in Schnurr (2014) and Schnurr and Dehling (2017) uses bivariate data
while we shall study the univariate case only. A very impressive example is sleep
stage classification using high-frequency data of a single EEG channel (Nicolaou and
Georgiou 2012; Kuo and Liang 2011; Bandt 2017, 2019). Here we have an abundance
of data and few statistical problems. In the next section we will briefly describe this
application.
Our main theme are order patterns in day-to-day financial data and their statistics.
The zigzag patterns of up and down have long been considered by stock traders. Today
they are certainly incorporated in secret algorithms for high-frequency trade. We are
interested in the statistical error of estimates of pattern probabilties, and in the change
point problem. We introduce our standard example of oil prices in Sect. 4.
A curious feature of such examples is their apparent‘self-similarity’ studied by
Mandelbrot since the 1960s (Mandelbrot 1997). This property implies equality of
frequencies of patterns for different lags, which can be compared with simulated
samples of Brownian motion and other Levy processes. One goal of the paper is to
develop tests which decide whether Brownian motion is an appropriate model. In
Sect. 5 this is done by simulation, in Sect. 7 rigorously.
It seems that for a large part, ‘order self-similarity’ is due to the uneven sampling of
market data, with missing weekends and holidays. In contrast to measurements done
in nature, the observed values are not varying in natural time. Their change is triggered
by trade. Volume and number of buying and selling orders provide alternative scales
to natural time. Under such conditions, classical tools like autocorrelation become
123
Order patterns, their variation and change points... 1567
useless. It may be a necessity to postulate equality of pattern frequencies for small
lags. Our discussion in Sect. 6 shows that the assumption is justified and can be used
to improve estimates of pattern frequencies.
Our expectations should be modest: with at most a few thousand data, statistical
accuracy will not be magic. In Sect. 7 we introduce the two most stable and interpretable
order parameters, up-down balance and turning rate. They are used to provide statistical
tests for comparing models and data series. Actually, a first test for the turning rate
was suggested already in Bienaymé (1874, 1875). The basic message is that pattern √
statistics has the 1 / n accuracy coming from binomial distribution. In Bienaymè’s
case it is even
```

## candidate-26 [null-surrogate] — UNCONSUMED

**Title:** Fluctuating ecological networks: A synthesis of maximum‐entropy approaches for pattern detection and process inference

**URL:** https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/2041-210X.13985

**Description:** Review paper synthesizing maximum-entropy methods with soft (fluctuating) constraints as null models for detecting non-random patterns in ecological networks like food webs and plant-pollinator systems.

**Content extract (≤6k chars):**

```
Title: Fluctuating ecological networks: A synthesis of maximum‐entropy approaches for pattern detection and process inference
Authors: T. Caruso, Giulio Virginio Clemente, M. Rillig, D. Garlaschelli
Year: 2021
Citations: 10
Fields: Biology, Physics

Abstract:
Ecological networks such as plant–pollinator systems and food webs vary in space and time. This variability includes fluctuations in global properties such as the total number and intensity of interactions in the network but also in the number and intensity of local (i.e. node level) species interactions. Fluctuations of species' properties can significantly affect higher‐order network features, for example, robustness and nestedness, and should therefore be taken into account in null models for pattern detection and hypothesis testing. In ecological research, classical null models treat node‐level properties as ‘hard’ constraints that cannot fluctuate. Here, we review and synthesize a set of maximum‐entropy methods that allow for fluctuating (‘soft’) constraints, offering a new addition to the classical toolkit of the ecologist. We illustrate the methods with some practical examples, pointing to currently available open‐source computer codes. We clarify how this approach can be used by experimental ecologists to detect non‐random patterns with null models that not only rewire, but also redistribute interaction strengths by allowing fluctuations in the enforced constraints. Explicit modelling of interspecific heterogeneity through local (i.e. species level) fluctuations of topological and quantitative constraints offers a statistically robust and expanded (e.g. including weighted links) set of tools to understand the assembly and resilience of ecological networks.

TL;DR: It is clarified how this approach can be used by experimental ecologists to detect non‐random patterns with null models that not only rewire, but also redistribute interaction strengths by allowing fluctuations in the enforced constraints.
```

## candidate-27 [chain-complex] — UNCONSUMED

**Title:** 1 s2.0 S0370157320302489 main

**URL:** file:///c143cb937de54ebd4dd80f08b7e6dd8ebd50b2992b14afe3bd221c64bc8c9348/1-s2.0-S0370157320302489-main.pdf

**Description:** Comprehensive Physics Reports review (92 pages) on networks beyond pairwise interactions, surveying how higher-order structures—hypergraphs and simplicial complexes—extend classical graph theory to capture group interactions in biological, social, and technological systems. Covers representations, structural measures (incidence/adjacency matrices, centralities, simplicial homology, higher-order Laplacians), generative models (equilibrium and out-of-equilibrium), and dynamical processes (diffusion, synchronization, spreading, social dynamics, games) on higher-order structures. Argues that incorporating higher-order interactions yields qualitatively new emergent phenomena (e.g., explosive transitions, abrupt contagion) that pairwise models cannot capture.

**Content extract (≤6k chars):**

```
Physics Reports 874 (2020) 1–92
Contents lists available at ScienceDirect
Physics Reports
journal homepage: www.elsevier.com/locate/physrep
Networks beyond pairwise interactions: Structure and
dynamics
Federico Battiston a , ∗
, Giulia Cencetti b , Iacopo Iacopini c , d , Vito Latora c , e , f , g ,
Maxime Lucas h , i , j , Alice Patania k , Jean-Gabriel Young l , Giovanni Petri m , n
a Department of Network and Data Science, Central European University, Budapest 1051, Hungary
b Mobs Lab, Fondazione Bruno Kessler, Via Sommarive 18, 38123, Povo, TN, Italy
c School of Mathematical Sciences, Queen Mary University of London, London E1 4NS, United Kingdom
d Centre for Advanced Spatial Analysis, University College London, London, W1T 4TJ, United Kingdom
e Dipartimento di Fisica ed Astronomia, Università di Catania and INFN, I-95123 Catania, Italy
f The Alan Turing Institute, The British Library, London NW1 2DB, United Kingdom
g Complexity Science Hub Vienna (CSHV), Vienna, Austria
h Aix Marseille Univ, CNRS, CPT, Turing Center for Living Systems, Marseille, France
i Aix Marseille Univ, CNRS, IBDM, Turing Center for Living Systems, Marseille, France
j Aix Marseille Univ, CNRS, Centrale Marseille, I2M, Turing Center for Living Systems, Marseille, France
k Network Science Institute, Indiana University, Bloomington, IN, USA
l Center for the Study of Complex Systems, University of Michigan, Ann Arbor, MI, 48109, USA
m ISI Foundation, via Chisola 5, 10126 Turin, Italy
n ISI Global Science Foundation, 33 W 42nd St, 10036 New York, NY, USA
a r t i c l e i n f o a b s t r a c t
Article history: The complexity of many biological, social and technological systems stems from the
Received 11 May 2020 richness of the interactions among their units. Over the past decades, a variety of
Accepted 28 May 2020 complex systems has been successfully described as networks whose interacting pairs of
Available online 13 June 2020 nodes are connected by links. Yet, from human communications to chemical reactions
Editor: Dr. I. Procaccia and ecological systems, interactions can often occur in groups of three or more nodes
and cannot be described simply in terms of dyads. Until recently little attention has
been devoted to the higher-order architecture of real complex systems. However, a
mounting body of evidence is showing that taking the higher-order structure of these
systems into account can enhance our modeling capacities and help us understand and
predict their dynamical behavior. Here we present a complete overview of the emerging
field of networks beyond pairwise interactions. We discuss how to represent higher-
order interactions and introduce the different frameworks used to describe higher-order
systems, highlighting the links between the existing concepts and representations. We
review the measures designed to characterize the structure of these systems and the
models proposed to generate synthetic structures, such as random and growing bipar-
tite graphs, hypergraphs and simplicial complexes. We introduce the rapidly growing
research on higher-order dynamical systems and dynamical topology, discussing the
relations between higher-order interactions and collective behavior. We focus in partic-
ular on new emergent phenomena characterizing dynamical processes, such as diffusion,
synchronization, spreading, social dynamics and games, when extended beyond pairwise
interactions. We conclude with a summary of empirical applications, and an outlook on
current modeling and conceptual frontiers.
© 2020 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY
license (http://creativecommons.org/licenses/by/4.0/).
∗ Corresponding author.
E-mail addresses: battistonf@ceu.edu (F. Battiston), v.latora@qmul.ac.uk (V. Latora), giovanni.petri@isi.it (G. Petri).
https://doi.org/10.1016/j.physrep.2020.05.004
0370-1573/ © 2020 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/
licenses/by/4.0/).
2 F. Battiston, G. Cencetti, I. Iacopini et al. / Physics Reports 874 (2020) 1–92
Contents
1. Introduction............................................................................................................................................................................................... 3
2. Higher-order representations of networks............................................................................................................................................ 4
2.1. Elementary representations of higher-order interactions....................................................................................................... 4
2.1.1. Low- versus high-order representations ................................................................................................................... 4
2.1.2. Graph-based representations ...................................................................................................................................... 5
2.1.3. Explicit higher-order representations ........................................................................................................................ 6
2.2. Relations and links between representations........................................................................................................................... 7
3. Measures.................................................................................................................................................................................................... 8
3.1. Matrix representations of higher-order systems ..................................................................................................................... 8
3.1.1. Incidence matrix........................................................................................................................................................... 8
3.1.2. Adjacency matrix.....................................................
```

## candidate-28 [chain-complex] — UNCONSUMED

**Title:** Topology-Aware Layer Pruning for Large Vision-Language Models

**URL:** https://arxiv.org/abs/2604.16502

**Description:** A topology-aware layer pruning framework for Large Vision-Language Models that uses zigzag persistent homology on simplicial complexes of hidden states to preserve transition-critical layers during compression.

**Content extract (≤6k chars):**

```
Title: Topology-Aware Layer Pruning for Large Vision-Language Models
Authors: Pengcheng Zheng, Chaoning Zhang, Ya Wen, Wang Liu, Qigan Sun, Jiarong Mo, Jiaquan Zhang, Jewon Lee, Tae-Ho Kim, Kuien Liu, Tianyu Li, Caiyan Qin, Yang Yang
Year: 2026
Categories: cs.CV
arXiv: 2604.16502

Abstract:
Large Language Models (LLMs) have demonstrated strong capabilities in natural language understanding and reasoning, while recent extensions that incorporate visual inputs enable them to process multimodal information. Despite these advances, Large Vision-Language Models (LVLMs) incur substantial computational and memory costs, hindering deployment in resource-constrained scenarios. Existing layer pruning methods typically rely on local similarity metrics or static proxy signals, failing to capture the global and dynamic evolution of representations across model depth, which often leads to the removal of transition-critical layers. To address this limitation, we propose a topology-aware layer pruning framework for LVLMs. Specifically, we represent layer wise hidden states as point clouds and models their evolution using \textit{simplicial complexes}. By leveraging \textit{zigzag persistent homology}, we quantify inter-layer topological consistency and enable adaptive pruning that preserves critical representational transitions. Extensive experiments on diverse multimodal benchmarks demonstrate that the proposed framework consistently outperforms existing pruning methods across a wide range of sparsity ratios. Our code is available at https://github.com/zpc456/TopoVLM.
```
