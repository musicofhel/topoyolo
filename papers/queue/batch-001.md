# Queue batch-001 — link-forge export, 2026-08-24

Orchestrator export from link-forge Neo4j (2,226 research papers scanned).
Targets the A4-derived weak cells: neuroscience, Matching×InfoTheory, Dynamics×Matching, QEC×Joint-vs-Marginal.
Consume per papers/INGESTION.md (B1 defines it; ≤3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [neuroscience] — REJECTED
Walsh-matrix CNN engineering; instantiates zero of the six machines.

**Title:** Strengthening the Training of Convolutional Neural Networks By Using Walsh Matri

**URL:** file:///0bd28b2408a512d29038d599ce22dc128aeb41ecc1f6a5e5eff907a4898e3f9d/Strengthening_the_Training_of_Convolutional_Neural_Networks_By_Using_Walsh_Matri.pdf

**Description:** This research paper proposes DivFE, a modified deep neural network architecture that replaces fully connected layers with a minimum distance network (MDN) classifier and uses Walsh functions to strengthen CNN feature extraction training. The approach is tested across diverse classification tasks—ECG, EEG, heart sound, chest X-ray pneumonia detection, BGA solder defect inspection, and benchmark datasets (MNIST, IRIS, CIFAR10, CIFAR20)—demonstrating higher classification performance with significantly fewer network nodes, making it suitable for real-time applications.

**Content extract (≤6k chars):**

```
Strengthening the Training of Convolutional Neural Networks
By Using Walsh Matrix.
Tamer Ölmez and Zümray Dokur
Istanbul Technical University,
Department of Electronics and Communication Engineering, Istanbul, Turkey
corresponding author: olmezt@itu.edu.tr
ABSTRACT: DNN structures are continuously developing and achieving high performances in
classification problems. Also, it is observed that success rates obtained with DNNs are higher than those
obtained with traditional neural networks. In addition, one of the advantages of DNNs is that there is no
need to spend an extra effort to determine the features; the CNN automatically extracts the features from
the dataset during the training. Besides their benefits, the DNNs have the following three major
drawbacks among the others: (i) Researchers have struggled with over-fitting and under-fitting issues in
the training of DNNs, (ii) determination of even a coarse structure for the DNN may take days, and (iii)
most of the time, the proposed network structure is too large to be too bulky to be used in real time
applications. We have modified the training and structure of DNN to increase the classification
performance, to decrease the number of nodes in the structure, and to be used with less number of hyper
parameters. A minimum distance network (MDN) following the last layer of the convolutional neural
network (CNN) is used as the classifier instead of a fully connected neural network (FCNN). In order to
strengthen the training of the CNN, we suggest employing Walsh function. We tested the performances
of the proposed DNN (named as DivFE) on the classification of ECG, EEG, heart sound, detection
pneumonia in X-ray chest images, detection of BGA solder defects, and patterns of benchmark datasets
(MNIST, IRIS, CIFAR10 and CIFAR20). In different areas, it has been observed that a higher
classification performance was obtained by using the DivFE with less number of nodes.
Keyword:
Deep neural networks (DNN)
Convolutional neural network (CNN)
Pattern recognition
Training deep neural network
Classification
1. Introduction
From recent studies it is observed that convolutional neural networks are proved to be extremely
successful in classification problems. Especially, accurate and fast classification of biological
signals/images (EEG, ECG, heart sound and x-ray chest images etc.) is a crucial step in the
implementation of real-time arrhythmia diagnosis systems. High classification performances are
obtained by using the developed DNN structures. However, it is observed that the proposed network
structure is too large to be too bulky to be used in real time applications. In this study, the use of the
DivFE in different fields will be emphasized by demonstrating examples of our previous study.
It is observed that traditional neural network [1-7] and DNNs [8-16] are becoming popular in the
classification of ECG signals. In the studies [8-16], high classification performances are obtained by
using different deep neural network structures which generally consist of convolution neural network
and fully connected neural networks. However, the extremely large size of the DNNs is still a major
obstacle for real-time applications. For some patients suffering from cardiovascular problems, doctors
may ask for the continuous recording of the patient’s ECG in order to evaluate his/her heart activity on
a long-term basis, and also to detect any cardiac symptom that does not show up during the ECG
recording at a medical center, but may occur within a short time interval during the patient’s normal daily
routine. For these reasons, Holter monitors or some other similar systems, which are portable and
wearable medical devices that measure and analyze the everyday activity of the heart, are being carried
by selected patients. With such portable systems, if the doctor has sufficiently more information about
the condition of the heart, it will be easier for him/her to deal with a vital problem.
In our previous study [17], we observed that the classification performances of MI EEG signals
were evaluated on the BCI Competition III dataset [18] and IV dataset [19] by using traditional neural
network [20-30] and DNNs [17, 31-47]. Actually, classification performance for four-class MI EEG
signals is still not at a high level. Fortunately, DNNs produce high classification performances in almost
all machine learning areas. Besides their benefits, the DNNs have the following two major drawbacks
among the others in classification of MI EEG signals: (i) DNNs need big datasets, and (ii) determination
of even a coarse structure for the DNN may take days. We have noticed that by solving some problems
encountered in DNNs, classification performance for the MI EEG signals can be improved. A solution
for increasing the classification performance on small-sized MI EEG datasets was to use transfer learning
[41]. In the transfer learning of [41], the huge network pre-trained using a different and probably big data
set is retrained by the BCI MI EEG dataset. Though, high successes were achieved, the DNN really had
excessive number of nodes. In another solution, researchers mostly preferred using preprocessing or
transformation stage preceding the CNN structure to provide high classification performances with small
datasets [31-43,44-46]. The CSP [31,32,34,35,40,43,44-47], FFT [33], STFT [38,39] or CWT [41] were
preferred for the preprocessing (or transformation) stage. In those studies, CNNs investigate the features
in the input space determined by the preprocessing. However, these stages introduce considerable amount
of computational load to the decision making system. Because the classification performance is very
dependent on the correct determination of the parameters of the preprocessing stage, in addition to a
successful training of the DNN, the researchers need to determine the optimum parameters for each
subject.
Determining pneumonia from chest x-ray (CXR) images is an extremely di
```

---

## candidate-02 [neuroscience] — UNCONSUMED

**Title:** A Recurrent Probabilistic Neural Network with Dimensionality Reduction Based on

**URL:** file:///6d59c56e55b0d64da1f36f437b085215d070432230e2c7f231f1b4f01cd227f3/A_Recurrent_Probabilistic_Neural_Network_with_Dimensionality_Reduction_Based_on_.pdf

**Description:** This IEEE paper proposes the Time-series Discriminant Component Network (TSDCN), a recurrent probabilistic neural network that unifies dimensionality reduction and classification of high-dimensional time-series data into a single trainable architecture. It integrates orthogonal transformation matrices with a continuous-density HMM/GMM framework, using a Lagrange multiplier method within backpropagation through time to maintain orthogonality constraints while guaranteeing learning convergence. The approach is validated on high-dimensional artificial data and EEG signals, demonstrating improved classification accuracy and reduced computation time compared to separate dimensionality reduction and classification pipelines.

**Content extract (≤6k chars):**

```
1
A Recurrent Probabilistic Neural Network with
Dimensionality Reduction Based on Time-series
Discriminant Component Analysis
Hideaki Hayashi, Member, IEEE, Taro Shibanoki, Member, IEEE, Keisuke Shima, Member, IEEE,
Yuichi Kurita, Member, IEEE, and Toshio Tsuji, Member, IEEE
Abstract —This paper proposes a probabilistic neural network Σ ′ ( c,k,m ) 
Covariance matrix in the subspace
developed on the basis of time-series discriminant component ′ ( c,k,m ) ( c,k,m )
s ′ − 1
i,j Element of (Σ )
analysis (TSDCA) that can be used to classify high-dimensional γ c
time-series patterns. TSDCA involves the compression of high- k ′ ,k State change probability of an HMM
dimensional time series into a lower-dimensional space using π c
k Prior probability of an HMM
a set of orthogonal transformations and the calculation of X ( t ) Transformed vector in the original space
posterior probabilities based on a continuous-density hidden ( c,k,m )
X ′ ( t ) Transformed vector in the subspace
Markov model with a Gaussian mixture model expressed in the W ( c,k,m ) Weight between the first/second layers
reduced-dimensional space. The analysis can be incorporated into ( c,k,m )
a neural network, which is named a time-series discriminant w ( c,k,m )
i,j Element of W
component network (TSDCN), so that parameters of dimension- ( c,k ′ ,k,m ) 
W ′ Weight between the third/fourth layers
ality reduction and classification can be obtained simultaneously ( c,k ′ ,k,m ) ( c,k ′ ,k,m )
w ′ ′
as network coefficients according to a backpropagation through h Element of W
( i )
time-based learning algorithm with the Lagrange multiplier I Input of the i th unit
( i )
method. The TSDCN is considered to enable high-accuracy O Output of the i th unit
classification of high-dimensional time-series patterns and to Q ( n ) Teacher vector
reduce the computation time taken for network training. The J Negative log-likelihood function
validity of the TSDCN is demonstrated for high-dimensional L Lagrange function
artificial data and EEG signals in the experiments conducted
during the study. λ ( c,k,m ) Lagrange multiplier
h ( c,k,m ) Orthogonality conditions
Index Terms —neural network, dimensionality reduction, pat- ( c,k,m )
tern classification, hidden Markov model, Gaussian mixture d ( c,k,m
l Modification amount for W )
model.
I. I NTRODUCTION
N OMENCLATURE IME-SERIES pattern classification has a wide range of
D Dimensionality in the original space T applications such as speech recognition, gesture recogni-
D ′ Dimensionality in the subspace tion, and biosignal classification, and many studies have been
C Number of classes performed to investigate higher classification performance [1]–
K c Number of states [7].
M c,k Number of components Time-series pattern classification methods can be divided
P ( · ) Probability into three large categories — sequence distance-based classi-
arXiv:1911.06009v1 [cs.LG] 14 Nov 2019 x ( t ) Time-series vector in the original space fication, feature-based classification, and model-based classifi-
x ′ ( t ) Time-series vector in the subspace cation [8]. Sequence distance-based methods measure the sim-
V ( c,k,m ) Orthogonal transformation matrix ilarity between a pair of patterns based on a distance function
( c,k,m )
v i,j Element of V ( c,k,m ) such as the Euclidean distance, the Mahalanobis distance [9],
μ ( c,k,m ) [10], or dynamic time warping, and then classify the patterns
Mean vector in the original space
μ ′ ( c,k,m ) using conventional classification algorithms typified by a k -
Mean vector in the subspace nearest neighbor classifier. In feature-based methods, features
g ( · ) Gaussian distribution are extracted from the original time series and are classified
r c,k,m Mixture proportion of a GMM using a support vector machine, decision trees, and neural
H. Hayashi is with Department of Advanced Information Technology, networks (NNs). In particular, NNs are expanded for time-
Kyushu University, 744, Motooka, Nishi-ku, Fukuoka-shi, 819-0395 JAPAN. series classification, known as the appearance of the Jordan
e-mail: hayashi@ait.kyushu-u.ac.jp network [11], the Elman network [12], and time delay neural
T. Shibanoki is with College of Engineering, Ibaraki University, Hitachi,
Japan. networks [13]. The most popular approach in model-based
K. Shima is with Faculty of Engineering, Yokohama National University, methods is the hidden Markov model (HMM). In the HMM,
Yokohama, 240-8501 Japan. the system for each class is modeled by a Markov process with
Y. Kurita and T. Tsuji are with Institute of Engineering, Hiroshima
University, Higashi-hiroshima, 739-8527 Japan unobserved states. Time-series patterns are then classified into
the classes based on a likelihood that is calculated from the
2
model. All the above methods, however, have some drawbacks: the parameters of dimensional reduction and classification
Sequence distance-based methods and model based methods simultaneously, thereby supporting the accurate classification
need a large amount of training data to estimate the distribution of time-series data with high dimensionality.
of input data precisely. Feature-based methods are likely to The rest of this paper is organized as follows: Section II
cause overfitting because they have too many free parameters describes TSDCA. The structure and the learning algorithm of
and complex structures. the TSDCN are explained in Section III. The verification of
In recent years, a fourth option, “model-based NNs”, has the classification ability using high-dimensional artificial data
been proposed as a hybrid of NNs and model-based methods and electroencephalograms (EEGs) are presented in Section
[14]–[20]. Model-based NNs are developed by integrating IV and V. Finally, Section VI concludes the paper.
prior knowledge of the input data into the network structure
to be capable of saving the amount of training data and II. T IME - SERIES DISCRIMINANT COMPONENT ANALYSIS
preventing overfitting. Tsuji et al. [20] propose
```

---

## candidate-03 [neuroscience] — UNCONSUMED

**Title:** Multi View Self Supervised Learning For Multivariate Variable Channel Time Serie

**URL:** file:///e333952a0026c6c66855bcb99f9db7d004cb36956ba82f40b30e6a028efeb9ea/Multi-View_Self-Supervised_Learning_For_Multivariate_Variable-Channel_Time_Serie.pdf

**Description:** This IEEE MLSP 2023 paper proposes a channel-agnostic architecture for self-supervised contrastive learning on multivariate time series with varying numbers of input channels. The method applies a shared single-channel convolutional encoder to each channel individually, then uses a message passing neural network (MPNN) to aggregate representations across channels, enabling transfer between datasets with different channel configurations. Evaluated on EEG sleep staging, the approach combined with the TS2Vec loss outperforms baselines when pretraining on six-channel data and fine-tuning on two different channels.

**Content extract (≤6k chars):**

```
2023 IEEE INTERNATIONAL WORKSHOP ON MACHINE LEARNING FOR SIGNAL PROCESSING, SEPT. 17–20, 2023, ROME, ITALY
MULTI-VIEW SELF-SUPERVISED LEARNING FOR MULTIVARIATE
VARIABLE-CHANNEL TIME SERIES
Thea Br¨ usch, Mikkel N. Schmidt, Tommy S. Alstrøm
Department of Applied Mathematics and Computer Science, Technical University of Denmark
ABSTRACT learning tasks include the reconstruction of masked input pix-
els and loss functions that only require positive views. In this
Labeling of multivariate biomedical time series data is a la-
work, we focus on contrastive self-supervised learning .
borious and expensive process. Self-supervised contrastive
learning alleviates the need for large, labeled datasets through Previous work on contrastive pretraining for time series
pretraining on unlabeled data. However, for multivariate time data uses various different strategies to create positive pairs.
series data, the set of input channels often varies between ap- Broadly speaking, we divide the strategies into three cate-
plications, and most existing work does not allow for transfer gories. The first category uses augmentations such as mask-
between datasets with different sets of input channels. We ing, scaling, or random additive noise. The second category
propose learning one encoder to operate on all input channels uses contrastive predictive coding (CPC), where an autore-
individually. We then use a message passing neural network gressive model is used to predict future samples. A closely
to extract a single representation across channels. We demon- related strategy uses a combination of masking and CPC to
strate the potential of this method by pretraining our model on reconstruct masked out segments within the current sequence.
a dataset with six EEG channels and then fine-tuning it on a The third category relies on data that inherently contains mul-
dataset with two different EEG channels. We compare models tiple views, such as multiple channels or different modalities.
with and without the message passing neural network across We refer to the third strategy as a multi-view strategy.
different contrastive loss functions. We show that our method, Previous significant work on contrastive pretraining for
combined with the TS2Vec loss, outperforms all other meth- time series data includes Eldele et al. [5], who use augmenta-
ods in most settings. tions such as permutations and scaling. Furthermore, they
use a temporal contrasting strategy similar to CPC to pre-
Index Terms — Self-supervised learning, Message pass- dict future augmented samples. Zhang et al. [6] use sim-
ing neural networks, Multi-view learning, Multivariate time ilar augmentations but create a separate encoder in the fre-
series, Sleep staging quency domain and encourage time and frequency represen-
tations to be close. Yue et al. [7] use random cropping and
1. INTRODUCTION masking to augment the input signal as well as a new hier-
archical time series loss to train their model, which they call
In recent years, self-supervised learning has shown promising TS2Vec. BErt-like Neurophysiological Data Representation
results in the fields of computer vision and natural language (BENDR) by Kostas et al. [8] comprises a convolutional en-
processing [1, 2]. Self-supervised learning relies on inherent coder that tokenizes raw input EEG, and a transformer that
contextualizes the tokens. The network is then trained using
arXiv:2307.09614v2 [stat.ML] 20 Jul 2023 patterns within the data to enable pretraining on large, unla-
beled datasets, thus facilitating the transfer of learned struc- a combination of CPC and masking. Kiyasseh et al. [9] and
tures to smaller labeled datasets, usually called the down- Deldari et al. [10] both leverage the multi-view strategy for
stream tasks. Obtaining ground truth scoring for biomedi- creating positive pairs. Kiyasseh et al. [9] investigate con-
cal signals such as electroencephalography (EEG) often re- trastive pretraining for electrocardiography (ECG). They use
quires the expertise of multiple professionals, rendering label both neighboring samples in time and different channels as
acquisition a challenging and expensive endeavor [3]. Con- positive pairs. Finally, Deldari et al. [10] use different sensor
sequently, self-supervised learning methods are particularly modalities as positive pairs and present a new loss, COCOA,
interesting for biomedical time series data. tailored for contrastive learning in settings with more than one
Many self-supervised learning methods use contrastive view. We focus our work on the multi-view strategy for mul-
learning to pretrain the networks. Contrastive learning relies tivariate time series data.
on having both positive and negative pairs, where the positive A significant challenge for self-supervised learning ap-
pairs are encouraged to be close and the negative pairs distant plied on multivariate time series is that the number of chan-
in representation space [4]. Non-contrastive self-supervised nels may vary from application to application. The varying
979-8-3503-2411-2/23/$31.00 ©2023 IEEE
number of channels makes it difficult to transfer between Extract representations
Input:
tasks with different channels [11], and few of the current using the same encoder Output:
𝒙 % ∈ ℝ ! × & × $ ! 𝒉 % ∈ ℝ ! × ' × $ "
methods have a principled way of handling this issue. The H 𝜽 𝒉 !
mentioned previous work either pretrain and fine-tune on H 𝜽 𝒉 "
the same dataset [5, 7, 10], or discard excess channels or 𝒉 #
𝑿 ∈ ℝ ! × # × $ H
! 𝜽
zero-pad missing channels during fine-tuning and/or pretrain- H 𝜽 𝒉 $
ing [6, 8]. The work most closely related to ours is SeqCLR H 𝜽 𝒉 %
by Mohsenvand et al. [12]. SeqCLR is a single encoder that H 𝜽 𝒉 &
works separately on all channels individually. The encoder
is pretrained using augmentations. During fine-tuning, the Fig. 1 . We apply the same encoder H θ to each of the C input
outputs of all input channels are concatenated and used as channels x c to obtain
```

---

## candidate-04 [neuroscience] — ANNOTATED as wang-2024 (pass 12): GC-STCL EEG emotion recognition; prose promoted from third_pass_infotheo_cross.md TP-01

**Title:** GC STCL A Granger Causality Based SpatialTemporal Contrastive Learning Framework

**URL:** file:///4517d5a02abb869f1b6f782fd5ffae488068d2b25c5888da83f4cdf7b0ee62ec/GC-STCL_A_Granger_Causality-Based_SpatialTemporal_Contrastive_Learning_Framework.pdf

**Description:** This research paper proposes GC-STCL, a Granger causality-based spatial–temporal contrastive learning framework for EEG emotion recognition. The method constructs directed causal graphs between EEG channels using Granger causality tests (spatial dimension) and applies frequency-domain noise reduction with a Granger–Former model (temporal dimension), both within a self-supervised contrastive learning paradigm. Experiments on the DEAP and SEED benchmarks show 1.65% and 1.55% accuracy improvements over state-of-the-art unsupervised methods, with improved interpretability.

**Content extract (≤6k chars):**

```
entropy
Article
GC-STCL: A Granger Causality-Based Spatial–Temporal
Contrastive Learning Framework for EEG Emotion Recognition
Lei Wang 1 , Siming Wang 2 , Bo Jin 3, * and Xiaopeng Wei 4, *
1 School of Software Technology, Dalian University of Technology, Dalian 116024, China;
wanglei2611@mail.dlut.edu.cn
2 School of Information and Communication Engineering, University of Electronic Science and Technology of
China, Chengdu 611731, China; 202122010706@std.uestc.edu.cn
3 School of Innovation and Entrepreneurship, Dalian University of Technology, Dalian 116024, China
4 School of Computer Science and Technology, Dalian University of Technology, Dalian 116024, China
* Correspondence: jinbo@dlut.edu.cn (B.J.); xpwei@dlut.edu.cn (X.W.)
Abstract: EEG signals capture information through multi-channel electrodes and hold promising
prospects for human emotion recognition. However, the presence of high levels of noise and the
diverse nature of EEG signals pose significant challenges, leading to potential overfitting issues that
further complicate the extraction of meaningful information. To address this issue, we propose a
Granger causal-based spatial–temporal contrastive learning framework, which significantly enhances
the ability to capture EEG signal information by modeling rich spatial–temporal relationships. Specif-
ically, in the spatial dimension, we employ a sampling strategy to select positive sample pairs from
individuals watching the same video. Subsequently, a Granger causality test is utilized to enhance
graph data and construct potential causality for each channel. Finally, a residual graph convolutional
neural network is employed to extract features from EEG signals and compute spatial contrast loss.
In the temporal dimension, we first apply a frequency domain noise reduction module for data
enhancement on each time series. Then, we introduce the Granger–Former model to capture time
domain representation and calculate the time contrast loss. We conduct extensive experiments on
two publicly available sentiment recognition datasets (DEAP and SEED), achieving 1.65% improve-
ment of the DEAP dataset and 1.55% improvement of the SEED dataset compared to state-of-the-art
unsupervised models. Our method outperforms benchmark methods in terms of prediction accuracy
as well as interpretability.
Citation: Wang, L.; Wang, S.; Jin, B.;
Wei, X. GC-STCL: A Granger Keywords: EEG; emotion recognition; contrastive learning; noise reduction; Granger causal
Causality-Based Spatial–Temporal
Contrastive Learning Framework for
EEG Emotion Recognition. Entropy
2024 , 26 , 540. https://doi.org/
1. Introduction
10.3390/e26070540
As a crucial component of affective computing, emotion recognition has garnered
Received: 12 April 2024 increasing attention from scholars in recent years and has emerged as a significant research
Revised: 6 June 2024 topic at the intersection of neuroscience, psychology, computer science, and artificial
Accepted: 17 June 2024
intelligence [ 1 ]. Broadly speaking, emotion recognition methods can be categorized into
Published: 24 June 2024
two groups: one based on non-physiological signals such as speech, text, facial expressions,
etc. [ 2 , 3 ], and the other based on physiological signals like electroencephalogram (EEG),
electrocardiogram (ECG), EMG, etc. [ 4 – 6 ]. Physiological signals directly reflect the brain’s
Copyright: © 2024 by the authors. state under different emotions and are considered to be more objective. With advancements
Licensee MDPI, Basel, Switzerland. in EEG acquisition equipment and technology, EEG has become the preferred method for
This article is an open access article studying the brain’s response to emotional stimuli.
distributed under the terms and Firstly, the mining of complex spatial topological relationships among EEG channels
conditions of the Creative Commons poses a significant challenge. The EEG signals are captured through multiple electrode
Attribution (CC BY) license (https:// channels that collectively form the spatial structure of these signals. Existing studies often
creativecommons.org/licenses/by/ determine channel spatial topological relationships solely based on the physical distance
4.0/).
Entropy 2024 , 26 , 540. https://doi.org/10.3390/e26070540 https://www.mdpi.com/journal/entropy
Entropy 2024 , 26 , 540 2 of 16
between electrodes or channel correlation, as exemplified by GCNN, P-GCNN, and GCNs-
Net [ 7 – 9 ]. However, previous research has demonstrated that different brain electrical
channels frequently exhibit intricate causal relationships. Therefore, simple undirected
graph modeling struggles to accurately depict the complex information transmission be-
tween these channels [ 10 , 11 ]. Consequently, we argue that directed causal graph modeling
can effectively capture the causal relationship between channels.
Secondly, high levels of noise interference constitute the primary factor contributing to
model overfitting in emotion recognition tasks. During the process of EEG data collection,
it is often subject to interference from internal emotions and external devices, resulting in a
low signal-to-noise ratio characteristic of EEG data. Furthermore, the high temporal reso-
lution of EEG signals necessitates a time-consuming and labor-intensive sample labeling
process. Most supervised or semi-supervised methods are ineffective when dealing with
limited labeled training data.Previous studies, such as SGMC and CLISA [ 12 , 13 ], employed
video alignment to obtain similar samples for constructing positive sample pairs. These
studies utilized an unsupervised contrast learning framework to extract intrinsic features
of specific emotional EEG signals, thereby enhancing the model’s generalization capability.
However, these methods still lack robustness against noise interference. Therefore, an
effective strategy for constructing positive samples pairs temporally can further augment
the model’s generalization ability.
To address the aforemen
```

---

## candidate-05 [neuroscience] — ANNOTATED as simpson-2013 (pass 12): functional brain networks survey; prose promoted from second_pass.md SP-15

**Title:** Analyzing complex functional brain networks fusing statistics and network scienc

**URL:** file:///9ab41bd50cb89388e97b54912f738a9eebc5ce1cb2d21aa14faf020cfc2f357a/Analyzing_complex_functional_brain_networks_fusing_statistics_and_network_scienc.pdf

**Description:** A comprehensive survey paper that reviews statistical and network science methods for analyzing complex functional brain networks from fMRI data. It covers network construction (parcellation, estimation, thresholding), descriptive graph metrics (clustering coefficient, path length, centrality, community structure), and modeling/inferential frameworks, identifying critical methodological gaps where statistical rigor must be fused with network science to advance understanding of brain function and disorders.

**Content extract (≤6k chars):**

```
Analyzing complex functional brain networks: fusing statistics and
network science to understand the brain
Sean L. Simpson
Department of Biostatistical Sciences
Wake Forest School of Medicine
Winston-Salem, NC
and
Department of Biostatistics
University of North Carolina at Chapel Hill
Chapel Hill, NC
email: slsimpso@wakehealth.edu
F. DuBois Bowman
Department of Biostatistics and Bioinformatics
The Rollins School of Public Health
Emory University
Atlanta, GA
email: dbowma3@emory.edu
Paul J. Laurienti
Department of Radiology
Wake Forest School of Medicine
Winston-Salem, NC
email: plaurien@wakehealth.edu
1
Abstract : Complex functional brain network analyses have exploded over the last decade ,
gaining traction due to their profound clinical implications. The application of network science
(an interdisciplinary offshoot of graph theory) has facilitated these analyses and enabled
examining the brain as an integrated system that produces complex behaviors. While the field of
statistics has been integral in advancing activation analyses and some connectivity analyses in
functional neuroimaging research, it has yet to play a commensurate role in complex network
analyses. Fusing novel statistical methods with network-based functional neuroimage analysis
will engender powerful analytical tools that will aid in our understanding of normal brain
function as well as alterations due to various brain disorders. Here we survey widely used
statistical and network science tools for analyzing fMRI network data and discuss the challenges
faced in filling some of the remaining methodological gaps. When applied and interpreted
correctly, the fusion of network scientific and statistical methods has a chance to revolutionize
the understanding of brain function.
Key words and phrases : graph theory, connectivity, fMRI, small-world, neuroimaging, network
model
1. Introduction
As evidenced by the launching of the Human Connectome Project (HCP) by the National
Institutes of Health (NIH) in 2009 and the 1000 Functional Connectomes Project in the same
year, whole-brain functional magnetic resonance imaging (fMRI) connectivity analyses are key in
our understanding of normal brain function as well as alterations due to various brain disorders
[1, 2]. fMRI measures localized brain activity by capturing changes in blood flow (hemodynamic
response) and oxygenation associated with neural activity. The blood oxygen level-dependent
(BOLD) contrast exploits the magnetic properties of oxygenated and deoxygenated blood to
capture these changes [3]. The brain is generally parcellated into cubic regions roughly a few
millimeters in size called voxels in which the brain activity measurements are made across a
series of scans. For coarser representations the BOLD signal time series are averaged across
voxels within a specified region. Functional connectivity analysis (FC) examines functional
associations (e.g., correlations) between time series pairs in specified voxels or regions [4, 5].
Effective connectivity analysis (EC) examines the directed influence of a time series from one
region on that from another [5]. Complex functional brain network (or connectivity) analysis is a
specific subfield of connectivity analysis in which associations are quantified for all time series
pairs to create an interconnected representation of the brain (a brain network). Studying the brain
as a network is appealing as it can be viewed as a system with various interacting regions that
produce complex behaviors [6, 7]. As with other biological networks, understanding the complex
network organization of the brain has profound clinical implications [1, 2, 6, 8].
2
This emerging area of complex fMRI network analyses has revealed methodological gaps that
require the integration of statistical tools with network-based neuroimage analysis. The
application of network science to the brain has facilitated our understanding of how the brain is
structurally and functionally organized. Furthermore, studying the brain within this framework
has already shed light on how some disorders such as Parkinson's disease ,  schizophrenia , and
Alzheimer's disease affect the brain [8-10]. In the case of Alzheimer's disease, the precuneus
shows the most reliable changes based on clinical positron emission tomography (PET) imaging
[11, 12]. It has been difficult to reconcile this finding with the predominant clinical symptom of
memory dysfunction, a cognitive process associated with the hippocampi. However, recent
network analyses have discovered that the precuneus is anatomically and physiologically a
central hub (highly connected area) in the brain [13]; thus, damage to it can lead to a number of
conditions and reverberate throughout many areas of the brain including the hippocampus. In
practice, graph metrics such as clustering coefficient, path length and efficiency measures are
often used to characterize system properties of brain networks . Centrality metrics such as degree,
betweenness, closeness, and eigenvector centrality determine critical areas within the network.
Community structure is also essential for understanding network organization and topology.
Network science has led to a paradigm shift in the neuroscientific community, but many
statistical issues remain unaddressed [14]. A more rigorous statistical assessment and a greater
scientific understanding of how current network models apply to the brain are needed. An
integrated appraisal of multiple network metrics should be performed to better understand
network structure rather than focusing on univariate assessments. Statistically comparing groups
of brain networks while accounting for their complex topologies remains a fertile area for
methodological development. In addition to accounting for the dependence structure of networks,
a framework in which the effects of multiple variables of interest and local network features (e.g.,
disease status, age, race, nodal clustering, nodal centrality, etc.) on the o
```

---

## candidate-06 [neuroscience] — UNCONSUMED

**Title:** Powerful statistical inference for nested data using sufficient summary statisti

**URL:** file:///4cb831a6e9429124c0321259c19da0d3779f5128473a1958adc470c8ad88623f/Powerful_statistical_inference_for_nested_data_using_sufficient_summary_statisti.pdf

**Description:** This paper reviews and formalizes the sufficient-summary-statistic approach for conducting powerful group-level statistical inference on hierarchically-organized (nested) data common in psychology and neuroscience. It provides step-by-step instructions for applying inverse-variance-weighted estimation to multiple effect size measures (means, differences, AUC), demonstrating improved statistical power over naive summary-statistic methods. The approach is validated on simulated data and EEG data from a driving simulator experiment.

**Content extract (≤6k chars):**

```
Powerful statistical inference for nested data using su ffi cient summary statistics
Irene Dowding a, ∗ , Stefan Haufe a, ∗
a Technische Universit¨ at Berlin
Abstract
Hierarchically-organized data arise naturally in many psychology and neuroscience studies. As the standard assumption of
independent and identically distributed samples does not hold for such data, two important problems are to accurately estimate
group-level e ff ect sizes, and to obtain powerful statistical tests against group-level null hypotheses. A common approach is to
summarize subject-level data by a single quantity per subject, which is often the mean or the di ff erence between class means,
and treat these as samples in a group-level t-test. This ‘naive’ approach is, however, suboptimal in terms of statistical power, as it
ignores information about the intra-subject variance. To address this issue, we review several approaches to deal with nested data,
with a focus on methods that are easy to implement. With what we call the su ffi cient-summary-statistic approach, we highlight
a computationally e ffi cient technique that can improve statistical power by taking into account within-subject variances, and we
provide step-by-step instructions on how to apply this approach to a number of frequently-used measures of e ff ect size. The
properties of the reviewed approaches and the potential benefits over a group-level t-test are quantitatively assessed on simulated
data and demonstrated on EEG data from a simulated-driving experiment.
Keywords: hierarchical inference, group-level e ff ect size, significance test, statistical power, su ffi cient summary statistic,
inverse-variance-weighting, Stou ff er’s method, event-related potentials
1. Introduction inference can be implemented for other commonly used ef-
fect size measures such as correlations or di ff erences in the
Data with nested (hierarchical) structure arise naturally in general central tendencies of distributions.
many fields. In psychology and neuroimaging, for example, In the neuroimaging (e.g., electro- and magnetoen-
multiple data points are often acquired for the same subject cephalography, EEG / MEG) literature, the use of suboptimal
throughout the course of an experiment; thus, there exists a inference procedures is currently still widespread, as dis-
subject (lower) and a group (higher) level in the data hierar- cussed in [40, 47]. Common hierarchical approaches often
chy. Two important questions are how to obtain precise esti- summarize subject-level data by a single quantity per sub-
mators for group-level e ff ect sizes from nested data, and how ject, which is often the mean or the di ff erence between class
to obtain powerful statistical tests for the presence of group- means, and treat these as single samples in a group-level test.
level e ff ects. The main di ffi culty associated with such nested This ‘naive’ summary-statistics approach is, however, not op-
data is that the assumption of identically distributed observa- timal in terms of statistical power, as it ignores information
tions is typically violated: while samples acquired from the about the intra-subject variance. Given the low signal-to-
same subject can be considered to be identically distributed, noise ratios and small sample regimes that are typical for
di ff erent distributions must be assumed for di ff erent subjects. neuroimaging studies, the potential loss of statistical power
Therefore, simply pooling the data of all subjects in order is unfortunate.
to apply a standard statistical test like a t-test would lead to
Group-level statistical power can be improved by incorpo-
wrong results.
arXiv:1702.03476v2 [math.ST] 30 Aug 2018 rating variances at the lower level in relatively simple ways.
A flexible way to model nested data is to combine the data
The problem of estimating group-level e ff ect sizes and esti-
of all subject in a single linear model, referred to as the nested
mating their statistical significance can, moreover, be formu-
linear model, hierarchical linear model, multi-level model or
lated in a compellingly simple framework, where group-level
linear mixed model [49, 29, 67, 8]. Parameter estimation in
inference is conducted using the su ffi cient summary statistics
such models is, however, di ffi cult to implement and compu-
of separate subject-level analyses. The resulting statistical
tationally expensive, as it typically requires non-linear opti-
methods are simple to implement, computationally e ffi cient,
mization of non-convex objective functions. Moreover, the
and can be easily extended to settings with more than two
range of e ff ects that can be modeled is limited to linear coef-
nesting levels, which are common, e.g., in the analysis of
ficients. It is, therefore, worthwhile to study how group-level
functional magnetic resonance imaging (fMRI) data. Su ffi -
cient summary statistics approaches are popular in the field
∗ Authors contributed equally. Corresponding author. of meta analysis [5, 7]. In neuroimaging, they are commonly
Email addresses: irenedowding@web.de (Irene Dowding), used to estimate group-level coe ffi cients of hierarchical lin-
stefanhaufe@gmail.com (Stefan Haufe) ear model [see 4, 39, for methodological reviews]. Here, we
argue that a wider range of popular e ff ect size measures can In this paper, our goal is to make inference about the presence
benefit from the high statistical power of su ffi cient-summary- or absence of an e ff ect in the population. The null hypothesis
statistic-based estimators. While this has been exploited in is that no e ff ect is present. The zero e ff ect is denoted by θ 0 .
various experimental studies [54, 24, 66, 35, 3], the theoreti- The null hypothesis of no e ff ect is denoted by H 0 : θ = θ 0 .
cal grounds on which such estimators are derived for di ff erent The alternative hypothesis that an e ff ect is present is denoted
e ff ect size measures have not yet been summarized in a single by H 1 . A one-ta
```

---

## candidate-07 [neuroscience] — UNCONSUMED

**Title:** Multimodal Attention Network for Continuous Time Emotion Recognition Using Video

**URL:** file:///81bfc5fe52071764de42ab4406c2966770069b8167eb8dd4c43186e1a44a73f8/Multimodal_Attention_Network_for_Continuous-Time_Emotion_Recognition_Using_Video.pdf

**Description:** This IEEE Access paper proposes a multimodal attention network that fuses facial video and EEG signals for continuous-time emotion recognition, using bilinear pooling based on low-rank decomposition to compute adaptive attention weights across modalities. Evaluated on the MAHNOB-HCI dataset and a proprietary ASIA dataset, the fusion approach achieves a 6.9% improvement in valence regression over a video-only baseline, demonstrating that adaptive multimodal weighting outperforms simple concatenation or averaging fusion strategies.

**Content extract (≤6k chars):**

```
Received October 13, 2020, accepted October 27, 2020, date of publication November 9, 2020, date of current version November 19, 2020.
Digital Object Identifier 10.1109/ACCESS.2020.3036877
Multimodal Attention Network for
Continuous-Time Emotion Recognition
Using Video and EEG Signals
DONG YOON CHOI , (Graduate Student Member, IEEE),
DEOK-HWAN KIM, (Member, IEEE), AND
BYUNG CHEOL SONG , (Senior Member, IEEE)
Department of Electronic Engineering, Inha University, Incheon 22212, South Korea
Corresponding author: Byung Cheol Song (bcsong@inha.ac.kr)
This work was supported in part by the Institute of Information and Communications Technology Planning and Evaluation (IITP)
Grant funded by the Korean Government [Ministry of Science and ICT (MSIT)], Artificial Intelligence Convergence Research Center
(Inha University), under Grant 2020-0-01389, and in part by the Industrial Technology Innovation Program through the Ministry of Trade,
Industry, and Energy (MI, South Korea), Development of Human-Friendly Human–Robot Interaction Technologies Using Human Internal
Emotional States, under Grant 10073154.
ABSTRACT Emotion recognition is a very important technique for ultimate interactions between human
beings and artificial intelligence systems. For effective emotion recognition in a continuous-time domain,
this article presents a multimodal fusion network which integrates video modality and electroencephalo-
gram (EEG) modality networks. To calculate the attention weights of facial video features and the corre-
sponding EEG features in fusion, a multimodal attention network, that is utilizing bilinear pooling based on
low-rank decomposition, is proposed. Finally, continuous domain valence values are computed by using two
modality network outputs and attention weights. Experimental results show that the proposed fusion network
provides an improved performance of about 6.9% over the video modality network for the MAHNOB human
computer interface (MAHNOB-HCI) dataset. Also, we achieved the performance improvement even for our
proprietary dataset.
INDEX TERMS Emotion recognition, video, EEG, multimodality, multimodal fusion, attention.
I. INTRODUCTION feature such as power spectral density (PSD) is extracted,
Recognition of human emotions is a key technology for ulti- and a typical machine learning algorithm is applied to rec-
mate human–robot interaction (HRI). In addition, emotion ognize emotions [6]. A few EEG-based algorithms [7], [8]
recognition has received much attention in the field of arti- employed the inherent asymmetry characteristics between
ficial intelligence. Conventional emotion recognition algo- EEG channels as salient features for deep learning-based
rithms distinguished emotion categories by detecting changes emotion classification. However, the conventional techniques
in facial expressions [1], [2]. Recently, various emotion have a structure that recognizes only a single emotion per tens
recognition mechanisms based on convolutional neural net- of seconds of video clip. So it is hard to say that they can
work (CNN) which are trained in an end-to-end manner have ultimately perceive emotional changes in the continuous-time
been developed and showed reliable performance [3], [4]. domain.
On the other hand, there were many attempts to recognize Busso et al. proposed an emotion recognition mecha-
human emotions from tone information of voice signals [5]. nism based on multimodal signals where two or more sig-
However, since the voice information is temporally sparse, nals among video, voice, and bio-signals are employed for
those voice tone-based emotion recognition schemes have a emotion recognition [10]. It was reported that multimodal
fundamental limitation in extracting consecutive emotions. approach was superior to conventional unimodal approaches.
Recently, several emotion recognition algorithms using EEG, On the other hand, a world-wide emotion recognition chal-
which is an electrical bio-signal generated in the human brain lenge called Emotion Recognition in the Wild (EmotiW)
have been reported [6]–[8]. For example, a frequency-domain [11] ranks competing algorithms [12], [13] through per-
formance evaluation for Acted Facial Expressions in the
The associate editor coordinating the review of this manuscript and Wild (AFEW) dataset that is composed of wild audio-visual
approving it for publication was Shiqing Zhang . data excerpted from sitcoms and movies. The AFEW dataset
203814 This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ VOLUME 8, 2020
D. Y. Choi et al. : Multimodal Attention Network for Continuous-Time Emotion Recognition Using Video and EEG Signals
consists of seven discrete-domain emotion classes. Such a introduce the proposed algorithm. Finally, we conclude this
discrete-domain dataset does not represent complex emotions article with experimental results and a discussion.
due to the limitation of the number of emotional classes, II. RELATED WORKS
and it cannot express the intensity of emotions. Therefore, This section briefly introduces previous studies on emotion
studies using continuous emotional labels such as valence recognition and multimodal deep learning.
and arousal have become active recently. Psychologically,
A. VIDEO-BASED EMOTION RECOGNITION
valence is an index that can differentiate between positive and
negative emotions, and arousal is an index that can discrim- For a long time, human emotions have been regarded as
inate between high and low emotions. Note that valence and being the same as facial expressions. So, facial video–based
arousal can be mapped to discrete-domain emotion classes if methods have been intensively developed for emotion recog-
necessary and have an advantage of expressing the emotion nition. Tong et al. [1] detected activated areas in the face,
intensity. and defined action units (AU) according to their positions
Meanwhile, Soleymani et al. [
```

---

## candidate-08 [neuroscience] — ANNOTATED as 10.1371-journal.pcbi.1013995 (pass 12): Fasoli et al. whole-cortex attractor model; prose promoted from cross_domain_bridges.md

**Title:** journal.pcbi.1013995

**URL:** file:///7dd04096896e865edcfd1215414da15229cae79ea04ed9744ff14884e2683e29/journal.pcbi.1013995.pdf

**Description:** A computational neuroscience research paper that develops a whole-cortex neural network model of resting-state fMRI in the mouse brain, incorporating directed anatomical connectivity from the Allen mouse brain atlas with excitatory-inhibitory interactions. The model, fitted only to static fMRI properties, predicts rich attractor dynamics (stationary and oscillatory) that recapitulate the topographical organization of empirical co-activation patterns (CAPs), demonstrating that CAPs emerge as a self-organizing property of directed cortico-cortical interactions rather than solely from subcortical modulatory input.

**Content extract (≤6k chars):**

```
RESEARCH ARTICLE
Attractor dynamics of a whole-cortex network
model predicts emergence and structure of fMRI
co-activation patterns in the mouse brain
Diego Fasoli 1 * , Ludovico Coletta 2 , Daniel Gutierrez-Barragan 2 , Silvia Gini 2 , 3 ,
Alessandro Gozzi 2 , Stefano Panzeri 4 *
1 School of Computer Science, University of Leeds, Leeds, United Kingdom, 2 Functional Neuroimaging
Laboratory, Istituto Italiano di Tecnologia, Center for Neuroscience and Cognitive Systems @UniTn,
Rovereto, Italy, 3 Center for Mind and Brain Sciences, University of Trento, Rovereto, Italy, 4 Institute for
Neural Information Processing, Center for Molecular Neurobiology (ZMNH), University Medical Center
Hamburg-Eppendorf (UKE), Hamburg, Germany
* d.fasoli@leeds.ac.uk (DF); s.panzeri@uke.de (SP)
Abstract
Resting state fMRI signals in mammals exhibit rich dynamics on a fast, frame-by-
frame timescale of seconds, including the robust emergence of recurring fMRI
co-activation patterns (CAPs). To understand how such dynamics emerges from the
OPEN ACCESS underlying anatomical cortico-cortical connectivity, we developed a whole-cortex
Citation: Fasoli D, Coletta L, Gutierrez-Barragan model of resting-state fMRI signals in the mouse. Our model implemented neural
D, Gini S, Gozzi A, Panzeri S (2026) Attractor
dynamics of a whole-cortex network model input-output nonlinearities and excitatory-inhibitory interactions within cortical regions,
predicts emergence and structure of fMRI as well as directed anatomical connectivity between regions inferred from the Allen
co-activation patterns in the mouse brain. PLoS mouse brain atlas. We found that, even if the model parameters were fitted to explain
Comput Biol 22(2): e1013995. https://doi.
org/10.1371/journal.pcbi.1013995 static properties of fMRI signals on the timescale of minutes, the model generated
rich frame-by-frame attractor dynamics, with multiple stationary and oscillatory attrac -
Editor: Samir Suweis, University of Padova:
Universita degli Studi di Padova, ITALY tors. Guided by these theoretical predictions, we found that empirical mouse fMRI
Received: January 25, 2025 time series exhibited analogous signatures of attractor dynamics, and that model
attractors recapitulated the topographical organization of empirical fMRI CAPs. The
Accepted: February 6, 2026
model established key relationships between attractor dynamics, CAPs and features
Published: February 20, 2026
of the directed cortico-cortical intra- and inter-hemispheric anatomical connectivity.
Copyright: © 2026 Fasoli et al . This is an open
Specifically, we found that neglecting fiber directionality severely affected the num -
access article distributed under the terms of
the Creative Commons Attribution License , ber of model’s attractors and their ability to explain CAPs. Furthermore, modifying
which permits unrestricted use, distribution, inter-hemispheric anatomical connectivity strength by decreasing or increasing it
and reproduction in any medium, provided the
original author and source are credited. from the value of real mouse anatomical data, resulted in fewer attractors generated
by cortico-cortical interactions and reduced non-homotopic features of the attrac -
Data availability statement : The code and data
to reproduce our results is made available and tors generated by the model, which were important for better predicting empirical
can be found at https://data.mendeley.com/ CAPs. These results offer novel theoretical insight into the dynamic organization of
datasets/xscxtshgfx/2 .
resting state fMRI in the mouse brain and suggest that the frame-wise BOLD activity
Funding: We acknowledge the support from captured by CAPs reflects an emerging property of cortical dynamics resulting from
the Simons Foundation for Autism Research
directed cortico-cortical interactions.
PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1013995 February 20, 2026 1 / 31
Initiative (SFARI; grant number 982347) to AG
and SP, the NIH Brain Initiative R01 NS108410 Author summary
to SP, the European Research Council (ERC)
under the European Union’s Horizon 2020 Whole-brain activity at rest transitions on a timescale of seconds between
research and innovation program (#DISCONN; stereotyped co-activation patterns (CAPs), each with a distinct spatial profile of
no. 802371 to AG). The funders had no role co-activation across different brain regions. CAPs have been robustly reported
in study design, data collection and analysis,
decision to publish, interpretation of results, or across datasets and mammalian species, including humans and mice. However,
preparation of the manuscript. the significance and origin of these patterns remain unknown. Here we studied
Competing interests: We have read the jour - the origin of CAPs using a computational model of the whole cortex based on
nal’s policy and the authors of this manuscript real-world directed measurements of mouse cortical anatomical connectivity. We
have the following competing interests: SP found that we could explain the formation and topography of CAPs in terms of at -
is a member of the editorial board of PLOS
tractors (that is, states the network tends to converge to) that reflect the informa -
Computational Biology. The other authors have
declared that no competing interests exist. tion in the anatomical connections between cortical regions. Attractors and CAPs
are significantly influenced by the directionality of connectivity (available in mice
but not in humans) and the strength of inter-hemispheric coupling. Together, our
findings suggest an additional possible mechanism of CAP generation based on
cortico-cortical connectivity which adds to current explanations based on con -
tributions from arousing modulatory nuclei. We thus suggest that CAPs may at
least in part emerge from cortico-cortical interactions.
Introduction
Resting-state fMRI has been widely used to map functional organization of spon -
taneous large-scale activity in the human brai
```

---

## candidate-09 [neuroscience] — UNCONSUMED

**Title:** Learning about Expectation Violation from Prediction Error Paradigms A Meta Anal

**URL:** file:///9ea2991adbe65cbe121dd21709918b7f84c766b938260279758a2b60de922e16/Learning_about_Expectation_Violation_from_Prediction_Error_Paradigms_A_Meta-Anal.pdf

**Description:** A meta-analysis of fMRI studies contrasting brain activity during 'active' prediction error paradigms (requiring behavioral adaptation) versus 'passive' paradigms (mere observation). The study finds greater neuronal activity in the striatum, insula, and fusiform gyrus when participants actively adapt behavior following prediction errors, suggesting that deliberate execution of action alternatives facilitates integration of new information into existing expectations.

**Content extract (≤6k chars):**

```
ORIGINAL RESEARCH
published: 28 July 2017
doi: 10.3389/fpsyg.2017.01253
Learning about Expectation Violation
from Prediction Error Paradigms – A
Meta-Analysis on Brain Processes
Following a Prediction Error
Lisa D’Astolfo * and Winfried Rief
Department of Clinical Psychology and Psychotherapy, Philipps University of Marburg, Marburg, Germany
Modifying patients’ expectations by exposing them to expectation violation situations
(thus maximizing the difference between the expected and the actual situational
outcome) is proposed to be a crucial mechanism for therapeutic success for a variety
of different mental disorders. However, clinical observations suggest that patients often
Edited by:
Karin Meissner, maintain their expectations regardless of experiences contradicting their expectations.
Ludwig-Maximilians-Universität It remains unclear which information processing mechanisms lead to modification or
München, Germany
persistence of patients’ expectations. Insight in the processing could be provided
Reviewed by:
Stephan Geuter, by Neuroimaging studies investigating prediction error (PE, i.e., neuronal reactions to
University of Colorado Boulder, non-expected stimuli). Two methods are often used to investigate the PE: (1) paradigms,
United States in which participants passively observe PEs (”passive” paradigms) and (2) paradigms,
Florian Beissner,
Hannover Medical School, Germany which encourage a behavioral adaptation following a PE (“active” paradigms). These
*Correspondence: paradigms are similar to the methods used to induce expectation violations in clinical
Lisa D’Astolfo settings: (1) the confrontation with an expectation violation situation and (2) an enhanced
lisa.dastolfo@uni-marburg.de
confrontation in which the patient actively challenges his expectation. We used this
Specialty section: similarity to gain insight in the different neuronal processing of the two PE paradigms. We
This article was submitted to performed a meta-analysis contrasting neuronal activity of PE paradigms encouraging
Cognition,
a section of the journal a behavioral adaptation following a PE and paradigms enforcing passiveness following
Frontiers in Psychology a PE. We found more neuronal activity in the striatum, the insula and the fusiform gyrus
Received: 30 October 2016 in studies encouraging behavioral adaptation following a PE. Due to the involvement
Accepted: 10 July 2017
Published: 28 July 2017 of reward assessment and avoidance learning associated with the striatum and the
Citation: insula we propose that the deliberate execution of action alternatives following a PE is
D’Astolfo L and Rief W (2017) associated with the integration of new information into previously existing expectations,
Learning about Expectation Violation therefore leading to an expectation change. While further research is needed to directly
from Prediction Error Paradigms –
A Meta-Analysis on Brain Processes assess expectations of participants, this study provides new insights into the information
Following a Prediction Error. processing mechanisms following an expectation violation.
Front. Psychol. 8:1253.
doi: 10.3389/fpsyg.2017.01253 Keywords: expectation violation, prediction error, fMRI, meta-analysis, striatum, insula
Frontiers in Psychology | www.frontiersin.org 1 July 2017 | Volume 8 | Article 1253
D’Astolfo and Rief Learning about Expectation Violation
INTRODUCTION The particular mechanisms underlying the information
processing and the persistence and change of expectations have
Patients’ expectations have a great influence on their treatment remained unclear. Clinical observations suggests that patients
and outcomes in psychotherapy (Greenberg et al., 2006), with mental disorders are particularly resistant to expectation
medical conditions as well as in patients undergoing change and the perception on expectation violations (Rief et al.,
surgery (Auer et al., 2016; Rief and Glombiewski, 2016). 2015; Rief and Glombiewski, 2016). There are promising new
In addition, negative expectations about psychological approaches examining immunization as one of the processing
interventions may lead to negative effects of psychotherapy strategies following expectation violation (Kube et al., 2016).
(Ladwig et al., 2014). Rief et al. (2015) have proposed to This could explain why even after a successful expectation
consider dysfunctional expectations to be core features of violation, the expectation is not changed. The patients perceive
mental disorders. It has been argued that dysfunctional the violation of their pre-existing expectation but attribute
behavior is guided by dysfunctional expectations of situational the situation to contextual factors, e.g., the setting. Thus, the
associations and outcomes. Hence, behavioral therapy would confrontation with an aversive stimulus with aim of reducing an
only be successful if there is a change of the dysfunctional emotional response, as is commonly used in psychotherapeutic
expectations guiding the behavior. These dysfunctional settings, might not always be enough to induce a persistent
expectations are pre-existing assumptions about contingencies expectation change. Craske et al. (2014) proposed methods
with a high subjective associative strength, i.e., subjective of maximizing such exposure techniques, which are supposed
certainty. Patients would have to experience an expectation to increase the inhibitory learning of the old expectation
violation, i.e., a state, in which the expected outcome and about the contingencies. One of these methods is the active
the actual outcome differ, to induce a change in their testing of the pre-existing expectation. This is suggested to
expectations about the contingencies. This corresponds facilitate the relearning of the contingencies and to stabilize
to a relearning of the contingencies, i.e., a state, in which the newly learned expectation, thus inducing an expectation
they perceive a difference between expected outcome and change.
the actual outco
```

---

## candidate-10 [neuroscience] — UNCONSUMED

**Title:** A Review of the Status of Brain Structure Research in Transsexualism

**URL:** file:///9dc24ccf147889f5019a42e75ff730ca5bac17dd05ce97dbedf5f47c61c5af54/A_Review_of_the_Status_of_Brain_Structure_Research_in_Transsexualism.pdf

**Description:** A peer-reviewed review paper examining in vivo neuroimaging studies of brain structure in male-to-female and female-to-male homosexual transsexuals before and after cross-sex hormone treatment. The authors synthesize cortical thickness and diffusion tensor imaging findings to propose distinct brain phenotypes for MtFs (masculine, feminine, and demasculinized regions) and FtMs (feminine, masculine, and defeminized regions) that differ from both male and female controls. They hypothesize that these cortical differences arise from differently timed cortical thinning processes across brain regions, grounded in the neurohormonal theory of sexual differentiation.

**Content extract (≤6k chars):**

```
Arch Sex Behav (2016) 45:1615–1648
DOI 10.1007/s10508-016-0768-5
O RI G I N A L P A PE R
A Review of the Status of Brain Structure Research in
Transsexualism
Antonio Guillamon 1,2 • Carme Junque 3,4 • Esther Go ´mez-Gil 4,5
Received: 16 July 2014 / Revised: 22 September 2015 / Accepted: 29 April 2016 / Published online: 2 June 2016
Ó The Author(s) 2016. This article is published with open access at Springerlink.com
Abstract The present review focuses on the brain structure of Keywords Transsexualism  Sex differences 
male-to-female (MtF) and female-to-male (FtM) homosexual Gender identity  Gender dysphoria 
transsexuals before and after cross-sex hormone treatment as Cross-sex hormone treatment  Magnetic resonance imaging
shown by in vivo neuroimaging techniques. Cortical thickness
and diffusion tensor imaging studies suggest that the brain of
MtFs presents complex mixtures of masculine, feminine, and Introduction
demasculinized regions, while FtMs show feminine, masculine,
and defeminized regions. Consequently, the specific brain phe- Transsexuals seek or have undergone a social transition from
notypes proposed for MtFs and FtMs differ from those of both male to female (MtF) or female to male (FtM), a transition that in
heterosexual males and females. These phenotypes have theo- many, but not all, cases also involves a somatic transition by cross-
retical implications for brain intersexuality, asymmetry, and sex hormone treatment and genital surgery (American Psychiatric
bodyperceptionin transsexualsaswellasforBlanchard’shypothe- Association, 2013; Meyer-Bahlburg, 2010, 2013).
sis on sexual orientation in homosexual MtFs. Falling within the Although the etiology of transsexualism is unknown, biolog-
aegis of the neurohormonal theory of sex differences, we hypoth- ical and environmental factors have been suggested to contribute
esize that cortical differences between homosexual MtFs and FtMs to gender identity variations (Cohen-Kettenis & Gooren, 1999;
and male and female controls are due to differently timed cortical Savic, Garcia-Falgueras, & Swaab, 2010; Lawrence & Zucker,
thinning in different regions for each group. Cross-sex hormone 2014). Biological causes for gender dysphoria (GD) are sup-
studies have reported marked effects of the treatment on MtF and ported by studies on familial groups (Gomez-Gil et al., 2010;
FtM brains. Their results are used to discuss the early postmortem Green, 2000), birth order (Blanchard & Sheridan, 1992; Blan-
histological studies of the MtF brain. chard, Zucker, Cohen-Kettenis, Gooren, & Bailey, 1996; Gomez-
Gil et al., 2011; VanderLaan, Blanchard, Wood, Garzon, &
Zucker, 2015; Vasey & VanderLaan,2007), andtwins (McKee,
Roback, & Hollender, 1976; Zucker & Bradley, 1995). A review
& Antonio Guillamon of the literature of twins concordant and discordant for GD sug-
aguillamon@psi.uned.es
gests a role for genetics in the development of GD (Heylens et al.,
1 Departamento de Psicobiologı ´a, Universidad Nacional de 2012). Molecular genetics have been used to analyze peripheral
Educacio ´n a Distancia, c/Juand del Rosal, 10, 28040 Madrid, sex steroid-related polymorphisms in steroid receptors or steroid
Spain enzyme genes (Fernandez et al., 2014a, 2014b; Hare et al., 2009;
2 Academia de Psicologı ´a de Espan ˜a, Madrid, Spain Henningssonetal.,2005;Ujikeetal.,2009).Researchonprenatal
3 Departamento de Psiquiatrı ´a y Psicobiologı ´a Clı ´nica, androgen exposure markers has provided some evidence of
Universidad de Barcelona, Barcelona, Spain transsexual differences based on the 2D:4D ratio (Schneider,
4 Institute of Biomedical Research August Pi i Sunyer, Barcelona, Pickel & Stalla, 2006; Wallien, Zucker, Steensma & Cohen-
Spain Kettenis, 2008). The findings from all the above studies suggest
5 Unidad de Identidad de Ge ´nero, Hospital Clinic, Barcelona, that genetic factors could influence brain and behavioral phe-
Spain notypes.
123
1616 Arch Sex Behav (2016) 45:1615–1648
In regard to environmental variables, parental and family fac- address the structural phenotype of the brain in homosexual MtFs
tors have been reviewed (Lawrence & Zucker, 2014); parental and FtMs before cross-sex hormone treatment; (2) discuss these
influences seem to be a contributing factor to the development of brain phenotypes in the light of the neurohormonal theory of sex-
GID (Cohen-Kettenis & Gooren, 1999) and play a role in social ual differentiation of the brain; (3) describe the effects of cross-
gender transitioning (Steensma, McGuire, Kreukels, Beekman, sex hormone treatment on the structure of the brain; and (4) ana-
& Cohen-Kettenis, 2013). lyzethehistologicalpostmortemstudiesinlightoftheinvivoneu-
With respect to the developmental course of GD and sexual roimaging results. Investigating these objectives has suggested an
orientation, DSM-5 indicates that in both natally male and female explanatory hypothesis on gender. In approaching these objec-
children showing persistence, almost all are sexually attracted to tives, we encountered several difficulties. The main one is the
individuals of their natal sex. Moreover, there are two broad scant number of published MRI studies on the brain of transsexu-
trajectories for the development of GD: early-onset and late- als; this scarcity is more extreme in regard to nonhomosexual
onset. Early-onset GD starts in childhood and continues into MtFs and FtMs. Moreover, some studies do not report sexual ori-
adolescence and adulthood, while late-onset GD begins entation or mix homosexual and nonhomosexual subjects.
around puberty or even much later in life. Adolescent and adult
natal males with early onset of GD are almost always androphilic,
while most with a late onset are gynephilic. In natal females, the Morphological Characteristics of Sex Differences in
most common course is early-onset GD; they are almost always the Mammalian Brain
gynephilic, while the few with late-onset GD are usually andro-
philic (APA, 2013, pp. 455–456
```

---

## candidate-11 [neuroscience] — UNCONSUMED

**Title:** WAVELET TRANSFORMS FOR EEG SIGNAL DENOISING AND DECOMPOSITION

**URL:** file:///e25d140a6a63e56634f72726e73b8b8b8b771a83a429ae4016b1cf50b78b6ef8/WAVELET_TRANSFORMS_FOR_EEG_SIGNAL_DENOISING_AND_DECOMPOSITION.pdf

**Description:** A research paper comparing three wavelet transform methods (DWT, WPT, SWT) with three mother wavelets (Haar, Symlet2, Coiflet2) for EEG signal denoising, evaluated on the University of Bonn epilepsy benchmark dataset. The study finds Symlet2-SWT at level four achieves the best denoising performance (SNR 27.32, PSNR 40.02, MSE 5.09), and further compares four decomposition methods (DWT, MODWT, EMD, VMD) using energy, correlation, and PSD distance metrics, with EMD showing superior decomposition characteristics.

**Content extract (≤6k chars):**

```
Int. J.Adv.Sig.Img.Sci, Vol. 9, No. 2, 2023
WAVELET TRANSFORMS FOR EEG SIGNAL DENOISING
AND DECOMPOSITION
Ibtihal Hassan Elshekhidris
Biomedical Engineering Department,
Sudan University of Science and Technology,
Khartoum, Sudan.
hooola88@hotmail.com
Magdi Baker MohamedAmien
Electrical and Electronic Engineering Department,
University of Khartoum,
Khartoum, Sudan.
magdy.baker@uofk.edu
Ahmed Fragoon
Biomedical Engineering Department,
Sudan University of Science and Technology,
Khartoum, Sudan.
ahmedfragoon@sustech.edu
Submitted: Jul, 07, 2023 Revised: Sep, 11, 2023 Accepted: Sep, 21, 2023
Abstract: EEG signal analysis is difficult because there are so many unwanted
impulses from non-cerebral sources. Presently, methods for eliminating noise
through selective frequency filtering are afflicted with a notable deprivation of EEG
information. Therefore, even if the noise is decreased, the signal's uniqueness
should be preserved, and decomposition of the signal should be more accurate for
feature extraction in order to facilitate the classification of diseases. This step
makes the diagnosis faster. In this study, three types of wavelet transforms were
applied: Discrete Wavelet Transform (DWT), Wavelet Packet Transform (WPT), and
Stationary Wavelet Transform (SWT), with three mother functions: Haar, Symlet2,
and Coiflet2. Three parameters were used to evaluate the performance: Signal-to-
Noise Ratio (SNR), Mean Square Error (MSE), and Peak Signal-to-Noise Ratio
(PSNR). Most of the higher values of SNR and PSNR were 27.3189 and 40.019,
respectively, and the lowest value of MSE was 5.0853 when using Symlet2-SWT
level four. To decompose the signal, we relied on the best filter used in the
denoising process and applied four methods: DWT, Maximal Overlap DWTs
(MODWT), Empirical Mode Decomposition (EMD), and Variational Mode
Decomposition (VMD). The comparison has been made between the four methods
based on three metrics: energy, correlation coefficient, and distances between the
Power Spectral Density (PSD), where the highest value of energy was 5.09E+08
and the lowest value of the PSD was -1.2596 when using EMD.
Keywords: Wavelet transform, mother wavelet, empirical mode decomposition,
variational mode decomposition.
11
Int. J.Adv.Sig.Img.Sci, Vol. 9, No. 2, 2023
I. INTRODUCTION
The ElectroEncephaloGraphy (EEG) is a non-invasive degree of the electrical
interest of the mind thru the location of electrodes at the scalp in regions of the mind,
and used as the primary sign to pick out an expansion of brain-related conditions,
inclusive of narcolepsy, Sleep apnea syndrome, Insomnia, Parasomnia, and Epileptic
seizures. There are two origins of the artifacts that impact the EEG signal, namely
physiological and non-physiological. The physiological origins consist of
ElectroOculoGraphy (EOG) artifacts, ocular artifacts; muscular noise in
ElectroMyoGraphy (EMG), cardiac signals, whilst non-physiological factors
encompass line disruptions and electrode interference Therefore, removing noise from
the EEG signal is of utmost importance during the preprocessing phase. Additionally,
decomposition of the EEG signal performs a good function in feature extraction for
the classification of epileptic seizures.
When recording EEG data, it is important to be aware of signal artifacts as
they can greatly affect the quality of the data. These artifacts have the potential to
contaminate the EEG data and must be addressed in order to ensure accurate
results. Artifacts refer to undesirable signals that primarily stem from outside of the
body like environmental, and inside of the body like ocular, muscle, and cardiac
artifacts that produce notable distortions in EEG recordings originate from the body
itself [1]. Muscle artifacts are another origin of artifacts. The electrical signals
produced by the muscles when they contract can be detected on the surface of the
body by means of the EMG technique [2]. This type of artifact may arise from actions
such as swallowing, chewing, grimacing, frowning, talking and hiccupping, both
during wakefulness and sleep. In addition, the activity of the heart can also generate
artifacts in the EEG signal. Depending on the location of the electrodes and the shape
of the body, the electrical signals produced by the heart (as reflected in the ECG) may
interfere with the EEG [3].
Denoising and decomposition of the EEG signal have been proposed using
multiple techniques. The wavelet is the best method for denoising than others in [4].
A numerous noise elimination technique from EEG signal is studied in [5], and the
best result was obtained when using WPT. The efficacy of denoising techniques based
on wavelets for EEG signals has been investigated in a study on EEG signals [6]. Four
distinct discrete wavelet functions were employed to eliminate noise from the
Electroencephalogram signal obtained from two different patient groups (healthy and
epileptic) to demonstrate the efficiency of DWT in eliminating EEG noise.
IIR low pass filter, FIR low pass and wavelet transform method were applied to
the distorted EEG signal; the mother wavelet (symlet) has been more compatible with
the EEG signal founded by determining the higher SNR and minimum MSE than the
all other filters and wavelets in [7]. Wavelet transform with different kinds of filters
such as db2, db4, coif2, coif4, sym2, and sym4 are used to decompose the signal into
low and high frequency components in [8]. It is observed that minimax threshold
estimation with soft thresholding using the wavelet filter coif4 performs better in
terms of PSNR. Various wavelet transform based denoising techniques were discussed
in [9]. Several methods have presented the decomposition of a signal, and a
comparative study between DWT and maximal overlap DWT for testing stationarity
was described in [10]. EMD and VMD and its comparison was made between them in
[11]. In [12], a comparison between EMD and Intrinsic timescale decomposition (ITD)
was provided.
12
Int. J.
```

---

## candidate-12 [neuroscience] — UNCONSUMED

**Title:** Kolmogorov Arnold Networks for Time Series Granger Causality Inference

**URL:** file:///90c29206d81e47c4571628603455f1f9d3b9e402f66a16ef3543e20630c34b7c/Kolmogorov-Arnold_Networks_for_Time_Series_Granger_Causality_Inference.pdf

**Description:** This paper proposes KANGCI, a novel architecture extending Kolmogorov-Arnold Networks (KAN) to Granger causality inference for time series. By extracting base weights from KAN layers and applying group lasso penalty with ridge regularization, the model infers causal relationships from nonlinear, high-dimensional, limited-sample time series. A time-reversed Granger causality algorithm automatically selects or fuses causal adjacency matrices to mitigate spurious connections, achieving competitive performance across Lorenz-96, gene regulatory, fMRI, VAR, and EEG datasets.

**Content extract (≤6k chars):**

```
Kolmogorov-Arnold Networks for Time Series Granger Causality Inference
Meiliang Liu 1 Yunfang Xu 1 Zijin Li 1 Zhengye Si 1 Xiaoxiao Yang 1 Xinyue Yang 1 Zhiwen Zhao 1
Abstract neural network (RNN) (Khanna & Tan, 2019; Tank et al.,
We propose the Granger causality inference 2022), convolutional neural network (CNN) (Nauta et al.,
Kolmogorov-Arnold Networks (KANGCI), a 2019), or their combination (Cheng et al., 2024). These
novel architecture that extends the recently pro- models have achieved significant improvements in inferring
posed Kolmogorov-Arnold Networks (KAN) to nonlinear Granger causality but still have some limitations:
the domain of causal inference. By extracting (1) RNN-based models are more suitable for processing
base weights from KAN layers and incorporating long time series but experience decreased inference perfor-
the sparsity-inducing penalty and ridge regular- mance in the limited time-sample scenario. (2) MLP-based
ization, KANGCI effectively infers the Granger models face the challenge of low inference efficiency when
causality from time series. Additionally, we pro- dealing with high-dimensional and noisy time series. (3)
pose an algorithm based on time-reversed Granger CNN-based models perform ineffectively on many nonlin-
causality that automatically selects causal rela- ear datasets.
tionships with better inference performance from Therefore, our motivation is to propose a neural network-
the original or time-reversed time series or in- based Granger causality model that can effectively infer
tegrates the results to mitigate spurious connec- causal relationships from high-dimensional nonlinear time
tivities. Comprehensive experiments conducted series with limited sampling points. We consider a novel
on Lorenz-96, Gene regulatory networks, fMRI framework, the Kolmogorov-Arnold Network (KAN) (Liu
BOLD signals, VAR, and real-world EEG datasets et al., 2024), to construct a Granger causality inference
demonstrate that the proposed model achieves model. Different from MLP, which uses learnable weights
competitive performance to state-of-the-art meth- on the edges and fixed activation functions on the nodes,
ods in inferring Granger causality from nonlinear, KAN uses learnable univariate functions at the edges and
high-dimensional, and limited-sample time series. simple summation operations at the nodes, making its com-
putational graph much smaller than that of MLP (Kiamari
et al., 2024; Hou & Zhang, 2024).
1. Introduction
Our work extends the basic KAN to the field of causal
Granger causality is a statistical framework for analyzing the inference and aims to evaluate whether the KAN-based
causal relationship between time series. It offers a powerful model has the potential to outperform MLP-based and RNN-
tool to investigate temporal dependencies and the direction based baselines. Our main contributions are as follows:
of influence between variables (Seth, 2007; Maziarz, 2015;
Friston et al., 2014; Shojaie & Fox, 2022). By examining
the past values of time series, Granger causality seeks to de- • We propose a simple but effective Granger causal-
arXiv:2501.08958v2 [cs.LG] 5 Feb 2025
termine if the historical knowledge of one variable improves ity model based on KAN. The model only needs to
the prediction of another (Bressler & Seth, 2011; Barnett & extract base weights of KAN layers and impose the
Seth, 2014). Revealing inner interactions from time series sparsity-inducing penalty and ridge regularization to
has made Granger causality useful for the investigation in infer Granger causality.
many fields, such as econometrics (Mele et al., 2022), neu-
• We propose an algorithm that automatically selects
roscience (Chen et al., 2023), climate science (Ren et al.,
the Granger causality adjacency matrix with the higher
2023), etc.
inference performance from the origin or time-reversed
Recently, there has been a growing interest in incorporating time series or mitigates spurious connections by fusing
the neural network into the study of Granger causality due to both of them.
its inherent nonlinear mapping capabilities. For now, a vari-
ety of neural Granger causality models have been proposed, • Extensive experiments on Lorenz-96, Gene regulatory
mainly based on multi-layer perceptron (MLP) (Tank et al., networks, fMRI BOLD, VAR, and real-world EEG
2022; Bussmann et al., 2021; Zhou et al., 2024), recurrent datasets validate that the proposed model attains stable
1
Kolmogorov-Arnold Networks for Time Series Granger Causality Inference
and competitive performances in Granger causality depend on different past-time lags from all the series:
inference.
x ti = g i ( x <t 1 , . . . , x <tp ) + e ti (2)
2. Background and Related Works
To infer Granger causality from the component-wise NAR
2.1. Background: Neural network-based Granger
model, sparsity-inducing penalty is applied:
causality
Inferring Granger causality from nonlinear time series via X T
2
neural networks has attracted widespread attention. Tank min ( x
W ti − g i ( x <t 1 , . . . , x <tp ))
et al. (2022) proposed the cMLP and cLSTM, which ex- t = K
tracted the first-layer weights of MLP and long short-term X p (3)
memory (LSTM) and imposed the sparsity-inducing penalty + λ Θ ( W : ,j )
to infer Granger causality. Bussmann et al. (2021) pro- j =1
posed the Neural Additive Vector Autoregression (NAVAR)
where W is extracted from the neural network, Θ is the
model based on MLP and LSTM, called NAVAR(MLP) and
sparsity-inducing penalty that penalizes the parameters in
NAVAR(LSTM), for Granger causality inference. Khanna
W to zero, λ is the hyperparameter that controls the strength
& Tan (2019) proposed the economy-SRU (eSRU) model,
of the penalty. In the NAR model, if there exists a time lag
which extracted weights from statistical recurrent units
k , W k
(SRU) and also imposed sparsity-inducing penalty to in- : ,j contains non-zero parameters, time series j Granger-
causes to time series i .
fer Granger causality. Nauta
```

---

## candidate-13 [matching-infotheo] — ANNOTATED as 2604.08539 (pass 11): 1D-OT advantage matching in RL → Matching+Stability

**Title:** OpenVLThinkerV2 A Generalist Multimodal Reasoning Model for Multi domain Visual

**URL:** file:///6d47c3f42333238f164bf3b0856f87cecffe3aa777dc8fbc25e512892a3f1015/OpenVLThinkerV2_A_Generalist_Multimodal_Reasoning_Model_for_Multi-domain_Visual_.pdf

**Description:** This preprint introduces OpenVLThinkerV2, a generalist multimodal reasoning model built on Qwen3-VL-Instruct-8B, along with Gaussian GRPO (G²RPO)—a novel RL training objective that replaces linear reward standardization with non-linear distributional matching via 1D Optimal Transport, forcing advantage distributions to a standard normal N(0,1). Combined with task-level response length and entropy shaping, the approach achieves SOTA results across 18 benchmarks spanning general VQA, math, chart/document understanding, spatial reasoning, and visual grounding, surpassing GPT-4o, GPT-5, and Gemini 2.5 Pro on multiple tasks.

**Content extract (≤6k chars):**

```
Preprint. Under review.
OpenVLThinkerV2: A Generalist Multimodal Reasoning
Model for Multi-domain Visual Tasks
Wenbo Hu Xin Chen Yan Gao-Tian Yihe Deng Nanyun Peng
Kai-Wei Chang
University of California, Los Angeles (UCLA)
{whu, kwchang}@cs.ucla.edu
Project Page GitHub
Abstract
Group Relative Policy Optimization (GRPO) has emerged as the de facto
Reinforcement Learning (RL) objective driving recent advancements in
Multimodal Large Language Models. However, extending this success to
open-source multimodal generalist models remains heavily constrained by
two primary challenges: the extreme variance in reward topologies across
diverse visual tasks, and the inherent difficulty of balancing fine-grained
perception with multi-step reasoning capabilities. To address these issues,
we introduce Gaussian GRPO (G 2 RPO) , a novel RL training objective that
replaces standard linear scaling with non-linear distributional matching.
By mathematically forcing the advantage distribution of any given task
to strictly converge to a standard normal distribution, N ( 0, 1 ) , G 2 RPO
theoretically ensures inter-task gradient equity, mitigates vulnerabilities to
heavy-tail outliers, and offers symmetric update for positive and negative
rewards. Leveraging the enhanced training stability provided by G 2 RPO,
we introduce two task-level shaping mechanisms to seamlessly balance per-
ception and reasoning. First, response length shaping dynamically elicits
extended reasoning chains for complex queries while enforce direct outputs
to bolster visual grounding. Second, entropy shaping tightly bounds the
model’s exploration zone, effectively preventing both entropy collapse and
entropy explosion. Integrating these methodologies, we present OpenVL-
ThinkerV2 , a highly robust, general-purpose multimodal model. Extensive
evaluations across 18 diverse benchmarks demonstrate its superior perfor-
mance over strong open-source and leading proprietary frontier models.
25%
Task Categories
General VQA
20% +18.9% +19.1% Math VQA
arXiv:2604.08539v1 [cs.CV] 9 Apr 2026 +17.6% Chart VQA
Spatial Reasoning
Document Understanding
15% +13.3% Grounding
+11.2%
10%
+7.7% +7.0% +6.3% +5.6% +6.3%
5% +3.6% +4.3% +4.0% +3.9% +4.4% +4.1%
+1.6% +1.5%
0%
MMMU AI2D
MMBench MMStar
MathVista ChartQA DocVQA InfoVQA
MathVerse RefCOCO
MathVision CharXiv(RQ) EmbSpatial RefSpatial RoboSpatial OCRBench RefCOCO+ RefCOCOg
Figure 1: Performance improvement (relative) of OpenVLThinkerV2 over its baseline Qwen3-
VL-Instruct-8B across diverse visual tasks.
1
Preprint. Under review.
Previous Approaches: Imbalanced Gradient Update Ours: Gaussian, Symmetric, Balanced Update
Inter-Task Advantage Distribution Mismatch ❌ Inter-Task Equal Advantage Distribution ✅
GRPO DR.GRPO EMA-GRPO G ² RPO (Ours)
Binary Reward (e.g., Math, MCQ) Sparse Reward (e.g., OCR, Regression)
[0, 0, 0, 0, 1] [0.1, 0.1, 0.1, 0.2, 1.0]
GRPO [−0.5,−0.5,−0.5,−0.5, 2.0 ] Heavy Skewed, Outlier Impacts,
Strong Update EMA-GRPO [−1.28,−1.28,−1.28,−0.63, 4.48 ] Catastrophic Update
Ours [−0.32,−0.32,−0.32,−0.32,1.28] Symmetrical Robust to Outlier,
Update Ours [−0.6,−0.6,−0.6,0.52,1.28] Prevent Gradient Explosions
Binary Reward (e.g., Math, MCQ) Dense (e.g., Grounding)
[0, 0, 1, 1, 1] [0.81, 0.81, 0.82, 0.82, 0.83]
GRPO [−1.22,−1.22,0.81,0.81,0.81] Jagged Gradient DR.GRPO [−0.008,−0.008,0.02,0.02,0.02 Minimal Update,
Inter-task Imbalance
Ours [−0.9,−0.9,0.6,0.6,0.6] Continuous Update Ours [−0.9,−0.9,+0.26,0.26,1.28] Effective Update,
Inter & Intra Task Balance
Figure 2: Comparison of advantage formulations against previous methods. By enforcing
a Gaussian topology, G 2 RPO provides 1) intrinsic robustness to outliers, 2) symmetric
updates for positive and negative rewards, and 3) uniform variance across diverse tasks.
[0.81, 0.81, 0.82, 0.82, 0.83]
1 Introduction Previous: e.g.
DR.GRPO [−0.008,−0.008,0.02,0.02,0.02
Reinforcement Learning (RL) has emerged as a primary driver of recent advancements in Ours [−0.9,−0.9,+0.26,0.26,1.28]
Multimodal Large Language Models (MLLMs), significantly enhancing performance across
domains ranging from complex visual reasoning to fine-grained object detection (Bai et al.,
2025; Comanici et al., 2025; Singh et al., 2026; Liu et al., 2025c; Feng et al., 2025b; Team, 2026;
Seed, 2026), encompassing the diverse spectrum of tasks illustrated in Figure 1. However,
the vast diversity of visual tasks imposes a significant challenge when optimizing them
jointly during the MLLM post-training stage. The extreme variance in reward topologies—
Advantages: Long-tail Distribution Lucky Outlier
ranging from sparse, binary signals in math visual question answering (VQA) to dense,
continuous Intersection-over-Union (IoU) scores in grounding tasks—creates significant Advantages: Bi-modal Distribution Low-Variance
intra- and inter-task update imbalances. This instability is particularly detrimental to the
[−0.51,−0.51,−0.51,−0.25,1.79] Previous Approaches:
Group Relative Policy Optimization (GRPO) (Guo et al., 2025) algorithm, rendering it highly DR.GRPO [−0.2,−0.2,−0.2,−0.2, 0.8 ]
susceptible to gradient explosion during large-scale training.
[−0.008,−0.008,+0.002,+0.002,+0.012]
Standard GRPO suffers from intra-task imbalance because its sample-wise standard devia-
tion normalization disproportionately favors low-variance rollouts (Liu et al., 2025b; Bereket
& Leskovec, 2025; Chu et al., 2025; Huang et al., 2025). Dr.GRPO (Liu et al., 2025b) removes
this normalization but inevitably causes inter-task imbalance, where high variance tasks
dominate gradient update and low variance ones are suppressed. While recent methods like
EMA-GRPO (Feng et al., 2025b) mitigate this using task-wise moving averages of reward
variance, they fundamentally rely on linear transformations. Since linear scaling merely
matches the first two statistical moments (mean and variance) while preserving higher-order
distributional shapes, it fails to guarantee true inter-task gradient equity and leaves the
optimizatio
```

---

## candidate-14 [dynamics-matching] — REJECTED
DTW motif discovery is a single machine (alignment matching) and duplicates the DTW-matching coverage of 2002.00208.

**Title:** 2009.07907v1

**URL:** file:///962da28844dc3e87d1efd596a6696f29c9e472de612a455319b6fbe440509077/2009.07907v1.pdf

**Description:** This research paper introduces SWAMP (Scalable Warping Aware Matrix Profile), the first exact algorithm for discovering time series motifs under Dynamic Time Warping (DTW) distance rather than the traditional Euclidean distance. The authors present a novel hierarchy of lower bounds based on downsampled PAA representations that automatically trade off computation time against tightness, enabling admissible pruning of up to 99.99% of DTW computations. The work demonstrates that DTW-based motif discovery reveals conserved patterns in real-world data (e.g., electrical power demand, medical signals) that Euclidean distance motifs miss entirely.

**Content extract (≤6k chars):**

```
Matrix Profile XXI I : Exact Discovery of Time Series
Motifs under DTW
Sara Alaee Kaveh Kamgar Eamonn Keogh
University of California University of California University of California
Riverside Riverside Riverside
salae001@ucr.edu kkamg001@ucr.edu eamonn@cs.ucr.edu
Abstract — Over the last decade, time series motif discovery has motif. The complexity of the pattern that is conserved points to
emerged as a useful primitive for many downstream analytical a common mechanism. In fact, this is the case. This pattern
tasks, including clustering, classification, rule discovery, corresponds to a particular program from a dishwasher. Why
segmentation, and summarization. In parallel, there has been an was this pattern not discovered by the classic motif discovery
increased unders tanding that Dynamic Time Warping (DTW) is algorithm? As we will show, the us e of ED is the culprit and
the best time series similarity measure in a host of settings. DTW is the solution.
Surprisingly however, there has been virtually no work on using
DTW to discover motifs. The most obvious explanation of this is
A B C D
the fact that both mot if discovery and the use of DTW can be
computationally challenging, and the current best mechanisms to
address their lethargy are mutually incompatible. In this work, we
present the first scalable exact method to discover time series 60 minutes
motifs under DTW. Our method automatically performs the best
trade - off between time - to - compute and tightness - of - lower - bounds Fig. 2. A pair of subsequences from household electrical power demand data.
for a novel hierarchy of lower bounds representation we The pattern corresponds to a particular dishwasher cycle: (A) short run of
introduce. We show that under realistic settings, our algorithm discharge pump to empty any liquid in the machine, (B) pumpin g water into
can admiss i bly prune up to 99.99% of the DTW computations . reservoir, (C) spraying water over dishes (D) pumping out water.
Keywords — Time series Motifs, Dynamic Time Warping As we will show, given the ability to find motifs under DTW,
examples li ke the one above are replete in diverse domains such
I. I NTRODUCTION as industry, medicine, and human behavior. Given tha t there is
Time series motif discovery — the unearthing of locally a large body of literature on both motif discovery and DTW,
conserved behavior in a long time series — has emerged as one why are there essentially no DTW - based motif discovery tools?
of the most important time series primitives in the last decade We believe that the following explains this omission. Both
[1] . In re cent years, there has been significant progress in the motif discovery and DTW comparisons are famously
scalability of motif discovery, but essentially all algorithms use computationally demanding [1] [3] . Recent years have seen
the Euclidean Distance (ED) [2] [6] . This is somewhat significant progress for both, especially the Matrix Profile for
surprising, because in parallel, the community seems to have the forme r [13] , but the main speed - up techniques for each are
converged on the understanding that the Dynamic Time not obviously combinable.
Warping (DTW) is superior in most domains, at least for the
tasks of clustering, classification, and similarity search In this work we introduce a novel algorithm that makes
[3] [8] [9] [10] . Could DTW also be superior to ED for motif DTW motif discovery tenable fo r large datasets for the first time.
discovery? To preview our answer to this question, consider Fig. We call our algorithm SWAMP, Scalable Warping Aware
1 , which shows the top - 1 motif discovered in a n electrical power Matrix Profile. This is something of a misnomer, since we
demand dataset, using the Euclidean distance [7] . attempt to avoid computing most of the true DTW Matrix Profile
by instead computing much cheaper upper/lower bounding
Matrix Profiles. We claim the following contributions:
• We show, for the first time, that there exists conserved
structure in real - world time series that can be found with
60 minutes DTW motifs, but not with classic Euclidean distance
motifs [6] . It was not clear that this had to be the case, as
Fig. 1. The top - 1 Euclidean distance motif dis covered in a one - month long
electrical power demand dataset. The full dataset that this motif was extracted [6] and others had argued for the di minished utility of
from , like all other datasets used in this paper , is available at [16] . DTW for motif discovery ( all - to - all search), relative to its
known utility for similarity search ( one - to - all search).
We have no obvious reasons to discount this motif. It clearly
shows the highly conserved behavior . However, now let us • We introduce SWAMP, the first exact algorithm for DTW
consider Fig. 1 , which shows a different pair of subsequences motif discovery that significantly outperforms brute force
from the same dataset. In retrospect, we would surely have search by two or more orders of magnitude.
preferred to have discovered this pair of motifs as the top - 1
The rest of the paper is organized as follows. In Section II Similarity search under DTW can be demanding in terms of
and Section III , we present the formal definitions and CPU time. One way to a ddress this problem is to use a lower
background, before outlining our approach in IV . Section V bound to help prune sequences that could not possibly be a best
contains e xperimental evaluation s . Finally, we offer conclusions match [8] . While there exist dozens of lower bounds in the
and directions for future work in Section VI . literature, in our work we use a generalization of the LB Keogh
[3] [8] .
II. D EFINITIONS A ND N OTATIONS
Definition 6 : The LB Keogh lower bound between a time series
W e begin by introducing the necessary definitions and Q and another time series T , given a warping window size 𝑤 , is
fundamental concepts, beginning with the definition of a Time defined as the distan ce from the clos
```

---

## candidate-15 [dynamics-matching] — UNCONSUMED

**Title:** 2308.09995v1

**URL:** file:///7528eb8075fb34ebbe086f6907c4287298e4bff28dd98d8408497822dd79911e/2308.09995v1.pdf

**Description:** This IEEE conference paper proposes DTW-SOM, an adapted Self-Organizing Map that uses Dynamic Time Warping distance instead of Euclidean distance, to visually explore and organize time-series motifs extracted by motif discovery algorithms. The method introduces two new initialization routines (random sample and anchor) and adapts the SOM training phase to handle variable-length time-series subsequences. Tested on synthetic and UCR archive datasets, DTW-SOM demonstrates the ability to extract meaningful relationships between motifs and display them in a space-efficient visualization.

**Content extract (≤6k chars):**

```
Exploring time - series motifs through DTW - SOM
Maria Inês Silva & Roberto Henriques
Nova Information Manageme nt School (NOVA IMS), Campus de Campolide,
Universidade Nova de Lisboa, 1070 - 312 Lisboa, Portugal
d20170088@novaims.unl.pt ; roberto@novaims.unl.pt
This is the final, accepted version of the conference paper published by
IEEE
Silva, M. I., & Henriques, R. (2020). Exploring time - series motifs through DTW - SOM. In
2020 International Joint Conference on Neural Networks, IJCNN: 2020 Conference
Proceedings (pp. 1 - 8). [9207614] (Proceedings of the International Joint Conference on
Neural Networks). Institute of Electrical and Electronics Engineers Inc..
https://doi.org/10.1109/IJCNN48605.2020.9207614
© 20 2 0 IEEE. Persona l use of this material is permitted. Permission from IEEE must be
obtained for all other uses, in any current or future media, including
reprinting/republishing this material for advertising or promotional purposes, creating
new collective works, for resa le or redistribution to servers or lists, or reuse of any
copyrighted component of this work in other works.
Abstrac t
Motif discovery is a fundamental step in data mining tasks for time - series data such as
clustering, classification and anom aly detection. Even though many papers have
addressed the problem of how to find motifs in time - series by proposing new motif
discovery algorithms, not much work has been done on the exploration of the motifs
extracted by these algorithms. In this paper, w e argue that visually exploring time - series
motifs computed by motif discovery algorithms can be useful to understand and debug
results. To explore the output of motif discovery algorithms, we propose the use of an
adapted Self - Organizing Map, the DTW - SOM, on the list of motif's centers. In short,
DTW - SOM is a vanilla Self - Organizing Map with three main differences, namely (1) the
use the Dynamic Time Warping distance instead of the Euclidean distance, (2) the
adoption of two new network initialization rout ines (a random sample initialization and
an anchor initialization) and (3) the adjustment of the Adaptation phase of the training
to work with variable - length time - series sequences. We test DTW - SOM in a synthetic
motif dataset and two real time - series data sets from the UCR Time Series Classification
Archive [1]. After an exploration of results, we conclude that DTW - SOM is capable of
extracting relevant information from a set of motifs and display it in a visualization that
is space - efficient.
Keywords: Dyn amic Time Warping ; Self - Organizing Map ; Motif discovery ; Time - series ;
exploration
I. Introduction
In the last decade, motif discovery has become a fundamental step in many data mining
tasks for time - series data, such as clustering, classification or anomaly detection. In
general, a time - series motif corresponds to a over - represented segment of a time - s eries
and thus motif discovery involves extracting all (or a specific subset) of these over -
represented segments [2]. Figure 1 illustrates an example of two motifs built from
dummy data.
Fig. 1. Toy example of two different motifs, each with two highly con served subsequences
Due to its relevance, many methods and strategies have been proposed to tackle motif
discovery. However, the step of exploring and visualizing motifs, which can be useful to
understand results of downward tasks, has not received as mu ch attention. To the best
of our knowledge, papers that address this question focus only on visualizing the actual
time - series subsequences that belong to each individual motif [3][4] – [5]. We argue that,
even though exploring individual motifs can help to understand the individual patterns,
these methods cannot provide information about the overall relationships between the
extracted motifs. In other words, they are not ideal to answer questions such as: Are
motifs similar to each other? Can we define clust ers of motifs? Additionally, exploring
individual clusters is not tractable in the cases where a high number of motifs is
extracted.
In this paper, we propose the use of a widely - studied method for feature reduction and
visualization, the Self - Organizing M ap (SOM) [6], to explore the centers of motifs
extracted by any desired motif discovery algorithm. Taking into account that these
centers are time - series subsequences, with possibly variable lengths and multiple
dimensions, we adapted the original SOM algo rithm to apply the Dynamic Time Warping
(DTW) distance [7] as its similarity metric and added two specific initialization routines
for the SOM network.
The rest of the paper is organized as follows: section 2 introduces academic work related
to (1) motif d iscovery and (2) Self - Organizing Maps, section 3 describes our own
implementation of the Dynamic Time Warping Self - Organizing Map (DTW - SOM), section
4 presents the experimental setup and reports the results obtained on three different
datasets and, finally , section 5 concludes this paper and discusses future work.
II. Related Work
I n this section, we’ll cover two areas which, although seemingly unrelated, serve as basis
for this paper - motif discovery and self - organizing maps.
A. Motif Discovery
Despite, in general, the concept of motifs being associated with significant time - series
segments, there are two main definitions of motifs that vary on the way they set the
concept of "significance" [2]. Similarity - based motifs focus on the similarity of the time -
se ries segments and thus this definition results in highly similar motifs. On the other
hand, support - based motifs focus on the repetition of the segments throughout the
time - series and thus this definition leads to highly frequent motifs.
In addition to the concept of significance, there are additional constraints a group of
time - series segments must meet to be considered a motif [8]. The first is a behavior
constraint, which determines that segments in a motif should have 
```

---

## candidate-16 [dynamics-matching] — UNCONSUMED

**Title:** JQE Volume 21 Issue 1 Pages 1 28

**URL:** file:///b5bf44a88f3b8449d0ed54b32677c73de57276f334278cfa0e6343a7e55825a6/JQE_Volume 21_Issue 1_Pages 1-28.pdf

**Description:** A peer-reviewed research paper that proposes combining wavelet denoising as a preprocessing step with the Dynamic Time Warping (DTW) algorithm to recognize and predict stock price patterns on the Tehran Stock Exchange. The study applies the method to three major steel industry stocks over 2016–2020 (1,300 data points each), using K-fold validation, and finds that wavelet denoising significantly improves DTW prediction accuracy by removing noise from price time series.

**Content extract (≤6k chars):**

```
Quarterly Journal of Quantitative Economics(JQE ) ( 2024) 21(1) 1 - 28
Quarterly Journal of
Quantitative Economics
Journal Homepage:
www.jqe.scu.ac.ir
Print ISSN: 2008 - 5850
Online ISSN: 2717 - 4271
A Method Based o n Wavelet Denoising a nd DTW
Algorithm f or Stock Price Pattern Recognition i n Tehran
Stock Exchange
Rahim Ghasemiyeh * , Hasanali Sinaei , ** Elnaz Ghalambor Dezfuli***
* Associate Professor of Management, Department of Management, Faculty of Economics and
Social Sciences, Shahid Chamran University of Ahvaz, Ahvaz, Iran. (Corresponding Author)
** Professor of Financial Management, Department of Management, Faculty of Econo mics
and Social Sciences, Shahid Chamran University of Ahvaz, Ahvaz, Iran.
*** Master of Financial Management, Department of Management, Faculty of Economics and
Social Sciences, Shahid Chamran University of Ahvaz, Ahvaz. Iran. .
ARTICLE HISTORY JEL CLASSIFICATION:
G17, C30, C61
Received: 07 November 2022 KEYWORDS:
R evision: 24 February 2023 Dynamic time warping , wavelet denoising , stock
A acceptance: 20 May 2023 prediction
CORRESPONDING Postal address:
AUTHOR'S: Golestan street, Golestan , Department of
Email: Management , Faculty of Economics and Social
r.ghasemiyeh@scu.ac.ir Sciences, Shahid Chamran University of Ahvaz,
0000 - 0002 - 1042 - 3918 Ahvaz, Khuzestan, Postal code: 61357 - 93113, Iran
FURTHER INFORMATION:
The present article is taken from the MBA dissertation of Elanz Ghalambor Dezfuli
with Supervisor of Dr. Sinaei and Rahim Ghasemiyeh. at the Shahid Chamran
University of Ahvaz, Ahvaz, Iran.
ACKNOWLEDGMENTS: Acknowledgments may be made to individuals or
institutions that have made an important contribution.
CONFLICT OF INTEREST: The authors declare no conflict of interest.
FUNDING: The authors received no financial support for the research, authorship,
and publication of this article.
A Method Based o n Wavelet Denoising a nd DTW
2 Algorithm f or Stock Price Pattern Recognition i n
Tehran Stock Exchange
ABSTRACT
The primary reason most people invest in stocks is the potential return compared to
alternatives such as bank certificates of deposit, gold, and Treasury bonds. This requires
accurate information about the stock market, price changes and predicting future tre nds.
The main purpose of this study is to present a method based on wavelet denoising and
dynamic time warping to identify the stock price pattern in the Tehran Stock Exchange.
Instead of focusing and summarizing different and numerous methods to predict s tock
prices, this research concentrates on neural networks and wavelet denoising, and dynamic
time warping to identify the stock price patterns. This methodology has been approved by
researchers as a new effective technique. In this regard, first, using t he wavelet denoising
preprocessing step, noise is removed from the stock price time series, and then the extracted
data was used as input to the dynamic time warping prediction model. MATLAB software
version 9.11 was used to analyze the research data. The statistical population of the present
study includes 3 shares among the shares of steel industry companies of Tehran Stock
Exchange. The research was conducted in the period 2016 to 2020. The results show that
the predictions obtained from the dynamic time warping method equipped with the wavelet
denoising preprocessing step in comparison with the predictions obtained from the dynamic
time warping method without the wavelet denoising preprocessing step in the sample, have
been associated with much less accu racy and error.
How to Cite:
Ghasemiyeh, Rahim . , Sinaei, Hasanali & Ghalambor Dezfuli, Elnaz. ( 2024 ). A Method Based
o n Wavelet Denoising a nd DTW Algorithm f or Stock Price Pattern Recognition i n Tehran
Stock Exchange . Quietly Journal of Q uantitative Economics (JQE) , 21 ( 1 ), 1 - 28 .
https://doi.org/10.22055/jqe.2023.42285.2521
© 2024 Shahid Chamran University of Ahvaz, Ahvaz, Iran. This article is
an open access article distributed under the terms and conditions of the Creative Commons
Attribution - NonCommercial 4.0 International (CC BY - NC 4.0 license)
( http://creativecommons.org/licenses/by - nc/4.0/ )
Rahim Ghasemiyeh, Hasanali Sinaei , Elnaz Ghalambor
Dezfuli 3
Quarterly Journal of Quantitative Economics(JQE) ( 2024 ) 21 ( 1 )
1 - INTRODUCTION
Achieving economic growth and development in the country requires
continuous monitoring and control of financial markets. In economic
literature, financial markets as the flow of financial resources from
non - productive s ectors to productive play a vital role in economic
growth, job creation, investment, stabilization of monetary and
financial variables and overall improvement of society’s welfare (Jafari
Samimi & Baloonejad, 2013) . Facilitating economic activities at the
world level greatly increases the importance of these markets
(Zolfaghari, 2018) .
The financial system of each country is responsible for
transferring savings and allocating them as investment resources. The
role of the financial subsystem is to transfe r funds from units with
surplus to those with a lack of funds (Mohammadi, Mosleh Shirazi,
Abbasi, & Akhlaghpour, 2019) . In a general classification, financial
markets are divided into two categories: money and capital markets.
The stock exchange is an or ganized and formal capital market in which
buying and selling of shares or government bonds or bonds related to
reputable private institutions is done under certain rules and regulations
(Feghehmajidi. Ali & Shahidi.Fariba, 2018) . The capital market by
p roviding features such as low transaction costs, appropriate
dissemination of market information and clarification in this area,
attracting harmful liquidity in other parallel markets, assigning returns
to investors in appropriate risk, increasing liquidit y and facilitating
securities exchanges (Osoolian & Koushki, 2020) . The stock exchange
is the most important pillar in attracting and properly organizing
financial resources in the c
```

---

## candidate-17 [dynamics-matching] — UNCONSUMED

**Title:** Measuring the Impact of Financial News and Social

**URL:** file:///07df96a337ef83cdafbcde73eaa030104f7568595fcb11f12be204a996a2df00/Measuring_the_Impact_of_Financial_News_and_Social_.pdf

**Description:** This peer-reviewed paper investigates whether financial news articles and social media sentiment can improve stock closing price prediction when combined with technical analysis. It applies time series mining techniques—Symbolic Aggregate Approximation (SAX) and Dynamic Time Warping (DTW)—to discover periodic patterns linking textual information to price movements, then uses those patterns to augment a forecasting classifier. Results show clear improvement in prediction accuracy during periods where text-price patterns are identified versus periods where they are absent.

**Content extract (≤6k chars):**

```
algorithms
Article
Measuring the Impact of Financial News and Social
Media on Stock Market Modeling Using Time Series
Mining Techniques
Foteini Kollintza-Kyriakoulia 1 , Manolis Maragoudakis 1, * and Anastasia Krithara 2
1 Department of Information and Communication Systems Engineering, University of the Aegean,
GR-83200 Samos, Greece; fkollintzakyriakoulia@gmail.com
2 Institute of Informatics and Telecommunications, National Center for Scientific Center “Demokritos”,
GR-15310 Athens, Greece; akrithara@iit.demokritos.gr
* Correspondence: mmarag@aegean.gr; Tel.: +30-22730-82261
 
Received: 23 August 2018; Accepted: 23 October 2018; Published: 6 November 2018 
Abstract: In this work, we study the task of predicting the closing price of the following day
of a stock, based on technical analysis, news articles and public opinions. The intuition of this
study lies in the fact that technical analysis contains information about the event, but not the cause
of the change, while data like news articles and public opinions may be interpreted as a cause.
The paper uses time series analysis techniques such as Symbolic Aggregate Approximation (SAX)
and Dynamic Time Warping (DTW) to study the existence of a relation between price data and textual
information, either from news or social media. Pattern matching techniques from time series data
are also incorporated, in order to experimentally validate potential correlations of price and textual
information within given time periods. The ultimate goal is to create a forecasting model that exploits
the previously discovered patterns in order to augment the forecasting accuracy. Results obtained
from the experimental phase are promising. The performance of the classifier shows clear signs of
improvement and robustness within the time periods where patterns between stock price and the
textual information have been identified, compared to the periods where patterns did not exist.
Keywords: time series analysis; symbolic aggregate approximation; dynamic time warping; stock
market analysis
1. Introduction
One of the most challenging tasks faced by researchers in modeling dynamic systems is the
creation of accurate stock market forecast models. Dynamic systems are governed by complexity.
Volatility is another characteristic of market dynamics. As a result, much controversy has been
caused as to whether such a forecasting method could exist. Therefore, two main strategies have been
encapsulated by analysts, namely the fundamental and the technical strategy [ 1 ]. The former states that
the stock market change of prices derives from a security’s relative data. In a fundamentalist trading
philosophy, the price of a security can be determined through the nuts and bolts of financial numbers.
These numbers are derived from the overall economy, the particular industry’s sector or, most typically,
from the company dynamics. Parameters such as inflation, joblessness, return on equity (ROE),
debt levels and individual price to earnings (PE) ratios have been identified as components that aid
towards determining the price of a stock.
On the other axis, that of technical analysis, research is based on the belief that market timing is
the key concept. Technicians utilize historical data in the form of charts and figures in order to identify
trends in price. These strategists assume that market timing is critical, and thus, opportunities can arise
Algorithms 2018 , 11 , 181; doi:10.3390/a11110181 www.mdpi.com/journal/algorithms
Algorithms 2018 , 11 , 181 2 of 24
through the careful investigation of historical price and volume trends, comparing them against current
prices. Technical analysts also support the claim that certain high/low psychological price barriers
exist, such as support and resistance levels where opportunities may lurk. Furthermore, an additional
assumption that is adopted is that price movements are not completely unsystematic. Nevertheless,
according to a variety of researchers, the goal is not to question the predictability of financial time
series data, but to discover a good model, able to cope with the dynamics of stock market.
Even though many researchers adopt the aforementioned categorization between fundamentalist
trading philosophy and technical analysis, we are of the opinion that good fundamental knowledge
could be combined with patterns derived from technical analysis in an attempt to overcome issues
such as asymmetric or erroneous information.
Towards the latter path, stock market analysis utilizing sophisticated Information and
Communication Technology (ICT) has gained a significant amount of attention. Over the past few
years, there has been an increasing focus on the development of modeling systems, especially when
the expected outcomes appear to yield significant profits to the investors’ portfolios. In alignment
with modern globalized economy and the expansion of social media platforms that allow for rapid
exchange of information among users, the available resources are gradually becoming more plentiful,
thus difficult to be analyzed by typical statistical tools. Consequently, financial experts emphasize the
utilization of data mining methods, mainly due to the quantity and the increased rate by which data
are being formed. Thus far, there has been a significant number of research papers that have focused
on applying data mining methods solely upon past data from stock bond prices and other technical
indicators. Nevertheless, throughout recent studies, prediction is also based on textual information,
based on the logical assumption that the course of a stock price can be influenced by news articles,
ranging from companies’ releases and local politics to news of superpower economies [2].
However, gaining unrestricted electronic access to news data was not feasible earlier than 2000.
Nowadays, news is easily accessible, insights on important information such as inside company
data are fairly inexpensive and domain expert esti
```

---

## candidate-18 [dynamics-matching] — UNCONSUMED

**Title:** dtw gis

**URL:** file:///4048bc5a062667ca8dfc4a81190475bda8aadd7de59a3fa394a95610435d44d6/dtw-gis.pdf

**Description:** A research paper presenting a simple and efficient (1+ε)-approximation algorithm for Dynamic Time Warping (DTW) between point sequences sampled from curves. The algorithm achieves O(κ²/ε · n log σ) running time for κ-packed curves, offering an order of magnitude speedup over the standard O(mn) dynamic programming algorithm on sequences of 5,000+ points while keeping approximation error within 5–10%.

**Content extract (≤6k chars):**

```
A Simple Efficient Approximation Algorithm for Dynamic
Time Warping
Rex Ying Jiangwei Pan Kyle Fox
Stanford University Duke University Duke University
rexying@stanford.edu jwpan@cs.duke.edu kylefox@cs.duke.edu
Pankaj K. Agarwal
Duke University
pankaj@cs.duke.edu
ABSTRACT 1. INTRODUCTION
Dynamic time warping (DTW) is a widely used curve sim- Curves have become ubiquitous representations of com-
ilarity measure. We present a simple and efficient (1 +  )- plex shapes. They are simpler structures than the shapes
approximation algorithm for DTW between a pair of point they represent, and can often be used directly in compu-
sequences, say, P and Q , each of which is sampled from a tations even when processing their original shapes is infea-
curve. We prove that the running time of the algorithm is sible. Matching similar curves is particularly useful. The
O ( κ 2 notion of curve matching allows one to compare, cluster,
 n log σ ) for a pair of κ -packed curves with a total of n
points, assuming that the spreads of P and Q are bounded and summarize curves, and it is used in a variety of ap-
by σ . The spread of a point set is the ratio of the maximum plications, including learning and recognizing signals from
to the minimum pairwise distance, and a curve is called κ - speech, handwriting, fingerprints, and image features.
packed if the length of its intersection with any disk of radius One application of curve matching of particular interest is
r is at most κr . Although an algorithm with similar asymp- in the area of trajectory analysis. Trajectories are functions
totic time complexity was presented in [1], our algorithm is from a time interval to R d , for d ≥ 1, and they describe
considerably simpler and more efficient in practice. how physical systems change over time. They are sensed or
We have implemented our algorithm. Our experiments on inferred, often as ordered sequences of points, from a vari-
both synthetic and real-world data sets show that it is an ety of sources including GPS sensors in smart phones and
order of magnitude faster than the standard exact DP algo- vehicles, surveillance videos, and the observed movement of
rithm on point sequences of length 5 , 000 or more while keep- hurricanes. Fundamental tasks for analyzing trajectory data
ing the approximation error within 5–10%. We demonstrate include measuring the similarity between a pair of trajecto-
the efficacy of our algorithm by using it in two applications ries and computing similar portions between them. These
— computing the k most similar trajectories to a query tra- steps are important for many applications such as subtra-
jectory, and running the iterative closest point method for jectory clustering of GPS trajectories, detecting anomalous
a pair of trajectories. We show that we can achieve 8-12 trajectories, similarity queries on trajectories, object seg-
times speedup using our algorithm as a subroutine in these mentation from video trajectories [4], and smart phone au-
applications, without compromising much in accuracy. thentication using touch screen trajectories [6]. This paper
presents a simple and efficient algorithm for computing sim-
ilarity between two curves using dynamic time warping that
CCS Concepts is easy to implement and works well in practice.
• Theory of computation → Approximation algorithms
analysis; Computational geometry; • Information sys- Problem statement. Let P = 〈 p 1 , . . . , p m 〉 and Q =
〈 q 1 , . . . , q n 〉 be two sequences of points in R d 
tems → Spatial-temporal systems; Information retrieval query for some fixed
processing; d ≥ 1. We define a correspondence as a pair ( p i , q j ). A set
C of correspondences is monotone if for any pair ( p i , q j ) ,
( p i ′ , q j ′ ) ∈ C with i ′ > i , we have j ′ ≥ j . In other words,
Keywords the pairs of correspondences do not cross; see Figure 1. We ∑
Curve matching, dynamic time warping; approximation al- define the cost of C to be ( p,q ) ∈ C || pq || , where || · || is the
gorithm; trajectory analysis Euclidean norm. The similar portions of P and Q are rep-
resented by a set C of monotone correspondences, with the
cost of C quantifying the quality of similarity. The goal is
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed to compute a monotone set of correspondences with certain
for profit or commercial advantage and that copies bear this notice and the full cita- properties. While numerous criteria for computing corre-
tion on the first page. Copyrights for components of this work owned by others than spondences have been proposed, we focus on computing the
ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or re-
publish, to post on servers or to redistribute to lists, requires prior specific permission dynamic time warping (DTW) between P and Q , a widely
and/or a fee. Request permissions from permissions@acm.org. used criterion [6, 9, 18, 21]. DTW computes a monotone set
SIGSPATIAL’16, October 31-November 03, 2016, Burlingame, CA, USA C of correspondences for which every point of P and Q ap-
© c 2016 ACM. ISBN 978-1-4503-4589-7/16/10. . . $15.00 pear at least once, and it minimizes the cost of C subject to
DOI: http://dx.doi.org/10.1145/2996913.2996954 this constraint, denoted by dtw ( P, Q ).
( i + 1 , j + 1). The algorithm computes a minimum-weight
path from (1 , 1) to ( m, n ) in this grid graph using dynamic
programming (DP).
Because of the popularity of DTW, several heuristics have
been proposed to expedite the DTW computation. For ex-
Figure 1. Example of DTW correspondences between two ample, the commonly used library of Giorgino [12] uses con-
sequences of points sampled from two underlying curves. straints such as the Sakoe-Chiba Band [22] that only con-
structs a small “band” around the diagonal of the DP grid
and restricts the search within this band. This approach
It 
```

---

## candidate-19 [dynamics-matching] — UNCONSUMED

**Title:** s10618 018 0557 y

**URL:** file:///45a793a931a531290a34600acddaf4faf01e23c78c8d4ba8b7b9eaa04b9d7dfe/s10618-018-0557-y.pdf

**Description:** A peer-reviewed paper in Data Mining and Knowledge Discovery that proposes embedding Pruned Warping Paths into the UCR suite to speed up exact similarity search under Dynamic Time Warping (DTW). The method targets the internal DTW computation bottleneck—the residual pairs that survive lower-bound pruning—and achieves up to 5x speedup over the state-of-the-art for long queries and wide warping windows.

**Content extract (≤6k chars):**

```
Data Min Knowl Disc (2018) 32:988–1016
https://doi.org/10.1007/s10618-018-0557-y
Speeding up similarity search under dynamic time
warping by pruning unpromising alignments
Diego F. Silva 1 , 2 · Rafael Giusti 1 ·
Eamonn Keogh 3 · Gustavo E. A. P. A. Batista 1
Received: 31 March 2017 / Accepted: 16 February 2018 / Published online: 12 March 2018
© The Author(s) 2018
Abstract Similarity search is the core procedure for several time series mining tasks.
While different distance measures can be used for this purpose, there is clear evidence
that the Dynamic Time Warping (DTW) is the most suitable distance function for a
wide range of application domains. Despite its quadratic complexity, research efforts
have proposed a significant number of pruning methods to speed up the similarity
search under DTW. However, the search may still take a considerable amount of time
depending on the parameters of the search, such as the length of the query and the
warping window width. The main reason is that the current techniques for speeding
up the similarity search focus on avoiding the costly distance calculation between as
many pairs of time series as possible. Nevertheless, the few pairs of subsequences that
were not discarded by the pruning techniques can represent a significant part of the
entire search time. In this work, we adapt a recently proposed algorithm to improve the
internal efficiency of the DTW calculation. Our method can speed up the UCR suite,
considered the current fastest tool for similarity search under DTW. More important,
the longer the time needed for the search, the higher the speedup ratio achieved by our
Responsible editor: Jian Pei.
This work was funded by Grants #2012/08923-8, #2013/26151-5, and #2016/04986-6 São Paulo Research
Foundation (FAPESP) and 306631/2016-4 National Council for Scientific and Technological
Development (CNPq).
B Diego F. Silva
diegofsilva@usp.br; diegofs@ufscar.br
1 Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo, São Carlos,
Brazil
2 Departamento de Computação, Universidade Federal de São Carlos, São Carlos, Brazil
3 Department of Computer Science and Engineering, University of California, Riverside, USA
123
Speeding up similarity search under dynamic time warping . . . 989
method. We demonstrate that our method performs similarly to UCR suite for small
queries and narrow warping constraints. However, it performs up to five times faster
for long queries and large warping windows.
Keywords Time series · Similarity search · Dynamic time warping
1 Introduction
Following the remarkable availability of temporal data, time series mining is becom-
ing a necessary procedure in a wide range of application domains. The estimate of a
distance or similarity value between time series objects or subsequences is a common
subroutine for several temporal data mining tasks. Consequently, the choice of the
distance measure adopted to compare the time series may harshly affect the perfor-
mance of most distance-based algorithms. The scientific community has shown that
the Dynamic Time Warping (DTW) is arguably the most suitable distance measure
for a wide range of applications and mining tasks, such as classification (Wang et al.
2013; Kate 2016), clustering (Begum et al. 2015), and pattern matching (Chavoshi
et al. 2016).
The similarity search consists of finding the most similar subsequence of a given
query in a long reference data. For some applications, it may be extended to the k -
nearest neighbor search, i.e., when the user is interested in finding a group of k similar
subsequences.
A straightforward implementation of DTW is quadratic regarding time and space
complexities. With the speed and the amount of data collected in several applications,
this makes the search under DTW impractical. However, Rakthanmanon et al. (2012)
have introduced the UCR suite, a set of optimizations that make the subsequence
similarity search under DTW even faster than Euclidean distance with the techniques
considered state-of-the-art up to that moment. Specifically, that work mainly consists
of lower-bounding and early-abandon methods to discard nearest neighbors candidates
before the computation of DTW. In most cases, the UCR suite can avoid the need for
a DTW distance calculation.
Regarding the problem of finding the best match of a small subsequence in a long
time series, Rakthanmanon et al. (2012) claim that “ for the problem of exact similarity
search with arbitrary length queries, our UCR suite is close to optimal ”. In fact,
the authors use a large set of experiments to support this claim. However, while the
UCR suite approaches the optimality in avoiding the DTW calculation, such costly
operation is still required for a relatively small percentage of the time series. Even
being performed only to a small fraction of the subsequences, the DTW computation
still represents a significant amount of the similarity search runtime.
A simple experiment can illustrate this fact. When searching a query in an electro-
cardiography (ECG) dataset with approximately 30 million data points, the DTW is
calculated for only 4% of the total number of assessed subsequences. It demonstrates
the extraordinary ability of the pruning techniques in avoiding DTW calculations.
Even with this notable reduction of computations, the time for estimating the distance
between the query and the assessed subsequences corresponds to approximately 60%
123
990 D. F. Silva et al.
of the entire search runtime. This cost is even higher in some cases, depending on the
parameters of the similarity search, such as the query length.
In this work, we propose to embed a recently introduced method into the UCR suite
procedure, in order to make it even faster. Specifically, we adapt the DTW with Pruned
Warping Paths (Silva and Batista 2016) to improve the internal efficiency of the DTW
calculation. In this way, we can speed up the bottleneck of the similarity search under
the warping distance, i.e.,
```

---

## candidate-20 [dynamics-matching] — UNCONSUMED

**Title:** sustainability 13 01011

**URL:** file:///97c1c804b465a1a29cf9407d80f65e51dd8524a3924444adb84f2c384a168891/sustainability-13-01011.pdf

**Description:** A peer-reviewed research paper that proposes optimal models for predicting intraday stock trading volume using dynamic time warping (DTW) and genetic algorithms (GA) to improve volume weighted average price (VWAP) execution. Using KOSPI 200 futures data from 2006–2020, the study compares four volume prediction methods and finds that a simple average over a GA-optimized lookback period achieves the best forecasting performance, enabling large institutions to reduce market impact.

**Content extract (≤6k chars):**

```
sustainability
Article
Using a Genetic Algorithm to Build a Volume Weighted
Average Price Model in a Stock Market
Seung Hwan Jeong 1 , Hee Soo Lee 2 , Hyun Nam 3 and Kyong Joo Oh 1, *
1 Department of Industrial Engineering, Yonsei University, Seoul 03722, Korea; jsh0331@yonsei.ac.kr
2 Department of Business Administration, Sejong University, Seoul 05006, Korea; heesoo@sejong.ac.kr
3 Department of Investment Information Engineering, Yonsei University, Seoul 03722, Korea;
mcgyver3@gmail.com
* Correspondence: johanoh@yonsei.ac.kr; Tel.: +82-2-2123-5720
Abstract: Research on stock market prediction has been actively conducted over time. Pertaining
to investment, stock prices and trading volume are important indicators. While extensive research
on stocks has focused on predicting stock prices, not much focus has been applied to predicting
trading volume. The extensive trading volume by large institutions, such as pension funds, has a
great impact on the market liquidity. To reduce the impact on the stock market, it is essential for large
institutions to correctly predict the intraday trading volume using the volume weighted average
price (VWAP) method. In this study, we predict the intraday trading volume using various methods
to properly conduct VWAP trading. With the trading volume data of the Korean stock price index 200
(KOSPI 200) futures index from December 2006 to September 2020, we predicted the trading volume
using dynamic time warping (DTW) and a genetic algorithm (GA). The empirical results show that
the model using the simple average of the trading volume during the optimal period constructed by
GA achieved the best performance. As a result of this study, we expect that large institutions will
  perform more appropriate VWAP trading in a sustainable manner, leading the stock market to be
 revitalized by enhanced liquidity. In this sense, the model proposed in this paper would contribute
Citation: Jeong, S.H.; Lee, H.S.; Nam, to creating efficient stock markets and help to achieve sustainable economic growth.
H.; Oh, K.J. Using a Genetic
Algorithm to Build a Volume Keywords: dynamic time warping; genetic algorithm; sliding window; volume forecasting; volume
Weighted Average Price Model in a weighted average price
Stock Market. Sustainability 2021 , 13 ,
1011. https://doi.org/
10.3390/su13031011
1. Introduction
Received: 29 December 2020
Accepted: 14 January 2021 Over time, studies to predict prices in the stock market have actively been conducted.
Published: 20 January 2021 Various studies have been carried out to predict stock prices using the auto-regressive inte-
grated moving average (ARIMA) model, which is a time series data prediction method [ 1 , 2 ],
Publisher’s Note: MDPI stays neutral as well as other methods. Pai and Lin [ 3 ] applied a hybrid methodology combining the
with regard to jurisdictional claims in ARIMA model and support vector machine (SVM) for stock price prediction. Wang and
published maps and institutional affil- Leu [ 4 ] proposed a model that predicts the price trend of Taiwan’s stock market by combin-
iations. ing the ARIMA model and a neural network. Adebiyi et al. [ 5 ] compared the performance
of the ARIMA model and the artificial neural network (ANN) model using the stock data
of the New York Stock Exchange (NYSE). Oh and Kim [ 6 ] proposed a piecewise nonlinear
model using ANN to predict the stock market, which uses backpropagation neural net-
Copyright: © 2021 by the authors. works to find points of continuous change in time series data. Similarly, there has been
Licensee MDPI, Basel, Switzerland. much research on applying neural network methodology to stock price prediction. Yoon
This article is an open access article and Swales [ 7 ] proved that neural networks are effective for solving complex problems
distributed under the terms and such as stock price prediction, and Kohara et al. [ 8 ] showed that the neural network and
conditions of the Creative Commons prior knowledge of prediction were effective in predicting stock prices. Tsai and Wang [ 9 ]
Attribution (CC BY) license (https:// showed that when a stock price prediction model was created by combining ANN and de-
creativecommons.org/licenses/by/ cision tree, it showed higher accuracy than a single model. Hadavandi et al. [ 10 ] proposed
4.0/). a stock price prediction expert system by combining ANN and a genetic fuzzy system.
Sustainability 2021 , 13 , 1011. https://doi.org/10.3390/su13031011 https://www.mdpi.com/journal/sustainability
Sustainability 2021 , 13 , 1011 2 of 16
Chen et al. [ 11 ] proved that a fuzzy time series model based on the Fibonacci sequence is
effective in predicting the Taiwan semiconductor manufacturing company (TSMC) stock
price data and Taiwan capitalization weighted stock index (TAIEX) data. Cheng et al. [ 12 ]
proposed a hybrid model for stock price prediction based on genetic algorithms and rough
sets theory.
In addition to predicting stock prices of various markets, investors are also interested
in stock trading volume. Trading volume is an important indicator for investors to buy or
sell certain stocks. A number of studies confirmed that the trading volume has a positive
correlation with the volatility of the price [ 13 , 14 ], and various studies predicted the price
volatility based on this positive correlation by utilizing the trading volume [ 15 , 16 ]. Tsang
and Chong [ 17 ] presented a strategy to obtain investment returns using volume-based
on-balance volume (OBM) indicators, and Nedunchezian [ 18 ] conducted a study to predict
the price movement of multi commodity exchange (MCX) energy using OBV indicators.
However, research that predicts the actual intraday trading volume, rather than just using
the trading volume as an indicator for prediction, has not been actively conducted [ 19 ].
Without sophisticated research on the intraday trading volume, large institutions are still
taking the strategy to consume liquidity using the simple a
```

---

## candidate-21 [dynamics-matching] — ANNOTATED as 2002.00208

Promotion note: the paper was already fully annotated as a prose block in
`by-domain/information_theory.md` (pre-A3 residue); this pass promoted that
annotation verbatim to `annotations/2002.00208.md` + dual index (composite_systems,
optimal_transport). No new annotation written.

**Title:** Variable lag Granger Causality and Transfer Entropy for Time Series Analysis

**URL:** file:///e22d95abd959a722afa11ee293a03d8114887c6d7f6cbb2dcf404c2cf99e7fc3/Variable-lag_Granger_Causality_and_Transfer_Entropy_for_Time_Series_Analysis.pdf

**Description:** This paper introduces Variable-lag Granger Causality and Variable-lag Transfer Entropy, generalizations that relax the fixed time delay assumption in traditional causal inference for time series. The authors integrate Dynamic Time Warping (DTW) with Granger causality and transfer entropy to infer causal relations where causes influence effects with arbitrary, dynamically changing delays. They prove traditional fixed-lag definitions are special cases and demonstrate superior performance on simulated and real-world datasets including collective movement and financial markets.

**Content extract (≤6k chars):**

```
1
Variable-lag Granger Causality and Transfer Entropy for Time
Series Analysis
CHAINARONG AMORNBUNCHORNVEJ, National Electronics and Computer Technology Center
ELENA ZHELEVA, University of Illinois at Chicago
TANYA BERGER-WOLF, University of Illinois at Chicago and The Ohio State University
Granger causality is a fundamental technique for causal inference in time series data, commonly used in the
social and biological sciences. Typical operationalizations of Granger causality make a strong assumption
that every time point of the effect time series is influenced by a combination of other time series with a fixed
time delay. The assumption of fixed time delay also exists in Transfer Entropy, which is considered to be a
non-linear version of Granger causality. However, the assumption of the fixed time delay does not hold in
many applications, such as collective behavior, financial markets, and many natural phenomena. To address
this issue, we develop Variable-lag Granger causality and Variable-lag Transfer Entropy, generalizations of
both Granger causality and Transfer Entropy that relax the assumption of the fixed time delay and allow causes
to influence effects with arbitrary time delays. In addition, we propose methods for inferring both variable-lag
Granger causality and Transfer Entropy relations. In our approaches, we utilize an optimal warping path of
Dynamic Time Warping (DTW) to infer variable-lag causal relations. We demonstrate our approaches on
an application for studying coordinated collective behavior and other real-world casual-inference datasets
and show that our proposed approaches perform beer than several existing methods in both simulated and
real-world datasets. Our approaches can be applied in any domain of time series analysis. The software of this
work is available in the R-CRAN package: VLTimeCausality.
CCS Concepts: • Information systems → Spatial-temporal systems; Data mining; • Computing method-
ologies → Cooperation and coordination;
Additional Key Words and Phrases: Granger Causality, Transfer Entropy, Time Series, Causal Inference,
Statistical Methodology
ACM Reference format:
Chainarong Amornbunchornvej, Elena Zheleva, and Tanya Berger-Wolf. 2020. Variable-lag Granger Causality
and Transfer Entropy for Time Series Analysis. ACM Trans. Knowl. Discov. Data. 1, 1, Article 1 (January 2020),
30 pages.
DOI: 10.1145/1122445.1122456
arXiv:2002.00208v3 [cs.LG] 1 Jun 2020
1 INTRODUCTION
Inferring causal relationships from data is a fundamental problem in statistics, economics, and
science in general. The gold standard for assessing causal effects is running randomized controlled
trials which randomly assign a treatment (e.g., a drug or a specific user interface) to a subset
of a population of interest, and randomly select another subset as a control group which is not
given the treatment, thus aributing the outcome difference between the two groups to the
treatment. However, in many cases, running such trials may be unethical, expensive, or simply
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored.
Abstracting with credit is permied. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2020 ACM. 1556-4681/2020/1-ART1 $ 15.00
DOI: 10.1145/1122445.1122456
ACM Transactions on Knowledge Discovery from Data, Vol. 1, No. 1, Article 1. Publication date: January 2020.
1:2 C. Amornbunchornvej et al.
impossible [ 50 ]. To address this issue, several methods have been developed to estimate causal
effects from observational data [29, 46].
In the context of time series data, a well-known method that defines a causal relation in terms
of predictability is Granger causality [ 19 ]. X Granger-causes Y if past information on X predicts
the behavior of Y beer than Y ’s past information alone [ 6 ]. In this work, when we refer to
causality, we mean specifically the predictive causality defined by Granger causality. The key
assumptions of Granger causality are that 1) the process of effect generation can be explained by a
set of structural equations, and 2) the current realization of the effect at any time point is influenced
by a set of causes in the past. Similar to other causal inference methods, Granger causality assumes
unconfoundedness and that all relevant variables are included in the analysis [19, 32].
There are several studies that have been developed based on Granger causality [7, 26, 31].
Granger causality is typically studied in the context of linear structural equations. Transfer
Entropy has been developed as a non-linear extension of Granger causality [9, 25, 37].
The typical operational definitions [ 7 ] and inference methods for inferring Granger causality,
including the common software implementation packages [ 1 , 2 ], assume that the effect is influenced
by the cause with a fixed and constant time delay.
However, the assumption of an effect is fixed-lag influenced by the cause still exists in both
Granger causality and transfer entropy.
This assumption of a fixed and constant time delay between the cause and effect is, in fact,
too strong for many applications of understanding natural world and social phenomena. In such
domains, data is often in the form of a set of time series and a common question of interest is which
time series are the (causal) initiators of paerns of behaviors captured by another set of time series.
For example, who are the individuals who influence a group’s direction in collective movement?
What are the sectors that influence the stock market dynamics right now? Which part of the brain
is critical in activating a 
```

