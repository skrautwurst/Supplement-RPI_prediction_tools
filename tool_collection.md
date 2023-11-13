Used review papers for tool gathering

* Zhang 2019 [https://doi.org/10.1093/bib/bbx168](https://doi.org/10.1093/bib/bbx168)
* Yan 2016 [https://doi.org/10.1093/bib/bbv023](https://doi.org/10.1093/bib/bbv023)
* Corley 2020 [https://doi.org/10.1016/j.molcel.2020.03.011](https://doi.org/10.1016/j.molcel.2020.03.011)
* Marchese 2016 [https://doi.org/10.1002/wrna.1378](https://doi.org/10.1002/wrna.1378)
* Pan 2019 [https://doi.org/10.1002/wrna.1544](https://doi.org/10.1002/wrna.1544)
* Wei 2022 [https://doi.org/10.1093/bib/bbab540](https://doi.org/10.1093/bib/bbab540)
* Miao 2015 [https://doi.org/10.1371/journal.pcbi.1004639](https://doi.org/10.1371/journal.pcbi.1004639)

**_Available prediction tools_**

<table>
  <tr>
   <td><strong>Tool</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Year</strong>
   </td>
   <td><strong>Citations</strong>
<p>
<strong>(Google Scholar)</strong>
   </td>
   <td><strong>Link & access</strong>
   </td>
   <td><strong>Input</strong>
   </td>
   <td><strong>Prediction output</strong>
   </td>
   <td><strong>Notes</strong>
   </td>
  </tr>
  <tr>
   <td>RPISeq
   </td>
   <td>Muppirala et al.
<p>
<a href="https://doi.org/10.1186/1471-2105-12-489">https://doi.org/10.1186/1471-2105-12-489</a>
   </td>
   <td>2011
   </td>
   <td>399
   </td>
   <td><a href="http://pridb.gdcb.iastate.edu/RPISeq/">http://pridb.gdcb.iastate.edu/RPISeq/</a>
<p>
web server
   </td>
   <td>RNA and protein sequence
   </td>
   <td>score result (interaction probability)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>XRPI
   </td>
   <td>Jain et al.
<p>
<a href="https://doi.org/10.1038/s41598-018-27814-2">https://doi.org/10.1038/s41598-018-27814-2</a>
   </td>
   <td>2018
   </td>
   <td>15
   </td>
   <td><a href="https://universe.bits-pilani.ac.in/goa/aduri/xRPI">https://universe.bits-pilani.ac.in/goa/aduri/xRPI</a>
<p>
stand alone
<p>
<a href="http://xrpi.ddns.net/">http://xrpi.ddns.net/</a>
<p>
web server
   </td>
   <td>RNA and protein sequence
   </td>
   <td>score result (interaction probability)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>PLIP
   </td>
   <td>Adasme et al.
<p>
<a href="https://doi.org/10.1093/nar/gkab294">https://doi.org/10.1093/nar/gkab294</a>
   </td>
   <td>2021
   </td>
   <td>325 (1333 on previous publication from 2015)
   </td>
   <td><a href="https://plip-tool.biotec.tu-dresden.de/plip-web/plip/index">https://plip-tool.biotec.tu-dresden.de/plip-web/plip/index</a>
<p>
stand alone and web server
   </td>
   <td>determined 3D structure / PDB file
   </td>
   <td>interacting residues of RNA and protein in structural context (+ bond type)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>PRI Hotscore
   </td>
   <td>Krüger et al.
<p>
<a href="https://doi.org/10.1261/rna.066464.118">https://doi.org/10.1261/rna.066464.118</a>
   </td>
   <td>2018
   </td>
   <td>44
   </td>
   <td><a href="https://pri-hotscore.labs.vu.nl/main.php">https://pri-hotscore.labs.vu.nl/main.php</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file of RP-complex
   </td>
   <td>interacting residues of protein in structural context
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>PredPRBA
   </td>
   <td>Deng et al.
<p>
<a href="https://doi.org/10.3389/fgene.2019.00637">https://doi.org/10.3389/fgene.2019.00637</a>
   </td>
   <td>2019
   </td>
   <td>24
   </td>
   <td><a href="http://predprba.denglab.org/">http://predprba.denglab.org/</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file
   </td>
   <td>predicted binding free energy (ΔG) between protein and RNA chain of PDB complex
   </td>
   <td>gradient boosting regression tree models with learned features from protein and RNA sequence and structure (data set)
   </td>
  </tr>
  <tr>
   <td>NucleicNet
   </td>
   <td>Lam et al.
<p>
<a href="https://doi.org/10.1038/s41467-019-12920-0">https://doi.org/10.1038/s41467-019-12920-0</a>
   </td>
   <td>2019
   </td>
   <td>57
   </td>
   <td><a href="http://www.cbrc.kaust.edu.sa/NucleicNet/">http://www.cbrc.kaust.edu.sa/NucleicNet/</a>
<p>
web server
<p>
<a href="https://github.com/jhmlam/NucleicNet/wiki">https://github.com/jhmlam/NucleicNet/wiki</a>
<p>
stand alone
   </td>
   <td>determined 3D structure / PDB file (protein or both)
   </td>
   <td>protein surface analysis:
<p>
Pymol session with top binding sites for RNA chains
<p>
logo: weblogo of RNA-protein complex
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>PRIdictor
   </td>
   <td>Tuvshinjargal et al.
<p>
<a href="https://doi.org/10.1016/j.biosystems.2015.10.004">https://doi.org/10.1016/j.biosystems.2015.10.004</a>
   </td>
   <td>2016
   </td>
   <td>43
   </td>
   <td><a href="http://www.rnainter.org/PRIdictor/">http://www.rnainter.org/PRIdictor/</a>
<p>
web server
<p>
<a href="http://bclab.inha.ac.kr/pridictor/usage.html">http://bclab.inha.ac.kr/pridictor/usage.html</a>
<p>
web application
   </td>
   <td>RNA and protein sequence
   </td>
   <td>interaction probability per residue for RNA and protein
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>RsiteDB
   </td>
   <td>Shulman-Peleg et al.
<p>
<a href="https://doi.org/10.1016/j.jmb.2008.03.043">https://doi.org/10.1016/j.jmb.2008.03.043</a>
   </td>
   <td>2008
   </td>
   <td>51
   </td>
   <td><a href="http://bioinfo3d.cs.tau.ac.il/rsitedb/rsite_about.html">http://bioinfo3d.cs.tau.ac.il/rsitedb/rsite_about.html</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file
   </td>
   <td>binding sites (based on other similar proteins)
   </td>
   <td>based on human/model organisms; only a limited dataset of PDB entries are covered
   </td>
  </tr>
  <tr>
   <td>catRAPID
   </td>
   <td>Agostini et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btt495">https://doi.org/10.1093/bioinformatics/btt495</a>
   </td>
   <td>2013
   </td>
   <td>234
   </td>
   <td><a href="http://service.tartaglialab.com/update_submission/423433/0cd5163900">http://service.tartaglialab.com/update_submission/423433/0cd5163900</a>
<p>
web server
   </td>
   <td>RNA and protein sequence
   </td>
   <td>interaction probability per residue for RNA and protein (as heatmap)
   </td>
   <td>trained on model organisms/human
   </td>
  </tr>
  <tr>
   <td>PRince
   </td>
   <td>Barik et al.
<p>
<a href="https://doi.org/10.1093/nar/gks535">https://doi.org/10.1093/nar/gks535</a>
   </td>
   <td>2012
   </td>
   <td>20
   </td>
   <td><a href="http://www.facweb.iitkgp.ac.in/~rbahadur/prince/home.html">http://www.facweb.iitkgp.ac.in/~rbahadur/prince/home.html</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file
   </td>
   <td>lists (in PDB format) interface atoms for both protein and RNA chain + output parameters
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>hybridNAP
   </td>
   <td>Zhang et al.
<p>
<a href="https://doi.org/10.1093/bib/bbx168">https://doi.org/10.1093/bib/bbx168</a>
   </td>
   <td>2019
   </td>
   <td>83
   </td>
   <td><a href="http://biomine.cs.vcu.edu/servers/hybridNAP/">http://biomine.cs.vcu.edu/servers/hybridNAP/</a>
<p>
web server
   </td>
   <td>protein sequence
   </td>
   <td>csv with propensity per amino acid to bind nucleic acids or protein (+ visualization in browser)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>GraphProt
   </td>
   <td>Maticzka et al.
<p>
<a href="https://doi.org/10.1186/gb-2014-15-1-r17">https://doi.org/10.1186/gb-2014-15-1-r17</a>
   </td>
   <td>2014
   </td>
   <td>241
   </td>
   <td><a href="https://github.com/dmaticzka/GraphProt">https://github.com/dmaticzka/GraphProt</a>
<p>
<a href="http://www.bioinf.uni-freiburg.de/Software/GraphProt">http://www.bioinf.uni-freiburg.de/Software/GraphProt</a>
<p>
stand alone
   </td>
   <td>experimental datasets; RNA sequence
   </td>
   <td>binding site motifs for RNA sequence and secondary structure elements
   </td>
   <td>experimental dataset (RNAcompete, CLIP-Seq; self-supplied) with bound and unbound RBPs, included RNA secondary structure
   </td>
  </tr>
  <tr>
   <td>HOCNNLB
   </td>
   <td>Zhang et al.
<p>
<a href="https://doi.org/10.1016/j.ab.2019.113364">https://doi.org/10.1016/j.ab.2019.113364</a>
   </td>
   <td>2019
   </td>
   <td>17
   </td>
   <td><a href="https://github.com/NWPU-903PR/HOCNNLB">https://github.com/NWPU-903PR/HOCNNLB</a>
<p>
stand alone
   </td>
   <td>lncRNA sequence dataset
   </td>
   <td>binding site for RBP on lncRNA sequences
   </td>
   <td>higher-order nucleotide encoding convolutional neural network-based method
   </td>
  </tr>
  <tr>
   <td>BERT-RBP
   </td>
   <td>Yamada & Hamada
<p>
<a href="https://doi.org/10.1093/bioadv/vbac023">https://doi.org/10.1093/bioadv/vbac023</a>
   </td>
   <td>2022
   </td>
   <td>6
   </td>
   <td><a href="https://github.com/kkyamada/bert-rbp">https://github.com/kkyamada/bert-rbp</a>
<p>
stand alone
   </td>
   <td>CLIP dataset (RNA sequences)
   </td>
   <td>RBP-binding property of RNA sequences (yes or no)
   </td>
   <td>data-trained model, analyses transcript region type, RNA secondary structure elements and binding motifs
   </td>
  </tr>
  <tr>
   <td>PredRBR
   </td>
   <td>Tang et al.
<p>
<a href="https://doi.org/10.1186/s12859-017-1879-2">https://doi.org/10.1186/s12859-017-1879-2</a>
   </td>
   <td>2017
   </td>
   <td>39
   </td>
   <td><a href="http://denglab.org/PredRBR/">http://denglab.org/PredRBR/</a>
<p>
stand alone
   </td>
   <td>determined 3D structure / PDB file (has to cover both protein and RNA)
   </td>
   <td>predicts RNA-binding residues in the protein structure
   </td>
   <td>sequential and spatial features are included in the model; older idea from PredPRBA people
   </td>
  </tr>
  <tr>
   <td>PRIME3D2D
   </td>
   <td>Xie et al.
<p>
<a href="https://doi.org/10.1038/s42003-020-1114-y">https://doi.org/10.1038/s42003-020-1114-y</a>
   </td>
   <td>2020
   </td>
   <td>6
   </td>
   <td><a href="http://www.rnabinding.com/PRIME-3D2D/">http://www.rnabinding.com/PRIME-3D2D/</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file for protein and RNA each
   </td>
   <td>nucleotides predicted as binding site for the protein get labeled with “+”
   </td>
   <td>structures used, RNA is “reduced” to secondary structure information
   </td>
  </tr>
  <tr>
   <td>aPRBind
   </td>
   <td>Liu et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btaa747">https://doi.org/10.1093/bioinformatics/btaa747</a>
   </td>
   <td>2021
   </td>
   <td>10
   </td>
   <td><a href="https://github.com/ChunhuaLiLab/aPRbind">https://github.com/ChunhuaLiLab/aPRbind</a>
<p>
stand alone
   </td>
   <td>protein sequence
   </td>
   <td>RNA-binding residues in protein structure model
   </td>
   <td>CNN model with sequence features, evolutionary information, residue properties & propensities (from protein structure model)
   </td>
  </tr>
  <tr>
   <td>RBPPred
   </td>
   <td>Zhang & Liu
<p>
<a href="https://doi.org/10.1093/bioinformatics/btw730">https://doi.org/10.1093/bioinformatics/btw730</a>
   </td>
   <td>2017
   </td>
   <td>72
   </td>
   <td><a href="http://rnabinding.com/RBPPred.html">http://rnabinding.com/RBPPred.html</a>
<p>
stand alone
   </td>
   <td>protein sequence(s)
   </td>
   <td>predicts whether the protein binds RNAs in general (probability)
   </td>
   <td>model based on evolutionary information and  physicochemical properties of proteins, SVM classifier
   </td>
  </tr>
  <tr>
   <td>RCK
   </td>
   <td>Orenstein et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btw259">https://doi.org/10.1093/bioinformatics/btw259</a>
   </td>
   <td>2016
   </td>
   <td>65
   </td>
   <td><a href="http://rck.csail.mit.edu/">http://rck.csail.mit.edu/</a>
<p>
stand alone
   </td>
   <td>RPI dataset: set of RNA sequences with estimated binding affinities + RNA secondary structure annotations of sequences
   </td>
   <td>RNA-protein motif preference (for short RNA transcripts each a binding “intensity” is given)
   </td>
   <td>trained on  RNAcompete experimental data; k-mer model with local secondary structure preferences; extension to RNAcontext (adding k-mer approach)
   </td>
  </tr>
  <tr>
   <td>MEME
   </td>
   <td>Bailey et al.
<p>
<a href="https://doi.org/10.1093/nar/gkv416">https://doi.org/10.1093/nar/gkv416</a>
   </td>
   <td>2015
   </td>
   <td>1762
   </td>
   <td><a href="https://meme-suite.org/meme/tools/meme">https://meme-suite.org/meme/tools/meme</a>
<p>
web server and stand alone
   </td>
   <td>(one or) multiple sequences where common motif should be found
   </td>
   <td>motif with weblogo and position in sequence (DNA, RNA, protein)
   </td>
   <td>not necessarily interaction related
<p>
add-on: MEMERIS
<p>
<a href="https://doi.org/10.1093/nar/gkl544">https://doi.org/10.1093/nar/gkl544</a>
   </td>
  </tr>
  <tr>
   <td>DRNApred
   </td>
   <td>Yan & Kurgan
<p>
<a href="https://doi.org/10.1093/nar/gkx059">https://doi.org/10.1093/nar/gkx059</a>
   </td>
   <td>2017
   </td>
   <td>154
   </td>
   <td><a href="http://biomine.cs.vcu.edu/servers/DRNApred/">http://biomine.cs.vcu.edu/servers/DRNApred/</a>
<p>
web server
   </td>
   <td>protein sequence
   </td>
   <td>txt file with interaction probability for DNA/RNA per amino acid
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>COACH
   </td>
   <td>Yang et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btt447">https://doi.org/10.1093/bioinformatics/btt447</a>
   </td>
   <td>2013
   </td>
   <td>780
   </td>
   <td><a href="https://zhanggroup.org/COACH/">https://zhanggroup.org/COACH/</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file or protein sequence
   </td>
   <td>binding site recognition based on homologous template structures
   </td>
   <td>further versions:
<p>
COACH-D
<p>
<a href="https://doi.org/10.1093/nar/gky439">https://doi.org/10.1093/nar/gky439</a>
<p>
NucBind
<p>
<a href="https://doi.org/10.1093/bioinformatics/bty756">https://doi.org/10.1093/bioinformatics/bty756</a>
   </td>
  </tr>
  <tr>
   <td>aaRNA
   </td>
   <td>Li et al.
<p>
<a href="https://doi.org/10.1093/nar/gku681">https://doi.org/10.1093/nar/gku681</a>
   </td>
   <td>2014
   </td>
   <td>54
   </td>
   <td><a href="http://sysimm.ifrec.osaka-u.ac.jp/aarna/">http://sysimm.ifrec.osaka-u.ac.jp/aarna/</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file or protein sequence
   </td>
   <td>binary propensity and di-nucleotide propensity of each residue (amino acid) to bind RNA in general, also structural visualization
   </td>
   <td>neural network trained on RNA-RBP-complex datasets
   </td>
  </tr>
  <tr>
   <td>Deepnet-RBP
   </td>
   <td>Zhang et al.
<p>
<a href="https://doi.org/10.1093/nar/gkv1025">https://doi.org/10.1093/nar/gkv1025</a>
   </td>
   <td>2015
   </td>
   <td>252
   </td>
   <td><a href="https://github.com/thucombio/deepnet-rbp">https://github.com/thucombio/deepnet-rbp</a>
<p>
stand alone
   </td>
   <td>CLIP dataset (RNA sequences)
   </td>
   <td>RNA sequence and 3D structure motifs for RBP binding site preferences
   </td>
   <td>multimodal deep learning model based on experimentally identified RBP binding sites (CLIP-seq)
   </td>
  </tr>
  <tr>
   <td>DeepBoost
   </td>
   <td>Li et al.
<p>
<a href="https://doi.org/10.1093/nar/gkx492">https://doi.org/10.1093/nar/gkx492</a>
   </td>
   <td>2017
   </td>
   <td>22
   </td>
   <td><a href="http://github.com/dongfanghong/deepboost">http://github.com/dongfanghong/deepboost</a>
<p>
stand alone
   </td>
   <td>RNA-protein data set (experimental)
   </td>
   <td>binding site preferences
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>DeepSite
   </td>
   <td>Jiménez et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btx350">https://doi.org/10.1093/bioinformatics/btx350</a>
   </td>
   <td>2017
   </td>
   <td>342
   </td>
   <td><a href="https://playmolecule.com/deepsite/">https://playmolecule.com/deepsite/</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file
   </td>
   <td>binding site/pocket (highlighted in spatial structure)
   </td>
   <td>general ligand binding site prediction, not exclusively RNA
   </td>
  </tr>
  <tr>
   <td>SSMART
   </td>
   <td>Munteanu et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/bty404">https://doi.org/10.1093/bioinformatics/bty404</a>
   </td>
   <td>2018
   </td>
   <td>19
   </td>
   <td><a href="https://ohlerlab.mdc-berlin.de/software/SSMART_137/">https://ohlerlab.mdc-berlin.de/software/SSMART_137/</a>
<p>
stand alone
   </td>
   <td>RNA-protein data set (experimental)
   </td>
   <td>RNA motif (weblogo)
   </td>
   <td>RNA motif finder in RBP
   </td>
  </tr>
  <tr>
   <td>ThermoNet
   </td>
   <td>Su et al.
<p>
<a href="https://doi.org/10.1371/journal.pcbi.1007283">https://doi.org/10.1371/journal.pcbi.1007283</a>
   </td>
   <td>2019
   </td>
   <td>21
   </td>
   <td><a href="https://github.com/suyufeng/ThermoNet">https://github.com/suyufeng/ThermoNet</a>
<p>
stand alone
   </td>
   <td>CLIP dataset (RNA sequences)
   </td>
   <td>
   </td>
   <td>sequence - (k-mer-)embedding convolutional neural network + thermodynamics of secondary structures
   </td>
  </tr>
  <tr>
   <td>iCapsule
   </td>
   <td>Shen et al.
<p>
<a href="https://doi.org/10.1109/TCBB.2019.2943465">https://doi.org/10.1109/TCBB.2019.2943465</a>
   </td>
   <td>2019
   </td>
   <td>21
   </td>
   <td><a href="https://github.com/naturomics/CapsNet-Tensorflow">https://github.com/naturomics/CapsNet-Tensorflow</a>
<p>
stand alone
   </td>
   <td>RNA-protein data set (experimental)
   </td>
   <td>motif (weblogo)
   </td>
   <td>based on multiple modifications of Capsnet
   </td>
  </tr>
  <tr>
   <td>ProbeRating
   </td>
   <td>Yang et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btaa580">https://doi.org/10.1093/bioinformatics/btaa580</a>
   </td>
   <td>2020
   </td>
   <td>3
   </td>
   <td><a href="https://github.com/syang11/ProbeRating">https://github.com/syang11/ProbeRating</a>
<p>
stand alone
   </td>
   <td>RNA-protein data set
   </td>
   <td>binding profiles for RBPs
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>RPI-Net
   </td>
   <td>Yan et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btaa456">https://doi.org/10.1093/bioinformatics/btaa456</a>
   </td>
   <td>2020
   </td>
   <td>29
   </td>
   <td><a href="https://github.com/HarveyYan/RNAonGraph">https://github.com/HarveyYan/RNAonGraph</a>
<p>
stand alone
   </td>
   <td>CLIP dataset (RNA sequences)
   </td>
   <td>RNA secondary structure models and motifs
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>GraphBind
   </td>
   <td>Xia et al.
<p>
<a href="https://doi.org/10.1093/nar/gkab044">https://doi.org/10.1093/nar/gkab044</a>
   </td>
   <td>2021
   </td>
   <td>25
   </td>
   <td><a href="http://www.csbio.sjtu.edu.cn/bioinf/GraphBind/">http://www.csbio.sjtu.edu.cn/bioinf/GraphBind/</a>
<p>
web server and stand alone
   </td>
   <td>determined 3D structure / PDB file (protein)
   </td>
   <td>identify RNA-binding residues in protein (highlighted in protein structure on website, csv file to download)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>DeepCLIP
   </td>
   <td>Grønning et al.
<p>
<a href="https://doi.org/10.1093/nar/gkaa530">https://doi.org/10.1093/nar/gkaa530</a>
   </td>
   <td>2020
   </td>
   <td>50
   </td>
   <td><a href="http://deepclip.compbio.sdu.dk">http://deepclip.compbio.sdu.dk</a>
<p>
web server and stand alone
   </td>
   <td>CLIP datasets; RNA sequence
   </td>
   <td>binding profiles and motifs for RNA sequence (i.e. potential binding sites)
   </td>
   <td>pre-trained models based on experimental datasets (CLIP-Seq, iCLIP, etc)
   </td>
  </tr>
  <tr>
   <td>PrismNet
   </td>
   <td>Sun et al.
<p>
<a href="https://doi.org/10.1038/s41422-021-00476-y">https://doi.org/10.1038/s41422-021-00476-y</a>
   </td>
   <td>2021
   </td>
   <td>42
   </td>
   <td><a href="http://prismnet.zhanglab.net/">http://prismnet.zhanglab.net/</a>
<p>
web server
<p>
<a href="https://github.com/kuixu/PrismNet">https://github.com/kuixu/PrismNet</a>
<p>
stand alone
   </td>
   <td>RNA-protein data set (experimental)
   </td>
   <td>predict dynamic RBP binding across sequence, motif visualization
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>iDeepS
   </td>
   <td>Pan et al.
<p>
<a href="https://doi.org/10.1186/s12864-018-4889-1">https://doi.org/10.1186/s12864-018-4889-1</a>
   </td>
   <td>2018
   </td>
   <td>193
   </td>
   <td><a href="https://github.com/xypan1232/iDeepS">https://github.com/xypan1232/iDeepS</a>
<p>
stand alone
   </td>
   <td>RNA-protein data set (experimental) / RNA sequence (prediction)
   </td>
   <td>binding site motif
   </td>
   <td>previous version: iDeepE <a href="https://doi.org/10.1093/bioinformatics/bty364">https://doi.org/10.1093/bioinformatics/bty364</a>
   </td>
  </tr>
  <tr>
   <td>3dRPC
   </td>
   <td>Huang et al.
<p>
<a href="https://doi.org/10.1038/srep01887">https://doi.org/10.1038/srep01887</a>
   </td>
   <td>2013
   </td>
   <td>64
   </td>
   <td><a href="http://biophy.hust.edu.cn/new/3dRPC/create">http://biophy.hust.edu.cn/new/3dRPC/create</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file for protein and RNA each
   </td>
   <td>RNA and protein docking to a complex + scoring
   </td>
   <td>dock RNA and protein structure
   </td>
  </tr>
  <tr>
   <td>KYG
   </td>
   <td>Kim et al.
<p>
<a href="https://doi.org/10.1093/nar/gkl819">https://doi.org/10.1093/nar/gkl819</a>
   </td>
   <td>2006
   </td>
   <td>139
   </td>
   <td><a href="http://cib.cf.ocha.ac.jp/KYG/">http://cib.cf.ocha.ac.jp/KYG/</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file (protein) + MSA (depending on used method)
   </td>
   <td>RNA interface residue prediction
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>OPRA
   </td>
   <td>Pérez-Cano & Fernández-Recio
<p>
<a href="https://doi.org/10.1002/prot.22527">https://doi.org/10.1002/prot.22527</a>
   </td>
   <td>2009
   </td>
   <td>98
   </td>
   <td><a href="https://life.bsc.es/pid/opra/default/index">https://life.bsc.es/pid/opra/default/index</a>
<p>
web server
   </td>
   <td>determined 3D structure / PDB file
   </td>
   <td>binding potential per residue (protein) to bind RNA (annotated pdb file and score result file)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>RBPmap
   </td>
   <td>Paz et al.
<p>
<a href="https://doi.org/10.1093/nar/gku406">https://doi.org/10.1093/nar/gku406</a>
   </td>
   <td>2014
   </td>
   <td>409
   </td>
   <td><a href="http://rbpmap.technion.ac.il/index.html">http://rbpmap.technion.ac.il/index.html</a>
<p>
web server and stand alone
   </td>
   <td>RNA sequence(s) and an RBP motif
   </td>
   <td>RBP-binding motifs in RNA (potential binding sites for RBP)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>IPMiner
   </td>
   <td>Pan et al.
<p>
<a href="https://doi.org/10.1186/s12864-016-2931-8">https://doi.org/10.1186/s12864-016-2931-8</a>
   </td>
   <td>2016
   </td>
   <td>110
   </td>
   <td><a href="https://github.com/xypan1232/IPMiner">https://github.com/xypan1232/IPMiner</a>
<p>
stand alone
   </td>
   <td>RNA-protein dataset; RNA and protein sequences
   </td>
   <td>interaction score for RNA and protein
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>DLPRB
   </td>
   <td>Ben-Bassat et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/bty600">https://doi.org/10.1093/bioinformatics/bty600</a>
   </td>
   <td>2018
   </td>
   <td>64
   </td>
   <td><a href="https://github.com/ilanbb/dlprb">https://github.com/ilanbb/dlprb</a>
<p>
stand alone
   </td>
   <td>RNA-protein dataset (experimental), i.e.: RNA sequence file with binding affinity + file with structural information (vector of 5 possible structural elements for each position)
   </td>
   <td>binding site preference visualized as RNA sequence and structure logos
   </td>
   <td>CNN
   </td>
  </tr>
  <tr>
   <td>ssHMM
   </td>
   <td>Heller et al.
<p>
<a href="https://doi.org/10.1093/nar/gkx756">https://doi.org/10.1093/nar/gkx756</a>
   </td>
   <td>2017
   </td>
   <td>39
   </td>
   <td><a href="https://github.molgen.mpg.de/heller/ssHMM">https://github.molgen.mpg.de/heller/ssHMM</a>
<p>
stand alone
   </td>
   <td>RNA-binding protein data (e.g. CLIP-Seq)
   </td>
   <td>sequence - structure motifs/preferences of RNAs (for the RBPs) as a graph
   </td>
   <td>hidden Markov model (HMM) with Gibbs sampling
   </td>
  </tr>
  <tr>
   <td>beRBP
   </td>
   <td>Yu et al.
<p>
<a href="https://doi.org/10.1093/nar/gky1294">https://doi.org/10.1093/nar/gky1294</a>
   </td>
   <td>2019
   </td>
   <td>33
   </td>
   <td><a href="http://bioinfo.vanderbilt.edu/beRBP/predict.html">http://bioinfo.vanderbilt.edu/beRBP/predict.html</a>
   </td>
   <td>RNA sequence(s) + PWM or sequence of RBP
   </td>
   <td>RBP-binding sites/motifs in RNA sequence
   </td>
   <td>limited to a trained selection of human RBPs
   </td>
  </tr>
</table>


**_Unavailable prediction tools_**


<table>
  <tr>
   <td><strong>Tool</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Year</strong>
   </td>
   <td><strong>Tool link</strong>
   </td>
   <td><strong>Info</strong>
   </td>
  </tr>
  <tr>
   <td>RPIFSE
   </td>
   <td>Wang et al.
<p>
<a href="https://doi.org/10.1016/j.jtbi.2018.10.029">https://doi.org/10.1016/j.jtbi.2018.10.029</a>
   </td>
   <td>2019
   </td>
   <td>-
   </td>
   <td> not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>DeepRKE
   </td>
   <td>Deng et al.
<p>
<a href="https://doi.org/10.1109/BIBM47256.2019.8983345">https://doi.org/10.1109/BIBM47256.2019.8983345</a>
   </td>
   <td>2019
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>RPI-SAN
   </td>
   <td>Yi et al.
<p>
<a href="https://doi.org/10.1016/j.omtn.2018.03.001">https://doi.org/10.1016/j.omtn.2018.03.001</a>
   </td>
   <td>2018
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>CTF / CGR
   </td>
   <td>Wang & Wu
<p>
<a href="https://doi.org/10.1080/21655979.2018.1470721">https://doi.org/10.1080/21655979.2018.1470721</a>
   </td>
   <td>2018
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>ELM
   </td>
   <td>Wang et al.
<p>
<a href="https://doi.org/10.1109/TCBB.2018.2874267">https://doi.org/10.1109/TCBB.2018.2874267</a>
   </td>
   <td>2018
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>LGBM
   </td>
   <td>Zhan et al.
<p>
<a href="https://doi.org/10.3389/fgene.2018.00458">https://doi.org/10.3389/fgene.2018.00458</a>
   </td>
   <td>2018
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>Oli
   </td>
   <td>Livi & Blanzieri
<p>
<a href="https://doi.org/10.1186/1471-2105-15-123">https://doi.org/10.1186/1471-2105-15-123</a>
   </td>
   <td>2014
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>ProteRNA
   </td>
   <td>Huang et al.
<p>
<a href="https://doi.org/10.1186/1471-2164-11-S4-S2">https://doi.org/10.1186/1471-2164-11-S4-S2</a>
   </td>
   <td>2010
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>RNAProB
   </td>
   <td>Cheng et al.
<p>
<a href="https://doi.org/10.1186/1471-2105-9-S12-S6">https://doi.org/10.1186/1471-2105-9-S12-S6</a>
   </td>
   <td>2008
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>Struct-NB
   </td>
   <td>Towfic et al.
  <p>
  <a href="https://doi.org/10.1504/ijdmb.2010.030965">https://doi.org/10.1504/ijdmb.2010.030965</a>
   </td>
   <td>2010
   </td>
   <td>-
   </td>
   <td>not accessible / no link available
   </td>
  </tr>
  <tr>
   <td>RNAcontext
   </td>
   <td>Kazan et al.
  <p>
  <a href="https://doi.org/10.1371/journal.pcbi.1000832">https://doi.org/10.1371/journal.pcbi.1000832</a>
   </td>
   <td>2010
   </td>
   <td><a href="http://morrislab.med.utoronto.ca/software">http://morrislab.med.utoronto.ca/software</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>  
  <tr>
   <td>RNAcommender
   </td>
   <td>Corrado et al.
  <p>
  <a href="https://doi.org/10.1093/bioinformatics/btw517">https://doi.org/10.1093/bioinformatics/btw517</a>
   </td>
   <td>2016
   </td>
   <td><a href="http://rnacommender.disi.unitn.it/">http://rnacommender.disi.unitn.it/</a>
   <p>
   <a href="https://github.com/gianlucacorrado/RNAcommender">https://github.com/gianlucacorrado/RNAcommender</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>  
  <tr>
   <td>lncPRO
   </td>
   <td>Lu et al.
  <p>
  <a href="https://doi.org/10.1186/1471-2164-14-651">https://doi.org/10.1186/1471-2164-14-651</a>
   </td>
   <td>2013
   </td>
   <td><a href="http://bioinfo.bjmu.edu.cn/lncpro/">http://bioinfo.bjmu.edu.cn/lncpro/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>    
  <tr>
   <td>CFRP
   </td>
   <td>Dai et al.
<p>
<a href="https://doi.org/10.3389/fgene.2019.00018">https://doi.org/10.3389/fgene.2019.00018</a>
   </td>
   <td>2019
   </td>
   <td><a href="http://www.dailab.cn/CFRP/index.html">http://www.dailab.cn/CFRP/index.html</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RPiRLS
   </td>
   <td>Shen et al.
<p>
<a href="https://doi.org/10.3390/molecules23030540">https://doi.org/10.3390/molecules23030540</a>
   </td>
   <td>2018
   </td>
   <td><a href="http://bmc.med.stu.edu.cn/RPiRLS">http://bmc.med.stu.edu.cn/RPiRLS</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RPI-Bind
   </td>
   <td>Luo et al.
<p>
<a href="https://doi.org/10.1038/s41598-017-00795-4">https://doi.org/10.1038/s41598-017-00795-4</a>
   </td>
   <td>2017
   </td>
   <td><a href="http://ctsb.is.wfubmc.edu/publications/RPI-Bind-Pred.php">http://ctsb.is.wfubmc.edu/publications/RPI-Bind-Pred.php</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RNAProSite
   </td>
   <td>Sun et al.
<p>
<a href="https://doi.org/10.1186/s12859-016-1110-x">https://doi.org/10.1186/s12859-016-1110-x</a>
   </td>
   <td>2016
   </td>
   <td><a href="http://lilab.ecust.edu.cn/NABind">http://lilab.ecust.edu.cn/NABind</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>rpiCOOL
   </td>
   <td>Akbaripour-Elahabad et al.
<p>
<a href="https://doi.org/10.1016/j.jtbi.2016.04.025">https://doi.org/10.1016/j.jtbi.2016.04.025</a>
   </td>
   <td>2016
   </td>
   <td><a href="http://biocool.ir/rpicool.html">http://biocool.ir/rpicool.html</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RPI-Pred
   </td>
   <td>Suresh et al.
<p>
<a href="https://doi.org/10.1093/nar/gkv020">https://doi.org/10.1093/nar/gkv020</a>
   </td>
   <td>2015
   </td>
   <td><a href="http://ctsb.is.wfubmc.edu/projects/rpi-pred">http://ctsb.is.wfubmc.edu/projects/rpi-pred</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>DeepBind
   </td>
   <td>Alipanahi et al.
<p>
<a href="https://doi.org/10.1038/nbt.3300">https://doi.org/10.1038/nbt.3300</a>
   </td>
   <td>2015
   </td>
   <td><a href="http://tools.genes.toronto.edu/deepbind/">http://tools.genes.toronto.edu/deepbind/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>PRIPU
   </td>
   <td>Cheng et al.
<p>
<a href="https://doi.org/10.1142/S021972001541005X">https://doi.org/10.1142/S021972001541005X</a>
   </td>
   <td>2015
   </td>
   <td><a href="http://admis.fudan.edu.cn/projects/pripu.htm">http://admis.fudan.edu.cn/projects/pripu.htm</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RBscore
   </td>
   <td>Miao & Westhof
<p>
<a href="https://doi.org/10.1093/nar/gkv446">https://doi.org/10.1093/nar/gkv446</a>
   </td>
   <td>2015
   </td>
   <td><a href="http://ahsoka.u-strasbg.fr/rbscore/">http://ahsoka.u-strasbg.fr/rbscore/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RBRIdent
   </td>
   <td>Xiong et al.
<p>
<a href="https://doi.org/10.1002/prot.24806">https://doi.org/10.1002/prot.24806</a>
   </td>
   <td>2015
   </td>
   <td><a href="http://166.111.152.91/RBRIdent">http://166.111.152.91/RBRIdent</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RNABindRPlus
   </td>
   <td>Walia et al.
<p>
<a href="https://doi.org/10.1371/journal.pone.0097725">https://doi.org/10.1371/journal.pone.0097725</a>
   </td>
   <td>2014
   </td>
   <td><a href="http://einstein.cs.iastate.edu/RNABindRPlus/">http://einstein.cs.iastate.edu/RNABindRPlus/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RBRDetector
   </td>
   <td>Yang et al.
<p>
<a href="https://doi.org/10.1002/prot.24610">https://doi.org/10.1002/prot.24610</a>
   </td>
   <td>2014
   </td>
   <td><a href="http://ibi.hzau.edu.cn/rbrdetector">http://ibi.hzau.edu.cn/rbrdetector</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>SRCpred
   </td>
   <td>Fernandez et al.
<p>
<a href="https://doi.org/10.1186/1471-2105-12-S13-S5">https://doi.org/10.1186/1471-2105-12-S13-S5</a>
   </td>
   <td>2011
   </td>
   <td><a href="http://tardis.nibio.go.jp/netasa/srcpred">http://tardis.nibio.go.jp/netasa/srcpred</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>DRNA / SPOT
   </td>
   <td>Zhao et al.
<p>
<a href="https://doi.org/10.1093/nar/gkq1266">https://doi.org/10.1093/nar/gkq1266</a>
   </td>
   <td>2011
   </td>
   <td><a href="http://sparks.informatics.iupui.edu/spot">http://sparks.informatics.iupui.edu/spot</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>Predict_RBP
   </td>
   <td>Wang et al.
<p>
<a href="https://doi.org/10.1007/s00726-010-0639-7">https://doi.org/10.1007/s00726-010-0639-7</a>
   </td>
   <td>2010
   </td>
   <td><a href="http://cic.scu.edu.cn/bioinformatics/Predict_RBP.rar">http://cic.scu.edu.cn/bioinformatics/Predict_RBP.rar</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>NAPS
   </td>
   <td>Carson et al.
<p>
<a href="https://doi.org/10.1093/nar/gkq361">https://doi.org/10.1093/nar/gkq361</a>
   </td>
   <td>2010
   </td>
   <td><a href="http://proteomics.bioengr.uic.edu/NAPS">http://proteomics.bioengr.uic.edu/NAPS</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>PiRaNhA
   </td>
   <td>Murakami et al.
<p>
<a href="https://doi.org/10.1093/nar/gkq474">https://doi.org/10.1093/nar/gkq474</a>
   </td>
   <td>2010
   </td>
   <td><a href="http://www.bioinformatics.sussex.ac.uk/PIRANHA">http://www.bioinformatics.sussex.ac.uk/PIRANHA</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>BindN+
   </td>
   <td>Wang et al.
<p>
<a href="https://doi.org/10.1186/1752-0509-4-S1-S3">https://doi.org/10.1186/1752-0509-4-S1-S3</a>
   </td>
   <td>2010
   </td>
   <td><a href="http://bioinfo.ggc.org/bindn+/">http://bioinfo.ggc.org/bindn+/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>PRBR
   </td>
   <td>Ma et al.
<p>
<a href="https://doi.org/10.1002/prot.22958">https://doi.org/10.1002/prot.22958</a>
   </td>
   <td>2010
   </td>
   <td><a href="http://www.cbi.seu.edu.cn/PRBR/">http://www.cbi.seu.edu.cn/PRBR/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>PRNA
   </td>
   <td>Liu et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btq253">https://doi.org/10.1093/bioinformatics/btq253</a>
   </td>
   <td>2010
   </td>
   <td><a href="http://www.aporc.org/doc/wiki/PRNA">http://www.aporc.org/doc/wiki/PRNA</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>PRIP
   </td>
   <td>Maetschke & Yuan
<p>
<a href="https://doi.org/10.1186/1471-2105-10-341">https://doi.org/10.1186/1471-2105-10-341</a>
   </td>
   <td>2009
   </td>
   <td><a href="https://qfab.org/PRIP">https://qfab.org/PRIP</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>PRINTR
   </td>
   <td>Wang et al.
<p>
<a href="https://doi.org/10.1007/s00726-007-0634-9">https://doi.org/10.1007/s00726-007-0634-9</a>
   </td>
   <td>2008
   </td>
   <td><a href="http://210.42.106.80/printr/">http://210.42.106.80/printr/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>RISP
   </td>
   <td>Tong et al.
<p>
<a href="https://doi.org/10.1016/j.cmpb.2007.12.003">https://doi.org/10.1016/j.cmpb.2007.12.003</a>
   </td>
   <td>2008
   </td>
   <td><a href="http://grc.seu.edu.cn/RISP">http://grc.seu.edu.cn/RISP</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>Pprint
   </td>
   <td>Kumar et al.
<p>
<a href="https://doi.org/10.1002/prot.21677">https://doi.org/10.1002/prot.21677</a>
   </td>
   <td>2007
   </td>
   <td> <a href="http://www.imtech.res.in/raghava/pprint/">http://www.imtech.res.in/raghava/pprint/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td>DBS-Pred
   </td>
   <td>Ahmad et al.
<p>
<a href="https://doi.org/10.1093/bioinformatics/btg432">https://doi.org/10.1093/bioinformatics/btg432</a>
   </td>
   <td>2004
   </td>
   <td><a href="http://www.netasa.org/dbs-pred/">http://www.netasa.org/dbs-pred/</a>
   </td>
   <td>not maintained / accessible anymore
   </td>
  </tr>
  <tr>
   <td> DR_bind1
   </td>
   <td>Chen et al.
<p>
<a href="https://doi.org/10.1093/nar/gkt1299">https://doi.org/10.1093/nar/gkt1299</a>
   </td>
   <td>2014
   </td>
   <td><a href="https://drbind.limlab.ibms.sinica.edu.tw/">https://drbind.limlab.ibms.sinica.edu.tw/</a>
   </td>
   <td>tool does not perform
   </td>
  </tr>
</table>
