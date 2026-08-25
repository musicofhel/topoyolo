# Queue batch-002 — link-forge export, 2026-08-25

Orchestrator export from link-forge Neo4j (2,226 research papers scanned).
Targets pass-8's zero-result search gaps (rate-distortion, channel capacity,
geometric DL, LDPC coding, stochastic thermodynamics) plus SEPARATRIX-adjacent
topics (basin boundaries, decision boundaries) and Hodge/spin-glass crossrefs.
Consume per papers/INGESTION.md (≤3 papers/pass; triage-reject with one sentence is fine).

---

## candidate-01 [geometric-dl] — REJECTED
Soft-equivariance weight projection with error bounds; a vision-engineering method instantiating zero of the six machines.

**Title:** Tunable Soft Equivariance with Guarantees

**URL:** file:///38944c7a0e82697d41851bd9ac16d7a177d4634d5a64c81cd929e1e017666ee7/Tunable_Soft_Equivariance_with_Guarantees.pdf

**Description:** Research paper proposing a framework for constructing soft equivariant models by projecting pre-trained model weights into a designed subspace derived from Lie algebra representations. The method provides theoretical bounds on induced equivariance error and allows tunable trade-off between equivariance and expressiveness. Empirically improves performance and reduces equivariance error on ImageNet, PASCAL VOC, and trajectory prediction tasks across ViT, ResNet, DINOv2, and Segformer backbones.

**Content extract (≤6k chars):**

```
Tunable Soft Equivariance with Guarantees
Md Ashiqur Rahman 1 Lim Jun Hao 2 Jeremiah Jiang 2 Teck-Yian Lim 2 Raymond A. Yeh 1
1 Purdue University 2 DSO National Laboratories
Equivariant Soft equivariant Non-equivariant
Weights
Features
Eq. Error
Low error High error
Figure 1. Visualization of the ViT [ 12 ] weights with our soft equivariance layer (w.r.t. 90 ◦ rotation) under different softness levels, along
with the corresponding extracted features and the equivariance errors. Our tunable design allows the layers’ weights to transition smoothly
from perfectly equivariant to fully non-equivariant behavior in a controlled manner.
Abstract applications [ 8 , 29 , 45 , 46 , 49 , 55 , 63 , 69 ], such architectures
remain uncommon in mainstream vision systems. In practice,
Equivariance is a fundamental property in computer vision real-world data only approximately satisfies equivariance,
models, yet strict equivariance is rarely satisfied in real- and strictly enforcing it can reduce a model’s expressiveness.
world data, which can limit a model’s performance. Control- This led to the development of soft equivariant mod-
ling the degree of equivariance is therefore desirable. We pro- els, i.e ., models that are only approximately equivariant.
pose a general framework for constructing soft equivariant Common approaches include augmentation [ 3 , 57 , 59 ] and
models by projecting the model weights into a designed sub- regularization-based methods [ 14 , 28 , 56 ]. However, these
space. The method applies to any pre-trained architecture techniques do not offer guarantees on a model’s equivariance
and provides theoretical bounds on the induced equivariance properties after training. Another direction [ 16 , 53 , 61 , 62 ]
error. Empirically, we demonstrate the effectiveness of our achieves soft equivariance by adding non-equivariant com-
method across multiple pre-trained backbones, including ViT ponents into equivariant models, providing a way to trade
and ResNet, for image classification, semantic segmentation, off between expressiveness and equivariance. Nonetheless,
and human-trajectory prediction. Notably, our approach these methods still lack guarantees on the resulting equivari-
arXiv:2603.26657v1 [cs.CV] 27 Mar 2026 improves the performance while simultaneously reducing ance and rely on specialized architectural designs that cannot
equivariance error on the competitive ImageNet benchmark. be easily adapted from off-the-shelf models.
To address these challenges, we propose to construct soft-
equivariant models through a generalized notion of “blurring”
1. Introduction filters, which can be applied to any pre-trained model. This
is inspired by the special case of shift-invariance in con-
A model is equivariant to a transformation if applying that volutional neural networks (CNNs) by Zhang [76] , where
transformation to the input results in a predictable transfor- anti-aliasing (blurring) filters are used to make CNNs more
mation at the output. Consider image segmentation: when an invariant. Our approach extends this idea beyond shift equiv-
object in an image is shifted, the predicted mask is expected ariance to other groups and further provides a bound on the
to shift by the same amount; this is known as shift equivari- equivariance error. This allows us to systematically tune
ance. Although designing models with built-in equivariance the trade-off between equivariance and expressiveness in a
has been well studied and shown to be effective in various principled manner; see illustration in Fig. 1.
In our experiments, we first demonstrate the tunability models. In contrast, our framework is architecture-agnostic.
of the proposed soft equivariant models on small-scale im- While our approach shares conceptual similarities with Finzi
age classification. We then incorporate the proposed layer et al. [17] , it generalizes the idea beyond exact equivariance,
into various pre-trained backbones, including ViT [ 12 ], DI- integrates seamlessly with modern pre-trained vision models,
NOv2 [ 43 ], ResNet [ 21 ], and Segformer [ 71 ] for image and provides explicit control over the level of equivariance.
classification (CIFAR10/100 [ 31 ], and ImageNet [ 11 ]) and Signal processing (SP). Traditional signal processing es-
segmentation task (PASCAL VOC [ 15 ]). We demonstrate tablishes a tight connection between low-pass filters, ban-
that utilizing our soft equivariance layer further improves dlimited subspaces, and shift-invariance: a bandlimited sub-
the model’s performance and reduces equivariance errors. space remains bandlimited under shifts [ 65 ]. Equivalently, a
Finally, we go beyond image tasks and evaluate our layers low-pass (anti-aliasing) filter can be interpreted as a projec-
on trajectory prediction [ 19 ] and a synthetic O (5) -invariant tion operator onto a shift-invariant bandlimited space. This
regression problem [17]. Our main contributions: projection viewpoint has been generalized to graph signal
• We introduce a novel framework for constructing soft processing via the graph Laplacian [ 6 , 7 ], extended to ar-
equivariant layers by restricting the parameters via projec- bitrary discrete groups [ 47 ], and recently adapted to image
tions, applicable to any pre-trained model. generative models [78].
• We derive bounds on the equivariance error, which guides
the design of the tunable soft equivariant layers, allowing 3. Preliminaries
a controllable expressiveness-equivariance trade-off.
For readers needing a refresher on the concept of groups, we
• Extensive experiments on three applications (classifica-
provide a review in Appendix Sec. B. Here, we will only
tion, segmentation, and trajectory prediction) and four
discuss the most essential background information.
backbones demonstrate the practicality and effectiveness
A group G is a set with a binary operation that is closed,
of the proposed approach.
associative, has an identity element e , and every element has
2. Related Work an i
```

## candidate-02 [geometric-dl] — REJECTED
Geometric Hawkes processes via graph-conv RNNs; Hawkes excitation is already covered and this is an application wrapper, not new machine structure.

**Title:** Geometric Hawkes Processes with Graph Convolutional Recurrent Neural Networks

**URL:** file:///2e99753f971f3fab70b43cc031398415395ccdc6178f165fef8c74ef73a9cb6f/Geometric_Hawkes_Processes_with_Graph_Convolutional_Recurrent_Neural_Networks.pdf

**Description:** This AAAI-19 paper proposes the Geometric Hawkes Process (GHP) model, which integrates geometric deep learning with Hawkes processes to efficiently model large collections of correlated temporal event sequences. The approach encodes inter-process correlations as graphs and uses spectral graph convolutional recurrent neural networks to learn embeddings that parameterize individual Hawkes processes, achieving constant parameter complexity independent of graph size. Experiments on real-world datasets demonstrate prediction improvements over state-of-the-art methods.

**Content extract (≤6k chars):**

```
The Thirty-Third AAAI Conference on Artificial Intelligence (AAAI-19)
Geometric Hawkes Processes with Graph
Convolutional Recurrent Neural Networks
Jin Shang, Mingxuan Sun
Division of Computer Science and Engineering
Louisiana State University
jshang2@lsu.edu, msun@csc.lsu.edu
Abstract occurrence of new events in another. For example, in so-
cial event analysis, the events of an individual user can be
Hawkes processes are popular for modeling correlated tem- modeled as an one-dimensional Hawkes process and events
poral sequences that exhibit mutual-excitation properties. Ex- in a network can be modeled as a Multivariate Hawkes pro-
isting approaches such as feature-enriched processes or varia- cess (Farajtabar et al. 2014; Mei and Eisner 2017; Yang et al.
tions of Multivariate Hawkes processes either fail to describe
the exact mutual influence between sequences or become 2018), which captures the correlations of both endogenous
computational inhibitive in most real-world applications in- and exogenous event intensities. Extensive studies (Lemon-
volving large dimensions. Incorporating additional geometric nier, Scaman, and Kalogeratos 2017; Etesami et al. 2016;
structure in the form of graphs into Hawkes processes is an Eichler, Dahlhaus, and Dueck 2017; Xu, Farajtabar, and
effective and efficient way for improving model prediction Zha 2016) have focused on estimating the excitation ma-
accuracy. In this paper, we propose the Geometric Hawkes trix of multivariate processes for different inference tasks.
Process (GHP) model to better correlate individual processes, However, those approaches are either unable to accurately
by integrating Hawkes processes and a graph convolutional capture the mutual influence between processes or become
recurrent neural network. The deep network structure is com- computational inhibitive in most real-world events involv-
putational efficient since it requires constant parameters that ing large dimensions (Eichler, Dahlhaus, and Dueck 2017;
are independent of the graph size. The experiment results on
real-world data show that our framework outperforms recent Hall and Willett 2016).
state-of-art methods. Incorporating geometric structure in the form of graphs
into Hawkes processes is an effective and efficient way for
improving model prediction accuracy. In many real world
Introduction applications, correlations between different Hawkes pro-
Hawkes processes, which are capable of modeling tempo- cesses can be encoded by a graph. For example, in mod-
ral events that exhibit self-exciting properties, have been eling the sequences of user-item interactions, the similarity
widely applied in various applications such as supporting of users and items can be represented by a user graph and
decision making in smart health (Xu et al. 2017), inferring an item graph, respectively. Such additional graph informa-
granger causality (Xu, Farajtabar, and Zha 2016), and pre- tion can be used to impose smoothness priors on the pa-
dicting recurrent user behaviors (Zhou, Zha, and Song 2013; rameters such as the base intensities of each individual pro-
Du et al. 2016; Shang and Sun 2018). Generally, Hawkes cess. Recently, geometric deep learning (Bruna et al. 2014;
processes are useful for modeling a collection of correlated Defferrard, Bresson, and Vandergheynst 2016; Kipf and
event sequences such as earthquakes at N locations or the Welling 2017; Monti, Bronstein, and Bresson 2017) are
diffusion of M infectious diseases among a group of N peo- promising techniques that can learn meaningful representa-
ple. For example, in analyzing on-line user behaviors such as tions for geometric structure data such as graphs and have
visiting websites, recent approaches such as (Du et al. 2015) been successfully applied in various applications such as
treat the recurrent events of each user-item pair as an one- matrix completion.
dimensional Hawkes process, and assume the parameters of In this paper, we propose a novel Geometric Hawkes Pro-
all processes have a low-rank structure. However, methods cess (GHP) model by integrating geometric deep learning
that typically treat each process independently would fail to into Hawkes processes, which aims to efficiently capture
achieve good performance when there are insufficient obser- meaningful patterns in a large collection of correlated se-
vations for each process. quences of recurrent events. Specifically, each sequence is
Multivariate Hawkes processes (Liniger 2009) are suit- modeled as a Hawkes process and the proximities between
able for modeling multiple correlated sequences, where the different processes are encoded in a graph. A novel convo-
occurrence of an event in one sequence may influence the lutional and recurrent neural network is adopted to extract
local meaningful patterns from the graph. The learned mean-
Copyright c © 2019, Association for the Advancement of Artificial ingful embeddings are then used to generate parameters such
Intelligence (www.aaai.org). All rights reserved. as the base intensities that characterize Hawkes processes.
4878
Comparing to traditional methods, our GHP correlates each modeling two dimensional data in the from of a M by N
individual Hawkes process effectively through graph em- matrix without considering temporal dynamics.
bedding and it is computational efficient since the deep net-
work structure requires constant parameters that are inde- Model
pendent of the graph size. To the best of our knowledge, our In this section, we introduce our Geometric Hawkes Process
GHP model is the first one to learn Hawkes processes with model.
geometric deep learning. We also present the detail design
of the single-graph and multi-graph cases for our Geomet- Background on Hawkes Processes
ric Hawkes Process (GHP) model. Extensive experiments on
A univariate Hawkes process is a self-exiting temporal point
real-world datasets demonstrate the predicting performance
process and the realization of the process consists
```

## candidate-03 [geometric-dl] — REJECTED
Allegro local-equivariant interatomic potentials; equivariant-network engineering with no matching/stability/etc. atlas object.

**Title:** www.nature.com

**URL:** https://www.nature.com/articles/s41467-023-36329-y.pdf

**Description:** Nature Communications paper introducing Allegro, a strictly local equivariant neural network architecture for learning interatomic potentials that scales to large atomistic dynamics simulations.

**Content extract (≤6k chars):**

```
%PDF-1.4
%����
1 0 obj
<>
endobj
2 0 obj
<>stream


   
      
         application/pdf
         doi:10.1038/s41467-023-36329-y
         
            
               Learning local equivariant representations for large-scale atomistic dynamics
            
         
         
            
               Albert Musaelian
               Simon Batzner
               Anders Johansson
               Lixin Sun
               Cameron J. Owen
               Mordechai Kornbluth
               Boris Kozinsky
            
         
         
            
               Springer US
            
         
         
            
         
         
            
               Nature Communications, doi:10.1038/s41467-023-36329-y
            
         
      
      
         Springer
         2023-02-03T05:46:08+01:00
         2023-02-03T07:47:16+05:30
         2023-02-03T05:46:08+01:00
      
      
         True
      
      
         
      iText® 5.3.5 ©2000-2012 1T3XT BVBA (SPRINGER SBM; licensed version)
      
         uuid:f66f3a33-52bb-4a0c-9f17-cb322fc11f4a
         uuid:c1ee5402-9185-4282-92fc-ed73b17d738b
         default
         1
         
            
               
                  converted
                  uuid:200f8618-3460-43d2-9152-68356fde8c0e
                  converted to PDF/A-2b
                  pdfToolbox
                  2023-02-03T07:48:10+05:30
               
            
         
      
      
         2
         B
      
      
         
            
               
                  http://ns.adobe.com/pdf/1.3/
                  pdf
                  Adobe PDF Schema
                  
                     
                        
                           internal
                           A name object indicating whether the document has been modified to include trapping information
                           Trapped
                           Text
                        
                     
                  
               
               
                  http://ns.adobe.com/pdfx/1.3/
                  pdfx
                  Adobe Document Info PDF eXtension Schema
                  
                     
                        
                           internal
                           ID of PDF/X standard
                           GTS_PDFXVersion
                           Text
                        
                        
                           internal
                           Conformance level of PDF/X standard
                           GTS_PDFXConformance
                           Text
                        
                        
                           internal
                           Company creating the PDF
                           Company
                           Text
                        
                        
                           internal
                           Date when document was last modified
                           SourceModified
                           Text
                        
                     
                  
               
               
                  http://ns.adobe.com/xap/1.0/mm/
                  xmpMM
                  XMP Media Management Schema
                  
                     
                        
                           internal
                           UUID based identifier for specific incarnation of a document
                           InstanceID
                           URI
                        
                        
                           internal
                           The common identifier for all versions and renditions of a document.
                           OriginalDocumentID
                           URI
                        
                     
                  
               
               
                  http://www.aiim.org/pdfa/ns/id/
                  pdfaid
                  PDF/A ID Schema
                  
                     
                        
                           internal
                           Part of PDF/A standard
                           part
                           Integer
                        
                        
                           internal
                           Amendment of PDF/A standard
                           amd
                           Text
                        
                        
                           internal
                           Conformance level of PDF/A standard
                           conformance
                           Text
                        
                     
                  
               
            
         
      
   
                                                                                                   
                                                                                                   
                                                                            
```

## candidate-04 [geometric-dl] — UNCONSUMED

**Title:** Classification of hierarchical text using geometric deep learning: the case of clinical trials corpus

**URL:** https://arxiv.org/abs/2110.15710

**Description:** A geometric deep learning approach that represents hierarchical documents as graphs and uses graph neural networks with a selective pooling operation to classify clinical trial protocols as completed or terminated.

**Content extract (≤6k chars):**

```
Title: Classification of hierarchical text using geometric deep learning: the case of clinical trials corpus
Authors: Sohrab Ferdowsi, Nikolay Borissov, J. Knafou, P. Amini, D. Teodoro
Year: 2021
Citations: 10
Fields: Computer Science
arXiv: 2110.15710

Abstract:
We consider the hierarchical representation of documents as graphs and use geometric deep learning to classify them into different categories. While graph neural networks can efficiently handle the variable structure of hierarchical documents using the permutation invariant message passing operations, we show that we can gain extra performance improvements using our proposed selective graph pooling operation that arises from the fact that some parts of the hierarchy are invariable across different documents. We applied our model to classify clinical trial (CT) protocols into completed and terminated categories. We use bag-of-words based, as well as pre-trained transformer-based embeddings to featurize the graph nodes, achieving f1-scoresaround 0.85 on a publicly available large scale CT registry of around 360K protocols. We further demonstrate how the selective pooling can add insights into the CT termination status prediction. We make the source code and dataset splits accessible.

TL;DR: This work considers the hierarchical representation of documents as graphs as graphs and uses geometric deep learning to classify them into different categories and applies this model to classify clinical trial (CT) protocols into completed and terminated categories.
```

## candidate-05 [geometric-dl] — UNCONSUMED

**Title:** Conditional Clifford-Steerable CNNs with Complete Kernel Basis for PDE Modeling

**URL:** https://arxiv.org/abs/2510.14007

**Description:** A paper showing that Clifford-Steerable CNNs have an incomplete kernel basis and proposing input-conditioned equivariant kernels that improve expressivity on PDE forecasting tasks like fluid dynamics and relativistic electrodynamics.

**Content extract (≤6k chars):**

```
Title: Conditional Clifford-Steerable CNNs with Complete Kernel Basis for PDE Modeling
Authors: Bálint László Szarvas, Maksim Zhdanov
Year: 2025
Categories: cs.LG, cs.AI
arXiv: 2510.14007

Abstract:
Clifford-Steerable CNNs (CSCNNs) provide a unified framework that allows incorporating equivariance to arbitrary pseudo-Euclidean groups, including isometries of Euclidean space and Minkowski spacetime. In this work, we demonstrate that the kernel basis of CSCNNs is not complete, thus limiting the model expressivity. To address this issue, we propose Conditional Clifford-Steerable Kernels, which augment the kernels with equivariant representations computed from the input feature field. We derive the equivariance constraint for these input-dependent kernels and show how it can be solved efficiently via implicit parameterization. We empirically demonstrate an improved expressivity of the resulting framework on multiple PDE forecasting tasks, including fluid dynamics and relativistic electrodynamics, where our method consistently outperforms baseline methods.
```

## candidate-06 [geometric-dl] — UNCONSUMED

**Title:** Group Equivariance Meets Mechanistic Interpretability: Equivariant Sparse Autoencoders

**URL:** https://arxiv.org/abs/2511.09432

**Description:** Introduces adaptively equivariant sparse autoencoders that incorporate group symmetries to discover more interpretable features, improving probing performance over regular SAEs on rotated synthetic images.

**Content extract (≤6k chars):**

```
Title: Group Equivariance Meets Mechanistic Interpretability: Equivariant Sparse Autoencoders
Authors: Ege Erdogan, Ana Lucic
Year: 2025
Categories: cs.LG
arXiv: 2511.09432

Abstract:
Sparse autoencoders (SAEs) have proven useful in disentangling the opaque activations of neural networks, primarily large language models, into sets of interpretable features. However, adapting them to domains beyond language, such as scientific data with group symmetries, introduces challenges that can hinder their effectiveness. We show that incorporating such group symmetries into the SAEs yields features more useful in downstream tasks. More specifically, we train autoencoders on synthetic images and find that a single matrix can explain how their activations transform as the images are rotated. Building on this, we develop adaptively equivariant SAEs that can adapt to the base model's level of equivariance. These adaptive SAEs discover features that lead to superior probing performance compared to regular SAEs, demonstrating the value of incorporating symmetries in mechanistic interpretability tools.
```

## candidate-07 [ldpc-coding] — UNCONSUMED

**Title:** Constraint satisfaction problems and neural networks a statistical physics persp

**URL:** file:///239a3a3233ce95f440d35c1b85ca2148b1e65bf3970f58228dd47d5da3c2cca4/Constraint_satisfaction_problems_and_neural_networks_a_statistical_physics_persp.pdf

**Description:** A perspective paper by Mézard and Mora introducing how statistical physics methods—particularly message passing algorithms like Belief Propagation and Survey Propagation—can solve hard constraint satisfaction problems (random k-SAT, LDPC decoding, perceptron learning). It unifies satisfiability, error correction, and neuroscience inference problems under a common graphical-model framework and proposes a novel message passing algorithm for reconstructing neural interactions from multi-electrode correlation data.

**Content extract (≤6k chars):**

```
Constraint satisfaction problems and neural networks:
a statistical physics perspective
Marc M´ ezard
LPTMS, UMR 8626 CNRS et Univ. Paris-Sud, 91405 Orsay CEDEX, France
Thierry Mora
Lewis-Sigler Institute for Integrative Genomics, Princeton University, Princeton, NJ 08544, USA
Abstract
A new field of research is rapidly expanding at the crossroad between statistical physics, infor-
mation theory and combinatorial optimization. In particular, the use of cutting edge statistical
physics concepts and methods allow one to solve very large constraint satisfaction problems like
random satisfiability, coloring, or error correction.
Several aspects of these developments should be relevant for the understanding of functional
complexity in neural networks. On the one hand the message passing procedures which are used
in these new algorithms are based on local exchange of information, and succeed in solving some
of the hardest computational problems. On the other hand some crucial inference problems in
neurobiology, like those generated in multi-electrode recordings, naturally translate into hard
constraint satisfaction problems.
This paper gives a non-technical introduction to this field, emphasizing the main ideas at
work in message passing strategies and their possible relevance to neural networks modelling.
It also introduces a new message passing algorithm for inferring interactions between variables
from correlation data, which could be useful in the analysis of multi-electrode recording data.
1. Introduction: Constraint Satisfaction Problems
arXiv:0803.3061v1 [q-bio.NC] 20 Mar 2008
Engineers offer encounter problems with many degrees of freedom (‘variables’) but
also many constraints. The problem is to find a value of the variables which satisfies
all constraints, or the most probable configuration of variable given the constraints and
some a priori measure. Obvious applications are scheduling (classes, airplanes...), or job
assignment. But similar problems occur in various branches of scientific activity, and
are crucial in several domains. To be short we shall focus here on four of them. The
satisfiability problem is at the core of the theory of computational complexity in computer
science. Error correcting codes are one of the main topic of information theory. Learning
Preprint submitted to Elsevier 2 December 2024
from examples is a basic process in cognitive neuroscience. Reconstruction of neuron
interactions from multi-electrode recording is a problem which is becoming more and
more important.
All these problems can be formulated in a common language (M´ ezard & Montanari,
2008), and have a strong relationship to fundamental issues in statistical physics like the
existence of phase transition, and the possibility of glassy phases. They can also be cast
into a somewhat generic formalism, based a graphical representation of the topology of
constraints (Kschischang et al., 2001), which allows to apply a general ‘message passing’
strategy to all of them. Some of these message passing algorithms have actually shown
strikingly good performance, solving some problems in satisfiability or perceptron learn-
ing that are unreachable by any other algorithms. It is interesting in itself to understand
how fundamental issues in computational complexity and information processing can be
formulated in the same language as relevant problems in neuroscience, the main aim of
this paper is to give some clues on these connexions.
2. Satisfiability
The problem of satisfiability involves N Boolean variables x i ∈ { T, F } . There exist
thus 2 N possible configurations of these variables. The constraints take the special form
of ‘clauses’, which are logical ‘OR’ functions of the variables. For instance the clause
x 1 ∨ x 2 ∨ x ¯ 3 is satisfied whenever x 1 = T or x 2 = T or x 3 = F (the bar means negation:
T ¯ = F and F ¯ = T ). Therefore, among the 8 possible configurations of x 1 , x 2 , x 3 , the
only one which is forbidden by this clause is x 1 = x 27 = 0, x 3 = 1. An instance of the
satisfiability problem is given by the list of all the clauses it contains. The problem is to
find a choice of the Boolean variables (called an ’assignment’) such that all constraints
are satisfied. When there exists such a choice the corresponding instance is said to be
‘SAT’, otherwise it is ‘UNSAT’, and one typically seeks a configuration of variables which
violates the smallest number of constraints.
Satisfiability plays an essential role in the theory of computational complexity, be-
cause many other difficult problems like the traveling salesman, the colouring of graphs,
scheduling, protein folding, can be mapped ‘polynomially’ to it. It was the first problem
which has been shown to be ‘NP-complete’ (Cook, 1971). This means that if one could
find an algorithm that solves satisfiability in a ‘polynomial’ time (growing like a power
of N ), one could also solve all these other problems in polynomial time: life would be
much easier, in particular the life of scientists... This is generally considered unlikely, but
the corresponding mathematical problem (whether the NP class is distinct or not from
the ‘P’ class of problems which are solvable in polynomial time) is an important open
problem in mathematics.
The result of Cook is a worst case analysis of the satisfiability problem. However it
appears more and more important to study ‘typical case’ complexity of satisfiability
problems by introducing some classes of instances. A much studied class is the ran-
dom ‘3-SAT’ problem. Each clause contains exactly three variables chosen randomly in
{ x 1 , .., x N } , and each variable is negated randomly with probability 1 / 2. This problem
is particularly interesting because its difficulty can be tuned by varying one single con-
trol parameter, the ratio α = M
N of constraints per variable. One expects intuitively
that for small α most instances are SAT, while for large α most of them are UNSAT.
2
1
0.8 10000
0.6
P N P N 1000
0.4
1
```

## candidate-08 [separatrix] — UNCONSUMED

**Title:** Towards Continual Learning Desiderata via HSIC Bottleneck Orthogonalization and

**URL:** file:///ffe89edecf388d7b8f3235fd8ca54f424aa7efdbe9b874f186d9a46cf07b3017/Towards_Continual_Learning_Desiderata_via_HSIC-Bottleneck_Orthogonalization_and_.pdf

**Description:** An AAAI-24 paper proposing CLDNet, a continual learning method that combines HSIC-Bottleneck Orthogonalization (HBO) for non-overwritten parameter updates with EquiAngular Embedding (EAE) for decision boundary adaptation between old and new tasks. The method achieves competitive accuracy without exemplar buffers and with only 1.02x model expansion, outperforming state-of-the-art rehearsal-based baselines by 7.54% on CIFAR-100.

**Content extract (≤6k chars):**

```
The Thirty-Eighth AAAI Conference on Artificial Intelligence (AAAI- 24)
Towards Continual Learning Desiderata via HSIC-Bottleneck Orthogonalization
and Equiangular Embedding
Depeng Li 1* , Tianqi Wang 1* , Junwei Chen 1 , Qining Ren 1 , Kenji Kawaguchi 2 , Zhigang Zeng 1†
1 School of Artificial Intelligence and Automation, Huazhong University of Science and Technology
2 School of Computing, National University of Singapore
{ dpli, tianqiwang, junwei chen, qiningren, zgzeng } @hust.edu.cn, kawaguch@csail.mit.edu
Abstract 70
60 70 Ours 65 Ours 100 Ours
50 60 63 PCL 90
Deep neural networks are susceptible to catastrophic for- 40 50 ER 61 APD 80 OWM
getting when trained on sequential tasks. Various continual 30 40 59
20 70
learning (CL) methods often rely on exemplar buffers or/and Average Accuracy 10 30 OCM 57 DEN 60
20 DER++
network expansion for balancing model stability and plastic- 100 200 2000 RCL
DualHSIC 3000 55 50
Average Accuracy 10 Buffer Size 53 40
ity, which, however, compromises their practical value due to 100 200 500 2000 3000 100 120 140 160 180 3 4 5
privacy and memory concerns. Instead, this paper considers a Buffer Size Model Expansion Ratio (%) Number of Tasks
strict yet realistic setting, where the training data from previ- (a) (b) (c)
ous tasks is unavailable and the model size remains relatively Figure 1: Comparison between our method and representa-
constant during sequential training. To achieve such desider-
ata, we propose a conceptually simple yet effective method tive CL approaches. (a) Rehearsal-based ones are often sen-
that attributes forgetting to layer-wise parameter overwrit- sitive to buffer sizes. (b) Some architecture-based ones scale
ing and the resulting decision boundary distortion. This rapidly during sequential training. (c) Most regularization-
is achieved by the synergy between two key components: based ones struggle with the stability-plasticity dilemma
HSIC-Bottleneck Orthogonalization (HBO) implements non- whose performance is not satisfactory in the class-IL (hy-
overwritten parameter updates mediated by Hilbert-Schmidt brid with (a) or/and (b) excluded). By contrast, our method
independence criterion in an orthogonal space and EquiAn- reaches multiple CL desiderata simultaneously.
gular Embedding (EAE) enhances decision boundary adapta-
tion between old and new tasks with predefined basis vectors.
Extensive experiments demonstrate that our method achieves
competitive accuracy performance, even with absolute supe-
riority of zero exemplar buffer and 1.02 × the base model. subset of past samples and retrain them with those from a
new task jointly (Liu et al. 2020; Hayes et al. 2020; Bon-
icelli et al. 2022; Guo, Liu, and Zhao 2022; Luo et al.
Introduction 2023). Critically, these methods pose a threat to data pri-
vacy and often decline performance as buffer size decreases,
Current deep learning models have shown promising perfor-
as depicted in Figure 1(a). Architecture-based approaches
mance in various fields, but they lack the ability of continual
dynamically modify the network architecture to accommo-
learning (CL) that humans possess (Kang et al. 2022; Smith
date knowledge needed for new tasks (Serr` a et al. 2018; Ke
et al. 2023). CL entails progressively acquiring knowledge
et al. 2021; Yang et al. 2023a; Hu et al. 2023). In partic-
from sequentially presented tasks, with access to only cur-
ular, network expansion involves adding a sub-network for
rent task data and no past data (Li and Zeng 2023b). As a
each task and utilizing aggregated feature representation for
result, directly retraining a well-trained model on new task
final prediction (Yan, Xie, and He 2021; Wang et al. 2022a).
data using stochastic gradient descent (SGD) leads to the
As shown in Figure 1(b), their model size expands rapidly
well-known phenomenon of catastrophic forgetting (Mc-
as the number of tasks grows, which should be counted
Closkey and Cohen 1989), which refers to abrupt and signif-
into the memory budget for a fair comparison (Zhou et al.
icant performance degradation on previously learned tasks.
2023). Regularization-based approaches penalize parame-
Recent works have experienced a remarkable surge in ad-
ter variations over an over-parameterized network, where
dressing catastrophic forgetting (Wang et al. 2021a; Tong
each network parameter is associated with weight impor-
et al. 2023; Zhou et al. 2023). However, it is noteworthy
tance (Kirkpatrick et al. 2017; Zeng et al. 2019; Wołczyk
that the merits of CL come with costs. Rehearsal-based ap-
et al. 2022). However, the performance of these methods that
proaches , as the mainstay of CL, explicitly buffer a small
do not store any past data is yet unsatisfactory, especially in
* These authors contributed equally. the class-incremental learning (class-IL) scenario, which ad-
† Corresponding author. dresses the most common problem of incrementally learning
Copyright © 2024, Association for the Advancement of Artificial new classes without the provision of test-time task identities
Intelligence (www.aaai.org). All rights reserved. (Zhuang et al. 2022; Wang et al. 2022b) (see Figure 1(c)).
13464
The Thirty-Eighth AAAI Conference on Artificial Intelligence (AAAI- 24)
In summary, for alleviating catastrophic forgetting, many To address the aforementioned second question, we draw
CL methods prioritize accuracy performance to the detri- inspiration from the recently proposed equiangular basis
ment of other fronts. This motivates us to find new methods vectors (EBVs) (Shen, Sun, and Wei 2023). Unlike the
against forgetting while satisfying multiple CL desiderata: trainable fully-connected layer with softmax, the EBVs is
(i) It should no longer access the training data of previous parameter-free since its learning objective is to minimize the
tasks . While keeping prior observations demonstrates supe- spherical distance of learned representations with predefined
rior ability in combating forgetting, reliance on re
```

## candidate-09 [hodge] — UNCONSUMED

**Title:** Hodge Aware Contrastive Learning

**URL:** file:///8875203cc5c27bc60e580aff6439263900d0875ea1155acc71e1637899f9e964/Hodge-Aware_Contrastive_Learning.pdf

**Description:** Research paper proposing Hodge-aware contrastive learning (SCL) for simplicial complexes, which leverages the Hodge decomposition to design spectral-preserving augmentations and reweight negative samples in the InfoNCE loss. The method generates embeddings encoding interpretable gradient, curl, and harmonic properties of edge flows, outperforming fully supervised approaches on two standard edge flow classification benchmarks, especially in label-scarce settings.

**Content extract (≤6k chars):**

```
HODGE-AWARE CONTRASTIVE LEARNING
Alexander M¨ ollers ∗ , Alexander Immer † , Vincent Fortuin ‡ , Elvin Isufi ∗
ABSTRACT While these supervised learning (SL) methods for simplicial
Simplicial complexes prove effective in modeling data with data have their merits, they also come with limitations such as a
multiway dependencies, such as data defined along the edges of over-reliance on labeled examples and suboptimal performance in
networks or within other higher-order structures. Their spectrum data-scarce scenarios. SL methods are also mainly designed for a
can be decomposed into three interpretable subspaces via the Hodge specific task and the resulting output is generally not reusable in
decomposition, resulting foundational in numerous applications. We different applications. Therefore, we propose a contrastive learn-
leverage this decomposition to develop a contrastive self-supervised ing (CL) approach for simplicial data that addresses these issues.
learning approach for processing simplicial data and generating em- To this end, we employ a simplicial convolutional neural network
beddings that encapsulate specific spectral information. Specifically, (SCNN) to produce embeddings and optimise it in a self-supervised
we encode the pertinent data invariances through simplicial neural manner using the InfoNCE loss [14]. The resulting CL approach
networks and devise augmentations that yield positive contrastive can use both labeled and unlabeled examples to create robust and
examples with suitable spectral properties for downstream tasks. reusable representations for simplicial data. These representations
Additionally, we reweight the significance of negative examples in can subsequently be employed in various downstream tasks, offering
the contrastive loss, considering the similarity of their Hodge com- improved accuracy especially in label-scarce scenarios.
ponents to the anchor. By encouraging a stronger separation among To further enhance our method, we propose stochastic augmen-
less similar instances, we obtain an embedding space that reflects tations and introduce information about the Hodge Decomposition
the spectral properties of the data. The numerical results on two into the embeddings by i) optimizing the parameters of the augmen-
standard edge flow classification tasks show a superior performance tations so that they generate positive examples that respect the spec-
even when compared to supervised learning techniques. Our find- tral properties of the data; and ii) weighting the negative samples
ings underscore the importance of adopting a spectral perspective in the InfoNCE loss by a Hodge-aware distance to the anchor (true
for contrastive learning with higher-order data. datum). This approach results in a spectrally organized embedding
space and facilitates downstream learning. We corroborate the latter
Index Terms — Hodge Laplacian, simplicial filter, contrastive in two edge flow classification settings and show superior perfor-
learning. mance compared with a fully-supervised model. Related to this, our
1. INTRODUCTION contribution is threefold:
The difficulty to represent many biological, social, and technologi-
cal networks arises from the complexity of their inherent relational C1) we propose simplicial contrastive learning (SCL), design re-
structures and the nuanced definitions of the associated data. Im- lated augmentations and experimentally validate all our ap-
portantly, the data in such networks is often defined on higher-order proaches;
components like edges and triangles, thus demanding an approach C2) we show how augmentations in the simplicial domain can be
that incorporates interactions beyond the pairwise paradigm [1]. optimized with respect to the Hodge decomposition;
Simplicial complexes (SCs) have been proposed to model such de-
pendencies in higher-order networks [2, 3]. Amongst others, SCs C3) we introduce a reweighing of the negative examples based
have shown particular efficacy in edge flow applications (e.g., mass, on the similarity of their Hodge components to encourage a
energy, information, or trajectories) for which traditional graph- spectrally organized embedding space.
based techniques do not induce a good inductive bias [4,5]. Notably,
they have been leveraged to alleviate the curse of dimensionality in 2. DATA PROCESSING ON SIMPLICIAL COMPLEXES
autoregressive flow prediction for water networks [6] and to remove In this section, we introduce the fundamental concepts behind sim-
arXiv:2309.07364v1 [cs.LG] 14 Sep 2023 arbitrage opportunities in currency exchange markets [7]. plicial data structures and related data processing techniques.
An important property of SCs is that they enjoy an algebraic
representation via the Hodge Laplacian matrices, ultimately allow- 2.1. Simplicial Data and Structures
ing for spectral analysis. The latter is achieved through the Hodge
decomposition of the spectrum and has been used to develop Hodge- Let V = { 1 , . . . , N } be a set of vertices. A k − simplex S k is a sub-
aware signal processing and learning techniques for edge flows and set of V that contains k + 1 distinct elements. A simplicial complex
other simplicial data [5, 8, 9]. Recent advances include developing a X K of order K is a collection of simplices such that it contains at
simplicial Fourier transform [4], convolutional filters [7], and neural least one K − simplex and if S k ∈ X K we have that all subsets of
networks that are trained in a (semi-)supervised manner. [10–13]. S k are also elements of X K . From a geometric representation per-
spective, in a SC of order K = 2 , nodes are 0 -simplices, edges are
∗ TU Delft, Delft, The Netherlands. † ETH Z¨ urich, Z¨ urich, Switzer- 1-simplices and (filled) triangles are 2-simplices [2, 3].
land. ‡ Helmholtz AI, Munich, Germany. EI is supported by the TU Delft AI Neighborhood relations in an SC can be represented via the in-
Labs Programme. AI is supported by a Max Planck ETH Center for Learning ci
```

## candidate-10 [hodge] — UNCONSUMED

**Title:** Topological Point Cloud Clustering

**URL:** https://arxiv.org/abs/2303.16716

**Description:** Introduces Topological Point Cloud Clustering (TPCC), combining spectral clustering with topological data analysis via Hodge-Laplacians on simplicial complexes to cluster points by their contribution to global topological features.

**Content extract (≤6k chars):**

```
Title: Topological Point Cloud Clustering
Authors: Vincent P. Grande, Michael T. Schaub
Year: 2023
Categories: math.AT, cs.CG, cs.LG, cs.SI
arXiv: 2303.16716

Abstract:
We present Topological Point Cloud Clustering (TPCC), a new method to cluster points in an arbitrary point cloud based on their contribution to global topological features. TPCC synthesizes desirable features from spectral clustering and topological data analysis and is based on considering the spectral properties of a simplicial complex associated to the considered point cloud. As it is based on considering sparse eigenvector computations, TPCC is similarly easy to interpret and implement as spectral clustering. However, by focusing not just on a single matrix associated to a graph created from the point cloud data, but on a whole set of Hodge-Laplacians associated to an appropriately constructed simplicial complex, we can leverage a far richer set of topological features to characterize the data points within the point cloud and benefit from the relative robustness of topological techniques against noise. We test the performance of TPCC on both synthetic and real-world data and compare it with classical spectral clustering.
```

## candidate-11 [hodge] — UNCONSUMED

**Title:** Root-to-Leaf Path Random Walks, Normalized Hodge Laplacians, and Cheeger Inequalities on Simplicial Complexes

**URL:** https://arxiv.org/pdf/2604.27241

**Description:** Research paper introducing root-to-leaf path random walks on double covers of graded signed graphs to derive normalized Hodge Laplacians and Cheeger inequalities for simplicial complexes.

**Content extract (≤6k chars):**

```
Title: Root-to-Leaf Path Random Walks, Normalized Hodge Laplacians, and Cheeger Inequalities on Simplicial Complexes
Authors: Francesco Viganò, Tolga Birdal, Michael T. Schaub, Mauricio Barahona
Year: 2026
Categories: math.CO, math.AT, math.SP
arXiv: 2604.27241

Abstract:
We introduce root-to-leaf path random walks on double covers of graded signed graphs and analyze their behavior in a general setting. Viewing simplicial complexes within this framework, we show that these walks induce the natural normalization of the coboundary operator and of the Hodge Laplacians while preserving the basic structural features of combinatorial Hodge theory. We then derive Cheeger inequalities for the upper side of the normalized Hodge spectrum, identify the coherent structures governing these bounds, and combine the up- and down-cases into sharper estimates.
```

## candidate-12 [spin-glass-codes] — UNCONSUMED

**Title:** Predictability of complex networks

**URL:** https://www.pnas.org/doi/10.1073/pnas.2535161123

**Description:** PNAS paper establishing a network predictability theory by mapping link prediction onto a spin glass model and using the cavity method to derive a local sampling algorithm and predictability index.

**Content extract (≤6k chars):**

```
Title: Predictability of complex networks
Authors: Fei Jing, Zi-Ke Zhang, Qingpeng Zhang, Giorgio Parisi
Year: 2026
Citations: 0

Abstract:
We establish network predictability theory by mapping link prediction onto a spin glass model, where network partitions correspond to spin configurations, and predictability equals the system’s average energy. Using the cavity method from statistical physics, we prove that global predictability decomposes into individual link contributions, enabling an efficient local sampling algorithm that reduces the computational complexity of evaluating individual link contributions from being dependent on the entire network to only its local neighborhood, scaling with the average degree. We derive exact results for canonical network models: Erdös–Rényi networks exhibit universal predictability of 0.5 regardless of algorithm choice, establishing the random baseline, while structured networks show predictability controlled by their prior parameters. We introduce the predictability index, which quantifies the maximum achievable performance without information loss and accurately predicts algorithm performance under random division. Analysis of real networks validates our framework, revealing how degree heterogeneity and structural patterns govern predictability. This physics-based approach provides both theoretical insights into link prediction limits and practical tools for assessing network reconstruction potential, with implications for applications from biological network inference to social network analysis.

TL;DR: It is proved that global predictability decomposes into individual link contributions, enabling an efficient local sampling algorithm that reduces the computational complexity of evaluating individual link contributions from being dependent on the entire network to only its local neighborhood, scaling with the average degree.
```

## candidate-13 [atlas-general] — UNCONSUMED

**Title:** Rational connectedness and boundedness of Fano manifolds

**URL:** file:///aa32076fb8eb266115dbf31034857b02034ad46096f8b587abbadbaad488e922/Rational_connectedness_and_boundedness_of_Fano_manifolds.pdf

**Description:** A foundational paper in algebraic geometry proving that Fano manifolds over algebraically closed fields of characteristic zero are rationally connected — any two general points can be joined by an irreducible rational curve of bounded anticanonical degree. As a corollary, the authors establish that n-dimensional Fano manifolds form a bounded family parametrized by a quasiprojective scheme, with an effective (though rapidly growing) degree bound c(n).

**Content extract (≤6k chars):**

```
J. DIFFERENTIAL GEOMETRY
36(1992)765-779
RATIONAL CONNECTEDNESS AND
BOUNDEDNESS OF FANO MANIFOLDS
JANOS KOLLAR, YOICHI MIYAOKA & SHIGEFUMI MORI
0. Introduction
Fano manifolds are, by definition, smooth projective varieties with am-
ple first Chern class (= anticanonical class). They are of special interest
from the viewpoint of classification theory via minimal models; in fact,
a principal goal of the minimal model program is to decompose a gen-
eral algebraic variety into the Fano-like part and the minimal part (cf. [5],
[11]).
Two-dimensional Fano manifolds are usually called Del Pezzo surfaces.
Their classification into ten families of rational surfaces is an immediate
consequence of Castelnuovo's criteria for rationality and minimality and
Enriques' theory of adjunction. However, the systematic study of Fano
manifolds initiated by G. Fano has revealed that their structure is not so
simple in higher dimensions. For instance, the list of Fano 3-folds consists
of 104 deformation classes, many of which are not rational [4], [12]. In di-
mension > 4, their complete classification is thus virtually impossible and
we should rather be concerned with vague but more accessible questions:
Question 1. Does the set of ^-dimensional Fano manifolds form a
bounded family?
Question 2. What can be said about geometric properties shared by
the Fano manifolds in common?
The aim of this paper is to answer these questions: rational connected-
ness and boundedness.
A variety X is said to be rationally connected if two general points
can be joined by an irreducible rational curve on X . Rational connect-
edness is a birational and deformation invariant, thus fitting well into
the classification theory [8]. Roughly speaking, it is a crude generaliza-
tion of unirationality, which is often too subtle to deal with in a general
framework. Through crude, this generalization is natural enough to yield
most of the geometric properties known for unirational varieties such as
Received December 30, 1991.
766 JANOS KOLLAR, YOICHI MIYAOKA & SHIGEFUMI MORI
1-connectedness, vanishing of global differential forms, etc. For further
implications of rational connectedness, the reader is referred to [8].
Theorem 0.1 A Fano manifold X over an algebraically closed field of
characteristic zero is rationally connected. More precisely, any two general
points x and y can be joined by an irreducible rational curve C such that
(C, -K χ ) < c(dimX), where c(n) is an effectively computable function
in n , a positive integer.
As was pointed out by G. Fano (cf. [7]), we can derive from (0.1) an
effective bound of the degree of a Fano ft-fold:
Theorem 0.2. For a Fano manifold X of dimension n over an alge-
braically closed field of characteristic zero, the degree of X with respect to
the anticanonical divisor is bounded, i.e.,
n
c χ (X) <c(n)\
where the function c(n) is the same one as in (0.1). In particular, by a
theorem of Kollάr and Matsusaka [6], the n-dimensional Fano manifolds
form a bounded family, i.e., they are (noneffectively) parametrized by a
quasiprojective scheme.
This article is the third part of our joint program. In the first part [7],
Fano manifolds with Picard number one are discussed. In this specific
2 
case, we can choose a rather small number \{n + 2) instead of c(n) .
For general Fano manifolds with Picard number > 2 treated here, our
bounding function c(n) grows very rapidly as follows: c(n) = O(n ).
For the explicit definition of c(n) , see §4 below.
The second part [8] is devoted to the general theory of rationally con-
nected varieties, including a numerical characterization of rationally con-
nected 3-folds. Note that "maximal rationally connected fibrations" con-
structed there will provide a shortcut toward the rational connectedness
of Fano manifolds, except that we cannot keep track of the degrees of
rational curves by this method.
In general classification theory, we have to deal with Q-Fano varieties
as well. In the fourth part (in preparation), we will prove the rational
connectedness and the boundedness of Q-Fano 3-folds with only terminal
singularities.
In this paper, all schemes are defined over an algebraically closed field
with uncountable elements.
Our joint program has grown out of our discussion at University of
Utah while the two Japanese authors were visiting there with financial
support from the US-Japan Cooperative Science Program of the Japan
Society for the Promotion of Science. Partial support for the first author
RATIONAL CONNECTEDNESS OF FANO MANIFOLDS 767
was provided by the NSF, under the grant numbers DMS-8707320 and
DMS-8946082, and by an A. P. Sloan fellowship. Essential ideas in this
article were addressed at a conference at University of Utah in October of
1990.
In his new papers [1], [2], F. Campana proves that two points on a
Fano manifold can be joined by a chain of rational curves (cf. Theorem
3.3 below). His idea is basically the same as ours in §§1-3.
1. Free rational curves and the associated rational fibration
In this section, we recall and strengthen some results in [7], [8], to which
the reader is referred for more detail.
Let T χ denote the tangent sheaf of a smooth variety X.
An irreducible rational curve C on smooth projective X is said to
be free if T χ restricted to C is semipositive. Let / : P 1 -* X be the
composite of the normalization and the embedding of C (in what follows,
/ is called the normalization of C for simplicity). C is free if and only
if f*T χ is generated by global sections.
Let g 7 = {C s } seS be a flat family of curves on X. *& is called a
covering family of irreducible rational curves if
(1) the parameter space S is an irreducible variety,
(2) every member C s is an irreducible rational curve, and
(3) \J seS C s contains an open dense subset of X .
A variety X is uniruled if and only if there exists a covering family of
irreducible rational curves on X .
Proposition 1.1. Let X be a smooth projective variety over an alge-
braically closed fiel
```

## candidate-14 [atlas-general] — UNCONSUMED

**Title:** 19880001113

**URL:** file:///1163430369bcf6665226956c9a99b39b1ca5a56b48370d451fdab470a07bfe12/19880001113.pdf

**Description:** Foundational ICASE/NASA technical paper introducing the level-set method (PSC algorithms) for tracking fronts propagating with curvature-dependent speed via Hamilton-Jacobi formulations with parabolic right-hand sides. The authors recast the moving interface as the zero level set of a higher-dimensional function and apply hyperbolic conservation law techniques (non-oscillatory upwind schemes) to capture sharp gradients and cusps. The method handles topological merging/breaking naturally in any dimension and selects the entropy-satisfying viscous limit, demonstrated on flame propagation and crystal-growth-style surface motion problems.

**Content extract (≤6k chars):**

```
, NASA Contractor Report 178382
I
I ICASE REPORT NO. 87-66
I C A S E
FRONTS PROPAGATING WITH CURVATURE DEPENDENT SPEED:
ALGORITHMS BASED ON HAMILTON-JACOB1 FORMULATIONS
- __ _ _ ~~ ~ 
/ ~ ~ ~
[I A S A - C B - 1783 8 2) FRONTS PROP AG AT I IG Y IT H M88- 19495
C U R V A T U R E DEPENDENT SPEED: A L G O R I T H H S B h S E D
OI E A H X L T O N - J A C O B X POR?IULATIONS F i n a l Repart
( N A S A ) 54 p A v a i l : NTIS €IC AO4/nP A 0 1 U n c l a s
CSCL 12A 63/59 0103588
Stanley %her
James A. Sethian
C o n t r a c t No. N A S 1 - 1 8 1 0 7
S e p t e m b e r 1987
INSTITUTE FOR COMPUTER APPLICATIONS IN SCIENCE AND ENGINEERING
NASA Laugley Research Center, Rampton, Virginia 23665
Operated by the Universities Space Research Association
'.,
Fronts Propagating with Curvature Dependent Speed:
Algorithms Based on Hamilton-Jacobi Formulations
Stanley Osher
Department of Mathematics
University of California
Los Angeles, California 90024
James A. Sethian
Department of Mathematics
University of California
Berkeley, California 94720
We devise new numerical algorithms, called PSC algorithms, for following fronts propagating with
curvature-dependent speed. The speed may be an arbitrary function of curvature, and the front can also be
passively advected by an underlying flow. These algorithms approximate the equations of motion, which
resemble Hamilton-Jacobi equations with parabolic right-hand-sides, by using techniques from the hyper-
bolic conservation laws. Non-oscillatory schemes of various orders of accuracy are used to solve the equa-
tions, providing methods that accurately capture the formation of sharp gradients and cusps in the moving
fronts. The algorithms handle topological merging and breaking naturally, work in any number of space
dimensions, and do not require that the moving surface be written as a function. The methods can be also
used for more general Hamilton-Jacobi-type problems. We demonstrate our algorithms by computing the
solution to a variety of surface motion problems.
This work is supported in part by the Applied Mathematics Subprogram of the Office of Energy Research
under contract DE-AC03-76SF00098, NSF under the National Science Foundation Mathematical Sciences
Program, Sloan Foundation, NSF Grant No., DMs85-03294, ARO Grant. No. DAAG29-85-K-0190,
DARPA Grant in the ACMP Program, ONR Grant N00014-86-K-0691, NASA Langley Grant NAG1-270.
This work was also supported by the National Aeronautics and Space Administration under NASA Con.
tract No. NAS1-18107 while the first author was in residence at the Institute for Computer Application!;
in Science and Engineering (ICASE), NASA Langley Research Center, Hampton, VA 23665.
i
Fronts Propagating with Curvature Dependent Speed:
Algorithms Based on Hamilton-Jacobi Formulations
I. INTRODUCTION
In a variety of physical phenomena, one wants to track the motion of a front whose speed depends on
t h e local curvature. Two well-known examples are crystal growth [3,19,20,24,25,30,381 and flame propa-
gation [6,18,22,23,37,39]. In this paper, we introduce, analyze, and utilize a collection of new numerical
algorithms for studying such problems. These new algorithms approximate the equations of motion of pro-
pagating fronts, which resemble Hamilton-Jacobi equations with viscosity terms. We demonstrate our algo-
rithms by computing the solutions t o a variety o f surface motion problems.
-
The background theory and numerical experimentation behind this approach have been developed in
a series of papers, see [31,32,33,34]. In this paper, these ideas are coupled to the technology for the
numerical approximation of hyperbolic conservation laws to produce algorithms which we call PSC
schemes, for Propagation of Surfaces under Curvature. These new schemes allow one to follow the motion
of an N-1 dimensional surface in N space dimensions. The speed may be an arbitrary function of the curva-
ture, and the h n t can also be passively advected by an underlying flow. The algorithms can be con-
structed with any desired accuracy in space and time and do not require the front to remain a function. The
methods are in a Eulerian framework, thus the number of computational elements is fixed at the outset.
Topological merging and breaking is hahdled naturally, and the basic first order scheme is extremely sim-
ple to program.
As illustration of the wide applicability of such algorithms, consider the case of flame propagation,
see [34]. A common model idealizes the burning flame as an infinitely thin boundary which separates
regions of constant steady-state velocity, density, and temperature and propagates into the unburnt fluid at a
speed dependent on the local curvature. The idea here is that cool convex fingers reaching out into the
unburnt gas somehow propagate slower than do concave regions which are hot gases surrounding a small
unburnt pocket. At the same time, particles along the flame front undergo an increase in volume as they
2
bum, creating a jump in velocity across the flame front. This discontinuity in the velocity field creates vor-
ticity along the burning flame, which can be related to the local curvature, and this new vorticity field con-
tributes to the advection of the propagating flame. Thus, there are at least two distinct ways in which the
speed of the moving flame depends on the local curvature.
Typically, there have been two types of numerical algorithms employed in the solution of such prob-
lems. The &st parameterizes the moving front by some variable and discretizes this parameterization into a
set of marker points. The positions of the marker points are updated in time according to approximations to
the equations of motion. Such techniques can be extremely accurate in the attempt to follow the motions of
small perturbations. However, for large, complex motion, several problems soon occur. First, marker parti-
cles come together in regions where the curvature of the propagating front builds, causing numerical insta-
bility unless 
```

## candidate-15 [atlas-general] — UNCONSUMED

**Title:** 2309.03085v1

**URL:** file:///8939f61537c0ee6269f2068ce9b4c503586fb3410a53a53a85000f28ee1982d0/2309.03085v1.pdf

**Description:** This paper by Jacob Barandes (Harvard) introduces generalized stochastic systems—a broad mathematical framework encompassing Markov chains and random dynamical systems—and proves a stochastic-quantum theorem establishing a precise correspondence between any such system and a unitarily evolving quantum system. This yields a new formulation of quantum theory (alongside Hilbert-space, path-integral, and quasiprobability formulations) and provides first-principles explanations for why quantum mechanics uses complex numbers, Hilbert spaces, linear-unitary evolution, and the Born rule. The correspondence also suggests that quantum computers could simulate any generalized stochastic process.

**Content extract (≤6k chars):**

```
The Stochastic-Quantum Theorem
Jacob A. Barandes 1, ∗
1 Jefferson Physical Laboratory, Harvard University, Cambridge, MA 02138
(Dated: September 7, 2023)
This paper introduces several new classes of mathematical structures that have close connections
with physics and with the theory of dynamical systems. The most general of these structures,
called generalized stochastic systems, collectively encompass many important kinds of stochastic
processes, including Markov chains and random dynamical systems. This paper then states and
proves a new theorem that establishes a precise correspondence between any generalized stochastic
system and a unitarily evolving quantum system. This theorem therefore leads to a new formulation
of quantum theory, alongside the Hilbert-space, path-integral, and quasiprobability formulations.
The theorem also provides a first-principles explanation for why quantum systems are based on the
complex numbers, Hilbert spaces, linear-unitary time evolution, and the Born rule. In addition,
the theorem suggests that by selecting a suitable Hilbert space, together with an appropriate choice
of unitary evolution, one can simulate any generalized stochastic system on a quantum computer,
thereby potentially opening up an extensive set of novel applications for quantum computing.
cluding Hilbert spaces over the complex numbers, linear-
unitary evolution, and the Born rule.
Seen from another point of view, this stochastic-
I. INTRODUCTION quantum correspondence yields an alternative way to for-
mulate quantum theory, in the language of trajectories
In the development of physical theories, it sometimes unfolding stochastically in configuration spaces. This
turns out that existing definitions are too conceptually alternative formulation is distinct from the traditional
limiting, and that more flexible definitions are needed. Hilbert-space formulation [4, 5], the path-integral formu-
Working with more flexible definitions at a higher level of lation [6–8], and the quasi-probability formulation [9, 10].
abstraction or generality may make it easier to discover From a more practical perspective, turning this
new connections or prove new theorems, which would stochastic-quantum correspondence around suggests that
then also apply down at the lower level of the original unitarily evolving quantum systems can be put to work
definitions. simulating a very broad class of non-Markovian stochas-
This paper will argue that by appropriately generaliz- tic processes, thereby potentially opening up an extensive
ing standard definitions of dynamical systems, one can suite of new applications for quantum computers.
obtain novel classes of mathematical structures that en- Section II begins by defining deterministic generaliza-
compass an extensive array of physically important mod- tions of dynamical systems, followed by the introduction
els. As with a traditionally defined dynamical system, of important distinctions between indivisible , divisible ,
each such mathematical structure describes a physical and Markovian dynamics. Section III provides a gener-
system moving deterministically or stochastically along alized definition of a system with stochastic laws, shows
some trajectory in a configuration space, albeit with a how to represent such a generalized stochastic system
more general set of laws than according to standard def- in the formalism of linear algebra, describes connections
initions. (For pedagogical treatments of the standard between this work and the existing research literature,
theory of dynamical systems, see, for instance, [1–3].) defines the relationship between a composite system and
This paper also states and proves a new theorem show- its subsystems, and introduces the crucial notion of a
arXiv:2309.03085v1 [quant-ph] 3 Sep 2023
ing that despite being based on trajectories in configu- unistochastic system . Section IV states the stochastic-
ration spaces, the newly introduced class of generalized quantum theorem, whose proof is this paper’s primary
stochastic systems actually includes all quantum systems. goal, and then discusses some important corollaries and
As a consequence, this stochastic-quantum theorem of- provides a simple example of the theorem in practice.
fers a more conceptually transparent way to understand Section V lays out the theorem’s proof, which entails ex-
quantum systems, with superpositions no longer regarded plicitly constructing the claimed correspondence between
as literal blends of physical states. The theorem also pro- stochastic systems and quantum systems along the way.
vides a first-principles explanation for features of quan- Section VI concludes the paper with a brief discussion of
tum theory that are usually taken to be axiomatic, in- future work.
∗ jacob barandes@harvard.edu
2
II. DETERMINISTIC SYSTEMS that will be called the system’s dynamical map .
This dynamical map f takes as inputs any state
A. Generalized Dynamical Systems i and any time t , and outputs a state f ( i, t ) ∈ X :
i, t  7 → f ( i, t ) ∈ X [for all i ∈ X , t ∈ T ] . (3)
Dynamical systems are abstract mathematical struc-
tures that usefully model many deterministic physical
processes. According to the standard definition [1–3], • Fixing the time t turns f into a time-dependent
a dynamical system consists of a map representing some dynamical map
kind of evolution law that can be repeatedly applied to
the elements of some set of states. A dynamical system f t : X → X (4)
is usually assumed to be divisible , in the sense that one
can ‘divide up’ its evolution law over any time duration defined by
into well-defined evolution laws that describe intermedi-
i  7 → f
ate time durations. The more general case would be an t ( i ) ≡ f ( i, t ) [for all i ∈ X ] . (5)
indivisible dynamical system that might lack this feature.
The terms ‘divisible’ and ‘indivisible’ for dynamical • Without any important loss of generality, the set
laws are remarkably new. The terminology appears to of t
```

## candidate-16 [atlas-general] — UNCONSUMED

**Title:** Local positivity of ample line bundles

**URL:** file:///c27503d4c90c3240f961a3d80e25a4ebbd42c68d0ed7824997244203b37562fb/Local_positivity_of_ample_line_bundles.pdf

**Description:** A research paper in the Journal of Differential Geometry establishing lower bounds on Seshadri constants that measure the local positivity of ample line bundles at general points of complex projective varieties of arbitrary dimension. The authors prove that for a nef and big line bundle L on an n-dimensional irreducible projective variety, ε(L,x) ≥ 1/n at very general points, using a novel differentiation lemma for families of divisors inspired by techniques from diophantine approximation and boundedness arguments for Fano manifolds.

**Content extract (≤6k chars):**

```
J.DIFFERENTIAL GEOMETRY
Vol. 42, No.2 September, 1995
LOCAL POSITIVITY OF AMPLE LINE BUNDLES
LAWRENCE EIN, OLIVER KUCHLE & ROBERT LAZARSFELD
Introduction
The purpose of this paper is to establish a lower bound on the Se-
shadri constants measuring the local positivity of an ample line bundle
at a general point of a complex projective variety of arbitrary dimen-
sion.
Let X be an irreducible complex projective variety, and let L be a
nef line bundle on X. Demailly [6] has introduced a very interesting
invariant which in effect measures how positive L is locally near a given
smooth point x G X. This Seshadri constant e(L,x) £ R may be
defined as follows. Consider the blowing up
ι
of X at x, and denote by E = f~ (x) C Y the exceptional divisor.
Then f*L is a nef line bundle on Y, and we put
e(L, x) = sup {e > 0 | f*L - e E is nef } .
Here f*L — eE is considered as an R-divisor on Y, and to say that it
is nef means simply that f*L C" > eE C for every irreducible curve
C C Y. For example, if L is very ample, then e(L,x) > 1 for every
smooth point x G X. Seshadri's criterion (cf. [10 (Chapter 1)]) states
that L is ample if and only if there is a positive number e > 0 such
that e(L,rr) > e for every x £ X. We refer to Section 1 below, as well
as [6 (§6)], for alternative characterizations and further properties of
Seshadri constants.
Received August 15, 1994, and, in revised form, November 8, 1994. The first
author was partially supported by NSF Grant DMS 93-02512, the second author was
supported by Deutsche Forschungsgemeinschaft, and the third author was partially
supported by NSF Grant DMS 94-00815.
193
194 L. EIN, O. KUCHLE & R. LAZARSFELD
It was shown by an elementary argument in [7] that if S is a smooth
projective surface, and L is an ample line bundle on S, then e(L, x) > 1
for all except perhaps countably many x G S. This suggested the
somewhat surprising possibility that there could be a similar lower
bound on the local positivity of an ample line bundle at a general
point of an irreducible projective variety of any dimension. Our main
result shows that this is indeed the case:
Theorem 1. Let L be a nef and big line bundle on an irreducible
projective variety X of dimension n. Then
e(L,x) > -
for all x G X outside a countable union of proper closed subvarieties of
X. Moreover given any δ > 0 the locus
L x)>
ex « > άδ}
contains a Zariski-open dense set.
More generally, we prove that if there exists a countable union B C X
of proper closed subvarieties, plus a real number α > 0 such that for
1 < r < n:
r r 
Cι(L) > (r a) V r-dimensional Y CX with Y (£_
L
then e(L,x) > a for all sufficiently general x G X. Examples con-
structed by Miranda show that given any b > 0, there exist X, L and x
such that 0 < e(L, x) < b. In other words, there cannot be a bound (in-
dependent of X and L) that holds at every point. On the other hand,
it is unlikely that the particular constant appearing in Theorem 1 is
optimal. In fact, it is natural to conjecture that in the setting of the
Theorem one should have e(L,x) > 1 for a very general point x G X.
Recent interest in Seshadri constants stems in part from the fact that
they govern an elementary method for producing sections of adjoint
bundles. Our bounds then imply the following, which complements the
non-vanishing theorems of Kollar ([12 (§3)]):
Corollary 2. Let L be a nef line bundle on a smooth projective
variety X of dimension n > 2, and given an integer s > 0 suppose that
L
LOCAL POSITIVITY OF AMPLE LINE BUNDLES 195
for every r-dimensional subvariety Y C X not contained in some fixed
countable union B C X of proper subvarieties. Then the adjoint series
\Oχ(K x + L)\ generates s-jets at a general point x E X, i.e., the
evaluation map
s +1
H°(X, O X (K X + D) —>• H°(X,O X (K X + L)® O x /l x )
is surjective. In particular.
2
It follows for example that if A is ample, then Oχ(K x + (ns + n )A)
generates s-jets at almost all points x G l . We remark that contrary to
what one might expect from extrapolating the well-known conjectures
of Pujita [9] on global generation and very ampleness, there cannot exist
a linear function f(s) (depending on n, but independent of X and A)
such that Oχ(K x + f{s)A) generates s-jets for s » 0 at every point of
X (Remark 1.7).
Similarly, we have
Corollary 3. Suppose that L is a nef and big line bundle on a
2
smooth protective variety X of dimension n > 2. Then for all m > 2n ,
1
the linear series \K x +mL\ is very big , i.e., the corresponding rational
map
Φ\K x +mL\ : X — > P
maps X birationally onto its image.
For example, suppose that X is a smooth minimal variety of general
type, i.e., K x is nef and big. Then the pluricanonical rational maps
Φ\mκ\ : X —> P
2
are birational onto their images for m > 2n . This extends (with
somewhat weaker numbers) the results of Ando [1] in the cases n < 5.
More generally, if X is a general type minimal n-fold of global index
2
r, then \mrKχ\ is again very big when m > 2n (Corollary 4.6). As
lr Γhis terminology was suggested by Kollar to replace what used to be known as
"birationally very ample"
196 L. EIN, O. KUCHLE & R. LAZARSFELD
above, one also has an analogue of Corollary 3 for the linear series
\K X + L\ involving intersection numbers of L with subvarieties of X.
The proof of Theorem 1 draws inspiration from two sources: first,
the arguments used in [17], [4] and [14] to prove boundedness of Fano
manifolds of Picard number one; and secondly, some of the geometric
ideas occuring in [3], [18] and especialy [8]. Roughly speaking, if The-
orem 1 fails, then given a general point x E X there exists a curve
C x C X through x such that
mxύt x (C x ) ^
We start by fixing a divisor E x E \kL\ for k » 0 with suitably large
multiplicity at x. If one could arrange that C x <£. E x , then one arrives
right away at a contradiction by estimating E x C x in terms of mul-
tiplicities at x. Unfortunately it does not seem to be immediate that
one can do so. Instead, we use a gap construction to show
```

## candidate-17 [atlas-general] — UNCONSUMED

**Title:** Simple and Principled Uncertainty Estimation with Deterministic Deepn Learning v

**URL:** file:///e9a13befeff28d10bb227a8ac1c5b5394848257e56fe43d6ab611d5dbc1d7845/Simple_and_Principled_Uncertainty_Estimation_with_Deterministic_Deepn_Learning_v.pdf

**Description:** This NeurIPS 2020 paper proposes Spectral-normalized Neural Gaussian Process (SNGP), a deterministic single-model approach to uncertainty estimation that achieves quality competitive with deep ensembles. The authors formalize uncertainty quantification as a minimax learning problem and identify distance awareness—the model's ability to quantify how far a test example is from the training manifold—as a necessary condition for optimal uncertainty. SNGP enforces this via spectral normalization of hidden layers combined with a Gaussian Process output layer approximated through random features and Laplace approximation.

**Content extract (≤6k chars):**

```
Simple and Principled Uncertainty Estimation with
Deterministic Deep Learning via Distance Awareness
Jeremiah Zhe Liu ∗ Zi Lin † Shreyas Padhy †
Google Research & Harvard University Google Research Google Research
jereliu@google.com lzi@google.com shreyaspadhy@google.com
Dustin Tran Tania Bedrax-Weiss Balaji Lakshminarayanan
Google Research Google Research Google Research
trandustin@google.com tbedrax@google.com balajiln@google.com
Abstract
Bayesian neural networks and deep ensembles are principled approaches to esti-
mate the predictive uncertainty of a deep learning model. However their practicality
in real-time, industrial-scale applications are limited due to their heavy memory
and inference cost. This motivates us to study principled approaches to high-quality
uncertainty estimation that require only a single deep neural network (DNN). By
formalizing the uncertainty quantification as a minimax learning problem, we first
identify distance awareness , i.e., the model’s ability to properly quantify the dis-
tance of a testing example from the training data manifold, as a necessary condition
for a DNN to achieve high-quality (i.e., minimax optimal) uncertainty estimation.
We then propose Spectral-normalized Neural Gaussian Process (SNGP) , a simple
method that improves the distance-awareness ability of modern DNNs, by adding
a weight normalization step during training and replacing the output layer with a
Gaussian Process. On a suite of vision and language understanding tasks and on
modern architectures (Wide-ResNet and BERT), SNGP is competitive with deep
ensembles in prediction, calibration and out-of-domain detection, and outperforms
the other single-model approaches. 3
1 Introduction
Efficient methods that reliably quantify a deep neural network (DNN)’s predictive uncertainty
are important for industrial-scale, real-world applications, which include examples such as object
arXiv:2006.10108v2 [cs.LG] 26 Oct 2020 recognition in autonomous driving [ 22 ], ad click prediction in online advertising [ 76 ], and intent
understanding in a conversational system [ 84 ]. For example, for a natural language understanding
(NLU) model built for a domain-specific chatbot service (e.g, weather inquiry), the user’s input
utterance to the model can be of any topic, and the model needs to understand reliably and in real-time
whether to abstain or to trigger one of its known APIs.
When deep classifiers make predictions on input examples that are far from the support of the training
set, their performance can be arbitrarily bad [ 4 , 14 ]. This motivates the need for methods that are
aware of the distance between an input test example and previously seen training examples, so they
can return a uniform (i.e., maximum entropy) distribution over output labels if the input is too far
from the training set (i.e., the input is out-of-domain) [ 30 ]. Gaussian processes (GPs) with suitable
kernels enjoy such a property. However, to apply Gaussian processes to a high-dimensional machine
∗ Work done at Google Research.
† Work done as an Google AI Resident.
3 Code available at https://github . com/google/uncertainty-baselines/tree/master/baselines .
34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada.
learning problem, it is usually necessary to perform some form of feature extraction or dimensionality
reduction using a DNN. Ideally, the hidden representation of a DNN should reflect a meaningful
distance in the data manifold (e.g., the semantic textual similarity between two sentences), such that
this “distance aware” property is preserved. However, as we will show in the experiments, this is
often not guaranteed for common deep learning models (cf. Figure 1).
(a) Gaussian Process (b) Deep Ensemble (c) MC Dropout (d) DNN-GP (e) SNGP (Ours)
(f) Gaussian Process (g) Deep Ensemble (h) MC Dropout (i) DNN-GP (j) SNGP (Ours)
Figure 1: The uncertainty surface of a GP and different DNN approaches on the two ovals (Top Row) and
two moons (Bottom Row) 2D classification benchmarks. SNGP is the only DNN-based approach achieving a
distance-aware uncertainty similar to the gold-standard GP. Training data for positive ( Orange ) and negative
classes ( Blue ). OOD data ( Red ) not observed during training. Background color represents the estimated model
uncertainty (See 1e and 1j for color map). See Section 5.1 for details.
We propose a simple solution to this problem, namely adding spectral normalization to the weights
in each (residual) layer [ 54 ]. We refer to our method as ”Spectral-normalized Neural Gaussian
Processes” (SNGP). We show that this provides bounds on || h ( x ) − h ( x ′ ) || H relative to || x − x ′ || X ,
where x and x ′ are two inputs, h ( x ) is a deep feature extractor, and || . || X a semantically meaningful
distance for the data manifold. We can then safely pass h ( x ) into a distance-aware GP output layer.
To ensure computational scalability, we approximate the GP posterior using a Laplace approximation
to the random feature expansion of the GP, which gives rise to a model posterior that can be learned
scalably and in closed-form with minimal modification to the training pipeline of a deterministic
DNN, and allows us to efficiently compute the predictive uncertainty on a per-input basis without
Monte Carlo sampling.
In the rest of this paper, we first theoretically motivate the importance of distance awareness for
a model’s ability uncertainty estimation by studying it as a minimax learning problem (Section
2). We then introduce our SNGP method in detail in Section 3, and experimentally evaluate its
performance against other single-model approaches as well as deep ensembles in Section 5 [ 42 ].
On two challenging real world problems, namely image classification (using a Wide Resnet model
on CIFAR-10 and CIFAR-100) and conversational intent understanding (using a BERT model on
CLINC out-of-scope (OOS) intent dataset), we show that the SNGP method attains an uncerta
```

## candidate-18 [atlas-general] — UNCONSUMED

**Title:** ssrn 6630259

**URL:** file:///6b4de193c8036d42bcb199d6034233984538cafdbf7241b3c1db6d29f30b73e4/ssrn-6630259.pdf

**Description:** Research paper arguing that the Black-Scholes-Merton formula is the flat limit of an information-geometric pricing framework, exact on a one-dimensional sub-manifold of return distributions. The author proves two theorems placing BSM on the σ=σ₀ locus of the Gaussian Fisher manifold and identifies the volatility smile with curvature of an extended manifold incorporating leverage correlation, yielding a closed-form smile expression with bifurcation locus |ρ|=√(2/3). Empirical validation on 22 years of SPY/VIX data and SPY LEAPS predicts skew within 19% of observation with no parameters fitted to the options panel.

**Content extract (≤6k chars):**

```
Black-Scholes-Merton as the Flat Limit of Information Geometry
Bruce H. Dean, Ph.D.
ORCID: 0009-0008-8153-3269
symplectic.research@gmail.com
Supporting NASA’s Habitable Worlds Observatory (HWO) mission development under contract.
April 2026 (Draft v0.18)
Abstract. The Black-Scholes-Merton formula occupies a peculiar position in derivative pricing. It
is universally acknowledged to misprice options away from short maturity and at-the-money, yet it is
irreplaceable as the coordinate system through which implied volatilities are communicated. This paper
argues that the formula’s anomalous status has a single geometric explanation: BSM is the flat limit of an
information-geometric pricing framework, exact on a one-dimensional sub-manifold of the space of return
distributions and approximately accurate within a calculable neighbourhood of it. The volatility smile is
what the pricing problem records when the state of the market wanders off this flat slice into the curved
region around it.
Three results give the picture analytic content. Theorem 1 places BSM on the locus σ = σ 0 of the Gaussian
Fisher manifold and shows that the restriction is self-consistent precisely when ν 2 T ≪ σ 2
0 , a condition that
simultaneously locates where BSM works (short-dated, at-the-money) and where it breaks (long-dated, deep
out-of-the-money). Theorem 2 then identifies the smile with the curvature of an extended manifold that
incorporates the leverage correlation ρ between price and volatility; on this manifold the scalar curvature is
constant at R = − 2 and the leading smile reads
σ impl ( K , T ) / σ ATM ( T ) = 1 + γ m + ( κ eff / 2 ) m 2 + O ( m 3 ) , m = log ( K / F ) ,
p
with γ = ρν / ( 2 σ 0 ) and κ eff = ( 2 − 3 ρ 2 )( ν / σ 0 ) 2 / 6 . The latter is positive for | ρ | < 2 / 3 ≈ 0 . 816 , a
bifurcation locus separating smile from frown in the leading-order shape, and resolves a sign paradox that has
haunted earlier information-geometric treatments. An empirical anchor on the SPY LEAPS panel completes
the picture: at parameters estimated from realized time-series alone, the framework predicts the LEAPS
skew within 19 percent of observation with no parameters fitted to the options panel, and predicts a small
positive LEAPS curvature consistent with the wide empirical scatter of LEAPS curvatures across maturities.
A phase-plane analysis on 22 years of SPY/VIX data confirms a stable attractor of the joint ( ν / σ 0 , ρ )
dynamics adjacent to the bifurcation locus, sharpening Theorem 2 into a dynamical-systems statement
about where the market state actually concentrates. Along the way the construction identifies the SABR
exponent β = 1 as a structural consequence of ˇ Cencov’s theorem rather than a phenomenological choice,
and locates the historical sign paradox in a confusion between the time-dependence of the heat kernel and
the strike-dependence of the smile. The same ˇ Cencov-Fisher manifold underlies the temporal dynamics of
equity markets analyzed in prior work [9], where the SDHO Pareto frontier R 2 = Ω 2 / ( 1 + Ω 2 ) characterizes
the time-direction structure; the present paper’s strike-direction analysis is its natural orthogonal counterpart
on the same geometric object.
1. Introduction
1.1 The Black-Scholes-Merton paradox
The Black-Scholes-Merton formula [1, 2] is, by any practical measure, the most influential equation in mathematical
finance. It is also wrong almost everywhere it is applied. Equity options away from the at-the-money strike are
mispriced by it, options far from expiry are mispriced by it, and yet practitioners have not abandoned it. They have
done something more interesting: they have turned it upside down. Rather than using BSM as a pricing model, they
use it as the coordinate system through which implied volatilities are quoted, calibrated, and traded. A SABR fit
[3] is a curve through implied vols, not prices. A Heston calibration [4] is reported as σ impl ( K , T ) . The Dupire
local-volatility surface [5] is, by construction, a function σ loc ( K , T ) obtained by inverting the BSM formula at every
strike.
This combination of empirical inadequacy and practical irreplaceability is unusual. A formula that is wrong
everywhere should not be the universal language of a market that trades trillions of dollars in options annually. The
fact that it is suggests that BSM is not in the interior of a calibration landscape but at a particular boundary of it: a
special location, accurate in a definable region around itself, distorted in a definable way as one moves away. The
questions this paper addresses are where that location is, when being there is an accurate approximation, and what
1
the observed smile measures when the pricing state has wandered off it.
1.2 Information geometry as the natural setting
These questions take a clean form in information geometry. The state of the market at any moment is naturally
represented not as a single point but as a probability distribution over future returns. The space of such distributions
is a manifold, and the question of which two distributions are “close” is answered, uniquely up to scale, by ˇ Cencov’s
theorem [6]: the Fisher information matrix is the only Riemannian metric on a parametric family that is invariant
under sufficient statistics. For the lognormal family with parameters ( μ , σ ) that BSM assumes, the Fisher metric
makes the parameter space a hyperbolic plane of constant curvature R = − 1 , a rescaling of the Poincaré half-plane.
This particular manifold has appeared before in the author’s prior work on equity-market dynamics [7, 8, 9],
where geodesic flow on it (augmented by a contact-geometric dissipation term) was shown to capture the temporal
dynamics of liquid markets; §2.4 records the structural connection. The natural expectation is that option pricing
on the same manifold should produce BSM on some distinguished sub-structure, with the smile as a geometric
signature of departure from it. The body of this paper makes t
```

## candidate-19 [atlas-general] — UNCONSUMED

**Title:** Cohomology theory for financial Statistical Mechanics

**URL:** file:///ea838d400f90e5219f1c8ff3e2bbb886dfdaf935567177764377542136b812da/Cohomology-theory-for-financial-_2020_Physica-A--Statistical-Mechanics-and-i.pdf

**Description:** A peer-reviewed research paper published in Physica A that applies Khovanov cohomology and knot topology from mathematical physics to model financial time series as figure-eight hyperbolic knotted structures. The authors define Chern–Simons currents from trader behavior interactions over Wilson loops and prove theorems establishing the existence of 8 market states and 16 physiology cones as the smallest subunits of market microstructure, linking market curvature to knot and link properties.

**Content extract (≤6k chars):**

```
Physica A 546 (2020) 122212
Contents lists available at ScienceDirect
Physica A
journal homepage: www.elsevier.com/locate/physa
Cohomology theory for financial time series
Kabin Kanjamapornkul a , b , Richard Pinčák c , d , Erik Bartoš e , ∗
a Department of Survey Engineering, Faculty of Engineering, Chulalongkorn University, Pathumwan, Bangkok 10330, Thailand
b Faculty of Information Technology, Asia-Pacific International University, 195 Moo 3 Muak Lek, 18180 Saraburi, Thailand
c Institute of Experimental Physics, Slovak Academy of Sciences, Watsonova 47, 043 53 Košice, Slovak Republic
d Bogoliubov Laboratory of Theoretical Physics, Joint Institute for Nuclear Research, 141980 Dubna, Moscow Region, Russia
e Institute of Physics, Slovak Academy of Sciences, Dúbravská cesta 9, 845 11 Bratislava, Slovak Republic
h i g h l i g h t s
• We propose Khovanov cohomology in financial time series data.
• We try to connect a psychology of trader with the quantum finances.
• We study time series topology and give new definitions for bid–ask spread.
• We provide the prove of existence of market eight states with knot and link properties.
a r t i c l e i n f o a b s t r a c t
Article history: Khovanov cohomology in time series data is used to model financial time in figure-eight
Received 4 July 2018 hyperbolic knotted time series. We defined Chern–Simons current from the interaction
Received in revised form 5 April 2019 of behavior of traders over Wilson loop with link eight states. We build a new path
Available online 12 August 2019 integral for the market phase transitions as Wilson loop between predictor and predic-
Keywords: tant paths in physiology of time series data. The obtained results are presented in the
Cohomology group form of proved theorems. In the first theorem, we prove the existences of Chern–Simons
Time series current in the bid–ask spread as arbitrage opportunity for market phase transition of
Knot the interaction of Yang–Mills behavior field of the trader. In the second theorem, we
Chern–Simons current prove the existence of market 8 states. As a consequence of the theorems, we classify
Yang–Mills the smallest subunit of market microstructure as 16 physiology cones according to all
General equilibrium possibilities of the future outcome of endpoint state in time series data. The financial
Wilson loop market movements for up and down directions with the curvature as link number are
obtain from a market phase transition with eigenvalue of new defined Dirac operator
for the financial market. The market curvature value appears as knot and link properties
in time series data.
© 2019 Elsevier B.V. All rights reserved.
1. Introduction
Econophysics is a source of new definitions [1] and laws of complex evolution [2] in economics [3]. The interaction
of differential geometry [4] and knot topology [5] give us the theory for hidden particles [6,7] through the evolution of
matter. In physics, the particle means undivided quantity with its unique properties of spinor field. The Pauli exclusion
principle use the spinor field as the classification tool for all particles like electron, proton and etc. By contrast, the
microeconomics use a preference in the utility function and production function to classify types of markets. The smallest
∗ Corresponding author.
E-mail addresses: kabinsky@hotmail.com (K. Kanjamapornkul), pincak@saske.sk (R. Pinčák), erik.bartos@savba.sk (E. Bartoš).
https://doi.org/10.1016/j.physa.2019.122212
0378-4371/ © 2019 Elsevier B.V. All rights reserved.
2 K. Kanjamapornkul, R. Pinčák and E. Bartoš / Physica A 546 (2020) 122212
undivided composition of the market is classified into two types, the supply subunit type and demand subunit type of
market in the general equilibrium model. The source of demand subunit in the financial market is a buying operation
with ask price in the order book. On the other side the order book is discretized with 8 or 16 types of transition states [8]
with 16 types of tick size appearing as a market phase transition. Naturally there arises the question why order book
submission is only with 8 ticks or 16 ticks size generating a bid–ask spread in the order book for every financial market?
The defect of microeconomics theory is no existence of the spinor field or the Pauli exclusion principle which is classifying
the market subunit types. If we take into account the spinor field with the help of sheave cohomology, we can unify the
microeconomics theory with the macroeconomics theory in the analogy with the unification of E 8 × E 8 theory of ghost field
in nature [9] with the existence of hidden demand and hidden supply in the dual double auction market. The instrument
to study financial time series is a cohomology theory [10] for financial time series, for both of these theories with the
application to measure the human activity,. Cohomology [11], first discovered in topology by Poincaré [12], can be used to
detect a source of hidden inductive chain and cochain of k
```

## candidate-20 [atlas-general] — UNCONSUMED

**Title:** arovas Zhang1992A

**URL:** file:///68b96086b07cfc6afd61f4200a468e01bfc6d0088f7f0e3e5059e2e106e6f5e6/arovas-Zhang1992A.pdf

**Description:** A 1992 theoretical physics paper by Daniel Arovas and Shou-Cheng Zhang on topological aspects of quantum Hall physics. The work develops effective field theory descriptions of fractional quantum Hall states and their excitations, connecting topological order to observable physical properties in two-dimensional electron systems.

**Content extract (≤6k chars):**

```

```

## candidate-21 [atlas-general] — UNCONSUMED

**Title:** s41467 019 09668 y

**URL:** file:///8c61dc9fa37a598528624c82f10895e32e9db32066b7301cad51576708880618/s41467-019-09668-y.pdf

**Description:** This Nature Communications article demonstrates experimentally that the Chern number—a topological index characterizing equilibrium quantum states—can be measured from far-from-equilibrium dynamics by tracking momentum-space vortex trajectories after a quantum quench. Using non-interacting fermionic atoms in a periodically driven optical lattice realizing a Haldane-type model, the authors measure the linking number of dynamical vortices and show it directly corresponds to the ground-state Chern number, enabling mapping of the topological phase diagram.

**Content extract (≤6k chars):**

```
ARTICLE
https://doi.org/10.1038/s41467-019-09668-y OPEN
Measuring topology from dynamics by obtaining
the Chern number from a linking number
Matthias Tarnowski 1,2 , F. Nur Ünal 3 , Nick Fläschner 1,2 , Benno S. Rem 1,2 , André Eckardt 3 ,
Klaus Sengstock 1,2,4 & Christof Weitenberg 1,2
Integer-valued topological indices, characterizing nonlocal properties of quantum states of
matter, are known to directly predict robust physical properties of equilibrium systems. The
1234567890():,; Chern number, e.g., determines the quantized Hall conductivity of an insulator. Using non-
interacting fermionic atoms in a periodically driven optical lattice, here we demonstrate
experimentally that the Chern number determines also the far-from-equilibrium dynamics of
a quantum system. Extending a respective proposal to Floquet systems, we measure the
linking number that characterizes the trajectories of momentum-space vortices emerging
after a strong quench. We observe that it directly corresponds to the ground-state Chern
number. This one-to-one relation between a dynamical and a static topological index allows
us to experimentally map out the phase diagram of our system. Furthermore, we measure the
instantaneous Chern number and show that it remains zero under the unitary dynamics.
1 Institut für Laserphysik, Universität Hamburg, 22761 Hamburg, Germany. 2 The Hamburg Centre for Ultrafast Imaging, 22761 Hamburg, Germany. 3 Max-
Planck-Institut für Physik komplexer Systeme, Nöthnitzer Straße 38, 01187 Dresden, Germany. 4 Zentrum für Optische Quantentechnologien, Universität
Hamburg, 22761 Hamburg, Germany. These authors contributed equally: Matthias Tarnowski, F. Nur Ünal. Correspondence and requests for materials
should be addressed to K.S. (email: klaus.sengstock@physnet.uni-hamburg.de)
NATURE COMMUNICATIONS | (2019) 10:1728 | https://doi.org/10.1038/s41467-019-09668-y | www.nature.com/naturecommunications 1
ARTICLE NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-09668-y
opological quantum matter has recently received much Here we experimentally investigate a fascinating connection
attention, because it constitutes an entirely new class of between the topological properties of the ground state and its far-
T quantum phases and has potential applications ranging from-equilibrium dynamics following a strong quench from a
from precision measurements to quantum information proces- topologically trivial system that was recently proposed in ref. 15 .
sing and spintronics 1 . These phases are characterized by the The state tomography reveals two kinds of vortices in momentum
absence of symmetry breaking and of a local order parameter and space: (i) static vortices indicating the Dirac points and (ii)
are therefore beyond the conventional classi fi cation of phase dynamical vortices, which appear and disappear in pairs and trace
transitions. Instead, they are characterized by integer topological out a closed contour 16 . Whether this contour encloses one of the
indices, which are topologically protected and can only change static vortices or not is a topological index (called linking num-
value at a gap closing. An important role is played by the Chern ber), which directly corresponds to the ground-state Chern
number, which characterizes the topology of fi lled bands in two- number of the post-quench Hamiltonian 15 (see Fig. 1). We
dimensional lattice systems. It captures the winding of the experimentally access this topological index for topologically
eigenstates and is de fi ned via the integral of the Berry curvature non-trivial systems. Furthermore, using this correspondence we
over the fi rst Brillouin zone. A band with non-zero Chern map out the phase diagram of a Floquet-engineered Haldane-type
number is topologically non-trivial. When the highest occupied lattice model, characterized by different Chern numbers. This
band is non-trivial and completely fi lled, the state is called a characterization constitutes a direct measurement of Chern
topological insulator. Non-zero Chern numbers are also at the numbers in the Haldane model. A similar approach for a spin-
origin of the integer Quantum Hall effect, which arises in two- orbit coupled band structure was recently demonstrated in ref. 17 .
dimensional systems subject to a strong perpendicular magnetic Finally, using the time-resolved state tomography of the time-
fi eld, and they are responsible for the perfect quantization of the evolved wave function, we show experimentally that the instan-
Hall conductance. Via the bulk-boundary correspondence prin- taneous Chern number remains indeed zero during the dynamics.
ciple, the Chern number of the bulk bands also dictates the
number of chiral conducting edge states, which lie in the band
gap and give rise to topologically protected transport. Results
Ultracold quantum gases are a promising experimental plat- Floquet description of the driven hexagonal lattice . We start
form to explore these effects. On the one hand, they allow for the with a hexagonal optical lattice 18 with two sublattices A and B ,
realization of topologically nontrivial band structures and arti fi - which are connected by nearest-neighbor (NN) tunneling matrix
cial gauge fi elds 2 – 9 and on the other hand typical time scales for elements J AB and have a potential offset of Δ AB (see Fig. 2). It is
dynamical studies are experimentally accessible. Example, para-
digmatic topological band models have been realized: the Hof-
stadter model describing a lattice with a net magnetic fl ux and the
Haldane model on the honeycomb lattice, which contains topo- a
logically non-trivial bands even in the absence of a net magnetic A
fl ux. Moreover, they offer the perspective of combining these
effects with strong interactions (see, e.g., refs. 10 – 12 ), which can be B B
tuned independently. In cold atom systems, the Chern number
was measured for the Hofstadter model 13 using transport mea-
surements and for the Haldane model using quantize
```

## candidate-22 [atlas-general] — UNCONSUMED

**Title:** Two Scale Optimization of Graded Lattice Structures respecting Buckling on Micro

**URL:** file:///3568070a2e332ce6737503c14943904535fd8d36f9ad4772a5245ec3f1cda0dd/Two-Scale_Optimization_of_Graded_Lattice_Structures_respecting_Buckling_on_Micro.pdf

**Description:** An academic paper presenting a two-scale topology optimization approach for graded lattice structures that simultaneously accounts for buckling instabilities on both microscopic and macroscopic scales. The method uses asymptotic homogenization to upscale elastic properties and local buckling behavior from parameterized unit cells, then employs a worst-case model for the homogenized buckling load factor as a safeguard against pure local buckling. The approach is validated on dehomogenized designs and is applicable to arbitrary parameterized microstructures, not just beam-like lattices with well-defined slenderness ratios.

**Content extract (≤6k chars):**

```
Two-Scale Optimization of Graded Lattice Structures
respecting Buckling on Micro- and Macroscale
Daniel H¨ ubner 1* , Fabian Wein 1 and Michael Stingl 1
1 Applied Mathematics, Continuous Optimization, Friedrich-Alexander Universit¨ at
Erlangen-N¨ urnberg, Cauerstr. 11, Erlangen, 91058, Germany.
*Corresponding author(s). E-mail(s): daniel.huebner@fau.de;
Contributing authors: fabian.wein@fau.de; michael.stingl@fau.de;
Abstract
Interest in components with detailed structures increased with the progress in advanced manu-
facturing techniques in recent years. Parts with graded lattice elements can provide interesting
mechanical, thermal, and acoustic properties compared to parts where only coarse features are
included. One of these improvements is better global buckling resistance of the component. How-
ever, thin features are prone to local buckling. Normally, analyses with high computational effort
are conducted on high-resolution finite element meshes to optimize parts with good global and local
stability. Until recently, works focused only on either global or local buckling behavior. We use
two-scale optimization based on asymptotic homogenization of elastic properties and local buck-
ling behavior to reduce the effort of full-scale analyses. For this, we present an approach for
concurrent local and global buckling optimization of parameterized graded lattice structures. It is
based on a worst-case model for the homogenized buckling load factor, which acts as a safeguard
against pure local buckling. Cross-modes residing on both scales are not detected. We support
our theory with numerical examples and validations on dehomogenized designs, which show the
capabilities of our method, and discuss the advantages and limitations of the worst-case model.
Keywords: structural optimization, instability, buckling, two-scale, cellular materials
arXiv:2303.08710v1 [cs.CE] 15 Mar 2023
1 Introduction Two-scale optimization (Wu et al. 2021) can
be used to design such structures without the need
The ongoing progress in additive manufacturing to resolve all the fine details of the full design
allows structures with fine details to gain increas- in a single setting. The idea of this approach
ing focus. Lattice structures in particular, both started with the work of Bendsøe and Kikuchi
homogeneous and graded, are utilized in many (1988), in which the design process is divided into
applications, e.g., thermal management, energy two scales: the macroscopic scale, which describes
absorption, noise reduction, biomedical engineer- the overall component, and the microscopic scale,
ing, etc. (Rahman et al. 2022). Lattice infill is also which shows the fine details. Bendsøe and Kikuchi
recognized as potentially increasing global buck- bridged the gap between these two scales by
ling resistance of a component (Clausen et al. asymptotic homogenization (Allaire et al. 1997).
2016). However, fine features are prone to local This technique yields approximate material prop-
buckling (Ferrari and Sigmund 2019). erties of microstructures on the macroscopic scale,
1
which can then be used in macroscopic con- (Larsen et al. 2018), penalization of intermedi-
stitutive equations. Choosing a parameterized ate values in the objective (Allaire and Francfort
microstructure, Bendsøe and Kikuchi were able 1993; Allaire and Kohn 1993), or element removal
to effectively decouple the scales: Prior to any strategies (Behrou et al. 2021; Dalklint et al. 2020;
optimization procedure a discrete subset of the Giele et al. 2021). Clustering of eigenvalues can
parameter space is chosen and homogenization is be prevented by enforcing gaps between the eigen-
conducted for each of the microstructures gained values (Bendsøe and Sigmund 2003). However, a
from this parameter set. The obtained properties large number of eigenvalues may still have to be
are then interpolated in the continuous param- computed to achieve good convergence (Bruyneel
eter space and the interpolated material model et al. 2008), which compels the use of efficient
can later be reused to solve various optimization eigenproblem solvers (Dunning et al. 2016; Ferrari
problems. This technique introduces an interpola- and Sigmund 2020). Nevertheless, topology opti-
tion error, but requires less computational effort mization with respect to buckling still currently
when compared with on the fly homogenization, poses a challenging problem.
i.e., homogenization performed for each finite ele- More recently, stability requirements have also
ment in the discretized design domain and for been employed when tailoring microstructures
each update step of the design during an iterative (Neves et al. 2002b,a; Thomsen et al. 2018; Ander-
optimization procedure. Moreover the interpola- sen et al. 2022), though models for the buckling
tion error can be controlled in a rather straight of periodic microstructures have been investigated
forward way during preprocessing. for decades. Homogenization theory for buck-
Though there is exhaustive literature on opti- ling load factors is well established (Neves et al.
mal design considering the buckling behavior of 2002b; Thomsen et al. 2018), but several chal-
structures using beam models (Ferrari and Sig- lenges still arise in this context. Buckling modes
mund (2019) and references therein), only a rela- can range from high-frequency modes with a wave-
tively small number of publications for continuum length shorter than the characteristic size of the
models exist. The initial problems evolved around microstructure to modes that span over multiple
finding optimal cross-sections for columns of fixed periods of the microstructure. Floquet-Bloch the-
length and weight subject to uniaxial compression ory can be used to capture the latter in particular
loads (Clausen 1851; Keller 1960; Tadjbakhsh and (Neves 2019).
Keller 1962; Huang and Sheu 1968; Khot et al. For dehomogenized designs scale effects stem-
1976). Neves et al. (1995) were the first to conduct 
```

## candidate-23 [atlas-general] — UNCONSUMED

**Title:** Learning Flat Latent Manifolds with VAEs

**URL:** file:///146da1644649a2d5b47b9c4bcb664519463c6af0c90bfc4cc7404a3432800397/Learning_Flat_Latent_Manifolds_with_VAEs.pdf

**Description:** This ICML 2020 paper proposes Flat Manifold VAEs (FMVAEs), which define the latent space of a variational autoencoder as a Riemannian manifold and regularize the metric tensor to be a scaled identity matrix, so that Euclidean distance in latent space becomes a faithful proxy for observation-space similarity. By combining a flexible hierarchical prior (VHP) with Jacobian regularization via constrained optimization, the method achieves near state-of-the-art performance on video tracking benchmarks using unsupervised learning while retaining the computational efficiency of straight-line distance computation.

**Content extract (≤6k chars):**

```
Learning Flat Latent Manifolds with VAEs
Nutan Chen 1 Alexej Klushyn 1 Francesco Ferroni 2 Justin Bayer 1 Patrick van der Smagt 1
Abstract function. Computer vision pipelines, e.g. tracking over time,
Measuring the similarity between data points of- perform matching based on similarity scores.
ten requires domain knowledge, which can in But designing a distance function can be challenging: it is
parts be compensated by relying on unsupervised not always obvious to write down mathematical formulae
methods such as latent-variable models, where that accurately express a notion of similarity. Learning such
similarity/distance is estimated in a more compact functions has hence been proven as a viable alternative to
latent space. Prevalent is the use of the Euclidean manual engineering in this respect (NCA (Goldberger et al.,
metric, which has the drawback of ignoring in- 2005), metric learning (Xing et al., 2003), etc.). Often, these
formation about similarity of data stored in the methods rely on the availability of pairs labelled as simi-
decoder, as captured by the framework of Rie- lar or dissimilar. A different route is that of exploiting the
mannian geometry. We propose an extension to structure that latent-variable models learn. The assumption
the framework of variational auto-encoders allows that a set of high-dimensional observations is explained by
learning flat latent manifolds , where the Euclidean points in a much simpler latent space underpins these ap-
metric is a proxy for the similarity between data proaches. In their respective probabilistic versions, a latent
points. This is achieved by defining the latent prior distribution is transformed non-linearly to give rise
space as a Riemannian manifold and by regularis- to a distribution of observations. The hope is that simple
ing the metric tensor to be a scaled identity matrix. distances, such as the Euclidean distance measured in la-
Additionally, we replace the compact prior typ- tent space, implement a function of similarity. Yet, these
ically used in variational auto-encoders with a approaches do not incorporate the variation of the obser-
recently presented, more expressive hierarchical vations with respect to the latent points. For example, the
one—and formulate the learning problem as a con- observations will vary much more when a path in latent
strained optimisation problem. We evaluate our space will cross a class boundary.
method on a range of data-sets, including a video-
tracking benchmark, where the performance of In fact, recent approaches to non-linear latent variable mod-
our unsupervised approach nears that of state-of- els, such as the generative adversarial network (Goodfellow
the-art supervised approaches, while retaining the et al., 2014) or the variational auto-encoder (VAE) (Kingma
computational efficiency of straight-line-based ap- & Welling, 2014; Rezende et al., 2014), regularise the latent
proaches. space to be compact, i.e. to remove low-density regions.
This is in contrast to the aforementioned hope that Euclidean
distances appropriately reflect similarity.
1. Introduction The above insight leads us to the development of flat mani-
Measuring the distance between data points is a central fold variational auto-encoders. This class of VAEs defines
arXiv:2002.04881v3 [stat.ML] 12 Aug 2020
ingredient of many data analysis and machine learning ap- the latent space as Riemannian manifold and regularises
plications. Several kernel methods (KernelPCA (Sch olkopf ¨ the Riemannian metric tensor to be a scaled identity matrix.
et al., 1997), KernelNMF (Li & Ding, 2006), etc.), and other In this context, a flat manifold is a Riemannian manifold,
non-parametric approaches such as k-nearest neighbours which is isometric to the Euclidean space. To not compro-
(Altman, 1992) rely on the availability of a suitable distance mise the expressiveness, we relax the compactness assump-
tion and make use of a recently introduced hierarchical prior
1 Machine Learning Research Lab, Volkswagen Group, (Klushyn et al., 2019). As a consequence, the model is capa-
Munich, Germany 2 Autonomous Intelligent Driving GmbH, ble of learning a latent representation, where the Euclidean
Munich, Germany. Correspondence to: Nutan Chen < nu- metric is a proxy for the similarity between data points. This
tan.chen@gmail.com > .
results in a computational efficient distance metric which is
Proceedings of the 37 th International Conference on Machine practical for applications in real-time scenarios.
Learning , Online, PMLR 119, 2020. Copyright 2020 by the au-
thor(s).
Learning Flat Latent Manifolds with VAEs
2. Variational Auto-Encoders with Flat et al., 2016; Sønderby et al., 2016). Klushyn et al. (2019)
Latent Manifolds follow the line of argument in (Rezende & Viola, 2018)
and reformulate the resulting ELBO as the Lagrangian of a
2.1. Background on Learning Hierarchical Priors constrained optimisation problem:
in VAEs
L VHP ( θ, φ, Θ , Φ; λ ) ≡
Latent-variable models are defined as ( [ ] )
∫ F ( φ, Θ , Φ) + λ E 2
p D ( x ) E q φ ( z | x ) C θ ( x , z ) − κ , (4)
p ( x ) = p ( x | z ) p ( z ) d z , (1) with the optimisation objective [ F ( φ, Θ ] ,  Φ) , the inequal-
ity constraint E 2
p D ( x ) E q φ ( z | x ) C θ ( x , z ) ≤ κ , and the
where z ∈ R N z represents latent variables and x ∈ R N x the Lagrange multiplier λ . C θ ( x , z ) is defined as the
observable data. The integral in Eq. (1) is usually intractable reconstruction-error-related term in − log p θ ( x | z ) . Thus,
but it can be approximated by maximising the evidence we obtain the following optimisation problem:
lower bound (ELBO) (Kingma & Welling, 2014; Rezende min min max min L
Θ , Φ VHP ( θ, φ, Θ , Φ; λ ) s.t. λ ≥ 0 . (5)
et al., 2014): θ λ φ 
[ ] [ [ ] Building on that, the authors propose an optimisation
E p D ( x ) log p θ ( x ) ≥ E p D ( x ) E q φ ( z | x ) log p θ ( x | z ) algorithm—including a λ -update scheme—to achieve a tight
( ) ] lower bound on the log-likeliho
```

## candidate-24 [atlas-general] — UNCONSUMED

**Title:** Structure preserving contrastive learning for spatial time series

**URL:** file:///f8e503131746533f753a80477d334211b2b197ff2ccd039061c7a83743c4da4f/Structure-preserving_contrastive_learning_for_spatial_time_series.pdf

**Description:** This research paper introduces two structure-preserving regularisers for contrastive learning of spatial time series: a topology-preserving regulariser for global-scale similarity and a graph-geometry-preserving regulariser for local-scale similarity. The authors propose a dynamic weighting mechanism to adaptively balance contrastive learning and structure preservation during training. Validated on multivariate time series classification and macroscopic/microscopic traffic prediction, the method improves state-of-the-art performance across all tasks while better preserving similarity structures in the latent space.

**Content extract (≤6k chars):**

```
Structure-preserving contrastive learning for spatial time series
Yiru Jiao a,c , Sander van Cranenburgh b,c , Simeon Calvert a,c , Hans van Lint a,c
a Department of Transport & Planning, Delft University of Technology, Delft, the Netherlands
b Department of Engineering Systems and Services, Delft University of Technology, Delft, the Netherlands
c CityAI lab, Delft University of Technology, Delft, the Netherlands
Abstract
Neural network models are increasingly applied in transportation research to tasks such as pre-
diction. The e ff ectiveness of these models largely relies on learning meaningful latent patterns
from data, where self-supervised learning of informative representations can enhance model per-
formance and generalisability. However, self-supervised representation learning for spatially char-
acterised time series, which are ubiquitous in transportation domain, poses unique challenges due
to the necessity of maintaining fine-grained spatio-temporal similarities in the latent space. In
this study, we introduce two structure-preserving regularisers for the contrastive learning of spa-
tial time series: one regulariser preserves the topology of similarities between instances, and the
other preserves the graph geometry of similarities across spatial and temporal dimensions. To
balance the contrastive learning objective and the need for structure preservation, we propose a
dynamic weighting mechanism that adaptively manages this trade-o ff and stabilises training. We
validate the proposed method through extensive experiments, including multivariate time series
classification to demonstrate its general applicability, as well as macroscopic and microscopic
tra ffi c prediction to highlight its particular usefulness in encoding tra ffi c interactions. Across all
tasks, our method preserves the similarity structures more e ff ectively and improves state-of-the-art
task performances. This method can be integrated with an arbitrary neural network model and is
particularly beneficial for time series data with spatial or geographical features. Furthermore, our
findings suggest that well-preserved similarity structures in the latent space indicate more infor-
mative and useful representations. This provides insights to design and optimise more e ff ective
neural networks for data-driven transportation research. Our code is made openly accessible with
all resulting data at https://github.com/yiru-jiao/spclt .
arXiv:2502.06380v5 [cs.LG] 26 Oct 2025
Keywords: Contrastive learning, representation learning, time series, spatio-temporal data, tra ffi c
interaction
Published in Artificial Intelligence for Transportation at https://doi.org/10.1016/j.ait.2025.100031
1. Introduction
Modern transportation systems create massive streams of spatially distributed time series data,
such as tra ffi c speeds across road networks and transit ridership through various locations over
time. Extracting useful patterns from these data is crucial, especially as neural network models are
increasingly used for a range of downstream tasks such as tra ffi c forecasting [1, 2], congestion de-
tection [3, 4], and mobility analysis [5, 6]. In recent years, self-supervised representation learning
(SSRL) has emerged as a promising approach to leverage such large-scale datasets [7]. By learn-
ing informative latent representations, SSRL can e ff ectively facilitate model performance [8, 9, 10]
and generalisability [11, 12] in downstream tasks. This advantage is especially valuable in trans-
portation research, where real-world sensor measurements and labels are often noisy or sparse.
In SSRL of time series, contrastive learning is becoming the mainstay technique. This adop-
tion is supported by empirical investigation. In 2022, Lafabregue et al. [13] conducted an exten-
sive experimental comparison over 300 combinations of network architectures and loss functions
to evaluate the performance of time series representation learning. One of their key findings is
that the reconstruction loss used by traditional autoencoders does not su ffi ciently fit temporal pat-
terns. Instead, contrastive learning has emerged as a more e ff ective approach, which explicitly
pulls similar instances closer and pushes dissimilar instances farther apart in the latent space of
representations [14, 15]. This mechanism encourages neural networks to organise the latent space
according to the inherent similarities in data, yielding representations that capture meaningful pat-
terns.
Unique challenges arise when learning contrastive representations for spatially characterised
time series data. A foremost di ffi culty is the need to preserve fine-grained similarity structures
among data instances in the latent space. The notion of similarity for spatial time series can be
subtle and highly domain-specific. For example, financial time series may be considered similar
even if some variables show significant divergence, while movement traces with very di ff erent
spatial features can be anything but similar. Beyond preserving fine-grained similarities, spatially
characterised time series such as tra ffi c interactions can involve multiple scales of spatio-temporal
patterns. At the macroscopic scale, tra ffi c flow measures collective road usage evolving over the
road network; at the microscopic scale, trajectories describe the motion dynamics of individual
road users such as car drivers, cyclists, and pedestrians, in local road space. SSRL for spatial
time series must accommodate such heterogeneity, capturing patterns at the appropriate level of
granularity for the targeted task.
To address these challenges, this study explores contrastive learning regularised by structure
preservation to better capture the subtle similarities in spatial time series data. We introduce
two regularisers at di ff erent scales to preserve the original similarity structure in the latent space.
One is a topology-preserving regulariser for the global scale, and the other is a 
```

## candidate-25 [atlas-general] — UNCONSUMED

**Title:** The bottleneck degree of algebraic varieties

**URL:** file:///a6d0741f8ca6e5f33c2c98d0de852902042ff20c91164cd575c49a6de8a5d87f/The_bottleneck_degree_of_algebraic_varieties.pdf

**Description:** This research paper introduces and studies the bottleneck degree of smooth algebraic varieties, defined as the number of pairs of distinct points where the connecting line is normal to the variety at both points. The authors derive closed formulas for the bottleneck degree in terms of classical algebraic invariants—Chern classes and polar classes—providing explicit results in low dimensions and a general algorithm. The work is motivated by applications to computing the reach of manifolds, which is fundamental to manifold reconstruction, persistent homology, and dimensionality reduction in data science.

**Content extract (≤6k chars):**

```
THE BOTTLENECK DEGREE OF ALGEBRAIC VARIETIES
SANDRA DI ROCCO, DAVID EKLUND, AND MADELEINE WEINSTEIN
A BSTRACT . A bottleneck of a smooth algebraic variety X ⊂ C n is a pair ( x , y ) of distinct points x , y ∈ X such
that the Euclidean normal spaces at x and y contain the line spanned by x and y . The narrowness of bottlenecks
is a fundamental complexity measure in the algebraic geometry of data. In this paper we study the number of
bottlenecks of affine and projective varieties, which we call the bottleneck degree . The bottleneck degree is a
measure of the complexity of computing all bottlenecks of an algebraic variety, using for example numerical
homotopy methods. We show that the bottleneck degree is a function of classical invariants such as Chern
classes and polar classes. We give the formula explicitly in low dimension and provide an algorithm to compute
it in the general case.
1. I NTRODUCTION
In this paper we study geometric properties of algebraic varieties with applications to computational data
science. Let f 1 , . . . , f k ∈ R [ x 1 , . . . , x n ] be polynomials. The associated algebraic variety is the zero-set X ⊂ R n
given by X = { x ∈ R n : f 1 ( x ) = · · · = f k ( x ) = 0 } . Polynomial systems of equations arise in applications to
natural science, engineering, computer science and beyond. Examples include kinematics [54], economics
[44], chemistry [46], computer vision [41], machine learning [45] and optimization [43]. Polynomial systems
can be analyzed naturally through the machinery of algebraic geometry. In the present study we concentrate
on computing and counting so-called bottlenecks of an algebraic variety X ⊂ R n . This is the study of lines
in R n orthogonal to X at two or more points. Such lines contribute to the computation of the reach , see
Section 1.2, and may be found by solving a polynomial system (3). To be able to use the appropriate tools
from algebraic geometry we often have to move from the real numbers to the algebraically closed field
of complex numbers C , as we illustrate below. We will see that classical invariants such as polar classes
appear naturally and turn out to be essential to obtaining a closed formula for the number of bottlenecks. In
our opinion this work provides yet one more illustration that classical algebraic geometry and in particular
intersection theory are useful and often necessary in applications such as data science.
1.1. Bottlenecks and optimization. Finding lines orthogonal at two or more points is an optimization prob-
lem with algebraic constraints. The focus of this paper is to determine, or bound, the number of solutions to
this optimization problem.
Example 1.1. Consider the ellipse C ⊂ R 2 defined by f = x 2 + y 2 / 2 − 1 = 0. A bottleneck on C is a pair
arXiv:1904.04502v3 [math.AG] 2 Nov 2019
of points p , q ∈ C that span a line orthogonal to C at both points. The only such lines are the x -axis and the
y -axis, that is the principal axes of the ellipse, see Figure 1. A line l is orthogonal to C at a point p ∈ C if l
is orthogonal to the tangent line T p C at p . In other words l is the normal line N p X at p . The direction of the
normal line is given by the gradient ∇ f = ( 2 x , y ) . Consider a pair of points p = ( x , y ) ∈ C and q = ( z , w ) ∈ C .
The claim that ( p , q ) is a bottleneck may then be expressed as
x − z = λ 2 x ,
y − w = λ y ,
x − z = μ 2 z ,
y − w = μ w ,
2010 Mathematics Subject Classification. 14Q20, 62-07, 68Q32, 65D18.
Key words and phrases. bottlenecks of varieties, algebraic geometry of data, reach of algebraic manifolds.
1
2 SANDRA DI ROCCO, DAVID EKLUND, AND MADELEINE WEINSTEIN
C 
T p C T q C
p q
F IGURE 1. An ellipse with tangent lines and principal axes.
for some λ , μ ∈ R . These equations, together with x 2 + y 2 / 2 = 1 and z 2 + w 2 / 2 = 1, constitute a polynomial
system for computing bottlenecks on the curve C . Note that this is also the system we get if we apply the
Lagrange multiplier method to the problem of optimizing the squared distance function ( x − z ) 2 + ( y − w ) 2
subject to the constraints x 2 + y 2 / 2 − 1 = z 2 + w 2 / 2 − 1 = 0. This is thus an optimization problem and we
are asking for the critical points of the distance between pairs of points on C .
Consider again an arbitrary variety X ⊂ R n . For convenience, we will restrict to the case where X is
smooth , that is every point of X is a manifold point. A line is orthogonal to X if it is orthogonal to the tangent
space T x X ⊂ R n at x .
Definition 1.2. Let X ⊂ R n be a smooth variety. The bottlenecks of X are pairs ( x , y ) of distinct points
x , y ∈ X such that the line spanned by x and y is normal to X at both points.
Equivalently one can define bottlenecks as the critical points of the squared distance function
(1) R n × R n : ( x , y )  7 → || x − y || 2 ,
subject to the constraints x , y ∈ X as well as the non-triviality condition x  6 = y .
( A ) ( B )
F IGURE 2. Two curves and their bottlenecks.
Example 1.3. Figure 2a shows a quartic curve in R 2 and its 22 bottleneck lines. The curve is defined by
x 4 + y 4 + 1 − 4 y − x 2 y 2 − 4 x 2 − x − 2 y 2 = 0. The figure was produced by Paul Breiding and Sascha Timme
using the Julia package HomotopyContinuation.jl [17].
As another example consider the space curve in R 3 defined by
x 3 − 3 xy 2 − z = 0 ,
x 2 + y 2 + 3 z 2 − 1 = 0 .
Figure 2b shows this curve and its 24 bottleneck lines.
THE BOTTLENECK DEGREE OF ALGEBRAIC VARIETIES 3
( A ) Connected components ( B ) Sampling of a torus
F IGURE 3
1.2. Motivation. The geometry of bottlenecks plays an important role in several aspects of real geometry in
connection with analysis of data with support on an algebraic variety. Let X R ⊂ R n be a smooth variety which
is non-empty and compact. An interesting observation is that the distance between any two distinct connected
components of X R is realized by || x − y || for some bottleneck ( x , y ) with one point on each component. See
Figure 3 for an illustra
```

## candidate-26 [atlas-general] — UNCONSUMED

**Title:** Optimizing Neural Networks via Koopman Operator Theory

**URL:** file:///0e846120d5d0ff056254414c8bc73d293d6176b9a471c4a367b1f9b6e8b535a8/Optimizing_Neural_Networks_via_Koopman_Operator_Theory.pdf

**Description:** A NeurIPS 2020 research paper that applies Koopman operator theory — a linear framework for nonlinear dynamical systems — to neural network training by treating weight/bias evolution as a discrete dynamical system. The authors demonstrate that approximating the Koopman operator via the finite section method enables accurate prediction of weight trajectories over non-trivial training intervals, achieving >10x speedup over gradient descent methods (Adam, Adadelta, Adagrad) on feedforward networks including an NN differential equation solver and an MNIST classifier.

**Content extract (≤6k chars):**

```
Optimizing Neural Networks via Koopman Operator
Theory
Akshunna S. Dogra ∗ William T. Redman ∗
John A. Paulson School of Interdeparmental Graduate Program in
Engineering and Applied Sciences Dynamical Neuroscience
Harvard University University of California, Santa Barbara
Cambridge, MA 02138, Santa Barbara, CA 93106
asdpsn@gmail.com wredman@ucsb.edu
Abstract
Koopman operator theory, a powerful framework for discovering the underlying
dynamics of nonlinear dynamical systems, was recently shown to be intimately
connected with neural network training. In this work, we take the first steps in
making use of this connection. As Koopman operator theory is a linear theory,
a successful implementation of it in evolving network weights and biases offers
the promise of accelerated training, especially in the context of deep networks,
where optimization is inherently a non-convex problem. We show that Koopman
operator theoretic methods allow for accurate predictions of weights and biases of
feedforward, fully connected deep networks over a non-trivial range of training
time. During this window, we find that our approach is >10x faster than various
gradient descent based methods (e.g. Adam, Adadelta, Adagrad), in line with
our complexity analysis. We end by highlighting open questions in this exciting
intersection between dynamical systems and neural network theory. We highlight
additional methods by which our results could be expanded to broader classes of
networks and larger training intervals, which shall be the focus of future work.
1 Introduction
Despite their black box nature, the training of artificial neural networks (NNs) is a discrete dynamical
system. During training, weights/biases evolve along a trajectory in an abstract weight/bias space, the
path determined by the implemented optimization algorithm, the training data, and the architecture.
arXiv:2006.02361v3 [cs.NE] 22 Oct 2020 This dynamical systems picture is familiar: many introductions to optimization algorithms, such as
gradient descent (GD), visualize training as a process where weights/biases change iteratively under
the influence of the loss landscape. Yet, while dynamical systems theory has provided insight into the
behavior of many complex systems, its application to NNs has been limited.
Recent advances in Koopman operator theory (KOT) have made it a powerful tool in studying the
underlying dynamics of nonlinear systems in a data-driven manner [1–8]. This begs the question, can
KOT be used to learn and predict the dynamics present in NN training? If so, can such an approach,
which we call Koopman training , afford us benefits that traditional NN training approaches, like
backpropagation, cannot? This viewpoint was recently proposed in work by one of the authors, which
demonstrated that KOT and NN training are intimately connected [9]. While significant effort has
been dedicated to using NNs to discover important features of KOT [10–12], this work was, to our
knowledge, the first application of KOT for the training of NNs (see Sec. 1.1).
∗ Authors contributed equally
34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada.
An appealing aspect of KOT is that it is a linear theory for nonlinear dynamical systems. In our
case, this means that evolving NN weights/biases using Koopman operators involves only matrix
computations. We show, under certain mild assumptions, how these computations can be considerably
cheaper than standard NN training methods. Thus, we show how successful application of KOT to
NNs could lead to significantly accelerated training techniques. We demonstrate this potential in the
context of feedforward, fully connected NNs. We emphasize that our methods are applicable to a
wide range of NNs beyond the specific ones we study - indeed they should generalize well to a wide
variety of systems that make use of iterative optimization methods.
This work is structured as follows. We begin with a brief introduction to KOT. We describe and
deepen the existing argument that NN training can be viewed as a process that evolves weights/biases
through the action of a Koopman operator. We then discuss different implementations of Koopman
training, introducing a novel approach of partitioning the Koopman operator approximation. This
idea is crucial for ensuring that the run time complexity of Koopman training is comparable or better
than that of the standard training methods. We then present the results of Koopman training two
different feedforward, fully connected, deep NNs: an NN differential equation (DE) solver and a
classifier trained on the MNIST data set. These NNs show significant variation in architecture sizes,
objectives, optimizers, learning rate, etc, lending credence to our assertions that Koopman training is
a versatile and powerful technique. Our basic Koopman training implementations successfully predict
weight/bias evolutions over a non-trivial number of training steps, with computational costs one to
two orders of magnitude smaller than the standard methods we compared to. We end by discussing
future problems of interest in Koopman training and the potential more advanced KOT methods offer
in extending our results.
1.1 Related work
Earlier this year, one of the authors showed that the renormalization group (RG), a widely used
tool in theoretical physics, is a Koopman operator, and that KOT could help speedup computations
of relevance in the field (e.g. critical exponent calculations) [13]. These results were achieved by
viewing the RG as a discrete dynamical system in “algorithmic time”. The other author proposed
a similar view for NN training and showcased how it might lead to more efficient optimization
methods [9]. By suggesting a partitioning of the full weight/bias space into a collection of smaller
sub-spaces, [9] showed that Koopman training would be an economical optimization technique, if it
could accurately mode weight/bias evolutions.
Unbeknownst (and in paral
```

## candidate-27 [atlas-general] — UNCONSUMED

**Title:** Information Decomposition on Structured Space

**URL:** file:///9987c4cf84c5d97c2e3c6899962b487cd0827759667461b0252bf9c1d5d4b8de/Information_Decomposition_on_Structured_Space.pdf

**Description:** A research paper that builds information geometry on partially ordered sets (posets), defining orthogonal decomposition of KL divergence and entropy on incomplete hierarchies. It generalizes Amari's seminal hierarchical decomposition of probability distributions by introducing dual θ- and η-coordinate systems on posets, proving a Pythagoras theorem for KL divergence, and providing efficient algorithms for isolating higher-order statistical interactions.

**Content extract (≤6k chars):**

```
Information Decomposition on Structured Space
Mahito Sugiyama Hiroyuki Nakahara Koji Tsuda
ISIR, Osaka University RIKEN Brain Science Institute Graduate School of Frontier Sciences
JST PRESTO hiro@brain.riken.jp The University of Tokyo
mahito@ar.sanken.osaka-u.ac.jp tsuda@k.u-tokyo.ac.jp
Abstract —We build information geometry for a partially or- (a) (b)
dered set of variables and define the orthogonal decomposition 1234 1234
of information theoretic quantities. The natural connection be-
tween information geometry and order theory leads to efficient 123 124 134 234 123 124 234
decomposition algorithms. This generalization of Amari’s seminal
work on hierarchical decomposition of probability distributions
on event combinations enables us to analyze high-order statis- 12 13 14 23 24 34 23 24
tical interactions arising in neuroscience, biology, and machine
learning. 1 2 3 4 1 2 4
I. I NTRODUCTION
ø ø
Let e 1 , e 2 , . . . , e n denote the set of events. All combina-
tions of events are regarded as a partially ordered set and Fig. 1. Hierarchy of combinations of four events e 1 , e 2 , e 3 , and e 4 . Numbers
form a complete hierarchy (Figure 1 a ). Amari introduced the denote corresponding events. (a) The complete hierarchy of combinations of
events. (b) Incomplete hierarchy by removing gray combinations in (a) .
orthogonal decomposition of probability distributions defined
on the complete hierarchy of events [1]. That method provided
a theoretical foundation with which to analyze the higher- II. D UALLY F LAT M ANIFOLD ON P OSETS
order interactions in a wide variety of applications, such
Suppose that X is a discrete random variable and p ( x ) =
as firing patterns of neurons [2], [3], gene interactions [4],
Pr( X = x ) with x ∈ S is a probability mass function on a
and word associations in documents [5]. However, in many
finite set S . In information geometry [1], [7], each distribution
applications the hierarchy is often incomplete, because some
is treated as a mapping p : S → R and the set of all probability
event combinations can never occur (Figure 1 b ). For example,
distributions is understood to be a ( | S | − 1) -dimensional man-
if e 1 indicates a person being male and e 2 indicates a person ∑
ifold S = { p | p ( x ) > 0 for all x ∈ S, 
having ovarian cancer, the combination of e 1 and e 2 can never x ∈ S p ( x ) = 1 } ,
where probabilities form a coordinate system of S , called the
occur. Incomplete hierarchies can also result from a lack of
p -coordinate system . Information geometry gives us two more
data [6].
coordinate systems of S , the θ -coordinate system and the η -
We define information geometric dual coordinates on a
coordinate system, which are known to be dually orthogonal
partially ordered set , or a poset . They lead to an efficient
and key to decomposing KL divergence via the mixed coor-
algorithm for decomposing Kullback–Leibler divergence and
dinate system of θ and η . We introduce such two coordinates
entropy in an incomplete hierarchy. Our method can be used to
in Section II-A and show decomposition of KL divergence in
isolate the contribution of each event combination and assess
Section II-B.
its statistical significance [2]. From a theoretical viewpoint,
We consider the case where S is a partially ordered set,
arXiv:1601.05533v2 [cs.IT] 5 May 2016 our method offers a previously unexplored link between order
or a poset , which is one of the most fundamental structured
theory and information geometry.
space in computer science and mathematics. A partial order
The remainder of this paper is organized as follows. Sec-
“ ≤ ” satisfies the following three properties: for all x, y, z ∈
tion II introduces a dually flat manifold on a poset. In
S , (1) x ≤ x (reflexivity), (2) x ≤ y , y ≤ x ⇒ x = y
Section II-A, we show that, given a poset we introduce, the
(antisymmetry), and (3) x ≤ y , y ≤ z ⇒ x ≤ z (transitivity).
manifold of probability distributions will always have the same
Throughout the paper, we assume that S is always finite and
dually flat structure as that of the exponential family of the
includes the bottom element ⊥ ∈ S ; that is, ⊥ ≤ x for all
original variable set (Equations (3) and (5)). In Section II-B,
x ∈ S . We write the set S \ {⊥} by S + .
we present an efficient algorithm to decompose information on
For a subset I ⊆ S , we denote a lower set ↓ I = { x ∈
a poset (Algorithms 1, 2 and Theorem 1). As a representative
S | x ≤ s for some s ∈ I } , an upper set ↑ I = { x ∈ S |
application, in Section III, we show that our algorithm can
x ≥ s for some s ∈ I } , and ↓ x = ↓{ x } , ↑ x = ↑{ x } for each
efficiently isolate information of arbitrary order interactions of
x ∈ S . In order theory, ↓ x is called the principal ideal for x
events. We summarize and conclude the paper in Section IV.
and ↑ x is called the principal filter for x [8], [9], which are
A preprint is available at http://arxiv.org/abs/1601.05533. known to be fundamental mathematical objects in posets.
the e -flat manifold S , which means that our formulation of
η ( x ) = ∑ p ( s )
s ≥ x θ in Equation (4) is the e -affine coordinate. The m -affine
coordinate η : S → R , an alternative coordinate system that
introduces the duality to S , is given as the expectation of the
parameter F s ( x ) for each s ∈ S . In our case η is given as
x follows:
∑
η ( s ) = E [ F s ( x )] = p ( x ) = Pr( X ≥ s ) . (5)
x ≥ s
⊥ log p ( x ) = ∑ θ ( s ) Relationships of p , θ , and η are illustrated in Figure 2.
s ≤ x The two coordinate systems θ and η are connected with
Fig. 2. p ( x ) , θ ( x ) , and η ( x ) on poset. each other by the Legendre transformation. The remarkable
property is that θ and η are dually orthogonal :
[ ]
∂ ∂
A. θ - and η -coordinate Systems E log p ( x ; θ ) log p ( x ; η ) = δ ( s, s ′ ) (6)
∂θ ( s ) ∂η ( s ′ ) 
Let us first introduce the θ - coordinate system of the mani-
fold S , which is realized as a mapping θ : S → R . In the expo- for every s, s ′ ∈ S + with the Kronecker delta δ
```

## candidate-28 [atlas-general] — UNCONSUMED

**Title:** Ensemble Control on Lie Groups

**URL:** file:///e750a19b2180c1f9249dcf70b4ec6e1934cc12df3a6c6b93eaa208105ea338b0/Ensemble_Control_on_Lie_Groups.pdf

**Description:** This research paper studies controllability of bilinear ensemble systems defined on semisimple Lie groups, where a single broadcast control signal must simultaneously steer a large population of structurally identical dynamical systems. The authors develop a 'covering method' leveraging Cartan decompositions of semisimple Lie algebras to decompose the state space Lie group into generating Lie subgroups, reducing the infinite-dimensional ensemble controllability problem to finite-dimensional subsystem analysis. The main result establishes that classical controllability of each individual system implies ensemble controllability for bilinear systems on semisimple Lie groups, extending prior work on SO(3) to the general semisimple case including non-compact groups.

**Content extract (≤6k chars):**

```
1
Ensemble Control on Lie Groups
Wei Zhang and Jr-Shin Li
Abstract
Problems involving control of large ensmebles of structurally identical dynamical systems, called
ensemble control , arise in numerous scientific areas from quantum control and robotics to brain medicine.
In many of such applications, control can only be implemented at the population level, i.e., through
broadcasting an input signal to all the systems in the population, and this new control paradigm chal-
lenges the classical systems theory. In recent years, considerable efforts have been made to investigate
controllability properties of ensemble systems, and most works emphasized on linear and some forms
of bilinear and nonlinear ensemble systems. In this paper, we study controllability of a broad class
of bilinear ensemble systems defined on semisimple Lie groups, for which we define the notion of
ensemble controllability through a Riemannian structure of the state space Lie group. Leveraging the
Cartan decomposition of semisimple Lie algebras in representation theory, we develop a covering method
that decomposes the state space Lie group into a collection of Lie subgroups generating the Lie group,
which enables the determination of ensemble controllability by controllability of the subsystems evolving
on these Lie subgroups. Using the covering method, we show the equivalence between ensemble and
classical controllability, i.e., controllability of each individual system in the ensemble implies ensemble
controllability, for bilinear ensemble systems evolving on semisimple Lie groups. This equivalence
makes the examination of controllability for infinite-dimensional ensemble systems as tractable as for
a finite-dimensional single system.
I. I NTRODUCTION
arXiv:2008.03243v1 [math.OC] 7 Aug 2020
Finely manipulating a large ensemble of structurally identical dynamical systems has emerged
as an essential demand in diverse areas from quantum science and technology [18, 30, 34, 15,
16, 2], brain medicine [48, 13, 24, 50] and robotics [4] to sociology [7, 10]. In many applications
*This work was supported in part by the National Science Foundation under the award ECCS-1810202 and by the Air Force
Office of Scientific Research under the award FA9550-17-1-0166.
W. Zhang is with the Department of Electrical and Systems Engineering, Washington University, St. Louis, MO 63130, USA
wei.zhang@wustl.edu
J.-S. Li is with the Department of Electrical and Systems Engineering, Washington University, St. Louis, MO 63130, USA
jsli@wustl.edu . Questions, comments, or corrections to this document may be directed to J.-S. Li at this email address.
August 10, 2020 DRAFT
2
involving ensemble systems, control can only be exerted at the population level becasue it is
infeasible and often impossible to receive state feedback for each individual system. As a result,
considerable efforts have been made over the past years to understand the fundamental limit on
the extent to which an ensemble system can be manipulated with a broadcast open-loop signal.
This new control paradigm raised significant challenges in classical systems theory, while offering
abundant opportunities for making theoretical advancements.
Among the developments in this rising area, referred to as ensemble control, extensive focuses
have been placed on investigating the controllability property of ensemble systems, including
linear [28, 21, 42, 32, 14, 35], bilinear [31, 3, 12], and some forms of nonlinear ensemble systems
[29, 11, 26]. The work on analyzing controllability of an ensemble with each system defining on
the Lie group SO (3) set the milestone in formal and rigorous study of ensemble systems [31].
In this work, using Lie algebraic tools, the controllability analysis was translated to the problem
of polynomial approximation, which opened the door for addressing ensemble control problems
from the perspective of “approximation”. This new notion has led to seminal works on developing
necessary and/or sufficient conditions for ensemble controllability [28, 14, 21, 32, 42, 45, 35]
and observability [44, 43], and novel theory- and computational-based techniques for optimal
ensemble control design and synthesis [34, 49, 9, 38, 39, 40]. Although progress in understanding
fundamental properties of nonlinear ensemble systems is underdeveloped [29, 11] and much is
awaiting to be explored, the work presented in [31] shed light on revealing the equivalence
between ensemble controllability and classical controllability for certain classes of ensemble
systems.
In general, controllability of each individual system (i.e., classical controllability) in an ensem-
ble is a necessary condition to ensemble controllability but not sufficient. Namely, if an ensemble
system is ensemble controllable, then each individual system in the ensemble must be controllable
in the classical sense; however, the reversal is generally not true. Motivated by the work on the
control of ensemble systems on SO(3) [31], where controllability of each individual system led
to controllability of the entire ensemble, in this paper, we extend this previous finding to explore
such equivalence in classical and ensemble controllability for more general classes of ensemble
systems. Specifically, we study the bilinear ensemble system in which each individual system
evolves on the same semisimple Lie group. In our approach, such an ensemble is regarded
as a single system defined on the space of Lie group-valued functions, which is an infinite-
dimensional Lie group, and the concept of ensemble controllability is rigorously defined in the
August 10, 2020 DRAFT
3
sense of approximate controllability through a bi-invariant metric on this infinite-dimensional
Lie group. The main tool developed in this work is the covering method . The central idea
of this method is to decompose the state space Lie group of a bilinear ensemble system into a
collection of Lie subgroups, which generates the Lie group, so that controllability of the e
```

## candidate-29 [atlas-general] — UNCONSUMED

**Title:** Moment Based Ensemble Control

**URL:** file:///71440609e6e30463acbda22b6da39be48c9f5a2cd2fd8f0e3ff2bff50c98587c/Moment-Based_Ensemble_Control.pdf

**Description:** A research paper proposing a moment-based framework for controlling large populations (ensembles) of structurally identical dynamical systems with parametric variations. The authors extend the Hausdorff moment problem from a differential geometric perspective to establish equivalence between ensemble systems and their moment systems in terms of controllability, enabling closed-loop moment-feedback control using only aggregated (population-level) measurements rather than individual system state feedback.

**Content extract (≤6k chars):**

```
1
Moment-Based Ensemble Control
Vignesh Narayanan, Member, IEEE, Wei Zhang, Member, IEEE,
and Jr-Shin Li, Senior Member, IEEE
Abstract
Controlling a large population, in the limit, a continuum, of structurally identical dynamical systems
with parametric variations is a pervasive task in diverse applications in science and engineering. However,
the severely underactuated nature and the inability to avail comprehensive state feedback information of
such ensemble systems raise significant challenges in analysis and design of ensemble systems. In this
paper, we propose a moment-based ensemble control framework, which incorporates and expands the
method of moments in probability theory to control theory. In particular, we establish an equivalence
between ensemble systems and their moment systems in terms of control and their controllability
properties by extending the Hausdorff moment problem from the perspectives of differential geometry
and dynamical systems. The developments enable the design of moment-feedback control laws for
closing the loop in ensemble systems using the aggregated type of measurements. The feasibility of this
closed-loop control design procedure is validated both mathematically and numerically.
Index Terms
Ensemble systems, Aggregated measurements, Aggregated feedback, Hausdorff moment problem.
I. I NTRODUCTION
Large populations of uncoupled or interconnected dynamical systems are pervasive in diverse
arXiv:2009.02646v1 [math.OC] 6 Sep 2020
scientific domains, such as quantum science and technology [1, 2], power systems [3], neuro-
science [4, 5], emergent behaviors [6], and robotics [7]. These population systems, formally
referred to as ensemble systems , generally exhibit variations in the parameters characterizing
the dynamics of individual dynamic units in the ensemble. Such variations arise either by
nature (e.g., different weight and size of birds in a flock), manufacturing (e.g., the variability
*This work was supported in part by the National Science Foundation under the awards CMMI-1462796 and ECCS-1509342,
and by the Air Force Office of Scientific Research under the award FA9550-17-1-0166.
V. Narayanan, W. Zhang, and J.-S. Li are with the Department of Electrical and Systems Engineering, Washington University
in St. Louis, St. Louis MO, 63130 USA e-mail: vignesh.narayanan@wustl.edu, wei.zhang@wustl.edu, jsli@wustl.edu.
September 8, 2020 DRAFT
2
in the fabrication resulting in different mass, friction coefficients, etc., of robots in a swarm),
or design (e.g., the application of gradient fields resulting in Larmor frequency dispersion in
magnetic resonance imaging). Owing to their prevalence in diverse emerging applications and
rich mathematical structures, ensemble control problems have attracted significant attention and
formed a new paradigm in systems and control over past years. Theoretically, the notions of
ensemble controllability and observability have been introduced and extensively investigated,
especially for linear [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], bilinear [18, 19, 20, 21, 22, 23, 24],
and some classes of nonlinear systems [22]. Computationally, various numerical algorithms have
been proposed for synthesizing robust and optimal control signals to steer ensemble systems
between desired states [2, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34].
The fundamental challenges associated with ensemble control problems lie in the underactuated
nature and the lack of comprehensive state feedback information of the entire ensemble. These
bottlenecks have naturally pushed the research in ensemble control theory towards the direction
of pursuing open-loop and sparsely distributed control scenarios. However, in many cutting-edge
applications involving the control of ensemble systems, such as neuronal networks, robot swarms,
spin ensembles, and cellular oscillators, aggregated type of spatially sparse measurements, such
as coarse or fragmented images and partial snapshots, can be obtained [35, 36, 37, 32]. The
availability of such measurements then opens up the possibility for utilizing population-level
feedback to close the loop in ensemble control systems. In this paper, we adopt the idea of
statistical moments in probability theory to develop a moment-based ensemble control framework.
Approaches based on the use of “moments” have been introduced in systems theory, especially
widely adopted in the context of stochastic control [38, 39]. On the other hand, several efforts
have been made towards developing dynamic models and analyzing collective behaviors of
deterministic populations using statistical moments [40, 41]. For example, an original work on
controlling a homogeneous population of dynamical agents using their population density was
proposed in [42], and was later extended to control linear ensemble systems using their mean
and variance through output feedback [43] and, further, to analyze ensemble controllability and
observability for time-invariant linear ensemble systems [44, 14].
In contrast to the existing literature, the moment-based ensemble control framework proposed
in this paper focuses on the analysis and manipulation of ensemble systems through the systems
describing the dynamics of their moments induced by aggregated measurements. In particular,
we categorize such measurements into two types - labeled and unlabeled, commonly found in
September 8, 2020 DRAFT
3
practice, and associate ensemble systems with two different notions of moments, i.e., ensemble-
and output-moments, respectively. By extending the classical moment problem from a geometric
aspect, we establish a dynamic connection between an ensemble and its respective moment
system, so that controlling an ensemble can be achieved by controlling its moment system. In
addition, we show that both the ensemble system and the corresponding moment system share the
same controllability property. Such equivalences enable and facilitate the design of closed-loop
moment-feedback control laws by 
```

## candidate-30 [atlas-general] — UNCONSUMED

**Title:** General Purpose In Context Learning by Meta Learning Transformers

**URL:** file:///50eb99f253c1217a3d28690ee7e3d161b8683648ad40776682f8a44f0fe33481/General-Purpose_In-Context_Learning_by_Meta-Learning_Transformers.pdf

**Description:** This research paper investigates how Transformers can be meta-trained from scratch to act as general-purpose in-context learning algorithms (GPICL) with minimal inductive bias. The authors characterize phase transitions between memorization, task identification, and genuine learning-to-learn as model size and number of tasks scale, finding that meta-trained learner capabilities are bottlenecked by accessible state (memory) size rather than parameter count. They propose practical interventions including task augmentation via random input projections and label permutations that improve meta-generalization to entirely unseen datasets.

**Content extract (≤6k chars):**

```
G ENERAL -P URPOSE I N -C ONTEXT L EARNING
BY M ETA -L EARNING T RANSFORMERS
Louis Kirsch 1 2 , James Harrison 1 , Jascha Sohl-Dickstein 1 , Luke Metz 1
1 Google Research, Brain Team 2 The Swiss AI Lab IDSIA, USI, SUPSI
louis@idsia.ch, { jamesharrison,jaschasd,lmetz } @google.com
A BSTRACT
Modern machine learning requires system designers to specify aspects of the
learning pipeline, such as losses, architectures, and optimizers. Meta-learning,
or learning-to-learn, instead aims to learn those aspects, and promises to un-
lock greater capabilities with less manual effort. One particularly ambitious goal
of meta-learning is to train general-purpose in-context learning algorithms from
scratch, using only black-box models with minimal inductive bias . Such a model
takes in training data, and produces test-set predictions across a wide range of
problems, without any explicit definition of an inference model, training loss, or
optimization algorithm. In this paper we show that Transformers and other black-
box models can be meta-trained to act as general-purpose in-context learners. We
characterize transitions between algorithms that generalize, algorithms that mem-
orize, and algorithms that fail to meta-train at all, induced by changes in model
size, number of tasks, and meta-optimization. We further show that the capabili-
ties of meta-trained algorithms are bottlenecked by the accessible state size (mem-
ory) determining the next prediction, unlike standard models which are thought to
be bottlenecked by parameter count. Finally, we propose practical interventions
such as biasing the training distribution that improve the meta-training and meta-
generalization of general-purpose in-context learning algorithms.
1 I NTRODUCTION
Meta-learning is the process of automatically discovering new learning algorithms instead of de-
signing them manually (Schmidhuber, 1987). An important quality of human-engineered learning
algorithms, such as backpropagation and gradient descent, is their applicability to a wide range of
tasks or environments. For learning-to-learn to exceed those capabilities, the meta-learned learn-
ing algorithms must be similarily general-purpose . Recently, there has been significant progress
toward this goal (Kirsch et al., 2019; Oh et al., 2020). The improved generality of the discovered
arXiv:2212.04458v2 [cs.LG] 9 Jan 2024 learning algorithms has been achieved by introducing inductive bias, such as by bottlenecking the
architecture or by hiding information, which encourage learning over memorization. Methods in-
clude restricting learning rules to use gradients (Metz et al., 2019; Kirsch et al., 2019; Oh et al.,
2020), symbolic graphs (Real et al., 2020; Co-Reyes et al., 2021), or parameter sharing (Kirsch &
Schmidhuber, 2020; Kirsch et al., 2021).
While enabling generalization, these inductive biases come at the cost of increasing the effort to
design these systems and potentially restrict the space of discoverable learning algorithms. Instead,
we seek to explore general-purpose meta-learning systems with minimal inductive bias . Good can-
didates for this are black-box sequence-models as meta-learners such as LSTMs (Hochreiter et al.,
2001; Wang et al., 2016; Duan et al., 2016) or Transformers (Vaswani et al., 2017). These memory-
based or in-context learners take in training data and produce test-set predictions without any explicit
definition of an inference model, training loss, or optimization algorithm. With recent advances of
in-context learning in large language models (Brown et al., 2020), neural networks can already learn
many concepts from demonstrations. What are the necessary conditions such that those models can
learn from a wide range of demonstrations? To what extent can we elicit in-context learning that
generalizes to a wider range of problems, in a similar way how learning via backpropagation and
gradient descent can generalize?
1
In this work, we investigate how such in-context meta-learners can be trained to (meta-)generalize
and learn on significantly different datasets than used during meta-training. For this we propose a
Transformer-based General-Purpose In-Context Learner (GPICL) which is described with an as-
sociated meta-training task distribution in Section 3. In Section 4.1 we characterize algorithmic
transitions—induced by scaling the number of tasks or the model size used for meta-training—
between memorization, task identification, and general learning-to-learn. We further show in Sec-
tion 4.2 that the capabilities of meta-trained algorithms are bottlenecked by their accessible state
(memory) size determining the next prediction (such as the hidden state size in a recurrent net-
work), unlike standard models which are thought to be bottlenecked by parameter count. Finally,
in Section 4.3, we propose practical interventions that improve the meta-training of general purpose
learning algorithms. Additional related work can be found in Section 5.
2 B ACKGROUND
What is a (supervised) learning algorithm? In this paper, we focus on the setting of meta-
learning supervised in-context learning algorithms. Consider a mapping
 
{ x i , y i } N D
i =1 , x ′ 7 → y ′ (1)
from the training (support) set D = { x i , y i } N D
i =1 and a query input x ′ to the query’s prediction y ′
where x i , x ′ ∈ R N x , y i , y ′ ∈ R N y and N D , N x , N y ∈ N + . The subset of these functions that qualify
as learning algorithms are those that improve their predictions y ′ given an increasingly larger training
set D . Meta-learning then corresponds to finding these functions via meta-optimization. As in other
black-box meta-learning models, we use a neural network to represent such functions. Such in-
context learning is different from gradient-based meta-learning (such as MAML (Finn et al., 2017))
in that no explicit gradients are computed at meta-test time. All required mechanisms for learning
are implicitly encoded in the black-box neural network.
What is a genera
```

## candidate-31 [atlas-general] — UNCONSUMED

**Title:** The scheme of liftings and applications

**URL:** file:///f27c98ccc9374f74ecfa1cb07153d09d38090698b91aa4067069f4eaa2aff02a/The_scheme_of_liftings_and_applications.pdf

**Description:** A pure mathematics research paper studying the locus of liftings of a homogeneous ideal H in a polynomial ring over any field. The authors prove this locus carries a natural scheme structure (independent of term order) by showing the functor of liftings is representable, embed it in Hilbert schemes, establish topological properties (connectedness, openness of radical locus), and answer an open 1989 question of L.G. Roberts by proving every saturated ideal defining an arithmetically Cohen-Macaulay scheme of codimension two admits a radical lifting.

**Content extract (≤6k chars):**

```
THE SCHEME OF LIFTINGS AND APPLICATIONS
C. BERTONE, F. CIOFFI, M. GUIDA, AND M. ROGGERO
Abstract. We study the locus of the liftings of a homogeneous ideal H in a polynomial
ring over any field. We prove that this locus can be endowed with a structure of scheme
L H by applying the constructive methods of Gr¨ obner bases, for any given term order.
Indeed, this structure does not depend on the term order, since it can be defined as the
scheme representing the functor of liftings of H . We also provide an explicit isomorphism
between the schemes corresponding to two different term orders.
Our approach allows to embed L H in a Hilbert scheme as a locally closed subscheme,
and, over an infinite field, leads to find interesting topological properties, as for instance
that L H is connected and that its locus of radical liftings is open. Moreover, we show
that every ideal defining an arithmetically Cohen-Macaulay scheme of codimension two
has a radical lifting, giving in particular an answer to an open question posed by L. G.
Roberts in 1989.
Introduction
In this paper we consider the lifting problem as proposed in terms of ideals first in [19]
and then in [38] and, equivalently, in terms of K -algebras by Grothendieck (e.g. [38] and
the references therein or [8]). Many authors have investigated this interesting problem,
sometimes also describing particular lifting procedures to construct algebraic varieties
with specific properties (see [30, 22, 19, 36, 38, 33, 29] and the references therein).
We propose and use a new approach that is based on the theory of representable
functors. Indeed, we define the functor of liftings of a homogeneous polynomial ideal
H and show that it is representable, in the perspective given by [28] for Gr¨ obner strata
and according to the point of view of [3]. Our approach is constructive and we compute
the scheme of liftings L H of H , i.e. the scheme that parameterises the liftings of H and
represents the functor, by a reformulation of a result of [10] in terms of Gr¨ obner bases.
An almost immediate result of the application of our approach, together with the fea-
tures of Gr¨ obner strata, is that L H can be embedded in a Hilbert scheme, with the con-
arXiv:1312.7700v2 [math.AG] 4 Jun 2015
sequence that its locus of radical liftings is an open subset. This fact gives a contribution
to a question posed in [29, Remark at pag. 332].
Even though the scheme of liftings L H can be neither irreducible nor reduced (see
Examples 8.1 and 8.5), we prove that, over an infinite field, L H has several interesting
topological properties. For instance, L H is always connected, since the point corresponding
to H belongs to every irreducible component of L H . Moreover, L H is isomorphic to an
affine space if and only if it is smooth at this point. These properties are proved exploiting
the action of the torus K ∗ = K \ { 0 } on L H .
We then consider the special case of ideals H defining arithmetically Cohen-Macaulay
(aCM, for short) schemes of codimension two and prove that their schemes of liftings are
isomorphic to affine spaces. The problem of studying whether some particular families of
2000 Mathematics Subject Classification. 13P10, 14B10, 14M05.
Key words and phrases. lifting, Gr¨ obner basis, radical lifting, Cohen-Macaulay scheme.
1
2
ideals can be parameterised by an affine space has been also treated by other authors. For
instance, Gr¨ obner strata of ideals defining aCM schemes in P 2 are studied in [12, 13], and
other Gr¨ obner strata of polynomial ideals in any number of variables are studied in [37]
(see also the references therein). Some of the tools used in those papers also appear in the
present one. In particular, we quote the action of the torus K ∗ on the families of ideals,
and, in the aCM case, the description of ideals by means of Hilbert-Burch resolutions and
the use of the Pommaret basis of quasi-stable ideals.
We are also able to prove that every saturated ideal defining an aCM scheme of codi-
mension two has a radical lifting. This result is particularly significant in the context
of the study of radical liftings, because of the lack of information endured until now in
the case of polynomial homogeneous ideals in three variables. Indeed, we provide an
affermative answer to the question posed by L. G. Roberts in [36].
The paper is organized in the following way. Referring to [16, 37, 27, 28], in Section 2 we
recall definitions and main features of Gr¨ obner strata. Moreover, we give an improvement
of [27, Theorem 4.7] (Theorem 2.2) which will be useful to embed the scheme of liftings
of a homogeneous ideal in a Hilbert scheme.
In Section 3, we define the functor of liftings of a homogeneous polynomial ideal and
introduce the constructive tool we use to represent it, i.e. a reformulation of [10, Theorem
2.5] by means of Gr¨ obner bases (Theorem 3.2). In Section 4, we prove that a functor of
liftings is representable, thus obtaining that the construction of the scheme of liftings that
arises from Theorem 3.2 does not depend on the given term order, up to isomorphisms
(Theorem 4.3 and Corollary 4.5). In Section 5, we give an explicit construction of the
these isomorphisms (Theorem 5.2).
In Section 6, we describe how we embed the scheme of liftings L H in a Hilbert scheme
and deduce that its locus of radical liftings is an open subset (Proposition 6.1 and Corollary
6.3). Then, we investigate the action of the torus on the scheme of liftings obtaining the
topological properties we have previously described (Proposition 6.4 and Corollary 6.5).
In Section 7, we find that, if H is a saturated homogeneous polynomial ideal defining
an aCM scheme of codimension two, then L H is isomorphic to an affine space (Theorem
7.5). Moreover, exploiting the Hilbert-Burch Theorem and the potentiality of Gr¨ obner
deformations, we conceive a constructive method to show that every aCM scheme of
codimension two has a radical lifting (Theorem 7.8).
All the results we present are b
```

## candidate-32 [atlas-general] — UNCONSUMED

**Title:** Economy Statistical Recurrent Units For Inferring Nonlinear Granger Causality

**URL:** file:///0170d99cf2c7782122bc1f8e792623e0bde61927d0a8ffd51c69403586207c3d/Economy_Statistical_Recurrent_Units_For_Inferring_Nonlinear_Granger_Causality.pdf

**Description:** This ICLR 2020 paper proposes the economy Statistical Recurrent Unit (eSRU), a modified recurrent neural network for inferring nonlinear Granger causality between multivariate stochastic processes from time series data. The eSRU uses random projections to reduce parameters and group-wise regularization to produce time-localized causal features, enabling direct inference of causal network topology from structured sparse weight estimates. Extensive experiments demonstrate that eSRU outperforms MLP, LSTM, and attention-gated CNN baselines for Granger causal inference.

**Content extract (≤6k chars):**

```
Published as a conference paper at ICLR 2020
E CONOMY S TATISTICAL R ECURRENT U NITS F OR
I NFERRING N ONLINEAR G RANGER C AUSALITY
Saurabh Khanna Vincent Y. F. Tan
Department of Electrical and Computer Engineering Department of Electrical and Computer Engineering
National University of Singapore Department of Mathematics
elesaur@nus.edu.sg National University of Singapore
vtan@nus.edu.sg
A BSTRACT
Granger causality is a widely-used criterion for analyzing interactions in large-
scale networks. As most physical interactions are inherently nonlinear, we con-
sider the problem of inferring the existence of pairwise Granger causality between
nonlinearly interacting stochastic processes from their time series measurements.
Our proposed approach relies on modeling the embedded nonlinearities in the
measurements using a component-wise time series prediction model based on
Statistical Recurrent Units (SRUs). We make a case that the network topology
of Granger causal relations is directly inferrable from a structured sparse estimate
of the internal parameters of the SRU networks trained to predict the processes’
time series measurements. We propose a variant of SRU, called economy-SRU ,
which, by design has considerably fewer trainable parameters, and therefore less
prone to overfitting. The economy-SRU computes a low-dimensional sketch of its
high-dimensional hidden state in the form of random projections to generate the
feedback for its recurrent processing. Additionally, the internal weight parameters
of the economy-SRU are strategically regularized in a group-wise manner to fa-
cilitate the proposed network in extracting meaningful predictive features that are
highly time-localized to mimic real-world causal events. Extensive experiments
are carried out to demonstrate that the proposed economy-SRU based time series
prediction model outperforms the MLP, LSTM and attention-gated CNN-based
time series models considered previously for inferring Granger causality.
1 I NTRODUCTION
The physical mechanisms behind the functioning of any large-scale system can be understood in
arXiv:1911.09879v2 [cs.LG] 14 Jan 2020
terms of the networked interactions between the underlying system processes. Granger causality
is one widely-accepted criterion used in building network models of interactions between large en-
sembles of stochastic processes. While Granger causality may not necessarily imply true causality,
it has proven effective in qualifying pairwise interactions between stochastic processes in a variety
of system identification problems, e.g., gene regulatory network mapping (Fujita et al. (2007)), and
the mapping of human brain connectome (Seth et al. (2015)). This perspective has given rise to
the canonical problem of inferring pairwise Granger causal relationships between a set of stochastic
processes from their time series measurements. At present, the vast majority of Granger causal in-
ference methods adopt a model-based inference approach whereby the measured time series data is
modeled using with a suitable parameterized data generative model whose inferred parameters ul-
timately reveal the true topology of pairwise Granger causal relationships. Such methods typically
rely on using linear regression models for inference. However, as illustrated in the classical bivariate
example by Baek & Brock (1992), linear model-based Granger causality tests can fail catastrophi-
cally in the presence of even mild nonlinearities in the measurements, thus making a strong case for
our work which tackles the nonlinearities in the measurements by exploring new generative models
of the time series measurements based on recurrent neural networks.
1
Published as a conference paper at ICLR 2020
2 P ROBLEM FORMULATION
Consider a multivariate dynamical system whose evolution from an initial state is fully characterized
by n distinct stochastic processes which can potentially interact nonlinearly among themselves. Our
goal here is to unravel the unknown nonlinear system dynamics by mapping the entire network of
pairwise interactions between the system-defining stochastic processes, using Granger causality as
the qualifier of the individual pairwise interactions.
In order to detect the pairwise Granger causal relations between the stochastic processes, we as-
sume access to their concurrent, uniformly-sampled measurements presented as an n -variate time
series x = { x t : t ∈ N } ⊂ R n . Let x t,i denote the i th component of the n -dimensional vector mea-
surement x t , representing the measured value of process i at time t . Motivated by the framework
proposed in Tank et al. (2017), we assume that the measurement samples x t , t ∈ N are generated
sequentially according to the following nonlinear, component-wise autoregressive model:
x t,i = f i ( x t − p : t − 1 , 1 , x t − p : t − 1 , 2 , . . . , x t − p : t − 1 ,n ) + e t,i , i = 1 , 2 , . . . n, (1)
where x t − p : t − 1 ,j , { x t − 1 ,j , x t − 2 ,j , . . . , x t − p,j } represents the most recent p measurements of the
j th component of x in the immediate past relative to current time t . The scalar-valued component
generative function f i captures all of the linear and nonlinear interactions between the n stochastic
processes up to time t − 1 that decide the measured value of the i th stochastic process at time t . The
residual e i,t encapsulates the combined effect of all instantaneous and exogenous factors influenc-
ing the measurement of process i at time t , as well as any imperfections in the presumed model.
Equation 1 may be viewed as a generalization of the linear vector autoregressive (VAR) model in
the sense that the components of x can be nonlinearly dependent on one another across time. The
value p is loosely interpreted to be the order of the above nonlinear autoregressive model.
2.1 G RANGER CAUSALITY IN NONLINEAR DYNAMICAL SYSTEMS
We now proceed to interpret Granger causality in the context of the above component-wise time
series model. Recalling 
```

## candidate-33 [atlas-general] — UNCONSUMED

**Title:** AgentGL Towards Agentic Graph Learning with LLMs via Reinforcement Learning

**URL:** file:///3587f3f2ea660c8fe56df8cd760909a34c53c7ac5b527b25d52a7fa26c2d9dd4/AgentGL_Towards_Agentic_Graph_Learning_with_LLMs_via_Reinforcement_Learning.pdf

**Description:** This research paper introduces AgentGL, the first reinforcement learning-driven framework for Agentic Graph Learning (AGL), a paradigm that reframes graph learning as interleaved topology-aware navigation and LLM-based inference over Text-Attributed Graphs. The authors equip an LLM agent with graph-native search tools (1-hop, 2-hop, structure salience) and use search-constrained thinking plus graph-conditioned curriculum RL to stabilize long-horizon policy learning. AgentGL achieves absolute improvements of up to 17.5% in node classification and 28.4% in link prediction over strong GraphLLM and GraphRAG baselines.

**Content extract (≤6k chars):**

```
AgentGL: Towards Agentic Graph Learning with LLMs via
Reinforcement Learning
Yuanfu Sun 1 , 2 * , Kang Li 3 * , Dongzhe Fan 1 , 2 , Jiajin Liu 1 , 2 , Qiaoyu Tan 1 †
1 New York University Shanghai 2 New York University 3 Tsinghua University
{yuanfu.sun, qiaoyu.tan}@nyu.edu, lik24@mails.tsinghua.edu.cn
Abstract Generation (RAG) (Gao et al., 2023) and more re-
cent agentic search frameworks (Li et al., 2025;
Large Language Models (LLMs) increasingly
rely on agentic capabilities—iterative retrieval, Jin et al., 2025; Chen et al., 2025) allow LLMs to
tool use, and decision-making—to overcome iteratively query external resources and integrate
the limits of static, parametric knowledge. Yet retrieved evidence into a dynamic chain of thought.
existing agentic frameworks treat external in- Despite the power of agentic paradigms, they
formation as unstructured text and fail to lever- mainly operate on unstructured text, overlooking
age the topological dependencies inherent in the relational structures that underpin many cor-
real-world data. To bridge this gap, we in- pora. In critical domains such as citation networks
troduce Agentic Graph Learning (AGL), a
(Yang et al., 2016), social platforms (Hamilton
paradigm that reframes graph learning as an
interleaved process of topology-aware navi- et al., 2017), and commercial ecosystems (Shchur
gation and LLM-based inference. Specifi- et al., 2018), information naturally manifests as
cally, we propose AgentGL, the first reinforce- Text-Attributed Graphs (TAGs), where meaning is
ment learning (RL)–driven framework for AGL. derived from the interplay between textual content
AgentGL equips an LLM agent with graph- and graph topology. Consequently, agentic systems
native tools for multi-scale exploration, regu- that rely solely on lexical similarity cannot harness
lates tool usage via search-constrained think-
these structural dependencies. This raises a central
ing to balance accuracy and efficiency, and
employs a graph-conditioned curriculum RL question: Can the agentic learning paradigm be ex-
strategy to stabilize long-horizon policy learn- tended to graph-structured environments to enable
ing without step-wise supervision. Across dynamic, topology-aware reasoning, and how can
diverse Text-Attributed Graph (TAG) bench- such a system be built efficiently?
marks and multiple LLM backbones, AgentGL Existing graph learning efforts only partially
substantially outperforms strong GraphLLMs address this need. Traditional GNNs (Kipf and
and GraphRAG baselines, achieving absolute Welling, 2016; Velickovic et al., 2017) model struc-
improvements of up to 17.5% in node classi-
tural signals but struggle with rich textual seman-
fication and 28.4% in link prediction. These
results demonstrate that AGL is a promising tics (Yan et al., 2023). Recent LLM-based Graph
Models (GraphLLMs) integrate LLMs with graph
arXiv:2604.05846v1 [cs.CL] 7 Apr 2026 frontier for enabling LLMs to autonomously
navigate and reason over complex relational information via graph-guided prompting or instruc-
environments. The code is publicly available at tion tuning (e.g., GraphGPT (Tang et al., 2024),
https://github.com/sunyuanfu/AgentGL . GraphICL (Sun et al., 2025)), but these models rely
on static graph context extracted once at inference
1 Introduction
time, preventing adaptive exploration. GraphRAG
Large Language Models (LLMs) have achieved systems (Jimenez Gutierrez et al., 2024; Dong
strong performance across NLP tasks through their et al., 2025) construct large text-enriched knowl-
broad linguistic and reasoning capabilities (Achiam edge graphs (KGs) from corpora, yet these recon-
et al., 2023; Yang et al., 2025). Yet their para- structed KGs are costly to build and do not pre-
metric knowledge alone is insufficient for many serve the native topological correlations present
specialized or fast-evolving domains (Lewis et al., in real TAGs. Consequently, neither GraphLLMs
2020). To bridge this gap, Retrieval-Augmented nor GraphRAG offers mechanisms for dynamic ev-
* Equal contribution idence acquisition over real-world graph structure.
† Corresponding author This motivates the emergence of Agentic Graph
Learning (AGL), a new direction where a LLM ✦ We propose AgentGL , the first RL-driven AGL
agent can autonomously navigate a graph, accumu- framework that synergizes structural percep-
late structural evidence, and iteratively refine its tion , strategic reasoning , and policy learning .
search trajectory based on on-the-fly reasoning. Specifically, it orchestrates graph-native search
However, realizing AGL is non-trivial due to tools and search-constrained thinking to nav-
two fundamental challenges. (C1) Topology-aware igate complex topologies, employing graph-
navigation. Evidence on a graph is multi-scale: conditioned curriculum-based RL to optimize
some clues appear in tightly local neighborhoods, the policy without step-wise supervision.
whereas others emerge only through broader struc-
✦ We evaluate AgentGL across multiple TAG
tural patterns. An agent must decide where to
benchmarks and graph tasks, demonstrating
go next in a combinatorial space while avoiding
strong improvements over leading GraphLLM
redundant or uninformative regions. (C2) Long-
and GraphRAG baselines. Specifically, it de-
horizon policy optimization. Effective graph rea-
livers absolute accuracy improvements of up to
soning frequently requires multi-step exploration,
17.5% in node classification and up to 28.4% in
but ground-truth search trajectories are rarely avail-
link prediction across diverse LLM backbones.
able. This makes it difficult to learn policies that
balance exploration, exploitation, and reasoning 2 Related Work
depth, and easy for agents to drift into irrelevant
branches or incur unnecessary tool calls. Address- Graph Learning with LLMs. Recent work
ing these challenges demands a principled formula- has focused on bridging the gap between graph-
tion of graph-native action spaces and stable 
```

## candidate-34 [atlas-general] — UNCONSUMED

**Title:** 2601.01359v1

**URL:** file:///02e221c76591a58090ceb1aeb2d1fb06794faf3155868226a35a0cf95e4a5d57/2601.01359v1.pdf

**Description:** A mathematical research paper studying the homotopy properties of the shadow (geometric realization in Euclidean space) of Vietoris–Rips complexes. Using inverse system techniques from shape theory, the authors show that in the limit as the scale parameter β→0 and the sample S→X, the limit projection map behaves well with respect to homotopy and homology groups when X is an ANR satisfying regularity conditions. The results bridge topological and geometric reconstruction paradigms and have implications for finite reconstruction of one-dimensional submanifolds.

**Content extract (≤6k chars):**

```
THE SHADOW OF VIETORIS–RIPS COMPLEXES IN LIMITS
KAZUHIRO KAWAMURA, SUSHOVAN MAJHI, AND ATISH MITRA
A BSTRACT . The Vietoris–Rips complex, denoted R β ( X ) , of a metric space ( X, d ) at scale β is an ab-
stract simplicial complex where each k -simplex corresponds to ( k + 1 ) points of X within diameter
β . For any abstract simplicial complex K with the vertex set K ( 0 ) a Euclidean subset, its shadow,
denoted S ( K ) , is the union of the convex hulls of simplices of K . This article centers on the homotopy
properties of the shadow of Vietoris–Rips complexes K = R β ( X ) with vertices from R N , along with
the canonical projection map p : R β ( X ) → S ( R β ( X )) . The study of the geometric/topological behav-
ior of p is a natural yet non-trivial problem. The map p may have many “singularities”, which have
been partially resolved only in low dimensions N ≤ 3 . The obstacle naturally leads us to study sys-
tems of these complexes {S ( R β ( S )) | β > 0, S ⊂ X } . We address the challenge posed by singularities
in the shadow projection map by studying systems of the shadow complex using inverse system tech-
niques from shape theory, showing that the limit map exhibits favorable homotopy-theoretic prop-
erties. More specifically, leveraging ideas and frameworks from Shape Theory, we show that in the
limit “ β → 0 and S → X ”, the limit map “lim p ” behaves well with respect to homotopy/homology
groups when X is an ANR (Absolute Neighborhood Retract) and admits a metric that satisfies some
regularity conditions. This results in limit theorems concerning the homotopy properties of systems
of these complexes as the proximity scale parameter approaches zero and the sample set approaches
the underlying space (e.g., a submanifold or Euclidean graph). The paper concludes by discussing
the potential of these results for finite reconstruction problems in one-dimensional submanifolds.
1. I NTRODUCTION
Definition 1.1 (The Vietoris–Rips Complex) . Given a metric space ( X, d X ) and a positive proximity
scale β , the Vietoris–Rips complex of X at scale β , denoted R β ( X ) , is defined to be an abstract
simplicial complex having an m –simplex for every finite subset of σ ⊂ A with cardinality ( m + 1 )
and diameter less than β . More concretely,
R β ( X ) = { σ | σ is a finite subset of A, diam d X ( σ ) < β } .
The strict inequality in the above definition is essential to this paper. For simplicity, the geomet-
ric realization of R β ( X ) endowed with the Whitehead topology [30] is also denoted by the same
symbol.
The concept was initially introduced by L. Vietoris in 1927 [31] and subsequently studied ex-
tensively by E. Rips, particularly in the context of hyperbolic groups. Despite its early 20th-
arXiv:2601.01359v1 [math.AT] 4 Jan 2026
century inception, it has only been within the last decade that these complexes have gained in-
creasing popularity, especially within the applied topology and topological data analysis (TDA)
communities. The computational simplicity of Vietoris–Rips complexes makes them a more palat-
able choice for applications compared to traditional alternatives like the ˇ Cech complexes and α -
complexes [16, 14].
D EPARTMENT OF M ATHEMATICS , U NIVERSITY OF T SUKUBA , J APAN
D ATA S CIENCE P ROGRAM , G EORGE W ASHINGTON U NIVERSITY , USA
M ATHEMATICS D EPARTMENT , M ONTANA T ECHNOLOGICAL U NIVERSITY , USA
E-mail addresses : kawamura@math.tsukuba.ac.jp, s.majhi@gwu.edu, amitra@mtech.edu .
2020 Mathematics Subject Classification. 18A30 (Primary), 51F99, 55N31 (Secondary).
Key words and phrases. Vietoris–Rips complex, geometric complex, shadow complex, direct limit, inverse limit.
1
2 THE SHADOW OF VIETORIS–RIPS COMPLEXES IN LIMITS
F IGURE 1. Vietoris–Rips complexes on a point-cloud for a growing (left-to-right)
scale β . As β grows, the topology of the complex becomes more and more con-
nected until it eventually becomes contractible.
This combinatorial flexibility, however, is balanced by a theoretical cost: the topology of the Vi-
etoris–Rips complex of a metric space—even a finite one—is generally poorly understood. Nonethe-
less, there have been noteworthy developments in the study of Vietoris–Rips complexes con-
structed for near Riemannian manifolds [19, 24, 27], metric graphs [26, 21], and general geodesic
spaces of bounded Alexandrov curvature [23].
Hausmann’s pioneering work established that any closed Riemannian manifold M is homotopy
equivalent to its Vietoris–Rips complex R β ( M ) for sufficiently small scales β [19]. This fundamen-
tal result naturally motivated the finite reconstruction problem : identifying the conditions under
which M remains homotopy equivalent to the Vietoris–Rips complex of a finite, dense sample.
Latschev in [24] addressed this problem by extending the reconstruction context to metric spaces
close to M in the Gromov–Hausdorff sense [7]. Latschev’s Theorem states: For a closed Riemann-
ian manifold M , there exists a constant ϵ 0 ( M ) > 0 such that for any scale 0 < β ≤ ϵ 0 ( M ) , there exists a
δ ( β ) > 0 where any metric space S satisfying d GH ( S, M ) < δ ( β ) yields a Vietoris–Rips complex R β ( S ) ho-
motopy equivalent to M . While this result highlights that the sampling threshold ϵ 0 depends strictly
on the intrinsic geometry of M , it remains purely qualitative and existential. More recently, the
author of [27] provided a quantitative and practical analogue of Latschev’s result for manifolds,
which was subsequently extended to more general metric spaces with curvature bounds in [23].
F IGURE 2. [Left] An abstract simplicial complex K with planar vertices has been
depicted. [Middle] The shadow S ( K ) ⊂ R 2 has been shown as a subset of the
plane. [Right] A triangulation of the shadow is shown. The new shadow vertices
are shown in red.
1.1. Shadow of Complexes and Our Motivation. Our theoretical study of Vietoris–Rips com-
plexes and their shadows is motivated by the practical challenge of reconstructing the topology
an
```

## candidate-35 [atlas-general] — UNCONSUMED

**Title:** Persistent Homology based Graph Convolution Network for Fine grained 3D Shape Segmentation

**URL:** file:///ac6fce116289ed9634c58cb3c45cdd30db09473d041eed4300cb795562f85560/Persistent_Homology_based_Graph_Convolution_Network_for_Fine-grained_3D_Shape_Segmentation.pdf

**Description:** ICCV 2021 research paper proposing PHGCN, a Persistent Homology based Graph Convolution Network for fine-grained 3D shape segmentation. The model integrates persistent homology features from topological data analysis into GCN to capture multi-scale topological structures, and introduces a novel Persistence Diagram Loss to enforce topological correctness. Extensive experiments on 3D object-parts segmentation benchmarks show state-of-the-art performance over prior point cloud methods.

**Content extract (≤6k chars):**

```
2021 IEEE/CVF International Conference on Computer Vision (ICCV)
Persistent Homology based Graph Convolution Network for Fine-grained 3D
Shape Segmentation
Chi-Chong Wong Chi-Man Vong
University of Macau University of Macau
amilton.wong@connect.um.edu.mo cmvong@um.edu.mo
Abstract gions; ii) shape-dependent topological structures (e.g, han-
dles of objects, doorknobs, device wires). These properties
Fine-grained 3D segmentation is an important task in always exhibit in slim parts or multiple small connected
3D object understanding, especially in applications such components, which are semantically important to down-
as intelligent manufacturing or parts analysis for 3D ob- stream tasks, such as robotic manipulation. Sufficiently in-
jects. However, many challenges involved in such prob- terpreting such two main structures is essential for accu-
lem are yet to be solved, such as i) interpreting the com- rate 3D fine-grained semantic segmentation task. Failing
plex structures located in different regions for 3D objects; to tackle such challenges will drastically lower the perfor-
ii) capturing fine-grained structures with sufficient topol- mance of semantically understanding the 3D fine-grained
ogy correctness. Current deep learning and graph ma- objects and produce incoherent segmentation output, which
chine learning methods fail to tackle such challenges and is vital for intelligent manufacturing and robotic manipula-
thus provide inferior performance in fine-grained 3D anal- tion.
ysis. In this work, methods in topological data analysis In recent years, deep neural network based methods
are incorporated with geometric deep learning model for [6, 16, 21] and geometric learning methods [15, 27, 28] have
the task of fine-grained segmentation for 3D objects. We become the mainstream methods in 3D point cloud under-
propose a novel neural network model called Persistent standing tasks, from general 3D object classification to se-
Homology based Graph Convolution Network (PHGCN), mantic segmentation on objects and scenes. In retrospect
which i) integrates persistent homology into graph convolu- to these methods, it is found that they are not designed
tion network to capture multi-scale structural information specifically for the task of understanding fine-grained 3D
that can accurately represent complex structures for 3D ob- objects with complex structures or shape dependent topo-
jects; ii) applies a novel Persistence Diagram Loss ( L P D ) logical structures. Methods in [15, 27, 28] apply graph neu-
that provides sufficient topology correctness for segmenta- ral network (GNN) or graph convolutional network (GCN)
tion over the fine-grained structures. Extensive experiments model to extract features from geometrical structures in 3D
on fine-grained 3D segmentation validate the effectiveness point cloud. However, such approach only captures the
of the proposed PHGCN model and show significant im- pairwise relations represented by edges, since the neigh-
provements over current state-of-the-art methods. boring graphs constructed in GNN/GCN model only rep-
resent the pairwise relationships among 3D point clouds.
As a result, high dimensional relationships existed in com-
1. Introduction plex structures of fine-grained 3D objects cannot be finely
captured. The recent work PartNet model [31] applies cas-
Fine-grained 3D semantic segmentation is a task to se- cade binary labeling to represent a top-down recursive parts
mantically classify the labeling of each 3D point input in decomposition for hierarchical segmentation. However, the
detailed levels. It is an essential task for many applica- representation capability of binary labeling is limited by the
tions for detailed processing and analysis of 3D shapes, hierarchy depth and thus suffers from handling 3D objects
2021 IEEE/CVF International Conference on Computer Vision (ICCV) | 978-1-6654-2812-5/21/$31.00 ©2021 IEEE | DOI: 10.1109/ICCV48922.2021.00701 such as intelligent manufacturing, automatic interior design with multiple complex structures.
and furniture arrangement, autonomous robotic manipula- In fact, the geometric and topological information ex-
tion, human-machine interaction, 3D clothing analysis. isted in complex structure is the essential clue to under-
Segmenting fine-grained 3D objects involves many chal- stand the shapes of fine-grained objects. Topological Data
lenges, due to the specific properties in fine-grained 3D ob- Analysis (TDA) [3] is an emerging field which infers rele-
jects, such as i) complex structures located in different re- vant topological and geometric features from complex data.
978-1-6654-2812-5/21/$31.00 ©2021 IEEE 7078
DOI 10.1109/ICCV48922.2021.00701
Authorized licensed use limited to: University of North Carolina at Charlotte. Downloaded on April 27,2026 at 21:59:00 UTC from IEEE Xplore. Restrictions apply.
TDA uses a mechanism called complex filtration to con- 2. Preliminaries in Topological Data Analysis
struct the multi-scale topological structures for the input
point clouds, which extracts the high dimensional relation- Topological data analysis (TDA) [3] is an emerging field
ships existed in complex structures of point cloud, as illus- which goal is to capture the related topological and geomet-
trated in Fig. 1(a). Then, persistent homology, a tool in ric features from data of complex structure. In this section,
TDA, is applied on the resulting nested sequence of strictly a brief overview is provided to highlight the mechanism in
increasing subcomplexes, which are called filtered com- TDA. The details of TDA can be found in the seminal pa-
plexes, to compute the multi-scale topological features, rep- pers [11, 33].
resented as persistence barcodes and persistence diagram, 2.1. Simplicial Complex
as shown in Fig. 1(b) and (c). The 0-dim, 1-dim and 2-dim
persistent homological features in the resulting persistence As there is no direct approach in extracting topolog-
diagram correspond to the connecte
```

## candidate-36 [atlas-general] — UNCONSUMED

**Title:** 157 166

**URL:** file:///589347fa00acdb9a27f9499d06bf6dc84f9884c5cafc534f5d70913f761ea53f/157-166.pdf

**Description:** This Eurographics 2004 paper introduces the witness complex, a construction for computing topological invariants from point-cloud data using a small set of landmark points with the remaining points serving as 'witnesses' to edges and simplices. The authors demonstrate that witness complexes produce dramatically smaller simplicial approximations than standard Cech, Rips, or alpha-shape complexes while preserving homotopy type, and they integrate naturally with persistent homology for multi-scale analysis. They validate the approach on a 2-sphere benchmark and on Mumford's natural image patch dataset.

**Content extract (≤6k chars):**

```
Eurographics Symposium on Point-Based Graphics (2004)
M. Alexa, S. Rusinkiewicz, (Editors)
Topological estimation using witness complexes
Vin de Silva and Gunnar Carlsson †
Department of Mathematics, Stanford University, California, USA.
Abstract
This paper tackles the problem of computing topological invariants of geometric objects in a robust manner, using
only point cloud data sampled from the object. It is now widely recognised that this kind of topological analysis can
give qualitative information about data sets which is not readily available by other means. In particular, it can be
an aid to visualisation of high dimensional data. Standard simplicial complexes for approximating the topological
type of the underlying space (such as ˇ Cech, Rips, or α -shape) produce simplicial complexes whose vertex set has
the same size as the underlying set of point cloud data. Such constructions are sometimes still tractable, but are
wasteful (of computing resources) since the homotopy types of the underlying objects are generally realisable
on much smaller vertex sets. We obtain smaller complexes by choosing a set of ‘landmark’ points from our data
set, and then constructing a “witness complex” on this set using ideas motivated by the usual Delaunay complex
in Euclidean space. The key idea is that the remaining (non-landmark) data points are used as witnesses to the
existence of edges or simplices spanned by combinations of landmark points.
Our construction generalises the topology-preserving graphs of Martinetz and Schulten [MS94] in two direc-
tions. First, it produces a simplicial complex rather than a graph. Secondly it actually produces a nested family
of simplicial complexes, which represent the data at different feature scales, suitable for calculating persistent
homology [ELZ00, ZC04]. We find that in addition to the complexes being smaller, they also provide (in a precise
sense) a better picture of the homology, with less noise, than the full scale constructions using all the data points.
We illustrate the use of these complexes in qualitatively analyzing a data set of 3 × 3 pixel patches studied by
David Mumford et al [LPM03].
Categories and Subject Descriptors (according to ACM CCS) : I.3.5 [Computing Methodologies]: Computer Graph-
ics [Computational Geometry and Object Modeling]
1. Simplicial Approximation In this paper we focus on the analogous topological prob-
lem: how to find a representation of the data which can be
Given a point-cloud dataset sampled from an underlying used to compute topological invariants, robustly and effi-
space X , it is often desirable to build a simplicial complex S ciently. For example, the figure on the left is a (noisy) circle,
approximating the geometric or topological structure of X . and the figure on the right has three loop-shaped petals. How
For example, a laser scanning device applied to a solid ob-
ject might return the coordinates of thousands of points lying
on the objects 2-dimensional surface. A standard problem is
to build a triangular mesh from this unstructured collection
of points, perhaps for visual rendering. Such a mesh should
be a close geometrical approximation to X itself. Examples
of provably successful algorithms for surface reconstruction
can be found in the work of Amenta et al [ACDL02, AB99].
† Both authors have been supported in part by NSF grant DMS- does one extract this kind of topological information auto-
0101364. matically and reliably? There is increasing demand for such
© c The Eurographics Association 2004.
V. de Silva & G. Carlsson / Topological estimation using witness complexes
techniques; for example, Carlsson et al [ CCdS03 ] present we also define three families of complexes W ( D ; R , ν ) ,
algorithms for automatic feature-detection which depend on where ν = 0 , 1 , 2, dependent on a “feature size” parameter R .
being able to make accurate topological calculations. Any such family can be used to define persistent homology ,
which combines Betti number analysis with a notion of size
A natural approach is to represent the data by a sim-
(“persistence”) for the holes that are detected. Thus we can
plicial complex S , using the data points as vertices, and
exploit the powerful techniques of Edelsbrunner, Letscher
adding edges, triangles and higher-dimensional cells accord-
and Zomorodian [ ELZ00 ] to generate so-called persistence
ing to suitable rules. From S one can compute Betti numbers
b k = b k interval graphs for each family of complexes [ ZC04 ]. The
( S ) ; this is a standard procedure in classical algebraic
topological information carried in such an interval graph is
topology [ Mas91 ] for counting the k -dimensional holes of a
richer and more robust than a single Betti number by itself.
simplicial complex. If S is a faithful topological representa-
tion of X , then this effectively computes the numbers b k ( X ) , Our long-term goal is to put topological data analysis on
by proxy. The figures underlying the examples shown above a sound, quantifiable footing. To this end we give two ex-
are distinguished by their first Betti number b 1 : a circle has amples. The first example consists of points on the 2-sphere.
b 1 = 1, and a three-loop clover has b 1 = 3. The goal is to We compare the performance of witness complexes to a stan-
find an algorithm which produces simplicial complexes for dard construction, the Rips complex, in the task of obtaining
these data sets which have the same properties. the correct Betti numbers for the sphere. The second exam-
ple comes from a natural image database provided by David
The distinction between geometrical and topological ap-
Mumford [ LPM03 ] which exhibits rather subtle statistical
proximation may be seen in the following pictures. Twelve
behaviour. We feel that these examples vindicate the use of
witness complexes in topological data analysis.
We stress that our purpose in this paper is to provide a
detailed, motivated description of a family of constructions

```

## candidate-37 [atlas-general] — UNCONSUMED

**Title:** Deep Manifold Neural Network Mathematics

**URL:** file:///0f27a946acc923d2c4ba21677a7756d4e724b8ee40d3ff9c6f8eb26e29de7315/Deep_Manifold_Neural_Network_Mathematics.pdf

**Description:** A two-part research paper proposing the 'Deep Manifold' framework, which reinterprets neural networks as connected stacked piecewise-smooth manifolds governed by geometric structure rather than optimization objectives. The authors argue that geometry is the stable prior that determines what solutions can exist, and reformulate learning as Galerkin-type numerical fixed-point iteration on learned manifolds with Lagrangian constraints, rather than classical function optimization.

**Content extract (≤6k chars):**

```
Deep Manifold
Neural Network Mathematics
Max Ma and Gen-Hua Shi
2026.01
Deep Manifold Part 1: Anatomy of Neural Network Manifold, arXiv:2409.17592
Deep Manifold Part 2: Neural Network Mathematics, arXiv:2512.06563
Deep Manifold Part 1:Anatomy of Neural Network Manifold
Deep Manifold Part 1 : Anatomy of Neural Network Manifold, arXiv:2409.17592
Data Flow (Physical Domain)
Neural Network Mathematics
Neural Network Geometry
Geometry bestows the eye that beholds all things from above, a very ladder to the freedom
● Connected and stacked piecewise-smooth manifolds jointly form the
geometric structure of the representation space.
● Node covers act as the local units of these piecewise-smooth manifolds, and
their orientations change at every iteration.
● These piecewise-smooth manifolds are differentiable and integrable.
Geometry Rules
● Common AI View
○ Objectives(loss) + Optimization(parameter) determine the solution
○ Geometry emerges as a byproduct, secondary
● Deep Manifold View
○ Geometry determines what solutions can exist
○ Optimization only traverses a pre-shaped manifold
● Learning is inverse and non-identifiable
● Geometry is the only stable prior
● Geometry determines inference intrinsic pathways
Stacked Piecewise Manifold
● A manifold: a point, a line, a cycle, a triangle, an infinite-dimensional Banach manifold
● Image RGB: 3 stacked Pointwise Manifold
● Neural Network: connected, stretched, stacked piecewise Manifold
● Stacked Piecewise Manifold Benefit: High Order Nonlinear Data
Deep Manifold Part 1 : Anatomy of Neural Network Manifold, arXiv:2409.17592; Deep Manifold Part 2 : Neural Network Mathematics , arXiv:2512.06563
Y. LeCun is right for a single manifold, but why do Transformers work so well ?
● The exponential-decay critique treats generation as a single manifold trajectory with
independent failure at each step.
● Transformers operate on stacked piecewise manifolds , where deviations project onto
shared geometric subspaces.
● Error events overlap rather than compound. Generation stability follows union-bounded
geometry , not multiplicative probability collapse.
Deep Manifold Part 1 : Anatomy of Neural Network Manifold, arXiv:2409.17592; Deep Manifold Part 2 : Neural Network Mathematics , arXiv:2512.06563
Neural Network Algebra
Algebra is the science of operations, the silent one behind all transformation
● The coordinate system evolves with each iteration;
● Counting serves as the most primitive algebraic unit,
● Iterated-integral structure of forward propagation;
● Activation is propertyless
Neural Network Equation
An equation is the quiet connector that enables computation
● Fixed-Point Residual as the Primitive Equation
● Lagrangian Formulation of Neural Fixed Points
Deep Manifold Part 1 : Anatomy of Neural Network Manifold, arXiv:2409.17592; Deep Manifold Part 2 : Neural Network Mathematics , arXiv:2512.06563
Neural Network Stochastic
A stochastic world is an inequality world, but it is real
● Stochasticity is expressed through inequalities and group statistics based on
summation
● The statistical structure enables neural networks to learn the inherently
stochastic real world and naturally form stochastic fixed points.
● It is effortless
Neural Network Fixed Point
Fixed point theory is the theory of iteration, until fixed
● Iterations traverse billions of piecewise-smooth manifolds, giving rise to
innumerable fixed points and convergence paths within foundation models.
● Because the training data themselves contain high-order nonlinearity,
curvature (second derivatives), and moderate perturbations, the model can
distinguish the correct convergence direction toward a fixed point.
Deep Manifold Part 1 : Anatomy of Neural Network Manifold, arXiv:2409.17592; Deep Manifold Part 2 : Neural Network Mathematics , arXiv:2512.06563
Neural Network Boundary Condition
Boundary conditions give iteration purpose and direction
● Boundary conditions are the sole source of iterative direction and determine
the convergence path during training.
● When a foundation model lacks static fixed points, symmetric, weak, and
discrete boundary conditions become necessary to guide the convergence of
a high-order nonlinear system.
Learnable Numerical Computation
Mathematics & Numerical Computation
● Mathematics
○ Universal in principle: seeks analytical solutions that hold across domains
○ Mathematics excels at description; often not directly solvable or computable.
○ Structural limitation: analytical existence does not imply closed-form expressibility,
especially for high-order nonlinear, discontinuous, or stochastic systems.
● Numerical Computation
○ Galerkin method: a numerical solver that replaces exact solvability with weak consistency
on a chosen representation space.
○ Approximation theorem: a result guaranteeing that functions in a target class can be
approximated arbitrarily well by functions from a specified family, under a given metric.
discretization, approximation, iteration
○ Adaptable: empirical terms, adaptive meshes/layers, usable convergence over exactness.
○ Pragmatic: whatever works, as long as it converges.
Numerical computation can be deceptive. Without solid mathematical grounding, it may
advance remarkably far in practice—as seen in the supercomputer era, and again today in
AI. Scaling computational power does not imply scaling mathematical understanding.
Deep Manifold Part 1 : Anatomy of Neural Network Manifold, arXiv:2409.17592; Deep Manifold Part 2 : Neural Network Mathematics , arXiv:2512.06563
From Fixed Point to Learnable Computation
● Fixed point defines what learning is.
○ Beautiful descriptor, but not a solver; no numerical procedure
○ No notion of progress, No way to handle constraints (architecture, data)
● Lagrangian Formulation makes it solvable.
○ Lagrangian equilibrium = neural network fixed point
○ ℷ = boundary enforcer, g(θ) =0 architectural / data constraints
● Numerical iteration makes it real.
○ Mathematics becomes computation only when residuals are it
```

## candidate-38 [atlas-general] — UNCONSUMED

**Title:** quantitative toxicity prediction using topology based multitask deep neural networks

**URL:** file:///1d293ace4b1e5e507392c4c5e121beb534b70b9ba1fedc07fcb0b1aa88bc4708/quantitative-toxicity-prediction-using-topology-based-multitask-deep-neural-networks.pdf

**Description:** This research paper introduces Element-Specific Persistent Homology (ESPH) and topology-based multitask deep neural networks for quantitative toxicity prediction of small molecules. The authors construct Element-Specific Topological Descriptors (ESTDs) paired with deep learning, random forests, and gradient boosting, and propose a multitask strategy to leverage large datasets when handling small ones. Validation across four benchmark toxicity datasets shows the method outperforms state-of-the-art QSAR approaches.

**Content extract (≤6k chars):**

```
Article
Cite This: J. Chem. Inf. Model. 2018, 58, 520 − 531 pubs.acs.org/jcim
Quantitative Toxicity Prediction Using Topology Based Multitask
Deep Neural Networks
† , † , ‡ , ¶
Kedi Wu and Guo-Wei Wei *
† Department of Mathematics, ‡ Department of Electrical and Computer Engineering, and ¶ Department of Biochemistry and
Molecular Biology, Michigan State University, East Lansing, Michigan 48824, United States
* S Supporting Information
ABSTRACT: The understanding of toxicity is of paramount impor-
tance to human health and environmental protection. Quantitative
toxicity analysis has become a new standard in the fi eld. This work
introduces element speci fi c persistent homology (ESPH), an alge-
braic topology approach, for quantitative toxicity prediction. ESPH
retains crucial chemical information during the topological abstrac-
tion of geometric complexity and provides a representation of small
molecules that cannot be obtained by any other method. To inves-
tigate the representability and predictive power of ESPH for small
molecules, ancillary descriptors have also been developed based on
physical models. Topological and physical descriptors are paired with
advanced machine learning algorithms, such as the deep neural
network (DNN), random forest (RF), and gradient boosting decision
tree (GBDT), to facilitate their applications to quantitative toxicity predictions. A topology based multitask strategy is proposed
to take the advantage of the availability of large data sets while dealing with small data sets. Four benchmark toxicity data sets that
involve quantitative measurements are used to validate the proposed approaches. Extensive numerical studies indicate that the
proposed topological learning methods are able to outperform the state-of-the-art methods in the literature for quantitative
toxicity analysis. Our online server for computing element-speci fi c topological descriptors (ESTDs) is available at http://weilab.
math.msu.edu/TopTox/.
1. INTRODUCTION support vector machine, 1,4,5 and random forest. 6 These meth-
ods have advantages and disadvantages 7 
Toxicity is a measure of the degree to which a chemical can due to their statistical
adversely a ff ect an organism. These adverse e ff ects, which are natures. For instance, linear models overlook the relatedness
called toxicity end points, can be either quantitatively or qualita- between di ff erent features, while the nearest neighbor method
tively measured by their e ff ects on given targets. Qualitative largely depends on the choice of descriptors. To overcome
toxicity classi fi es chemicals into toxic and nontoxic categories, these di ffi culties, more re fi ned and advanced machine learning
methods have been introduced. Multitask (MT) learning 8 
while quantitative toxicity data set records the minimal amount was
of chemicals that can reach certain lethal e ff ects. Most toxicity proposed partially to deal with data sparsity problems, which
See https://pubs.acs.org/sharingguidelines for options on how to legitimately share published articles. tests aim to protect human from harmful e ff ects caused by chem- are commonly encountered in QSAR applications. The idea of
Downloaded via UNIV OF NORTH CAROLINA AT CHARLOTTE on April 27, 2026 at 21:58:23 (UTC). ical substances and are traditionally conducted in in vivo or in vitro MT learning is to learn the so-called “ inductive bias ” from
manner. Nevertheless, such experiments are usually very time- related tasks to improve accuracy using the same representa-
consuming and cost intensive, and even give rise to ethical con- tion. In other words, MT learning aims at learning a shared and
cerns when it comes to animal tests. Therefore, computer-aided generalized feature representation from multiple tasks. Indeed,
methods, or in silico methods, have been developed to improve MT learning strategies have brought new insights to bioinfor-
prediction e ffi ciency without sacri fi cing too much of accuracy. matics since compounds from related assays may share features
The quantitative structure − activity relationship (QSAR) approach at various feature levels, which is extremely helpful if the data set
is one of the most popular and commonly used approaches. is small. Successful applications include splice-site and MHC-I
binding prediction 9 
The basic QASR assumption is that similar molecules have sim- in sequence biology, gene expression anal-
ysis, and system biology. 10
ilar activities. Therefore, by studying the relationship between
Recently, deep learning (DL), 11,12 
chemical structures and biological activities, it is possible to pre- particularly convolutional
dict the activities of new molecules without actually conducting neural network (CNN), has emerged as a powerful paradigm to
lab experiments. render a wide range of the-state-of-the-art results in signal and
There are several types of algorithms to generate QSAR models:
linear models based on linear regression and linear discriminant Received: September 15, 2017
analysis; 1 nonlinear models including nearest neighbor, 2,3 Published: January 9, 2018
© 2018 American Chemical Society 520 DOI: 10.1021/acs.jcim.7b00558
J. Chem. Inf. Model. 2018, 58, 520 − 531
Journal of Chemical Information and Modeling Article
information processing fi elds, such as speech recognition 13,14 points makes our topology based multitask strategy a viable
and natural language processing. 15,16 Deep learning architecture approach to quantitative toxicity predictions.
is essentially based on arti fi cial neural networks. The major dif-
ference between deep neural network (DNN) models and non- 2. METHODS AND ALGORITHMS
DNN models is that DNN models consist of a large number of In this section, we provide a detail discussion about molecular
layers and neurons, making it possible to construct abstract descriptors used in this study, including element-speci fi c topo-
features. logical descriptors and auxiliary descriptors calculated from
Geometric represe
```

## candidate-39 [atlas-general] — UNCONSUMED

**Title:** ManCAR: Manifold-Constrained Latent Reasoning with Adaptive Test-Time Computation for Sequential Recommendation

**URL:** https://arxiv.org/abs/2602.20093

**Description:** ManCAR is a framework for sequential recommendation that constrains latent multi-step reasoning to a collaborative manifold via a local intent prior, with adaptive test-time stopping to prevent latent drift and over-refinement.

**Content extract (≤6k chars):**

```
Title: ManCAR: Manifold-Constrained Latent Reasoning with Adaptive Test-Time Computation for Sequential Recommendation
Authors: Kun Yang, Yuxuan Zhu, Yazhe Chen, Siyao Zheng, Bangyang Hong, Kangle Wu, Yabo Ni, Anxiang Zeng, Cong Fu, Hui Li
Year: 2026
Categories: cs.IR
arXiv: 2602.20093

Abstract:
Sequential recommendation increasingly employs latent multi-step reasoning to enhance test-time computation. Despite empirical gains, existing approaches largely drive intermediate reasoning states via target-dominant objectives without imposing explicit feasibility constraints. This results in latent drift, where reasoning trajectories deviate into implausible regions. We argue that effective recommendation reasoning should instead be viewed as navigation on a collaborative manifold rather than free-form latent refinement. To this end, we propose ManCAR (Manifold-Constrained Adaptive Reasoning), a principled framework that grounds reasoning within the topology of a global interaction graph. ManCAR constructs a local intent prior from the collaborative neighborhood of a user's recent actions, represented as a distribution over the item simplex. During training, the model progressively aligns its latent predictive distribution with this prior, forcing the reasoning trajectory to remain within the valid manifold. At test time, reasoning proceeds adaptively until the predictive distribution stabilizes, avoiding over-refinement. We provide a variational interpretation of ManCAR to theoretically validate its drift-prevention and adaptive test-time stopping mechanisms. Experiments on seven benchmarks demonstrate that ManCAR consistently outperforms state-of-the-art baselines, achieving up to a 46.88% relative improvement w.r.t. NDCG@10. Our code is available at https://github.com/FuCongResearchSquad/ManCAR.
```

## candidate-40 [atlas-general] — UNCONSUMED

**Title:** 2501.02015v1

**URL:** file:///8c6a7c03ac372782cbac1b3457c24babc2a05164b76c1ad03b81e01300008035/2501.02015v1.pdf

**Description:** This research paper presents KANS (Knowledge discovery graph Attention Network for Soft sensing), a framework for inferring hard-to-measure industrial process variables from easy-to-measure sensor data. The method introduces unsupervised contrastive graph structure learning to discover sensor relationships without predefined topology, combined with graph attention-based representation learning for parallel multivariate time series processing. Experimental results on real-world industrial datasets demonstrate KANS significantly outperforms baseline and state-of-the-art soft sensing methods while providing interpretable knowledge discovery of sensor correlations.

**Content extract (≤6k chars):**

```
KANS: Knowledge Discovery Graph Attention Network for Soft
Sensing in Multivariate Industrial Processes
Hwa Hui Tew 1 , Gaoxuan Li 1 , Fan Ding 1 , Xuewen Luo 1 Junn Yong Loo 1 , ∗ ,
Chee-Ming Ting 1 , Ze Yang Ding 2 , Chee Pin Tan 2
Abstract — Soft sensing of hard-to-measure variables is often the fast-evolving industrial systems [3]. There are two main
crucial in industrial processes. Current practices rely heavily categories of soft sensors: knowledge-based, and data-driven
on conventional modeling techniques that show success in methods. Developing a high-fidelity knowledge-based soft
improving accuracy. However, they overlook the non-linear na-
ture, dynamics characteristics, and non-Euclidean dependencies sensor relies on having a deep understanding of the process
between complex process variables. To tackle these challenges, mechanisms, as well as extensive experience and knowledge
we present a framework known as a Knowledge discovery about the system process. However, the increasing complex-
graph Attention Network for effective Soft sensing (KANS). ity of industrial processes have given rise to the difficulty of
Unlike the existing deep learning soft sensor models, KANS can meeting the basic preconditions. Therefore, for practicability,
discover the intrinsic correlations and irregular relationships
between the multivariate industrial processes without a prede- data-driven modeling has become the favorable soft sensing
fined topology. First, an unsupervised graph structure learning modeling method [4].
method is introduced, incorporating the cosine similarity be- Conventional data-driven approaches such as support vec-
tween different sensor embedding to capture the correlations tor regression (SVR) and partial least square regression
between sensors. Next, we present a graph attention-based (PLR) have been successfully applied to soft sensing in a
representation learning that can compute the multivariate
data parallelly to enhance the model in learning complex wide range of industrial applications [5]–[7]. Nonetheless,
sensor nodes and edges. To fully explore KANS, knowledge these models exhibit difficulty in handling multi-modal, high-
discovery analysis has also been conducted to demonstrate the dimensional sensor data associated with many complex real-
interpretability of the model. Experimental results demonstrate world systems. Recently, deep learning techniques such as
that KANS significantly outperforms all the baselines and state- artificial neural network (ANN), convolutional neural net-
of-the-art methods in soft sensing performance. Furthermore,
the analysis shows that KANS can find sensors closely related works (CNN) and recurrent neural networks (RNN) have
to different process variables without domain knowledge, sig- demonstrated superior capability in capturing the complex
nificantly improving soft sensing accuracy. non-linearity and rich dynamics underlying most systems.
Keywords- Soft sensing, graph attention network, knowledge This is attributed to the advanced expressiveness of these
discovery. deep models, allowing them to learn accurate representations
I. INTRODUCTION of the data [8]–[10]. Nevertheless, these conventional deep
models could not explicitly capture the meaningful non-
The fast advances in modern cyber-physical systems has
Euclidean correlations between the sensors; incorporating
fueled the ever increasing demand of highly-specialized
this spatial information could potentially improve soft sens-
sensors for quality measurements in interlinked multivariate
ing performance.
industrial processes. For example, a chemical process plant
Recent works have shown promising results in leveraging
requires numerous acquisitions such as pressure, flow rate,
a graph representation of the multivariate soft sensor data to
density, temperature, and current via physical or hardware
account for the underlying non-Euclidian spatial correlations
sensors for continuous monitoring of key quality variables
[11]–[14]. In particular, graph neural networks (GNN) have
that are critical for process operation [1]. However, physical
arXiv:2501.02015v1 [cs.LG] 2 Jan 2025 shown success in effectively modeling and analyzing graph-
sensors often suffer from a variety of limitations such as
structured data. For example, Jia et al . considered spatiotem-
susceptible to harsh conditions, need for regular maintenance
poral relations in GNN to predict the penicillin fermentation
and high costs. To overcome these limitations, a soft sensor
process [15]. Wang et al . utilized GNN to predict the volatile
can be developed as an alternative to the physical hardware
fatty acid concentration of kitchen waste [16]. Feng et al .
sensors [2].
applied GNN in predicting endpoint composition in steel
A soft sensor is capable of inferring hard-to-measure
[17]. However, they overlooked the use of rich graph em-
variables by utilising easy-to-measure variables as inputs. In
bedding for both nodes and edges within the graph structure
comparison to conventional hardware sensors, soft sensors
of soft sensing data, instead representing them exclusively as
are less expensive to build, more efficient, and flexible in
scalar process variables. Furthermore, Wang et al . proposed a
terms of their adaptability, customizability, and scalability to
fused representation of knowledge and a data-driven method
1 The authors are with the School of Information Technology, Monash that can enhance soft sensor modeling [18]. Nevertheless, it
University Malaysia, Jalan Lagoon Selatan, Bandar Sunway, 47500 Selan- did not learn the nodes and edges inherently, as opposed to
gor, Malaysia.
2 having them as prior knowledge, which requires extensive
The authors are with the School of Engineering, Monash University
Malaysia, Jalan Lagoon Selatan, Bandar Sunway, 47500 Selangor, Malaysia. human knowledge. Besides, Chen et al . presented a deep
∗ Corresponding author. attention GNN to explore data latent interactions of industrial

```
