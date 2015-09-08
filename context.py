NEWS_FIELD_COUNT = 3

NEWS = """

Computations 19x faster with new adaptive algorithm
Researchers using a new algorithmic process for a heuristic embedding strategy they call "Adaptive GDDA-BLAST" can now see the results of their computations 19 times faster than with their previous computational method. The new method has the added benefits of detecting structural homology in highly divergent protein sequences and isolating secondary structural elements of transmembrane and ankyrin-repeat domains, with possibly wide-ranging impacts on human health and disease studies.
http://www.huck.psu.edu/content/computations-19x-faster-new-adaptive-algorithm

Huck Institutes to host 2nd Annual Bioinformatics and Genomics Retreat - September 16th & 17th, 2011
Keynote speaker Dr. Richard Edward Green. Visionary talk and panel discussion. Poster sessions. Research presentations. Open to all Penn State faculty, postdocs, students, and staff. Registration is free!
http://www.huck.psu.edu/content/huck-institutes-host-2nd-annual-bioinformatics-and-genomics-retreat-september-16th-17th-2011

Galaxy genome-analysis system now available for cloud computing
Development provides vast increases in computational power for researchers worldwide.
http://science.psu.edu/news-and-events/2011-news/Nekrutenko11-2011

Genome instability studies could change treatment for cancer and other diseases.
Making steps toward the realization of personalized genomic medicine, Huck Institutes affiliates at the Center for Medical Genomics are finding and analyzing hotspots of genomic instability and mutation known as microsatellites.
http://www.huck.psu.edu/content/about/news-archive/genome-instability-studies-could-change-treatment-cancer-and-other-diseases

Huck Institutes seek new Associate Directors for positions in science leadership.
The Huck Institutes wish to appoint a series of new Associate Directors to work with the management team and help in developing new initiatives.
http://www.huck.psu.edu/content/about/news-archive/huck-institutes-seek-new-associate-directors-positions-science-leadership

New characterization of human genome mutability catalyzes biomedical research.
A crucial development for personalized genomic medicine researchers at the Center for Medical Genomics elucidate intricacies of mutagenesis.
http://www.huck.psu.edu/content/about/news-archive/new-characterization-human-genome-mutability-catalyzes-biomedical-research

Children born to older mothers have greater rates of mitochondrial mutations.
The discovery of a "maternal age effect" by a team of Penn State scientists that could be used to predict the accumulation of mitochondrial DNA mutations in maternal egg cells - and the transmission of these mutations to children - could provide valuable insights for genetic counseling.
http://news.psu.edu/story/330097/2014/10/14/research/children-born-older-mothers-have-greater-rates-mitochondrial

"""

def news():
	lines = NEWS.splitlines()
	lines = map(lambda x: x.strip(), lines)
	lines = filter(None, lines)
	group = [iter(lines)] * NEWS_FIELD_COUNT
	list = zip(*group)
	list.reverse()
	return list



LABS_FIELD_COUNT = 4

LABS = """

Assis Lab
Gene duplication, Sequence evolution of duplicate genes, Functional evolution of duplicate genes
http://bio.psu.edu/directory/rua15
raquel.png

Carrel Lab
Genomics of X chromosome inactivation
http://www.huck.psu.edu/users/luc3
laura.png

Cheng Lab
Convergence Science approaches to phenomics, cancer genetics, web-based resources, image Informatics, systems genetics, genomics, and pigmentation genetics
http://www.pennstatehershey.org/web/pathology/keith-cheng
cheng.png

Chiaromonte Lab
Statistical genomics
http://sites.psu.edu/chiaromonte/
francesca.png

DeGiorgio Lab
Statistical population genetics, Human evolutionary genomics, Phylogenetics
http://bio.psu.edu/directory/mxd60
michael.png


Dovat Lab
Pediatrics Hematology Oncology
https://profiles.psu.edu/profiles/display/112092
dovat.png

Eckert Lab
Molecular mechanisms of mutagenesis in human cells as related to cancer
http://www.pennstatehershey.org/web/pathology/research/faculty/experimental
kristin.png

Gerhard Lab
Genetics of Aging, Oxidative Stress, and Iron metabolism
https://profiles.psu.edu/profiles/display/112602
gerhard.png

Girirajan Lab
Genetics of neurodevelopmental disorders
http://bmb.psu.edu/directory/sxg47
santosh.png

Hicks, Steve
Assistant Prof in the Dept of Pediatrics
?
?

Janicki Lab
Anesthesiology
http://www.pennstatehershey.org/findaprovider/provider/1083
janicki.png

Krasilnikova Lab
Mechanisms of trinucleotide repeats diseases
http://bmb.psu.edu/directory/muk19
krasilnikova.png

Li Lab
Developing statistical methods for uncovering complicated patterns in large and complex data
http://www.personal.psu.edu/users/q/u/qul12/index.html
li.png

Makova Lab
Bioinformatics and genomics
http://www.bx.psu.edu/makova_lab/
kateryna.png

Medvedev Lab
Computational Approaches for High-Throughput Sequencing Data
http://medvedevgroup.com/
paul.png

Paul Lab
Newborn health outcomes, childhood obesity, breastfeeding, pediatric therapeutics, asthma
http://pennstatehershey.org/findaprovider/provider/932
ian.png

Poss Lab
Viruses as rapidly evolving markers of host population dynamics
http://www.cidd.psu.edu/people/mup14
mary.png

Spratt Lab
The Enzymology of DNA Repair and Mutagenesis; Mechanisms of fidelity and mutagenesis of DNA polymerases
https://profiles.psu.edu/profiles/display/112126
spratt.png
"""


def labs():
	lines = LABS.splitlines()
	lines = map(lambda x: x.strip(), lines)
	lines = filter(None, lines)
	group = [iter(lines)] * LABS_FIELD_COUNT
	list = zip(*group)
	return list



EVENTS_FIELD_COUNT = 8

EVENTS = """


The fourth annual retreat for the Center for Medical Genomics
N/A
April 30, 2013 - 10:00am
Pasquerilla Spiritual Center, University Park
http://maps.google.com/?q=Pasquerilla%20Spiritual%20Center,%20University%20Park%E2%80%9D
http://www.huck.psu.edu/content/events/fourth-annual-retreat-center-medical-genomics
Past
1

Melissa A. Wilson Sayres (University of California at Berkeley)
Sex-biased evolution and disease
September 10, 2013 - 11:00am
519 Wartik (with video to CG628 at Hershey)
http://maps.google.com/?q=519%20Wartik%20(with%20video%20to%20CG628%20at%20Hershey)%E2%80%9D
Organizer: Arkarachai Fungtammasan. Email: azf127@psu.edu 
Past
2

Arkarachai Fungtammasan (Penn State)
Great ape genetic diversity and population history discussion by Arkarachai using paper from Prado-Martinez and Sudmant 2013
September 20, 2013 - 2:00pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
N/A
Past
3

Bioinformatics and Genomics Retreat
This year we are honored to host THE leader in Functional Genomics, Dr. Michael Snyder, two concurrent statistics sessions to honor Dr. Herman Chernoff, the winner of this year s Rao Prize.
October 4, 2013 - 4:00pm
Life Sciences Building, University Park
http://maps.google.com/?q=Life%20Sciences%20Building,%20University%20Park%E2%80%9D
http://www.huck.psu.edu/content/events/year-we-are-honored-host-leader-functional-genomics-dr-michael-snyder-two-concurrent
Past
4

Thomas E. Spratt (Penn State Hershey)
Locating benzo[a]pyrene-DNA damage in the genome
October 8, 2013 - 11:00am
Room CG628 at Hershey; with video to 519 Wartik Lab
http://maps.google.com/?q=room%20CG628%20at%20Hershey;%20with%20video%20to%20519%20Wartik%20Lab%E2%80%9D
N/A
Past
5

Daniel Blankenberg (Penn State)
GEMINI: Integrative Exploration of Genetic Variation and Genome Annotations discussion by Daniel Blankenberg using paper from Paila 2013
October 18, 2013 - 2:00pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
Paper is available http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1003153(download pdf from: http://www.ploscompbiol.org/article/fetchObject.action?uri=info%3Adoi%2F10.1371%2Fjournal.pcbi.1003153&representation=PDF)
Past
6

Mary Poss
The purpose of this workshop is to identify research needs and advance collaborative research efforts on computational and statistical analyses of genomic data.
October 21, 2013 - 8:30am
306 West Millennium Sciences Complex
http://maps.google.com/?q=306%20West%20Millennium%20Sciences%20Complex%E2%80%9D
Topics: Computational challenges for comprehensive detection of genome variation; Selection on non-genic regions of the genome: Would we know it if we saw it?; Statistical approaches for integrating data on variation across the genomic landscape; Evolution of the genomic landscape;This workshop is sponsored by the Center for System Genomics & Center for Medical Genomics. For more information on Computational and Statistical Genomics Workshop please visit: http://csg.psu.edu/workshops/system-genomics-workshop
Past
7

Aleksandra (Sesa) Slavkovic (Penn State)
Privacy preserving data sharing for genome-wide association studies
November 12, 2013 - 11:00am
519 Wartik Lab, with video to Hershey Room CG628
http://maps.google.com/?q=519%20Wartik%20Lab,%20with%20video%20to%20Hershey%20Room%20CG628%E2%80%9D
The protection of privacy of individual-level information in genome-wide association study (GWAS) databases has been a major concern of researchers following the publication of "an attack" on GWAS data in Homer et al. (2008). Traditional statistical methods for the confidentiality protection do not scale well to deal with GWAS databases and external information on them. The more recent concept of differential privacy provides a rigorous definition of privacy with meaningful privacy guarantees in the presence of arbitrary external information. Building on such notions, we propose new methods to release aggregate GWAS data without compromising an individual s privacy. In this talk, we give a brief overview of challenges associated with protecting confidential data, and present methods for releasing differentially private minor allele frequencies, chi-square statistics and p-values. The proposed methods are compared on simulated data and on a GWAS study of canine hair length. Time permitting, we may also discuss preliminary results on the risk-utility analysis on a dataset consisting of DNA samples collected by the Wellcome Trust Case Control Consortium (WTCCC), and a privacy-preserving method for finding genome-wide associations based on a differentially private approach to penalized logistic regression.
Past
8

Piotr K. Janicki (Penn State Hershey)
Research and Clinical Questions in Perioperative Genomics
December 10, 2013 - 11:00am
Room CG628 at Hershey; with video to 519 Wartik Lab
http://maps.google.com/?q=room%20CG628%20at%20Hershey;%20with%20video%20to%20519%20Wartik%20Lab%E2%80%9D
N/A
Past
9

Prabhani Kuruppumullage Don (Penn State)
Model-based block clustering with EM algorithm
February 14, 2014 - 11:00am
519 Wartik Lab at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=519%20Wartik%20Lab%20at%20University%20Park;%20with%20video%20to%20room%20CG628%20at%20Hershey%E2%80%9D
The next meeting of the Center for Medical Genomics will take place at 11 am on Feb 14 (Fri). Our speaker will be Prabhani Kuruppumullage Don and she will talk about "Model-based block clustering with EM algorithm". Prabhani is a statistician, and she has been working on the development of novel and powerful methods for analysis of genomic and medical data. For instance, Prabhani has been working with Francesca Chiaromonte and me on segmenting the human genome into regions differing in mutation rates and patterns, and this work has implications for evaluating disease-causing variants. Prabhani has recently given this talk at Harvard, and it was very well received.
Past
10

Boris Rebolledo Jaramillo (Penn State)
Nucleotide variability at its limit? Insights into the number and evolutionary dynamics of the sex-determining specificities of the honey bee Apis mellifera.
February 21, 2014 - 2:00pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
N/A
Past
11

Marcia Shu-Wei Su (Penn State)
Andrew H. Moeller, Martine Peeters, Jean-Basco Ndjango, et al. 2013. Sympatric chimpanzees and gorillas harbor convergent gut microbial communities. Genome Research Oct;23(10):1715-20
March 21, 2014 - 2:00pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
http://genome.cshlp.org/content/23/10/1715.full.pdf
Past
12

The Fourth Annual Retreat of the Center for Medical Genomics (part of the Huck Institutes of the Life Sciences)
N/A
March 25, 2014 - 8:00am
University Conference Center, Penn State Hershey campus
http://maps.google.com/?q=University%20Conference%20Center,%20Penn%20State%20Hershey%20campus%E2%80%9D
The Fourth Annual Retreat of the Center for Medical Genomics (part of the Huck Institutes of the Life Sciences) will be held Tuesday, March 25, 2014 at the Penn State Hershey, University Conference Center.  The keynote speaker for this event will be Dr. Beth A. Tarini, M.D., University of Michigan, C.S. Mott Children s Hospital, Department of Pediatrics and Communicable Diseases. Dr. Tarini is Co-Chair of the American Academy of Pediatrics, Genetics in Primary Care Institute. The retreat also will include short talks by Penn State faculty, a poster session, and networking activities.  A goal of this retreat is to provide current genomics information and education to the Penn State University research community, particularly researchers wishing to participate in medical research.  All sessions are open to all interested participants.
Past
13

Samarth Rangavittal (Penn State)
Recombination Dynamics of a Human Y-Chromosomal Palindrome: Rapid GC-Biased Gene Conversion, Multi-kilobase Conversion Tracts, and Rare Inversions. Plos Genetics
April 4, 2014 - 2:00pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1003666
Past
14

Svitlana Tyekucheva (Harvard school of public health)
RNA expression profiling of archival formalin-fixed, paraffin embedded tissues
April 11, 2014 - 11:00am
519 Wartik Lab at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=519%20Wartik%20Lab%20at%20University%20Park;%20with%20video%20to%20room%20CG628%20at%20Hershey%E2%80%9D
One challenge limiting development of clinically useful biomarkers for cancer research lies in the paucity of well-annotated frozen specimens with long-term follow-up on which current high-throughput technologies largely rely. Archival formalin fixed paraffin embedded (FFPE) materials represent the only form of clinical specimens in large cohorts with extensive annotation and long-term clinical follow-up. Unfortunately to date no genomic platform has been identified which can accurately interrogate these specimens due to the extensive fixation- and storage-related RNA degradation. First, we compared two commercially available platforms for RNA expression profiling of archival FFPE specimens from clinical studies of prostate and ovarian cancer.  The first platform was the Affymetrix microarrays following whole-transcriptome amplification using NuGEN WT-Ovation FFPE System V2. The second platform was the Nanostring nCounter without amplification. For each assay, we profiled 7 prostate cancer and 11 ovarian cancer specimens, with block age range of 4 to 21 years. Both platforms produced gene expression profiles with high sensitivity and reproducibility through technical repeats from FFPE materials of prostate and ovarian cancers. RNA-Seq allows to simultaneously observe gene expression levels, mutations in the coding sequences, splice variants and gene fusions, which are especially important in cancer studies. Therefore, next we determined feasibility of RNA-Seq from archival samples, and identified challenges in the data analysis specific to FFPE by head-to-head comparisons to fresh frozen (FF) specimens using 16 pairs of prostate tumor and adjacent normal samples. We observed high average correlations between gene expression values for FFPE technical replicates, and between FF and FFPE pairs. Conclusions: we assessed two high-throughput approaches ideal for discovery studies (microarray and sequencing) and a more economical approach ideal for simultaneous validation of a developed signature consisting of multiple biomarkers. All platforms generated robust, reproducible data with high-level of intra- and inter-platform concordance, regardless of FFPE block age and RNA integrity.  Through this study, we have demonstrated the feasibility of using FFPE materials for biomarker discovery and validation for further integration into clinical practice. For more information on Svitlana Tyekucheva please visit: http://www.hsph.harvard.edu/svitlana-tyekucheva/
Past
15

Wilfried Guiblet (Penn State)
Selective propagation of functional mitochondrial DNA during oogenesis restricts the transmission of a deleterious mitochondrial variant. Nature Genetics
April 18, 2014 - 2:00pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
http://www.nature.com/ng/journal/v46/n4/full/ng.2920.html
Past
16

Laura Carrel (Penn State)
Topological and ncRNA influences on inactive X chromosome gene expression
May 9, 2014 - 11:00am
Room CG624F at Hershey; with video to 519 Wartik Lab
http://maps.google.com/?q=room%20CG624F%20at%20Hershey;%20with%20video%20to%20519%20Wartik%20Lab%E2%80%9D
N/A
Past
17

Dan Mishmar (Ben-Gurion University)
Finally, after 2 billion years, the mitochondrion is part of the general cellular regulation
June 6, 2014 - 11:00am
519 Wartik Lab at University Park; with video to room CG623 at Hershey
http://maps.google.com/?q=519%20Wartik%20Lab%20at%20University%20Park;%20with%20video%20to%20room%20CG623%20at%20Hershey%E2%80%9D
Billions of years have passed since the fusion event that gave rise to current eukaryotes and their energy producing mitochondria. During that time, the mitochondria, a once free living alpha proteo-bacterium, lost most of its genetic material and became dependent on the cell for its biogenesis. Only 37 genes, which are important for energy metabolism and mitochondrial protein translation, were retained in the current small circular mitochondrial genome. Hence, mitochondrial DNA replication, transcription and post transcriptional regulation are controlled by proteins that are currently encoded by the cell nucleus. It was believed that only a handful of mitochondrial dedicated proteins control mitochondrial function. Hence, one could argue that mitochondria are regulated separately from the rest of the cell. In this talk we will present findings supporting the hypothesis that mitochondria are not only regulated by dedicated factors but are also part of the general cellular regulatory system. We will demonstrate that focusing on mitochondrial DNA transcription and RNA editing. Hence, the long co-existence of the ancient prokaryote within our cells was accompanied by regulatory adaptation.
Past
18

Nicholas Stoler (Penn State)
Hypermutable DNA chronicles the evolution of human colon cancer (Naxerovaa 2014) PNAS
September 5, 2014 - 12:30pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
N/A
Past
19

Sayantani Basu Roy (University of Paris-SUD XI)
Meiotic Crossover Interference -- Modeling, Heterogeneity and Inter-Pathway Cross-Talk
September 11, 2014 - 3:00pm
W-257 MSC at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=W-257%20MSC%20at%20University%20Park;%20with%20video%20to%20room%20CG628%20at%20Hershey%E2%80%9D
For more information on Sayantani Basu Roy please visit: http://www.hhmi.org/scientists/marcelo-briones
Past
20

Bioinformatics and Genomics Retreat
The retreat consists of a one-and-a-half day meeting featuring a keynote speaker, faculty and student talks, data visualization workshop and poster presentations. Dr. Peter J. Park as the keynote speaker.
September 12, 2014 - 4:00pm
Life Sciences Building, University Park
http://www.huck.psu.edu/content/events/retreat-consists-one-and-half-day-meeting-featuring-keynote-speaker-faculty-and-student
N/A
Past
21

TBD (Penn State)
N/A
September 19, 2014 - 12:30pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
N/A
Past
22

Sarah J. Carnahan Craig (Penn State)
Paternally expressed genes predominate in the placenta (Wang 2013) PNAS
October 3, 2014 - 12:30pm
307 Wartik
http://maps.google.com/?q=307%20Wartik%E2%80%9D
N/A
Past
23

Marcelo R. S. Briones (Universidade Federal de Sao Paulo)
Evolution of genetic information in pathogenic microorganisms: Implications for diagnostics and epidemiology
October 9, 2014 - 3:00pm
W-257 MSC at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=W-257%20MSC%20at%20University%20Park;%20with%20video%20to%20room%20CG628%20at%20Hershey%E2%80%9D
I will briefly present my early work in Trypanosoma cruzi, the causative agent of Chagas disease, and then present my current research in Experimental Microbial Evolution using the pathogenic yeast model, Candida albicans. We study the effects of oxygen concentrations and temperature in morphology and mitochondrial and nuclear genomes. This has major implications for designing typing markers for hospital acquired infections, a severe problem in intensive care units.For more information on Marcelo R. S. Briones. Please visit: http://www.hhmi.org/scientists/marcelo-briones.
Past
24

Donna Korzick (Penn State)
Physiology Retreat 2014
November 7, 2014 - 4:30pm
Life Sciences
http://maps.google.com/?q=Life%20Sciences%E2%80%9D
This year we have joined forces with the Center for Reproductive Biology and Health (CRBH). The combined Physiology/CRBH retreat consists of a one-and-a-half day meeting featuring keynote speakers, faculty and student talks, and poster presentations. This year we are honored to host Drs. Michael Sturek and Carol Bagnell as keynote speakers. The retreat is open to everyone. Attendance is free, but you must register by November 1, 2014. This year we have joined forces with the Center for Reproductive Biology and Health (CRBH). The combined Physiology/CRBH retreat consists of a one-and-a-half day meeting featuring keynote speakers, faculty and student talks, and poster presentations. This year we are honored to host Drs. Michael Sturek and Carol Bagnell as keynote speakers. The retreat is open to everyone. Attendance is free, but you must register by November 1, 2014.
Past
25

Marzia A. Cremona (Politecnico di Milano (Milano, Italy))
Peak shape clustering: an application to GATA-1
November 13, 2014 - 3:00pm
W-257 MSC at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=W-257%20MSC%20at%20University%20Park;%20with%20video%20to%20room%20CG628%20at%20Hershey%E2%80%9D
In recent years many techniques have been developed to study genetic and epigenetic processes. Among Next Generation Sequencing method, we focus on ChIP-Seq (Chromatin Immuno Precipitation Sequencing), that permits to investigate protein-DNA interactions, e.g. the direct interaction between transcription factors, histones and DNA. At present, in the relevant literature, the analysis of ChIP-Seq data is mainly restricted to the detection of enriched regions (peaks) in the genome, considering only signal intensity. Motivated by the fact that these peaks can show very different shapes, we propose an innovative approach that takes into consideration also the shape of such peaks. We introduce some indices to summarize the shape and we use multivariate clustering techniques in order to detect statistically significant differences in peak shape. We show that an application of this analysis method to ChIP-Seq for the transcription factor GATA-1 reveals novel biological insights. Moreover, we suggest that a functional data analysis approach can lead to even more interesting results, treating peaks directly as curves. Joint work with I. Dellino, A. Parodi, P.G. Pelicci, L. Riva, L.M. Sangalli, P. Secchi and S. Vantini
Incoming
26

Marcia Shu-Wei Su (Penn State)
Maternal Age Effect and Severe Germline Bottleneck in the Inheritance of Human Mitochondrial DNA
December 11, 2014 - 3:00pm
W-257 MSC at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=W-257%20MSC%20at%20University%20Park;%20with%20video%20to%20room%20CG628%20at%20Hershey%E2%80%9D
N/A
Past
27

Michael Schatz (Cold Springs Harbor Lab)
The Resurgence of Reference Quality Genomes using 3rd Generation Sequencing Technologies
January 6, 2015 - 1:00pm
519 Wartik Lab at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
N/A
Past
28

David Koslicki (Oregon State University)
New Techniques to Analyze the Microbiome: analyze thousands of samples, compare without a reference, and profile a community down to the strain level
February 12, 2015 - 11:00am
519 Wartik, with video connection to CG628 in Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
I will present a number of techniques (namely: Quikr, EMDeBruijn, and CommonKmers) that I've recently developed in collaboration with colleagues, and discuss the advantages and disadvantages of applying these techniques in a variety of circumstances. Quikr is an extremely fast, high level taxonomic profiling tool suitable for understanding the global structure of many metagenomics samples. EMDeBruijn is a reference free, de Bruijn graph-based approach to quantifying the similarities and differences between metagenomic samples, even in the presence of many novel microbial organisms. Finally, CommonKmers is a new, highly accurate taxonomic profiling technique capable of faithfully profiling a community down to the strain level. This technique can then use the resulting taxonomic profile to inform the assembly of a metagenome.
Past
29

Marta Tomaszkiewicz (Penn State)
Deciphering the Sequence of Gorilla Y Chromosome and "amplicomics" of fertility genes
April 16, 2015 - 11:00am
519 Wartik Lab with connection to CG 624F in Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
Marta Tomaszkiewicz, Postdoctoral scholar, will be presenting "Deciphering the Sequence of Gorilla Y Chromosome and "amplicomics" of fertility genes". 
Past
30

Erika Kvikstad (Centre for Human Genetics, University of Oxford)
On nuisance events, junk DNA, and determining the impact of genomic pariah on human disease
August 27, 2015 - 11:00am
519 Wartik video-conferenced to CG623 Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
N/A
Past
31


"""

def events():
	lines = EVENTS.splitlines()
	lines = map(lambda x: x.strip(), lines)
	lines = filter(None, lines)
	group = [iter(lines)] * EVENTS_FIELD_COUNT
	list = zip(*group)
	list.reverse()
	return list




PUBS_FIELD_COUNT = 5

PUBS = """

Makova, K.D., S. Yang, and F. Chiaromonte
Indels are male-biased too: a whole genome analysis in rodents
Genome Research
2004
#

Taylor, J., S. Tyekucheva, M. Zody, F. Chiaromonte, and K. D. Makova
Strong and Weak Male Mutation Bias at Different Sites in the Primate Genomes: Insights from the Human-Chimpanzee Comparison
Molecular Biology and Evolution
2006
#

Carrel, L., C. Park, S. Tyekucheva, J. Dunn, F. Chiaromonte, and K. D. Makova
Genomic environment predicts expression patterns on the human inactive X chromosome.
PLoS Genet
2006
#

Kvikstad, E. M., S. Tyekucheva, F. Chiaromonte, and K. D. Makova
A macaque's-eye view of human insertions and deletions: differences in mechanisms
PLoS Computational Biology
2007
#

Kelkar, Y., S. Tyekucheva, F. Chiaromonte, and K. D. Makova
The genome-wide determinants of microsatellite evolution
Genome Research
2008
#

Tyekucheva, S., K. D. Makova, J. E. Karro, R. C. Hardison, W. Miller, and F. Chiaromonte
Human-macaque comparisons illuminate variation in neutral substitution rates.
Genome Biology
2008
#

Roy S.,J. Lavine, F. Chiaromonte, J. Terwee, S. VandeWoude, O. Bjornstad and M. Poss
Multivariate statistical analyses demonstrate uniquehost immune responses to single and dual lentiviral infection.
PLoS ONE
2009
#

Kvikstad, E.M., F. Chiaromonte, and K. D. Makova.
Ride the wavelet: a multi-scale analysis of genomic contexts flanking small insertions and deletions.
Genome Research
2009
#

Schuster, S.,.., K. D. Makova (one of 48 co-authors),.., V. Hayes
Complete Khoisan and Bantu genomes from southern Africa
Nature
2010
#

Park, C., L. Carrel, and K.D. Makova
Strong Purifying Selection at Genes Escaping X Chromosome Inactivation
Molecular Biology and Evolution
2010
#

Kelkar Y.D., N. Strubczewski , S. E. Hile , F. Chiaromonte, K.A. Eckert, and K.D. Makova
What Is a Microsatellite: A Computational and Experimental Definition Based upon Repeat Mutational Behavior at A/T and GT/AC Repeats.
Genome Biol. Evol.
2010
#

Simeonov I., X. Gong, O. Kim, M. Poss, F. Chiaromonte and J. Fricks
Exploratory spatial analysis of in vitro Respiratory Syncytial Virusco-infections
Viruses
2010
#

Ananda, G., F. Chiaromonte, and K.D. Makova. 
A genome-wide view of mutation rate co-variation using multivariate analyses.
Genome Biology
2011
#

Goto, H., B. Dickins, E. Afgan, I.M. Paul, J. Taylor, K.D. Makova, and A. Nekrutenko
Dynamics of mitochondrial heteroplasmy in three families investigated via a repeatable re-sequencing study
Genome Biology
2011
#

Afgan, E., D. Baker, N. Coraor, H. Goto, I.M. Paul, K.D. Makova, A. Nekrutenko, and J. Taylor
Harnessing cloud-computing for biomedical research with Galaxy Cloud
Nature Biotechnology
2011
#

Kelkar, Y., K. Eckert, F. Chiaromonte, and K.D. Makova
A matter of life or death: How microsatellites emerge in and vanish from the human genome.
Genome Research
2011
#

Fungtammasan, A., E. Walsh, F. Chiaromonte, K. A. Eckert, K. D. Makova.
A Genome-wide Analysis of Common Fragile Sites: What Features Determine Chromosomal Instability in the Human Genome?
Genome Research
2012
#

Wagstaff, B., D.J. Hedges, R.S. Derbes, R.C. Sanchez, F. Chiaromonte, K.D. Makova, and A.M. Roy-Engel.
Rescuing Alu: recovery of new inserts shows LINE-1 preserves Alu activity through A-tail expansion.
PLoS Genetics
2012
#

Ananda, G., E. Walsh, K. D. Jacob, M. Krasilnikova, K. A. Eckert, F. Chiaromonte, K. D. Makova.
Distinct mutational behaviors distinguish short tandem repeats from microsatellites in the human genome.
Genome Biology and Evolution
2013
#

Baptiste, B., G. Ananda, N. Strubczewski, A. Lutzkanin, S. J. Khoo, A. Srikanth, N. Kim, K. D. Makova, M. M. Krasilnikova, and K. A. Eckert.
Mature Microsatellites: Mechanisms Underlying Dinucleotide Microsatellite Mutational Biases in Human Cells.
Genes, Genomes, and Genetics
2013
#

Kuruppumullage Don, P., G. Ananda , F. Chiaromonte, K.D. Makova
Segmenting the human genome based on states of neutral genetic divergence.
Proceedings of the National Academy of Sciences
2013
#

Dickins, B., B. Rebolledo-Jaramillo, M. Shu-Wei Su, I. M. Paul, D. Blankenberg, N. Stoler, K. Makova, and A. Nekrutenko.
Controlling for contamination in re-sequencing studies with a reproducible web-based phylogenetic approach.
BioTechniques
2014
#

Campos-Sanchez, R., A. Kapusta, C. Feschotte, F. Chiaromonte, K.D. Makova
Genomic Landscape of Human, Bat, and Ex Vivo DNA Transposon Integrations
Molecular Biology and Evolution
2014
#

McElhoe, J. A., M. M.Holland. K. D. Makova,M.S.-W. Su, I. M. Paul, C. H. Baker, S. A. Faith, B. Young
Development and assessment of an optimized next-generation DNA sequencing approach for the mtgenome using the Illumina MiSeq.
Forensic Science International: Genetics
2014
#

Ananda, G., S. E. Hile , A. Breski, Y. Wang, Y. Kelkar,K. D. Makova, K. A. Eckert 
Microsatellite Interruptions Stabilize Primate Genomes and Exist as Population-Specific Single Nucleotide Polymorphisms within Individual Human Genomes.
PLoS Genet
2014
#

Paul, I. M., J. S. Williams, S. Anzman-Frasca, J. S. Beiler, K. D. Makova, M. E. Marini, L. B. Hess, S. E. Rzucidlo, N. Verdiglione, J. A. Mindell, L. L. Birch
The Intervention Nurses Start Infants Growing on Healthy Trajectories (INSIGHT) study.
BMC pediatrics
2014
#

"""



def publications():
	lines = PUBS.splitlines()
	lines = map(lambda x: x.strip(), lines)
	lines = filter(None, lines)
	group = [iter(lines)] * PUBS_FIELD_COUNT
	list = zip(*group)
	list.reverse()
	return list
