### DeepCLIP
- plot: >0 residues with binding site potential, <0 no binding affinity/preference

**7SK RNA - LARP7** / 1  
- interaction predicted: 1
- region: 0, because region of interest was already provided as input
- residues: 0
  - relevant stem-loop top (310-314) is not below zero for both models, but also not highly positive, U-stretch (3'end) below zero
  - overall score (0-1): 0.4325 and 0.3033


### MEME

**7SK RNA - LARP7** / 2    
- RNA: motif 1 covers exact hairpin top --> 1 point + 1 point for confidence
- protein:
  - RPI-involved regions covered by different motifs, but complete protein sequence in general is covered with motifs
    - RNP3 motif in ꞵ2 (483-485): YVD --> MEME motif 2 (turquoise)
    - ⍺3 covered with MEME motif 7 (dark blue), starting from 527 and 539, 8aa long
  --> 1 point for regions + 1 point for confidence

**MS2 coat** / 1  
- RNA motif found
- multiple motifs for protein, no further context

**VP30 - leader** / 1  
- RNA motifs are found although there is nothing known there
- protein: MEME finds motif NYRGEY which is starting directly downstream from the known conserved RXRSXXS motif (aa 27-33)

**ToxIN** / 1    
- RNA:
  - MEME motif 1 covers no specifically-mentioned RPI bases
  - MEME motif 2 covers 5'-end
- protein:   
  - interacting regions covered by different motifs, but again the whole protein sequence in general is covered with motifs  
  Asp19, Lys20, Val21, Asn23 --> partly motif 10  
  Tyr29, Lys33 --> motif 7  
  Thr52, Ser53, Lys55, His58 --> motif 1  
  Glu73 and Asn79 --> partly motif 8  
  Phe88 --> motif 5  
  Leu99, Leu100 and Leu102 --> partly motif 9  
  Leu114, Tyr115, Lys116, Gln117, Leu118 and Arg122 --> partly motif 3, partly motif 4  


### hybridNAP
We define residues as "likely to interact" with at least 2 of the 3 values (RAA, RSA, ECO) having "high binding probability" (green), as well as the predicted propensity being above threshold (green).  

**7SK RNA - LARP7** / 1  
- interaction predicted: 1
- a few residues predicted as interaction-likely, which are not part of xRRM domain (around 275, 360, 580)
- RPI-involved residues in xRRM domain: only R496 predicted (highly important) and K543, maybe region around 550 somewhat related

**MS2 coat** / 3   
- interactions predicted: 1
- regions and residues known from literature are predicted overall (all or 2/3 values are highlighted green)
- but: some residues also qualified as interacting, although not described in literature

**VP30 - leader** / 1    
- interactions predicted: 1
- important residues 26-40 not really there; other non-RPI residues with much higher values (e.g. Arg11)

**ToxIN** / 1  
- interaction predicted: 1
- correctly predicted RPI residues: only Lys2, Lys33, Lys55; no others
- predicted residues which are not directly RPI involved: Met113, Arg136, Arg158


### DRNAPred
- prediction as RNA binding: probability score >0.1493, binary RNA score = 1, upper case aa  

**7SK RNA - LARP7** / 0  
- no aa predicted as RNA binding

**MS2 coat** / 0    
- no aa predicted as RNA binding

**VP30 - leader** / 0   
- no aa predicted as RNA binding

**ToxIN** / 0  
- no aa predicted as RNA binding


### RBPPred
**7SK RNA - LARP7** / 1  
- interaction predicted as 1/yes   

**MS2 coat** / 1    
- interaction predicted as 1/yes   

**VP30 - leader** / 1    
- interaction predicted as 1/yes   

**ToxIN**  / 0  
- predicted as non-interacting  


### KYG
- side note from FAQ: "The question that the prediction method is trying to answer is "Here is a RNA-binding protein. Where is the RNA binding surface?" Therefore, if one perform prediction on non-RNA-binding proteins, the usage is out of the range of the question that we tried to answer by the method."

**7SK RNA - LARP7** / 1  
- interaction predicted: 1
- the plot represents one chain copy, but structure and score file contain both
- according to structure (+ score), the most C-terminal residues of chain B are likely for interaction, but these are just unstructured terminal residues not really involved in RPI
- other positive residue scores at Asp485A, Ile523A, 525A-528A + Arg531A (also in B) --> last few are involved in RPI, but further literature-RPI residues have strong negative scores predicted
- score: two chains are the same but got different scores per residue --> inconclusive reliability/confidence

**MS2 coat** / 1    
- interaction predicted: 1
- most important amino acids (https://doi.org/10.1016/S0969-2126(01)00156-3, https://doi.org/10.1038/371623a0) got a negative or near-zero score
- other residues show higher scores, although not mentioned in literature

**VP30 - leader** / 0    
- the provided PDB structure does not cover the interacting region from the literature and therefore no true positive prediction is expected --> nevertheless residues are predicted as interacting   

**ToxIN** / 1  
- interaction predicted: 1
- structure visualization: residues close to the RNA molecule are categorized as unlikely to interact
- attention: residue numbering was changed: PDB sequence covers 194aa, but with KYG only 168aa (KYG cuts the first 4aa and the C-terminus at position 173)
- positive residue scores (plot+score table): Pro34(38), Gly37(41), Ser53(57)#, Arg54(58)#, Asn55(59), Asp56(60), Lys57(61), Asn58(62), Arg74(78), Gln138(142)-Gly150(154) (except Leu148) (original sequence numbering in brackets, # indicates literature-known RPI residues) --> only two RPI residues
- many RPI-important residues got strong negative score


### aaRNA
- "A blue dashed line on the binary plot indicates the cutoff (0.164) under a stringency of 85% expected specificity evaluated from the training dataset. Residues with predicted scores greater than this cutoff are viewed as binding residues."

**7SK RNA - LARP7** / 1.5  
- interaction predicted: 1
- predicted residues above threshold in the binary plot (blue line): T447, R468, Y483, Y510 + T511 + E512, K535 --> only Y483 and K535 RPI involved
- high scoring residues in PDB structure with binding propensity annotation (AARNA3039767W_A_BP.pdb): T447, R468, Y483, R496, 508+510+511+512, K515+K516, K520, K535 --> two most important residues Y483 and R496 covered, but others not (half point)

**MS2 coat** / 2    
- interaction predicted: 1
- multiple aa correctly predicted above threshold: Ser47, Arg49, Lys61, Tyr85, Asn87
- other important RPI residues are not covered though: Val29, Thr45; further residues are somewhere near the threshold
- some aa far above threshold and not described in literature: Asn27, Ser35, Asn36, Arg38, Tyr129

**VP30 - leader** / 0   
- the provided PDB structure does not cover the interacting region from the literature and therefore no true positive prediction is expected --> nevertheless residues are predicted as interacting   
0 Punkte

**ToxIN** / 1.5  
- interaction predicted: 1
- predicted residues above threshold in the binary plot (blue line): Lys2#, Ser53#, Pro54, Lys56, Lys62, Tyr110# (# indicates literature-known RPI residues)
- in structure visualization, there are almost no residues highlighted as likely
- high scoring residues (>10) in PDB structure with binding propensity annotation (AARNA2844120W_A_BP.pdb): Lys2#, Tyr4, Ser53#, Pro54, Lys55#, Lys56, Trp57, Asn60, Lys62, Ser64, Asn85, Met89, Asn107, Tyr110#, Arg112, Lys116#, Arg122#, Gln145


### NucleicNet
- colors indicate RNA binding spots for: C (red), U (magenta), A (blue), G (cyan), P (yellow), R (green)

**7SK RNA - LARP7** / 2  
- interaction predicted: 1
- color-coded spots: stem-loop and U-rich stretch of RNA are surrounded by protein annotations
- protein annotations cover helix ⍺3, but nothing really for ꞵ3 and ꞵ2

**MS2 coat** / 1  
- interaction predicted: 1  
- many residues for which conclusions about interaction are hard to make, visualization is nice but difficult for detailed evaluation

**VP30 - leader** / 0    
- the provided PDB structure does not cover the interacting region from the literature and therefore no true positive prediction is expected --> nevertheless residues are predicted as interacting   

**ToxIN** / 1.5
- interaction predicted: 1
- annotations at RPI relevant regions: around amino acids 20, 50-70, 100
- also many annotations at regions not described for RPI


### RPISeq
**7SK RNA - LARP7** / 0.5  
- interaction predicted: 1 and 0 for the two classifiers, respectively (probabilities: 0.8 (RF) and 0.38 (SVM))

**MS2 coat** / 2    
- interaction predicted: 1 (both classifiers)
- both classifiers above 70% (RF: 1 and SVM: 0.96)

**VP30 - leader** / 1    
- interaction predicted: 1
- RF only slightly above threshold (0.55), SVM more confident (0.95)

**ToxIN** / 0.5  
- interaction predicted: 0 and 1 for the two classifiers, respectively (probabilities: 0.4 (RF) and 0.92 (SVM))


### XRPI
**7SK RNA - LARP7** / 1  
- interaction predicted: 1 (scores: 0.7544 (RPI2825), 0.5020 (RPI390))

**MS2 coat** / 2    
- interaction predicted: 1
- both classifiers highly confident (RPI2825: 0.9969, RPI390: 0.9191)

**VP30 - leader** / 1    
- interaction predicted: 1 (RPI390 model, score: 0.7075)
- RPI2825 model is just below the threshold (0.4775)

**ToxIN** / 0.5     
- interaction predicted: 1 and 0 for the two classifiers, respectively (scores: 0.9681 (RPI2825), 0.4638 (RPI390))


### PRIdictor
- results differ between web server and web application

**7SK RNA - LARP7** / 0.5  
- web server: no protein residues reaches threshold for interaction
- web application: only 1 aa and a handful of bases slightly above classification threshold of 0.5, but all not RPI involved

**MS2 coat** / 1    
- interaction predicted: 1
- RNA predictions look fine
- protein predictions not really: residues 44,46,49,50,52 are labeled as binding, according to literature only Arg49 is described as part of the RPI. other residues are missing

**VP30 - leader** / 2    
- interaction predicted: 1
- web server: predicts some interactions, but only Arg36 of interest
- web application: predicts more interacting residues, also within the RPI-important arginine-rich region. furthermore a lot of residues which are not described in the literature

**ToxIN** / 1  
- interaction predicted: 1
- web server: residues above threshold: Lys55, Lys56, Trp57, Ser65, Ser67, Asn107, Ser132, Arg136
- web application:
  - protein: Lys55, Trp57, Ser67, Arg122, Ser132, Arg136, Lys143
  - RNA: 5'end correctly predicted, but other highly involved bases (A6(10) and A32(36)) categorized as very unlikely
- only Lys55 and Arg122 mentioned in literature

### catRAPID
**7SK RNA - LARP7** / 1  
- interaction predicted: 1
- involved regions/residues not predicted as interacting, instead others which are not involved in RPI

**MS2 coat** / 1    
- interaction predicted: 1
- RNA bases all above threshold for interaction
- protein: literature residues are missing, instead aa 0-10 and ~110 are predicted
- especially relevant residues Tyr85, Asn87, Glu89, Thr91 are predicted with negative binding scores

**VP30 - leader** / 1    
- interaction predicted: 1
- interactions from literature not predicted, instead C-terminus highly interactive

**ToxIN** / 1  
- interaction predicted: 1
- no strongly predicted regions (likely or unlikely)
  - protein: N-terminal region predicted unlikely but would interact in molecule; likely region at around position 60 fits; other predicted regions not matching
  - RNA: no specific regions predicted


### PLIP
**7SK RNA - LARP7** / 4  
- interaction predicted: 1
- interacting region fits
- residues:
  - RNA correctly covered at U-stretch and hairpin loop top
  - protein: all 3 structural elements covered, almost no non-RPI-residues predicted
  - interacting partners also assigned accordingly

**MS2 coat** / 3    
- interaction predicted: 1
- all predicted residues are described in the literature (true positives)
- but: around half of residues mentioned in the literature are missing from the prediction (e.g. Arg49, Lys57, Asn87)
- no false positives predicted

**VP30 - leader** / na    
- not usable because RNA molecule is missing from PDB structure

**ToxIN** / 4  
- interaction predicted: 1
- almost all RPI involved residues/regions covered
- for both RNA and protein correct corresponding interaction partner residues assigned


### PredPRBA
- binding free energy represents RNA-protein binding affinity

**7SK RNA - LARP7** / 1  
- interaction predicted: 1 (energy: -9.9kcal/mol)

**MS2 coat** / 1   
- interaction predicted: 1 (energy: -10.81kcal/mol)

**VP30 - leader** / na  
- calculations never completed

**ToxIN** / 1  
- interaction predicted: 1 (energy: -8.18kcal/mol)


### PRIHotscore
- value>2: hot spot, 1>value>2: warm spot

**7SK RNA - LARP7** / 3  
- interaction predicted: 1
- hot spots: Y483, R548 / warm spot: R468, R472, R496, R540, K543, L544, Q546
- almost all of the predicted residues are RPI involved, the two most important ones covered
- non-interacting residues not predicted (true negatives)

**MS2 coat** / 3   
- interaction predicted: 1
- regions predicted correcly
- most important residues predicted, although not all of them as warm/hot spots

**VP30 - leader** / na  
- not usable because RNA molecule is missing from PDB structure

**ToxIN** / 3  
- interaction predicted: 1
- # are RPI involved -> predicted residues are mostly RPI involved or neighboring residues, but some are missing
  - hot spots: Asn79#, Leu81, Met113, Tyr115#, Lys116#, Gln119, Arg122#, Leu138, Met144
  - warm spots: Lys2#, Lys20#, Trp57, Leu66, Asn74, Lys87, Phe88#, Leu99#, Leu102#, Tyr110#, Arg112, Gln117#, Leu118#, Lys143


### OPRA
- colored structure visualization: red = most favorable residues, i.e., the predicted interface
- values below -1 trustworthy

**7SK RNA - LARP7** / 2  
- interaction predicted: 1
- residues predicted in chain A with negative OPRA value near -1
- many negative values predicted for residues in helix ⍺3, also in RNP3 motif; but not for beta-sheets

**MS2 coat** / 1    
- interaction predicted: 1
- no residue predicted with a score below -1; the most important amino acids (according to the literature) look like background noise
- few other residues seem interacting

**VP30 - leader** / 2    
- the provided PDB structure does not cover the interacting region from the literature and therefore no true positive prediction is expected
- many residues are above -1 -> true negatives   

**ToxIN** / 2  
- interaction predicted: 1
- residues in chain A with negative OPRA value near -1
- many residues which are RPI involved have negative values, but generally there are many negative values predicted


### COACH
**7SK RNA - LARP7** / 2  
- interaction predicted: 1
- multiple RPI residues covered in ꞵ3 and especially ⍺3
- side note: residue probabilities do not match in all cases between txt files and Bsites files
- confident prediction in "true negative" manner: low confidence score (all models <0.08)

**MS2 coat** / 4    
- interaction predicted: 1
- many residues from the literature show high probability (true positive prediction)
- except for a few exceptions (Cys46, Glu63), all other (non-RPI) residues show low probability

**VP30 - leader** / 2    
- the provided PDB structure does not cover the interacting region from the literature and therefore no true positive prediction is expected
- true negative prediction: nothing is predicted really
- only residues 55, 71 and 99 show >0.5 (0.63, 0.59, 0.60)

**ToxIN** / 2  
- interaction predicted: 1 (0.84 score)
- many residues predicted correctly (#), but also non-interacting ones covered:
  - 15, 19#, 20#, 21#, 22, 23#, 29#, 30, 31, 33#, 51, 52#, 53#, 54, 55#, 57, 60, 62, 63, 64, 65, 66, 67, 73#, 74, 79#, 80, 81, 82, 87, 88#, 100#, 102#, 109, 110#, 113, 114#, 115#, 116#, 117#, 118#, 119, 122#, 123, 127, 134, 137, 138, 141, 143, 144

### DeepSite
**7SK RNA - LARP7** / 1.5  
- interaction predicted: 1
- some regions correct (helix ⍺3, end of ⍺3), but also many residues which are not part of RPI

**MS2 coat** / 1    
- interaction predicted: 1
- residue 23 is not covered, but its neighbor
- all other residues not predicted

**VP30 - leader** / 0    
- the provided PDB structure does not cover the interacting region from the literature and therefore no true positive prediction is expected --> nevertheless residues are predicted as interacting   

**ToxIN** / 3  
- interaction predicted: 1
- almost all important residues covered, but also some non-RPI ones predicted
- regions/residues covered by "interaction centers":   
  - Lys2, Phe3 / Leu99, Leu100 and Leu102
  - Tyr29, Lys33
  - Thr52, Ser53
  - Glu73 and Asn79
  - Tyr110
  - Leu114, Tyr115, Lys116, Gln117, Leu118 and Arg122

________

Not able to evaluate (no assigned evaluation score):
- RBPmap: not applicable to our examples (no matching data available)
- aPRBind: not installable/hard to use
- GraphBind: no results provided/ run not done
- IPMiner: not installable
- beRBP: non-solvable error during input submission
- Prime3D2D: computations never finished
- RsiteDB: non-solvable error during input submission
- Prince: no results are presented
- 3dRPC: no feedback of web server, no results are provided
