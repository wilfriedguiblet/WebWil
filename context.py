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



EVENTS_FIELD_COUNT = 6

EVENTS = """

Michael Schatz (Cold Springs Harbor Lab)
The Resurgence of Reference Quality Genomes using 3rd Generation Sequencing Technologies
January 6, 2015 - 1:00pm
519 Wartik Lab at University Park; with video to room CG628 at Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
N/A

David Koslicki (Oregon State University)
New Techniques to Analyze the Microbiome: analyze thousands of samples, compare without a reference, and profile a community down to the strain level
February 12, 2015 - 11:00am
519 Wartik, with video connection to CG628 in Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
I will present a number of techniques (namely: Quikr, EMDeBruijn, and CommonKmers) that I've recently developed in collaboration with colleagues, and discuss the advantages and disadvantages of applying these techniques in a variety of circumstances. Quikr is an extremely fast, high level taxonomic profiling tool suitable for understanding the global structure of many metagenomics samples. EMDeBruijn is a reference free, de Bruijn graph-based approach to quantifying the similarities and differences between metagenomic samples, even in the presence of many novel microbial organisms. Finally, CommonKmers is a new, highly accurate taxonomic profiling technique capable of faithfully profiling a community down to the strain level. This technique can then use the resulting taxonomic profile to inform the assembly of a metagenome.

Marta Tomaszkiewicz (Penn State)
Deciphering the Sequence of Gorilla Y Chromosome and "amplicomics" of fertility genes
April 16, 2015 - 11:00am
519 Wartik Lab with connection to CG 624F in Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
Marta Tomaszkiewicz, Postdoctoral scholar, will be presenting "Deciphering the Sequence of Gorilla Y Chromosome and "amplicomics" of fertility genes". 

Erika Kvikstad (Centre for Human Genetics, University of Oxford)
On nuisance events, junk DNA, and determining the impact of genomic pariah on human disease
August 27, 2015 - 11:00am
519 Wartik video-conferenced to CG623 Hershey
http://maps.google.com/?q=519%20Wartik%20video-conferenced%20to%20CG623%20Hershey%E2%80%9D
N/A


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

Schuster, S.,.., K. D. Makova (one of 48 co-authors),..‚ V. Hayes
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

Campos-Sánchez, R., A. Kapusta, C. Feschotte, F. Chiaromonte, K.D. Makova
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
