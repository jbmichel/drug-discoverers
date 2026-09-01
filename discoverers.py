"""Source of truth for the drug-discoverer roster.

Run `python discoverers.py` to regenerate discoverers.csv and discoverers.md.

Field notes
-----------
category   : coarse bucket, used for grouping the corpus
status     : "active" (living, still producing public artifacts) /
             "emeritus" (living, corpus is mostly retrospective) /
             "historical" (deceased; corpus is fixed)
known_for  : the discovery/decision the person is on the list for
artifacts  : artifact types known to exist, ordered by usefulness for
             reasoning capture
richness   : A = large corpus of *explicit* reasoning (blog, podcast,
                 lectures, first-person case histories)
             B = moderate; talks + review/perspective papers + interviews
             C = mostly primary papers, patents, and third-party profiles
where      : where the reasoning actually lives — the crawl instruction
url        : only filled where the address has been verified; blank means
             "resolve in the next pass"
"""

from dataclasses import dataclass, asdict, fields
import csv
import pathlib


@dataclass
class Person:
    name: str
    category: str
    status: str
    affiliation: str
    known_for: str
    artifacts: str
    richness: str
    where: str
    url: str = ""


P = Person

PEOPLE = [
    # ------------------------------------------------------------------
    # 1. Meta-reasoners and commentators
    #    Highest reasoning-per-token in the whole list. These people
    #    explain *why* a decision was made, in public, continuously.
    # ------------------------------------------------------------------
    P("Derek Lowe", "commentary", "active", "Novartis (formerly); Science blogs",
      "In the Pipeline, 2002-present: ~20 yrs of daily medicinal-chemistry judgement",
      "blog;book;podcasts;talks;papers", "A",
      "Full blog archive 2002-present; Chemistry World columns; podcast guest spots",
      "https://www.science.org/blogs/pipeline"),
    P("Bruce Booth", "commentary", "active", "Atlas Venture",
      "LifeSciVC, 2011-present: company-building and portfolio reasoning made explicit",
      "blog;talks;podcasts;X", "A",
      "Full LifeSciVC archive; Atlas year-in-review posts; podcast interviews",
      "https://lifescivc.com/"),
    P("Pat Walters", "commentary", "active", "OpenADMET; UCSF; formerly Relay Tx, Vertex",
      "Practical Cheminformatics: how to evaluate computational drug-discovery claims",
      "blog;notebooks;talks;papers;X", "A",
      "Blog + companion Jupyter notebooks (reasoning shown as executable code)",
      "https://patwalters.github.io/"),
    P("Robert Plenge", "commentary", "active", "Bristol Myers Squibb",
      "PlengeGen: human-genetics-first target selection, written up as a method",
      "blog;papers;talks", "A",
      "Blog series on genetics-to-target logic; NRDD reviews",
      "https://plengegen.com/"),
    P("David Grainger", "commentary", "active", "Medicxi; RxCelerate",
      "DrugBaron / Forbes: contrarian analysis of why developers make bad decisions",
      "blog;essays;talks", "A",
      "DrugBaron archive + Forbes contributor column",
      "https://www.forbes.com/sites/davidgrainger/"),
    P("Dennis X. Hu", "commentary", "active", "Drug Hunter (founder); formerly Genentech",
      "Drug Hunter: structured case histories of approved and clinical molecules",
      "articles;newsletter;podcasts;webinars", "A",
      "Molecules-of-the-month write-ups; interviews with program leads",
      "https://drughunter.com/"),
    P("Daniel Erlanson", "commentary", "active", "Frontier Medicines; Practical Fragments",
      "Fragment-based lead discovery; 15+ yrs of critical fragment literature review",
      "blog;papers;book", "A",
      "Practical Fragments archive (with Teddy Zartler); FBDD reviews",
      "https://practicalfragments.blogspot.com/"),
    P("Jack Scannell", "commentary", "active", "Etheros Pharma; Univ. of Edinburgh",
      "Eroom's Law; the 'better-than-the-Beatles' and model-validity theories of R&D decline",
      "papers;essays;talks;podcasts", "A",
      "NRDD 2012 Eroom paper + follow-ups on predictive validity; lecture recordings", ""),
    P("Bernard Munos", "commentary", "active", "InnoThink; formerly Eli Lilly",
      "Quantitative analysis of pharma R&D output and where innovation actually comes from",
      "papers;essays;talks", "B",
      "NRDD innovation-output papers; conference keynotes; op-eds", ""),
    P("Jonathan Baell", "commentary", "active", "Monash University",
      "PAINS filters: how screening artifacts fool discovery teams",
      "papers;essays;talks", "B",
      "J Med Chem PAINS paper + Nature comment 'Chemistry: Chemical con artists'", ""),
    P("Lynn L. Silver", "commentary", "emeritus", "LNS Consulting; formerly Merck",
      "Why antibacterial discovery keeps failing — the most honest post-mortems in the field",
      "papers;reviews;talks", "B",
      "Clin Microbiol Rev 'Challenges of antibacterial discovery' and successors", ""),
    P("Anthony Nicholls", "commentary", "active", "OpenEye / Cadence Molecular Sciences",
      "Statistics and rigour in computational chemistry; 'what do we mean by validation?'",
      "papers;essays;talks", "B",
      "JCAMD 'What do we know and when do we know it?' series; conference talks", ""),

    # ------------------------------------------------------------------
    # 2. Foundational figures — the canon. Corpus is fixed but the
    #    retrospective first-person accounts are unusually explicit.
    # ------------------------------------------------------------------
    P("Paul Ehrlich", "foundational", "historical", "Frankfurt Institute",
      "Chemotherapy as a concept; side-chain/receptor theory; Salvarsan (1909)",
      "papers;lectures;biographies", "B",
      "Nobel lecture 1908; collected papers; Ehrlich's own 'magic bullet' essays", ""),
    P("Gerhard Domagk", "foundational", "historical", "Bayer",
      "Prontosil and the sulfonamides — the first broad antibacterial class",
      "papers;lectures;biographies", "C",
      "Nobel lecture 1939 (delivered 1947); Bayer archive accounts", ""),
    P("Selman Waksman", "foundational", "historical", "Rutgers University",
      "Systematic soil-screening for antibiotics; streptomycin; coined 'antibiotic'",
      "papers;lectures;memoir", "B",
      "Nobel lecture 1952; autobiography 'My Life with the Microbes'", ""),
    P("Gertrude B. Elion", "foundational", "historical", "Burroughs Wellcome",
      "Rational antimetabolite design: 6-MP, azathioprine, allopurinol, acyclovir",
      "lectures;interviews;oral_history;papers", "A",
      "Nobel lecture 1988 ('The purine path to chemotherapy'); extensive oral histories", ""),
    P("George H. Hitchings", "foundational", "historical", "Burroughs Wellcome",
      "Co-architect with Elion of the antimetabolite programme",
      "lectures;papers;oral_history", "B",
      "Nobel lecture 1988; Burroughs Wellcome oral-history collection", ""),
    P("Sir James Black", "foundational", "historical", "ICI; Smith Kline & French",
      "Propranolol (beta-blockade) and cimetidine (H2) — receptor-led drug design, twice",
      "lectures;interviews;papers", "A",
      "Nobel lecture 1988; interviews on 'the most fruitful basis of discovery is an old drug'", ""),
    P("Paul Janssen", "foundational", "historical", "Janssen Pharmaceutica",
      "~80 marketed drugs incl. haloperidol, fentanyl, risperidone, loperamide, ketoconazole",
      "papers;lectures;biography;interviews", "A",
      "Collected lectures; 'Paul Janssen: A Man for All Seasons'; Janssen archive", ""),
    P("Leo Sternbach", "foundational", "historical", "Hoffmann-La Roche",
      "Benzodiazepines: chlordiazepoxide and diazepam, from a shelved series",
      "papers;interviews;oral_history", "B",
      "First-person accounts of the 'abandoned compound' story; Roche archive", ""),
    P("Carl Djerassi", "foundational", "historical", "Syntex; Stanford University",
      "Norethindrone — the first orally active progestin (the Pill)",
      "papers;books;memoirs;interviews", "A",
      "Multiple memoirs; Science History Institute oral history", ""),
    P("Alfred Burger", "foundational", "historical", "University of Virginia",
      "Founded J. Med. Chem. and 'Burger's Medicinal Chemistry'; defined the discipline",
      "books;papers;essays", "B",
      "Textbook prefaces and historical essays on how med chem should reason", ""),
    P("Corwin Hansch", "foundational", "historical", "Pomona College",
      "QSAR / Hansch analysis — quantifying structure-activity relationships",
      "papers;reviews;interviews", "B",
      "Original QSAR papers plus retrospective 'how QSAR began' accounts", ""),
    P("Sir John Vane", "foundational", "historical", "Royal College of Surgeons; Wellcome",
      "Aspirin's mechanism (prostaglandin synthesis inhibition); ACE-inhibition concept",
      "lectures;papers;interviews", "B",
      "Nobel lecture 1982; accounts of the snake-venom-to-captopril chain", ""),
    P("Arvid Carlsson", "foundational", "historical", "University of Gothenburg",
      "Dopamine as a neurotransmitter; L-DOPA; groundwork for SSRIs (zimelidine)",
      "lectures;papers;interviews", "B",
      "Nobel lecture 2000; interviews on resistance to the dopamine hypothesis", ""),
    P("Solomon Snyder", "foundational", "emeritus", "Johns Hopkins University",
      "Opiate receptor identification; receptor-binding as a screening paradigm",
      "papers;books;essays;interviews", "A",
      "Memoir 'Brainstorming'; annual-review autobiographical chapters", ""),

    # ------------------------------------------------------------------
    # 3. Small-molecule drug hunters — the working canon of med chem
    # ------------------------------------------------------------------
    P("Christopher A. Lipinski", "medchem", "emeritus", "Pfizer (formerly)",
      "Rule of Five — property-based reasoning about oral drugs",
      "papers;essays;talks;interviews", "A",
      "Ro5 paper + many retrospectives on what the rule does and does not mean", ""),
    P("Akira Endo", "medchem", "historical", "Sankyo; Tokyo Noko University",
      "Compactin (ML-236B) — the first statin, from fungal screening",
      "papers;essays;lectures", "A",
      "First-person historical accounts of the statin discovery in ATVB/PNAS/Nat Med", ""),
    P("P. Roy Vagelos", "medchem", "emeritus", "Merck (R&D head, then CEO)",
      "Ran the lab-to-market machine behind lovastatin; the Mectizan donation decision",
      "books;interviews;lectures", "A",
      "Memoir 'Medicine, Science and Merck'; long-form interviews on portfolio calls", ""),
    P("Bruce Roth", "medchem", "emeritus", "Parke-Davis; later Genentech",
      "Atorvastatin — a 'me-too' program taken to best-in-class on chemistry judgement",
      "papers;talks;interviews", "B",
      "Retrospective lectures on the Lipitor program; ACS award addresses", ""),
    P("Miguel Ondetti", "medchem", "historical", "Squibb",
      "Captopril — the first rationally designed enzyme-inhibitor drug",
      "papers;lectures;retrospectives", "B",
      "Design-history papers on the ACE active-site model", ""),
    P("David Cushman", "medchem", "historical", "Squibb",
      "Co-designer of captopril; the ACE pharmacophore hypothesis",
      "papers;retrospectives", "C",
      "Joint Ondetti/Cushman design retrospectives", ""),
    P("Sir Simon Campbell", "medchem", "emeritus", "Pfizer (formerly)",
      "Amlodipine, doxazosin; led the chemistry culture that produced sildenafil",
      "talks;interviews;papers", "B",
      "RSC/ACS award lectures; interviews on running discovery chemistry", ""),
    P("Tu Youyou", "medchem", "emeritus", "China Academy of Chinese Medical Sciences",
      "Artemisinin — extraction insight from classical texts, self-experimentation",
      "lectures;papers;interviews", "B",
      "Nobel lecture 2015; accounts of Project 523", ""),
    P("Satoshi Omura", "medchem", "emeritus", "Kitasato Institute",
      "Avermectin from soil actinomycetes; the industrial-academic screening partnership",
      "lectures;papers;interviews", "B",
      "Nobel lecture 2015; essays on natural-product screening strategy", ""),
    P("William C. Campbell", "medchem", "emeritus", "Merck (formerly); Drew University",
      "Ivermectin — recognising and pushing the anthelmintic-to-human leap",
      "lectures;papers;essays", "B",
      "Nobel lecture 2015; essays on serendipity and persistence in screening", ""),
    P("Joshua Boger", "medchem", "emeritus", "Vertex (founder); formerly Merck",
      "Structure-based design as a company thesis; HIV and HCV protease inhibitors",
      "interviews;talks;book_subject", "A",
      "'The Billion-Dollar Molecule' (Werth) plus his own talks and interviews", ""),
    P("Paul Negulescu", "medchem", "active", "Vertex Pharmaceuticals",
      "CFTR modulators (ivacaftor, tezacaftor, elexacaftor) via functional screening",
      "papers;talks;interviews;podcasts", "A",
      "Breakthrough Prize / award lectures; CF program retrospectives", ""),
    P("Sabine Hadida", "medchem", "active", "Vertex Pharmaceuticals",
      "Chemistry lead for the CFTR corrector series",
      "papers;patents;talks", "B",
      "J Med Chem discovery papers for VX-809/VX-661/VX-445; ACS Heroes talks", ""),
    P("Stephen W. Fesik", "medchem", "active", "Vanderbilt University; formerly Abbott",
      "SAR by NMR; ABT-737 lineage leading to venetoclax; now MYC/RAS",
      "papers;lectures;interviews", "A",
      "Lecture series on fragment-to-lead reasoning; program retrospectives", ""),
    P("Harren Jhoti", "medchem", "active", "Astex Pharmaceuticals (founder)",
      "Industrialised fragment-based discovery; partnered programs incl. ribociclib, capivasertib",
      "papers;talks;interviews", "B",
      "FBDD reviews; keynotes on fragment screening economics", ""),
    P("Sir Tom Blundell", "medchem", "emeritus", "University of Cambridge; Astex co-founder",
      "Structure-based drug design as a discipline; protein crystallography to leads",
      "papers;lectures;reviews", "B",
      "Reviews on SBDD history and fragment methods; recorded lectures", ""),
    P("Andrew L. Hopkins", "medchem", "active", "Exscientia (founder); Univ. of Dundee",
      "Ligand efficiency; 'the druggable genome'; polypharmacology; AI-designed molecules",
      "papers;talks;interviews", "B",
      "NRDD ligand-efficiency and druggability papers; AI-design keynotes", ""),
    P("Dale L. Boger", "medchem", "active", "Scripps Research",
      "Total synthesis in service of med chem; vancomycin analogues against resistance",
      "papers;lectures", "B",
      "Award lectures; design rationale sections of synthesis papers", ""),
    P("Phil S. Baran", "medchem", "active", "Scripps Research",
      "Scalable synthesis and electrochemistry that changes what med chem can make",
      "papers;talks;X;podcasts", "A",
      "Group 'Baran Lab' teaching materials; heavily opinionated talks and threads", ""),
    P("E. J. Corey", "medchem", "emeritus", "Harvard University",
      "Retrosynthetic analysis — the explicit logic of synthesis planning",
      "books;papers;lectures", "A",
      "'The Logic of Chemical Synthesis'; Nobel lecture 1990", ""),
    P("Fiona Marshall", "medchem", "active", "MSD (formerly); Heptares founder",
      "Stabilised-receptor structures enabling GPCR structure-based design",
      "papers;talks;interviews", "B",
      "StaR technology papers; talks on GPCR druggability", ""),

    # ------------------------------------------------------------------
    # 4. Oncology and chemical biology
    # ------------------------------------------------------------------
    P("Brian J. Druker", "oncology", "active", "OHSU Knight Cancer Institute",
      "Imatinib — clinical champion of targeted kinase inhibition in CML",
      "papers;lectures;interviews;book_subject", "A",
      "Lasker/award lectures; extensive interviews on pushing a doubted program", ""),
    P("Nicholas Lydon", "oncology", "active", "Blueprint Medicines (co-founder); ex-Ciba-Geigy",
      "Kinase-inhibitor chemistry that produced imatinib",
      "papers;interviews;talks", "B",
      "Interviews on the internal case for a 'non-viable' target class", ""),
    P("Juerg Zimmermann", "oncology", "emeritus", "Novartis (formerly)",
      "Medicinal chemist who made imatinib and nilotinib",
      "papers;patents;talks", "B",
      "Discovery-history papers on the 2-phenylaminopyrimidine series", ""),
    P("Alex Matter", "oncology", "emeritus", "Ciba-Geigy/Novartis; EDDC Singapore",
      "Ran the oncology unit that backed imatinib; later neglected-disease discovery",
      "papers;essays;interviews", "B",
      "Essays on portfolio courage and on discovery in resource-limited settings", ""),
    P("Charles L. Sawyers", "oncology", "active", "MSKCC / HHMI",
      "Imatinib resistance mechanisms; enzalutamide; resistance-first thinking",
      "papers;lectures;interviews", "A",
      "Award lectures; commentaries on designing against resistance", ""),
    P("Michael E. Jung", "oncology", "active", "UCLA",
      "Chemistry behind enzalutamide and apalutamide",
      "papers;patents;talks", "B",
      "Discovery papers and lectures on the diarylthiohydantoin series", ""),
    P("Kevan M. Shokat", "oncology", "active", "UCSF / HHMI",
      "Drugging KRAS G12C via the switch-II pocket; analog-sensitive kinase alleles",
      "papers;lectures;interviews;podcasts", "A",
      "Talks explicitly reconstructing the 'undruggable' reasoning; long interviews", ""),
    P("Frank McCormick", "oncology", "active", "UCSF; NCI RAS Initiative",
      "RAS biology to therapeutics; Onyx founder (sorafenib)",
      "papers;reviews;talks", "B",
      "RAS Initiative reviews and progress talks", ""),
    P("Craig M. Crews", "oncology", "active", "Yale University; Arvinas founder",
      "PROTACs — targeted protein degradation as a new modality",
      "papers;talks;interviews;podcasts", "A",
      "Origin-story lectures; reviews framing degradation vs occupancy logic", ""),
    P("James E. Bradner", "oncology", "active", "Amgen (CSO); formerly Novartis NIBR",
      "JQ1 / BET bromodomain inhibition; open sharing of probes; then ran NIBR",
      "papers;talks;interviews;podcasts", "A",
      "TED and seminar talks; interviews on running an industrial research org", ""),
    P("Nathanael S. Gray", "oncology", "active", "Stanford University",
      "Covalent kinase inhibitors and degraders; chemical-probe discipline",
      "papers;talks", "B",
      "Seminar recordings; probe-quality position papers", ""),
    P("Benjamin F. Cravatt", "oncology", "active", "Scripps Research; Vividion founder",
      "Activity-based protein profiling; covalent ligandability of the proteome",
      "papers;lectures;interviews", "B",
      "Lectures on ligandability mapping; platform-rationale interviews", ""),
    P("Stuart L. Schreiber", "oncology", "active", "Broad Institute; Harvard",
      "Chemical biology as a discipline; FKBP/mTOR mechanism; many companies",
      "papers;essays;lectures", "A",
      "Programmatic essays on small molecules and biology; recorded lectures", ""),
    P("Alan Ashworth", "oncology", "active", "UCSF Helen Diller Cancer Center",
      "BRCA/PARP synthetic lethality — a genotype-directed therapeutic concept",
      "papers;lectures;interviews", "B",
      "Retrospectives on the synthetic-lethality bet; award lectures", ""),
    P("Stephen P. Jackson", "oncology", "active", "Gurdon Institute; KuDOS founder",
      "DNA-damage response biology into olaparib",
      "papers;talks;interviews", "B",
      "Talks tracing biology-to-company-to-drug; PARP retrospectives", ""),
    P("William G. Kaelin Jr.", "oncology", "active", "Dana-Farber / HHMI",
      "VHL-HIF oxygen sensing (belzutifan); also the field's sharpest writing on rigour",
      "papers;essays;lectures", "A",
      "Nature 'Publish houses of brick, not mansions of straw'; Nobel lecture 2019", ""),
    P("Judah Folkman", "oncology", "historical", "Boston Children's / Harvard",
      "Angiogenesis as a therapeutic target — a hypothesis held against consensus",
      "papers;lectures;biography", "A",
      "Lectures and the 'Dr. Folkman's War' account of sustaining a rejected idea", ""),

    # ------------------------------------------------------------------
    # 5. Biologics, immuno-oncology, cell therapy
    # ------------------------------------------------------------------
    P("Cesar Milstein", "biologics", "historical", "LMB Cambridge",
      "Monoclonal antibodies via hybridoma (with Georges Kohler)",
      "lectures;papers;interviews", "B",
      "Nobel lecture 1984; LMB oral histories (pair with Kohler's record)", ""),
    P("Sir Gregory Winter", "biologics", "emeritus", "LMB Cambridge; Cambridge Antibody Tech",
      "Humanised antibodies and phage display — the route to adalimumab and beyond",
      "lectures;papers;interviews", "A",
      "Nobel lecture 2018; interviews on making antibodies a drug platform", ""),
    P("Dennis J. Slamon", "biologics", "active", "UCLA",
      "HER2 as a target and the trastuzumab clinical program",
      "papers;lectures;interviews;book_subject", "B",
      "Award lectures; the 'Her-2' program history and its clinical fights", ""),
    P("Axel Ullrich", "biologics", "emeritus", "Max Planck Institute; formerly Genentech",
      "HER2 cloning; RTK-directed therapeutics; Sugen (sunitinib lineage)",
      "papers;lectures;interviews", "B",
      "Retrospective lectures on target cloning to clinic", ""),
    P("Napoleone Ferrara", "biologics", "active", "UC San Diego; formerly Genentech",
      "VEGF discovery to bevacizumab and ranibizumab",
      "papers;lectures;interviews", "B",
      "Lasker lecture; reviews on the anti-angiogenic thesis and its limits", ""),
    P("David V. Goeddel", "biologics", "emeritus", "Genentech scientist #1; Tularik founder",
      "First recombinant human insulin, growth hormone, interferons",
      "papers;interviews;oral_history", "B",
      "Oral histories on early Genentech decision-making", ""),
    P("James P. Allison", "biologics", "active", "MD Anderson Cancer Center",
      "CTLA-4 blockade — ipilimumab; the checkpoint concept",
      "lectures;papers;interviews;documentary", "A",
      "Nobel lecture 2018; 'Breakthrough' documentary; many long interviews", ""),
    P("Tasuku Honjo", "biologics", "emeritus", "Kyoto University",
      "PD-1 discovery leading to anti-PD-1 therapy",
      "lectures;papers;interviews", "B",
      "Nobel lecture 2018; accounts of the long PD-1 partnership", ""),
    P("Carl H. June", "biologics", "active", "University of Pennsylvania",
      "CD19 CAR-T cell therapy into the clinic",
      "papers;lectures;book;interviews", "A",
      "'Cancer Treatment Breakthrough' talks; memoir-style accounts of early patients", ""),
    P("Michel Sadelain", "biologics", "active", "Columbia; formerly MSKCC",
      "CAR design principles — costimulatory domains and second-generation CARs",
      "papers;reviews;talks", "B",
      "Design-rationale reviews on CAR architecture", ""),
    P("Steven A. Rosenberg", "biologics", "active", "National Cancer Institute",
      "Adoptive cell transfer, TIL therapy, IL-2 — decades of iterative clinical work",
      "papers;books;lectures;interviews", "A",
      "Memoirs ('The Transformed Cell'); NCI lecture archive", ""),
    P("Sir Marc Feldmann", "biologics", "emeritus", "University of Oxford",
      "Anti-TNF for rheumatoid arthritis — cytokine-network reasoning to infliximab",
      "papers;lectures;interviews", "B",
      "Lasker lecture; retrospectives on the TNF-as-apex-cytokine argument", ""),

    # ------------------------------------------------------------------
    # 6. Genetic medicines, nucleic acids, delivery
    # ------------------------------------------------------------------
    P("Katalin Kariko", "genetic_medicine", "active", "Univ. of Szeged; formerly BioNTech, Penn",
      "Nucleoside modification making mRNA therapeutically usable",
      "lectures;memoir;interviews;papers", "A",
      "Nobel lecture 2023; memoir 'Breaking Through'; extensive interviews", ""),
    P("Drew Weissman", "genetic_medicine", "active", "University of Pennsylvania",
      "Co-discovered modified-nucleoside mRNA; vaccine and therapeutic translation",
      "lectures;papers;interviews", "A",
      "Nobel lecture 2023; talks on the innate-immunity problem and its fix", ""),
    P("Robert S. Langer", "genetic_medicine", "active", "MIT",
      "Controlled release and delivery; co-founder of Moderna and ~40 others",
      "papers;talks;interviews;podcasts", "A",
      "Huge interview corpus on translating platforms into companies", ""),
    P("Pieter R. Cullis", "genetic_medicine", "active", "University of British Columbia",
      "Lipid nanoparticles for nucleic-acid delivery (patisiran, mRNA vaccines)",
      "papers;book;talks;interviews", "A",
      "Book on the LNP story; lectures on ionisable-lipid design logic", ""),
    P("Ugur Sahin", "genetic_medicine", "active", "BioNTech (co-founder)",
      "mRNA cancer immunotherapy and the COVID-19 vaccine (with Ozlem Tureci)",
      "papers;talks;interviews;book_subject", "A",
      "'The Vaccine' account; scientific talks on individualised neoantigen mRNA", ""),
    P("Barney S. Graham", "genetic_medicine", "active", "Morehouse; formerly NIH VRC",
      "Prefusion-stabilised antigen design (RSV F, spike-2P) — structure-based vaccinology",
      "papers;lectures;interviews", "A",
      "Lectures reconstructing the structure-based vaccine design logic", ""),
    P("Stanley T. Crooke", "genetic_medicine", "active", "Ionis (founder); n-Lorem",
      "Antisense oligonucleotides as a durable drug platform",
      "papers;books;talks;interviews", "A",
      "Books and reviews on building an entire modality over 30 years", ""),
    P("C. Frank Bennett", "genetic_medicine", "active", "Ionis Pharmaceuticals",
      "Nusinersen for SMA; CNS-delivered antisense",
      "papers;lectures;interviews", "B",
      "Breakthrough Prize lecture; program retrospectives with Krainer", ""),
    P("Adrian R. Krainer", "genetic_medicine", "active", "Cold Spring Harbor Laboratory",
      "SMN2 splicing biology into nusinersen",
      "papers;lectures;interviews", "B",
      "Lectures on splice-switching design; CSHL seminar archive", ""),
    P("Muthiah Manoharan", "genetic_medicine", "active", "Alnylam Pharmaceuticals",
      "siRNA chemistry and GalNAc conjugation — turned RNAi into medicines",
      "papers;reviews;talks", "B",
      "Chemistry-design reviews on stabilisation and targeting", ""),
    P("Katherine A. High", "genetic_medicine", "active", "AskBio; Spark Therapeutics co-founder",
      "AAV gene therapy: hemophilia B and voretigene neparvovec",
      "papers;lectures;interviews", "B",
      "Lectures on the first US gene-therapy approval and its regulatory path", ""),
    P("David R. Liu", "genetic_medicine", "active", "Broad Institute / HHMI",
      "Base editing and prime editing; Beam, Prime, Editas",
      "papers;lectures;interviews;podcasts", "A",
      "Exceptionally clear lectures that narrate the design reasoning step by step", ""),
    P("Fyodor Urnov", "genetic_medicine", "active", "UC Berkeley / Innovative Genomics Institute",
      "Genome editing as medicine; bespoke CRISPR therapies for n-of-1 patients",
      "essays;talks;papers;interviews", "A",
      "Long-form essays and opinionated talks on scaling gene-editing cures", ""),

    # ------------------------------------------------------------------
    # 7. Antivirals
    # ------------------------------------------------------------------
    P("Norbert W. Bischofberger", "antiviral", "active", "Kronos Bio; formerly Gilead CSO",
      "Tenofovir, oseltamivir, sofosbuvir-era Gilead R&D",
      "papers;talks;interviews", "B",
      "Interviews on prodrug strategy and on the Pharmasset acquisition call", ""),
    P("Michael J. Sofia", "antiviral", "active", "Arbutus; formerly Pharmasset",
      "Sofosbuvir — phosphoramidate prodrug design that cured HCV",
      "papers;lectures;interviews", "A",
      "Lasker lecture; J Med Chem discovery paper; talks on the prodrug logic", ""),
    P("Raymond F. Schinazi", "antiviral", "active", "Emory University",
      "Nucleoside antivirals: emtricitabine, lamivudine lineage, HCV nucleosides",
      "papers;talks;interviews", "B",
      "Talks on serial company formation around nucleoside chemistry", ""),
    P("Dennis C. Liotta", "antiviral", "active", "Emory University",
      "Chemistry behind emtricitabine and lamivudine",
      "papers;patents;talks", "B",
      "Discovery lectures; enantiomer-selection reasoning", ""),
    P("Hiroaki Mitsuya", "antiviral", "active", "NCI / Kumamoto University",
      "Identified AZT's anti-HIV activity; ddI, ddC; darunavir design",
      "papers;lectures;interviews", "B",
      "Retrospectives on the first HIV drugs and resistance-proof design", ""),
    P("Emilio A. Emini", "antiviral", "active", "Gates Foundation; formerly Merck, Pfizer",
      "HIV protease inhibitor and vaccine programs; later HPV and pneumococcal vaccines",
      "papers;talks;interviews", "B",
      "Talks on resistance-driven combination strategy and vaccine portfolio choices", ""),

    # ------------------------------------------------------------------
    # 8. Metabolic and cardiovascular
    # ------------------------------------------------------------------
    P("Michael S. Brown", "metabolic_cv", "active", "UT Southwestern",
      "LDL receptor pathway — the mechanistic basis for statins and PCSK9 drugs",
      "lectures;papers;essays", "A",
      "Nobel lecture 1985; joint essays with Goldstein on how to pick a problem", ""),
    P("Joseph L. Goldstein", "metabolic_cv", "active", "UT Southwestern",
      "Co-discoverer of LDL-receptor regulation; sharp essayist on scientific taste",
      "lectures;essays;papers", "A",
      "Nature Medicine 'Lasker' essays; Nobel lecture 1985", ""),
    P("Helen H. Hobbs", "metabolic_cv", "active", "UT Southwestern / HHMI",
      "PCSK9 and ANGPTL3 loss-of-function humans — genetics as target validation",
      "papers;lectures;interviews", "A",
      "Lectures on outlier-human genetics driving drug programs", ""),
    P("Sekar Kathiresan", "metabolic_cv", "active", "Verve Therapeutics (co-founder)",
      "Human genetics to base-edited PCSK9/ANGPTL3 therapies",
      "papers;talks;interviews;podcasts;X", "A",
      "Podcasts and threads that narrate the genetics-to-program logic", ""),
    P("Daniel J. Drucker", "metabolic_cv", "active", "University of Toronto",
      "GLP-1 biology; the intellectual through-line to incretin drugs",
      "papers;reviews;talks;X", "A",
      "Prolific reviews plus running public commentary on incretin claims", ""),
    P("Jens Juul Holst", "metabolic_cv", "active", "University of Copenhagen",
      "GLP-1 physiology and its therapeutic potential",
      "papers;lectures;interviews", "B",
      "Lectures on the 20-year path from peptide to blockbuster", ""),
    P("Svetlana Mojsov", "metabolic_cv", "active", "Rockefeller University",
      "Identified the bioactive GLP-1(7-37) fragment",
      "papers;interviews", "C",
      "Interviews reconstructing the fragment-identification work and its credit history", ""),
    P("Lotte Bjerre Knudsen", "metabolic_cv", "active", "Novo Nordisk",
      "Acylation design giving liraglutide and semaglutide their half-lives",
      "papers;lectures;interviews", "A",
      "Lectures on the albumin-binding design series; program retrospectives", ""),
    P("Richard D. DiMarchi", "metabolic_cv", "active", "Indiana University; formerly Lilly",
      "Insulin analogues (lispro); GIP/GLP-1 multi-agonist concept behind tirzepatide",
      "papers;lectures;interviews", "A",
      "Talks on peptide engineering and the co-agonist hypothesis", ""),
    P("Jeffrey M. Friedman", "metabolic_cv", "active", "Rockefeller University / HHMI",
      "Leptin — obesity as endocrine biology, reframing the whole field",
      "papers;lectures;essays", "B",
      "Lectures and essays on the discovery and its therapeutic disappointments", ""),

    # ------------------------------------------------------------------
    # 9. CNS
    # ------------------------------------------------------------------
    P("Steven M. Paul", "cns", "active", "Karuna Therapeutics (co-founder); formerly Lilly CSO",
      "Muscarinic agonism for psychosis (KarXT); candid on CNS attrition",
      "papers;talks;interviews;podcasts", "A",
      "Interviews on why CNS programs fail and what made xanomeline workable", ""),
    P("David T. Wong", "cns", "historical", "Eli Lilly",
      "Fluoxetine — selective serotonin reuptake inhibition",
      "papers;retrospectives;interviews", "B",
      "First-person accounts of the Prozac discovery and its internal skeptics", ""),
    P("John Hardy", "cns", "active", "University College London",
      "Amyloid cascade hypothesis from APP genetics; genetics-first neurodegeneration",
      "papers;essays;talks;interviews", "A",
      "Commentaries defending and revising the hypothesis — unusually explicit updating", ""),
    P("Husseini K. Manji", "cns", "active", "Oxford; formerly J&J neuroscience head",
      "Esketamine for treatment-resistant depression; CNS portfolio strategy",
      "papers;talks;interviews", "B",
      "Talks on rapid-acting antidepressant development and regulatory path", ""),

    # ------------------------------------------------------------------
    # 10. Computation, structure, AI
    # ------------------------------------------------------------------
    P("David Baker", "computational", "active", "University of Washington / IPD",
      "De novo protein design; designed binders and minibinder therapeutics",
      "papers;lectures;interviews", "A",
      "Nobel lecture 2024; IPD seminar archive", ""),
    P("John M. Jumper", "computational", "active", "Google DeepMind",
      "AlphaFold2 — structure prediction at usable accuracy",
      "papers;lectures;interviews;podcasts", "A",
      "Nobel lecture 2024; technical talks on what the model does and does not solve", ""),
    P("Mohammed AlQuraishi", "computational", "active", "Columbia University",
      "Protein structure prediction; the field's most analytical essayist on ML in bio",
      "blog;papers;talks;X", "A",
      "Long-form blog essays that reason in public at length",
      "https://moalquraishi.wordpress.com/"),
    P("Richard A. Friesner", "computational", "active", "Columbia; Schrodinger co-founder",
      "Glide docking and FEP+ free-energy methods used in live design cycles",
      "papers;talks", "B",
      "Method papers plus retrospective talks on prospective validation", ""),
    P("Gregory Landrum", "computational", "active", "RDKit; T5 Informatics; formerly Novartis",
      "RDKit — the open cheminformatics substrate of modern discovery",
      "blog;code;talks;papers", "A",
      "RDKit blog: careful, worked-example reasoning about molecular data",
      "https://greglandrum.github.io/rdkit-blog/"),

    # ------------------------------------------------------------------
    # 11. R&D strategy, open science, and how discovery orgs decide
    # ------------------------------------------------------------------
    P("Roger M. Perlmutter", "strategy", "active", "Eikon Therapeutics; formerly Merck, Amgen",
      "Backed pembrolizumab when it was shelved; explicit about R&D portfolio reasoning",
      "talks;interviews;podcasts;papers", "A",
      "Long interviews reconstructing the Keytruda decision and R&D restructuring", ""),
    P("Mene Pangalos", "strategy", "active", "formerly AstraZeneca BioPharmaceuticals R&D",
      "The '5R framework' — an explicit, published decision rubric for projects",
      "papers;talks;interviews", "A",
      "NRDD 5R papers (2014 and follow-up) plus talks on applying them", ""),
    P("Aled M. Edwards", "strategy", "active", "Structural Genomics Consortium (CEO)",
      "Open-science target discovery; argues publicly about incentives and duplication",
      "essays;talks;papers;interviews", "A",
      "Provocative essays and lectures on why the field works the way it does", ""),
    P("Chas Bountra", "strategy", "active", "University of Oxford; SGC",
      "Open target validation and pre-competitive collaboration",
      "talks;essays;papers", "A",
      "Talks explicitly about reducing duplicated failure across companies", ""),
    P("Paul Workman", "strategy", "active", "Institute of Cancer Research, London",
      "HSP90 and other programs; prolific writer on how to run drug discovery well",
      "papers;reviews;talks;blog", "A",
      "Perspectives on chemical probes, target validation, and 'the drugged genome'", ""),
    P("Sir Peter Ratcliffe", "strategy", "active", "University of Oxford",
      "Oxygen-sensing biology underpinning HIF-PHD inhibitors",
      "lectures;papers;interviews", "B",
      "Nobel lecture 2019; commentary on basic-to-applied translation", ""),
]


FIELDNAMES = [f.name for f in fields(Person)]

CATEGORY_TITLES = {
    "commentary": "Meta-reasoners and commentators",
    "foundational": "Foundational figures",
    "medchem": "Small-molecule drug hunters",
    "oncology": "Oncology and chemical biology",
    "biologics": "Biologics, immuno-oncology, cell therapy",
    "genetic_medicine": "Genetic medicines, nucleic acids, delivery",
    "antiviral": "Antivirals",
    "metabolic_cv": "Metabolic and cardiovascular",
    "cns": "CNS",
    "computational": "Computation, structure, AI",
    "strategy": "R&D strategy and open science",
}


def write_csv(path):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["id"] + FIELDNAMES)
        writer.writeheader()
        for i, person in enumerate(PEOPLE, start=1):
            row = {"id": i}
            row.update(asdict(person))
            writer.writerow(row)


def write_markdown(path):
    lines = [
        "# Drug discoverers roster",
        "",
        f"{len(PEOPLE)} people, generated from `discoverers.py`. Do not edit by hand.",
        "",
        "`richness`: **A** = large corpus of explicit reasoning (blog, podcast, lectures,",
        "first-person case histories) · **B** = talks, reviews, interviews ·",
        "**C** = mostly primary papers and third-party profiles.",
        "",
    ]
    for key, title in CATEGORY_TITLES.items():
        group = [p for p in PEOPLE if p.category == key]
        if not group:
            continue
        lines += [f"## {title} ({len(group)})", ""]
        lines += ["| Name | Known for | Rich | Where the reasoning lives |",
                  "| --- | --- | :---: | --- |"]
        for p in group:
            where = p.where
            if p.url:
                where = f"[{where}]({p.url})"
            lines.append(f"| {p.name} | {p.known_for} | {p.richness} | {where} |")
        lines.append("")
    counts = {}
    for p in PEOPLE:
        counts[p.richness] = counts.get(p.richness, 0) + 1
    lines += ["## Counts", "",
              f"- Total: {len(PEOPLE)}",
              f"- Richness A: {counts.get('A', 0)} · B: {counts.get('B', 0)} · C: {counts.get('C', 0)}",
              f"- Active: {sum(1 for p in PEOPLE if p.status == 'active')} · "
              f"emeritus: {sum(1 for p in PEOPLE if p.status == 'emeritus')} · "
              f"historical: {sum(1 for p in PEOPLE if p.status == 'historical')}",
              ""]
    pathlib.Path(path).write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    write_csv(here / "discoverers.csv")
    write_markdown(here / "discoverers.md")
    print(f"{len(PEOPLE)} people written to discoverers.csv and discoverers.md")
