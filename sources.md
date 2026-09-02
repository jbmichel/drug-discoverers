# Source manifest — Grade A

Concrete, checked sources for the 61 Grade A people in the roster. Generated from `sources/batch*.json` by `build_sources.py`; do not edit by hand.

`confidence`: **verified** — the address appeared in search results · **constructed** — built from a URL pattern confirmed for other people and cross-checked by search · **partial** — person resolved, best artifacts named rather than linked.

> Link-checking by direct fetch is blocked by this session's network egress policy (403 on CONNECT for nobelprize.org, apple podcasts and others). Every address here comes from a search result or a confirmed pattern, not from a successful fetch. `sources/check_links.py` will verify the whole set in one pass when run from an unrestricted network.

## Crawl these venues, not just these people

The highest-leverage move is to harvest a few venues that carry many people at once, before going person by person.

### NobelPrize.org laureate pages

`nobelprize.org/prizes/<medicine|chemistry>/<year>/<surname>/{lecture,interview,podcast,biographical,facts}/`

Four to five artifacts per laureate on a fixed URL pattern, confirmed across 1985/1988/1990/2018/2019/2023/2024. Full lecture PDFs also sit at nobelprize.org/uploads/<year>/<month>/<surname>-lecture.pdf. 12 Grade A people and ~12 more in the wider roster. The single cheapest bulk source in the project.

Covers here: Elion, Black, Corey, Kaelin, Kariko, Weissman, Brown, Goldstein, Baker, Jumper, Winter, Allison

### Eric Topol, Ground Truths (Substack)

`erictopol.substack.com`

Long-form interviews, transcribed, with a working scientist asking the questions. Already found for Kariko, Knudsen, Urnov, Liu and Drucker. Search the archive for the rest of the roster before doing anything else - it is one feed, many people.

Covers here: Kariko, Knudsen, Urnov, Liu, Drucker

### NIH VideoCast

`videocast.nih.gov`

Downloadable lecture video with a stable archive: NIH Director's WALS lectures and NCI symposia. Found for Shokat, Rosenberg and Baker; Graham and Folkman are likely there too.

Covers here: Shokat, Rosenberg, Baker, Graham?, Folkman?

### Lasker Foundation award essays

`laskerfoundation.org/winners/...`

Each award carries a first-person essay, often published in Cell or JCI. Sofia's 'Enter Sofosbuvir' is the model: a full design narrative, free PDF. Found for Sofia, Druker, Negulescu, Brown/Goldstein, Knudsen.

Covers here: Sofia, Druker, Negulescu, Brown, Goldstein, Knudsen

### JCI 'A conversation with ...' series

`jci.org/articles/view/<id>`

Long interview plus video, in a consistent house format. Found for Vagelos, Hobbs and Drucker; the series covers many more.

Covers here: Vagelos, Hobbs, Drucker

### SfN History of Neuroscience in Autobiography

`sfn.org/.../TheHistoryofNeuroscience/Volume-N/cNN.pdf`

Full first-person career accounts as free PDFs. Snyder is in volume 6. Check the whole series for CNS people.

Covers here: Snyder

### Science History Institute oral histories

`sciencehistory.org`

Oral-history-grade long interviews with chemists. Confirmed for Langer. The obvious place to chase Elion, Djerassi, Lipinski and other historical med chemists.

Covers here: Langer, Elion?, Djerassi?, Lipinski?

## Not on the web

Four targets that need a request, a library, or a subscription rather than a crawler.

**Paul Janssen** — Janssen Pharmaceutica archive, Beerse (Belgium): archives, a series of interviews, company publications, and 'Historical Record of Janssen Research Publications (1952-1990)'.

*850+ papers, 500+ presentations, 80+ medicines by one person. Not online; needs a direct request to the company archive.*

**Carl Djerassi** — Carl Djerassi papers (SC0348), Stanford Special Collections, 1952-2014.

*Finding aid is online; the material is not.*

**Solomon Snyder** — Authored-works collection donated to the Johns Hopkins Historical Collection on his 2022 retirement.

*Complements the SfN autobiography chapter, which is online.*

**Joseph Goldstein** — Annual Nature Medicine essay series accompanying the Lasker Awards, ~2000-present, on creativity and taste in science.

*Behind a publisher paywall and not indexed as a series. One of the best explicit statements of scientific judgement anywhere in this corpus - worth the effort to assemble in full.*

## People

### Commentary

#### Derek Lowe  `verified`

In the Pipeline, 2002-present: ~20 yrs of daily medicinal-chemistry judgement

- **home** — <https://www.science.org/blogs/pipeline>

> In the Pipeline blog, 2002-present, ~175 posts/yr. Also Chemistry World column at https://www.chemistryworld.com/derek-lowe/1294.bio and a digital feed at https://www.science.org/digital-feed/pipeline. Wikipedia: https://en.wikipedia.org/wiki/Derek_Lowe_(chemist)

#### Bruce Booth  `verified`

LifeSciVC, 2011-present: company-building and portfolio reasoning made explicit

- **home** — <https://lifescivc.com/>
- **x** — <https://x.com/LifeSciVC>
- **bio** — <https://atlasventure.com/team/bruce-booth-dphil/>

> Blogging since 2011; paginated archive at lifescivc.com/page/N/. Article index: https://muckrack.com/bruce-booth/articles

#### Pat Walters  `verified`

Practical Cheminformatics: how to evaluate computational drug-discovery claims

- **home** — <https://patwalters.github.io/>
- **archive** — <https://practicalcheminformatics.blogspot.com/>
- **x** — <https://x.com/wpwalters>
- **code** — <https://github.com/PatWalters/practical_cheminformatics_posts>
- **tutorials** — <https://github.com/PatWalters/practical_cheminformatics_tutorials>

> Blog moved from Blogger to GitHub Pages; Blogger remains as archive. Notebooks accompany posts. Chief Scientist at OpenADMET, adjunct UCSF, 2023 ACS Skolnik Award.

#### Robert Plenge  `verified`

PlengeGen: human-genetics-first target selection, written up as a method

- **home** — <https://plengegen.com/>
- **blog_index** — <https://plengegen.com/blog/category/drug-discovery/>
- **genetics** — <https://plengegen.com/blog/category/human-genetics/>

> Categorised blog archive (drug discovery / human genetics / NRDD). Full-time BMS employee.

#### David Grainger  `verified`

DrugBaron / Forbes: contrarian analysis of why developers make bad decisions

- **home** — <https://www.forbes.com/sites/davidgrainger/>
- **bio** — <https://www.medicxi.com/team/david-grainger>

> DrugBaron blog moved to Forbes; 20+ Forbes articles. Original DrugBaron archive needs locating. Founded Funxional Therapeutics, Total Scientific, RxCelerate.

#### Dennis X. Hu  `verified`

Drug Hunter: structured case histories of approved and clinical molecules

- **home** — <https://drughunter.com/>
- **profile** — <https://drughunter.com/contributor/dennis-x-hu>
- **x** — <https://twitter.com/denniswhom>

> Drug Hunter knowledge platform, 200+ R&D institutions. Ex-FLX Bio/RAPT and Genentech medicinal chemist. Stanford PhD.

#### Daniel Erlanson  `verified`

Fragment-based lead discovery; 15+ yrs of critical fragment literature review

- **home** — <https://practicalfragments.blogspot.com/>

> Practical Fragments, with Teddy Zartler. 15+ years of fragment-literature review.

#### Jack Scannell  `verified`

Eroom's Law; the 'better-than-the-Beatles' and model-validity theories of R&D decline

- **key_papers** — Eroom's Law, Nat Rev Drug Discov 2012
- **key_papers** — Predictive validity in drug discovery: what it is, why it matters and how to improve it
- **key_papers** — When Quality Beats Quantity: Decision Theory, Drug Discovery, and the Reproducibility Crisis
- **interviews** — https://decodingbio.substack.com/p/a-conversation-with-jack-scannell
- **interviews** — https://medium.com/@molecule.to/dr-jack-scannell-on-pharmas-evolving-landscape-f41add24a4f5
- **interviews** — https://molecule.xyz/blog/dr-jack-scannell-pharmas-evolving-landscape
- **chapter** — <https://www.oecd.org/en/publications/artificial-intelligence-in-science_a8d820bd-en/full-report/eroom-s-law-and-the-decline-in-the-productivity-of-biopharmaceutical-r-d_f42df75c.html>

> No personal blog. Reasoning lives in papers plus long interview transcripts. Etheros Pharma / Univ of Edinburgh.

### Foundational

#### Gertrude B. Elion  `partly-constructed`

Rational antimetabolite design: 6-MP, azathioprine, allopurinol, acyclovir

- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/1988/elion/lecture/>
- **lecture_text** — <https://openbooks.library.umass.edu/giftsofspeech/chapter/gertrude-b-elion-nobel-lecture-the-purine-path-to-chemotherapy-december-8-1988>
- **published_lecture** — <https://pubmed.ncbi.nlm.nih.gov/2679902/>

> Nobel lecture 'The purine path to chemotherapy' (8 Dec 1988), reprinted in Bioscience Reports 1989 and Angew Chem 1989. Oral history not yet located - check Science History Institute.

#### Sir James Black  `verified`

Propranolol (beta-blockade) and cimetidine (H2) — receptor-led drug design, twice

- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/1988/black/lecture/>
- **nobel_interview** — <https://www.nobelprize.org/prizes/medicine/1988/black/interview/>
- **biographical** — <https://www.nobelprize.org/nobel_prizes/medicine/laureates/1988/black-bio.html>
- **lindau** — <https://mediatheque.lindau-nobel.org/laureates/black>
- **legacy** — <https://www.cell.com/trends/pharmacological-sciences/fulltext/S0165-6147(11)00023-X>
- **royal_society_memoir** — <https://royalsocietypublishing.org/rsbm/article/doi/10.1098/rsbm.2019.0047/116082/Sir-James-Whyte-Black-OM-14-June-1924-22-March>

> Nobel lecture title: 'Drugs from emasculated hormones: the principles of syntopic antagonism'. Lindau Mediatheque holds lecture recordings.

#### Paul Janssen  `verified`

~80 marketed drugs incl. haloperidol, fentanyl, risperidone, loperamide, ketoconazole

- **heritage** — <https://www.jnj.com/our-heritage/meet-dr-paul-janssen-a-legend-in-pharmacology>
- **legacy** — <https://www.jnj.com/the-legacy-of-dr-paul-janssen-how-a-funny-idea-helped-change-the-course-of-modern-medicine>
- **memoriam** — <https://pubs.acs.org/doi/10.1021/jm040194j>
- **obituary_npp** — <https://www.nature.com/articles/1300423>
- **lancet** — <https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(03)15357-3/fulltext>

> 850+ publications, 100+ patents, 500+ scientific presentations, 80+ medicines. Janssen Pharmaceutica Beerse holds an extensive archive plus a series of interviews and company publications; complete publication list in 'Historical Record of Janssen Research Publications (1952-1990)'. That archive is the prize and needs a direct approach - not online.

#### Carl Djerassi  `verified`

Norethindrone — the first orally active progestin (the Pill)

- **autobiography** — The Pill, Pygmy Chimps, and Degas' Horse (1992)
- **home** — <https://www.djerassi.com/carl.html>
- **archive** — <https://archives.stanford.edu/findingaid/ark:/22236/s12da38ae9-37b4-4532-be3e-702b37af5c0f>
- **catalog** — <https://searchworks.stanford.edu/view/2208398>
- **profile** — <https://stanfordmag.org/contents/djerassi-reinvented>

> Carl Djerassi papers (SC0348), Stanford Special Collections, 1952-2014. Also wrote novels/plays. Science History Institute oral history not confirmed.

#### Solomon Snyder  `verified`

Opiate receptor identification; receptor-binding as a screening paradigm

- **book** — Brainstorming (Harvard University Press, 1989)
- **autobiography** — <https://www.sfn.org/-/media/SfN/Documents/TheHistoryofNeuroscience/Volume-6/c12.pdf>
- **scholar** — <https://scholar.google.com/citations?user=cmVIXBYAAAAJ>
- **archives** — <https://medicalarchives.jhmi.edu/portrait/solomon-h-snyder/>
- **collection** — <https://hopkinshistoryofmedicine.org/2025/01/15/collection-highlight-solomon-h-snyder-m-d/>
- **interview** — <https://www.psychiatrictimes.com/view/through-times-solomon-snyder-md>

> SfN History of Neuroscience in Autobiography vol 6 chapter is a full first-person career account (PDF). 1000+ papers. Donated authored-works collection to JHU on 2022 retirement.

### Medchem

#### Christopher A. Lipinski  `partial`

Rule of Five — property-based reasoning about oral drugs

- **wikipedia** — <https://en.wikipedia.org/wiki/Christopher_A._Lipinski>
- **profile** — <https://cen.acs.org/articles/85/i45/Christopher-Lipinski.html>
- **webinar** — <https://info.collaborativedrug.com/lipinski-bunin-ruleof5-0-0>

> Key primary artifact: the Adv Drug Deliv Rev Rule of Five paper and its 2001 reprint commentary. CDD webinar 'beyond the rule of 5' with Barry Bunin is a recorded discussion. No personal site.

#### Akira Endo  `verified`

Compactin (ML-236B) — the first statin, from fungal screening

- **first_person** — <https://www.jstage.jst.go.jp/article/pjab/86/5/86_5_484/_pdf>
- **obituary** — <https://www.pnas.org/doi/10.1073/pnas.2416550121>
- **tribute** — <https://academic.oup.com/eurheartj/article/45/9/647/7512939>

> 'A historical perspective on the discovery of statins', Proc Jpn Acad Ser B 86:484-493 (2010) - open-access first-person account, the single best artifact. Died 2024.

#### P. Roy Vagelos  `verified`

Ran the lab-to-market machine behind lovastatin; the Mectizan donation decision

- **book** — Medicine, Science and Merck (Vagelos & Galambos, Cambridge UP, 2004)
- **interview** — <https://hbr.org/1994/11/medicine-management-and-mergers-an-interview-with-mercks-p-roy-vagelos>
- **jci_interview** — <https://www.jci.org/articles/view/76755>

> JCI 'A conversation with P. Roy Vagelos' includes a video interview. Merck CEO 1985-1994.

#### Joshua Boger  `verified`

Structure-based design as a company thesis; HIV and HCV protease inhibitors

- **book_subject** — The Billion-Dollar Molecule (Barry Werth, 1994) and its sequel The Antidote
- **founder_story** — <https://www.youtube.com/watch?v=rlP_BdU197I>
- **stat_interview** — <https://www.statnews.com/2023/12/11/vertex-founder-joshua-boger-interview/>
- **rules** — <https://dallasinnovates.com/vertex-pharma-founder-shares-his-eight-lessons-for-startup-success/>
- **wesleyan** — <https://newsletter.blogs.wesleyan.edu/2011/05/24/boger-73-featured-in-cure-entrepreneur-video>
- **bio** — <https://www.hks.harvard.edu/about/joshua-boger>

> CEO of Vertex 1989-2009. 'Founder Stories' YouTube video plus the 2023 STAT Q&A on Casgevy are the two best first-person artifacts.

#### Paul Negulescu  `verified`

CFTR modulators (ivacaftor, tezacaftor, elexacaftor) via functional screening

- **wikipedia** — <https://en.wikipedia.org/wiki/Paul_Negulescu>
- **lasker** — <https://laskerfoundation.org/winners/combined-triple-drug-therapy-for-cystic-fibrosis/>
- **interview_series** — <https://cysticfibrosisnewstoday.com/cystic-fibrosis/vertex-cystic-fibrosis-and-steps-on-long-road-to-medical-history-part-one-interview-series/>

> 2025 Lasker-DeBakey, 2024 Breakthrough Prize, 2022 Shaw Prize, 2018 Warren Alpert - all with Van Goor and Hadida, and all carry acceptance remarks/lectures. Lasker page is the highest-value entry point.

#### Stephen W. Fesik  `partial`

SAR by NMR; ABT-737 lineage leading to venetoclax; now MYC/RAS

- **lab** — <https://lab.vanderbilt.edu/fesik-lab/>
- **publications** — <https://lab.vanderbilt.edu/fesik-lab/publications/>
- **profile** — <https://www.vanderbilt.edu/csb/faculty-core/steve-fesik/>
- **review** — <https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00892>

> 'Drugging Challenging Cancer Targets Using Fragment-Based Methods', Chem Rev 2025 - a full statement of method. Foundational: BCL-xL X-ray/NMR structure 1996 at Abbott. No lecture video located yet; check Vanderbilt and ACS channels.

#### Phil S. Baran  `verified`

Scalable synthesis and electrochemistry that changes what med chem can make

- **lab** — <https://baranlab.org/>
- **home** — <https://www.scripps.edu/faculty/baran/>
- **profile** — <https://www.chemistryworld.com/features/the-sultan-of-synthesis/7261.article>
- **interview** — <https://www.bio-itworld.com/news/2020/09/03/phil-baran-on-the-quest-to-make-chemistry-boring-again>

> Baran Lab site hosts group teaching materials/handouts. Co-founded Sirenas, Vividion, Elsie Biotechnologies, Elima. X handle not confirmed.

#### E. J. Corey  `verified`

Retrosynthetic analysis — the explicit logic of synthesis planning

- **book** — The Logic of Chemical Synthesis (Corey & Cheng, Wiley 1989)
- **book_pdf** — <https://ia601303.us.archive.org/25/items/Logic_of_Chemical_Synthesis_Corey_1989/Logic_of_Chemical_Synthesis_Corey_1989_text.pdf>
- **nobel_lecture** — <https://www.nobelprize.org/prizes/chemistry/1990/corey/lecture/>
- **nobel_lecture_pub** — <https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.199104553>

> Nobel lecture title 'The Logic of Chemical Synthesis: Multistep Synthesis of Complex Carbogenic Molecules'. Book is on Internet Archive in full text - the single densest artifact of explicit synthesis reasoning available. Retrosynthesis introduced in Harvard Chem 115, from 1960.

### Oncology

#### Brian J. Druker  `partial`

Imatinib — clinical champion of targeted kinase inhibition in CML

- **lasker** — <https://laskerfoundation.org/winners/molecularly-targeted-treatments-for-chronic-myeloid-leukemia/>
- **lasker_essay** — <https://www.jci.org/articles/view/41141>
- **account** — <http://www.cptech.org/ip/health/gleevec/drucker.html>
- **wikipedia** — <https://en.wikipedia.org/wiki/Brian_Druker>

> 2009 Lasker-DeBakey Clinical award (with Lydon and Sawyers) - the Lasker page and JCI essay carry the reasoning. cptech page is a first-person account of his Gleevec R&D involvement. Book context: 'The Philadelphia Chromosome' (Jessica Wapner). No lecture video located.

#### Charles L. Sawyers  `verified`

Imatinib resistance mechanisms; enzalutamide; resistance-first thinking

- **lab** — <https://www.mskcc.org/research-areas/labs/charles-sawyers>
- **overview** — <https://www.mskcc.org/research-areas/labs/charles-sawyers/overview>
- **publications** — <https://www.mskcc.org/research-areas/labs/charles-sawyers/publications>
- **lecture** — <https://www.mskcc.org/videos/science-spotlight-lecture-charles-sawyers-md>
- **takamatsu** — <https://ascopost.com/issues/april-10-2019/charles-sawyers-2019-aacr-princess-takamatsu-memorial-lectureship/>
- **profile** — <https://leadingdiscoveries.aacr.org/dr-charles-l-sawyers-at-the-leading-edge-of-targeted-therapies/>

> MSK Science Spotlight lecture (8 Apr 2020) is video. Four named enzalutamide-resistance mechanisms make his resistance-first reasoning unusually traceable. 2019 AACR Princess Takamatsu Memorial Lectureship.

#### Kevan M. Shokat  `verified`

Drugging KRAS G12C via the switch-II pocket; analog-sensitive kinase alleles

- **podcast** — <https://podcasts.apple.com/gb/podcast/kevan-shokat-drugging-the-undruggable-kras/id1690601747?i=1000651329103>
- **interview** — <https://journals.biologists.com/dmm/article/15/2/dmm049468/274597/Drugging-the-undruggable-Ross-Cagan-interviews>
- **nih_lecture** — <https://www.youtube.com/watch?v=rtR3yl5U4yk>
- **talk** — <https://www.youtube.com/watch?v=U2upT2-XIE0>
- **ras_chat** — <https://frederick.cancer.gov/news/ras-chat-interview-kevan-shokat-and-ziyang-zhang>
- **aacr** — <https://www.aacr.org/about-the-aacr/newsroom/pioneers-and-innovators/kevan-m-shokat-phd-drugging-the-elusive-kras/>

> Unusually rich: video podcast, NIH Director's WALS lecture (Mar 2023), two long interviews. Best single reasoning artifact is the Cagan interview.

#### Craig M. Crews  `verified`

PROTACs — targeted protein degradation as a new modality

- **profile** — <https://medicine.yale.edu/profile/craig-crews/>
- **podcast** — <https://www.discoveryontarget.com/Craig_Crews_Podcast>
- **origin_story** — <https://sne-chembio.ch/blog/craig-crews/>
- **wikipedia** — <https://en.wikipedia.org/wiki/Craig_M._Crews>

> PROTAC origin: met Ray Deshaies 1998 at a Burroughs Wellcome retreat. Podcast tells the birth-and-evolution story directly.

#### James E. Bradner  `verified`

JQ1 / BET bromodomain inhibition; open sharing of probes; then ran NIBR

- **ted** — <https://www.ted.com/talks/jay_bradner_open_source_cancer_research>
- **ted_speaker** — <https://www.ted.com/speakers/jay_bradner>
- **archive** — <https://archive.org/details/JayBradner_2011X>
- **youtube** — <https://www.youtube.com/watch?v=wOiKRVH0nQ8>

> TEDxBoston 2011 'Open-source cancer research' - the JQ1 open-sharing decision argued in his own words. Internet Archive copy is downloadable.

#### Stuart L. Schreiber  `verified`

Chemical biology as a discipline; FKBP/mTOR mechanism; many companies

- **bio** — <https://www.broadinstitute.org/bios/stuart-l-schreiber>
- **seminar** — <https://www.broadinstitute.org/videos/broad-mit-seminars-chemical-biology-stuart-schreiber>
- **vimeo** — <https://vimeo.com/359603257>
- **youtube_1** — <https://www.youtube.com/watch?v=F7eG7C8qYcI>
- **youtube_2** — <https://www.youtube.com/watch?v=M4LcM5MgdlY>
- **interview** — <https://pubmed.ncbi.nlm.nih.gov/15037226/>

> Broad-MIT Seminars in Chemical Biology lecture 'Listening to Probes: Individuals and Populations'. Founding director of Harvard ICCB 1997.

#### William G. Kaelin Jr.  `partly-constructed`

VHL-HIF oxygen sensing (belzutifan); also the field's sharpest writing on rigour

- **essay** — <https://www.nature.com/articles/545387a>
- **essay_pubmed** — <https://pubmed.ncbi.nlm.nih.gov/28541345/>
- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/2019/kaelin/lecture/>

> 'Publish houses of brick, not mansions of straw', Nature 545:387 (2017) - F1000Prime top recommended article for six months running. Nobel 2019 (with Ratcliffe, Semenza).

#### Judah Folkman  `partial`

Angiogenesis as a therapeutic target — a hypothesis held against consensus

- **biography** — Dr. Folkman's War: Angiogenesis and the Struggle to Defeat Cancer (Robert Cooke, 2001)
- **nlm** — <https://profiles.nlm.nih.gov/spotlight/mv/catalog/nlm:nlmuid-101584926X330-img>
- **obituary** — <https://www.thelancet.com/article/S0140-6736(08)60191-9/fulltext>

> Gave an NIH Director's Lecture 'New Directions in Angiogenesis Research'. Check NLM Profiles in Science for archived lecture video. Died 2008.

### Biologics

#### Sir Gregory Winter  `constructed`

Humanised antibodies and phage display — the route to adalimumab and beyond

- **nobel_lecture** — <https://www.nobelprize.org/prizes/chemistry/2018/winter/lecture/>
- **nobel_interview** — <https://www.nobelprize.org/prizes/chemistry/2018/winter/interview/>

> Nobel Chemistry 2018 (phage display of peptides and antibodies), shared with George Smith and Frances Arnold. Constructed from the confirmed URL pattern; validated separately. MRC LMB oral histories are a further target.

#### James P. Allison  `verified`

CTLA-4 blockade — ipilimumab; the checkpoint concept

- **documentary** — Jim Allison: Breakthrough (2019, dir. Bill Haney, narr. Woody Harrelson)
- **doc_page** — <https://www.collectiveeye.org/products/jim-allison-breakthrough>
- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/2018/allison/lecture/>
- **yervoy_story** — <https://crl.berkeley.edu/discoveries/the-story-of-yervoy-ipilimumab/>
- **cri** — <https://www.cancerresearch.org/blog/jim-allison-breakthrough-documentary>
- **qa** — <https://healthtree.org/myeloma/community/events/jim-allison-breakthrough-q-a-with-immunotherapy-pioneer-dr-allison-and-dr-sharma-on-november-15th-3-pm-eastern>

> The core reasoning move: recognising CTLA-4 as a brake rather than a pedal. UC Berkeley CRL's 'Story of Yervoy' documents the path. Documentary premiered SXSW March 2019.

#### Carl H. June  `verified`

CD19 CAR-T cell therapy into the clinic

- **documentary** — Of Medicine and Miracles (2022)
- **doc_page** — <https://www.pennmedicine.org/news/now-streaming-documentary-on-penn-developed-car-t-cancer-cure>
- **interview_parker** — <https://www.parkerici.org/the-latest/behind-the-breakthrough-an-interview-with-carl-june-the-father-of-car-t-cell-therapy/>
- **interview_aacr** — <https://www.aacr.org/blog/2020/08/31/an-interview-with-carl-june-md-a-pioneer-in-car-t-cell-therapy/>
- **podcast** — <https://www.cellandgene.com/doc/an-interview-with-dr-carl-june-0001>
- **a16z** — BioEatsWorld podcast episode on the future of CAR-T

> 2024 Breakthrough Prize. Documentary follows the Emily Whitehead case. Correction to roster: no memoir of his own located - the book-length account is the documentary plus third-party coverage.

#### Steven A. Rosenberg  `verified`

Adoptive cell transfer, TIL therapy, IL-2 — decades of iterative clinical work

- **book** — The Transformed Cell (Rosenberg & Barry, 1992)
- **nih_profile** — <https://ccr.cancer.gov/staff-directory/steven-a-rosenberg>
- **irp** — <https://irp.nih.gov/pi/steven-rosenberg>
- **podcast_attia** — <https://peterattiamd.com/stevenrosenberg/>
- **videocast_1** — <https://videocast.nih.gov/Summary.asp?File=18977>
- **videocast_2** — <https://videocast.nih.gov/watch=55071>
- **reflections** — <https://www.moffitt.org/endeavor/archive/immunotherapy-pioneer-steven-rosenberg-reflects-on-past-breakthroughs-and-future-promise/>

> NIH VideoCast holds a large archive incl. the symposium for his 50 years at NCI ('Past, Present, and Future of Cellular Immunotherapy'). Peter Attia episode #177 is a long-form interview. NIH VideoCast is downloadable and transcript-friendly.

### Genetic Medicine

#### Katalin Kariko  `verified`

Nucleoside modification making mRNA therapeutically usable

- **memoir** — Breaking Through: My Life in Science (2023)
- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/2023/kariko/lecture/>
- **nobel_interview** — <https://www.nobelprize.org/prizes/medicine/2023/kariko/interview/>
- **nobel_podcast** — <https://www.nobelprize.org/prizes/medicine/2023/kariko/podcast/>
- **interview_issues** — <https://issues.org/interview-katalin-kariko/>
- **podcast_lwos** — <https://www.lostwomenofscience.org/podcast-episodes/lost-women-of-science-conversations-breaking-through>
- **topol** — <https://erictopol.substack.com/p/katalin-kariko-the-unimaginable-obstacle>
- **pbs** — <https://www.pbs.org/video/she-was-demoted-threatened-then-she-won-the-nobel-prize-ztux>

> NobelPrize.org carries lecture + interview + podcast per laureate - a constructible four-artifact set. Eric Topol's Ground Truths interview is long-form and transcribed.

#### Drew Weissman  `constructed`

Co-discovered modified-nucleoside mRNA; vaccine and therapeutic translation

- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/2023/weissman/lecture/>
- **nobel_interview** — <https://www.nobelprize.org/prizes/medicine/2023/weissman/interview/>
- **nobel_podcast** — <https://www.nobelprize.org/prizes/medicine/2023/weissman/podcast/>

> Nobel 2023 with Kariko. Constructed from the confirmed NobelPrize.org URL pattern; validated separately. Pair his account with Kariko's - the two tell the same decade from different sides.

#### Robert S. Langer  `verified`

Controlled release and delivery; co-founder of Moderna and ~40 others

- **lab** — <https://langer-lab.mit.edu/>
- **news_archive** — <https://langer-lab.mit.edu/news/archive>
- **podcast_shi** — <https://sciencehistory.org/distillations/podcast/interview-with-robert-langer>
- **podcast_da** — <https://www.discoveringacademia.com/episodes/robert-langer>
- **podcast_us** — <https://www.unnaturalselection.net/podcast/s1e17>
- **video** — <https://communities.springernature.com/videos/an-interview-with-one-of-the-greatest-leaders-in-chemical-engineering-medicine-and-science-dr-robert-s-langer-sc-d-mit-institute-professor-and-co-founder-of-moderna>

> Science History Institute Distillations interview is a proper oral-history-grade artifact. 40+ companies founded; the recurring question across interviews is how he picks problems.

#### Pieter R. Cullis  `verified`

Lipid nanoparticles for nucleic-acid delivery (patisiran, mRNA vaccines)

- **profile** — <https://lsi.ubc.ca/people/pieter-cullis/>
- **review** — <https://www.nature.com/articles/s41578-021-00379-9>
- **review_pubmed** — <https://pubmed.ncbi.nlm.nih.gov/34567796/>
- **evolution** — <https://pubmed.ncbi.nlm.nih.gov/38965378/>
- **talk_pdf** — <https://www.phospholipid-research-center.com/wp-content/uploads/2021/09/OPS2021-Cullis.pdf>
- **britannica** — <https://www.britannica.com/biography/Pieter-Cullis>

> 'From lipids to lipid nanoparticles to mRNA vaccines' (Nat Rev Mater 2021) is a first-person narrative review and the best single artifact. 'The 60-year evolution of LNPs for nucleic acid delivery' (2024) is the long view. Book title not confirmed - remove the roster's book claim until verified.

#### Ugur Sahin  `verified`

mRNA cancer immunotherapy and the COVID-19 vaccine (with Ozlem Tureci)

- **ted** — <https://www.ted.com/speakers/ugur_sahin>
- **milstein_lecture** — <https://www2.mrc-lmb.cam.ac.uk/cesar-milstein-lecture-to-be-given-by-ugur-sahin-and-ozlem-tureci/>
- **book** — The Vaccine (Joe Miller with Sahin and Tureci, 2021)
- **book_page** — <https://us.macmillan.com/books/9781250280374/thevaccine/>
- **interview_cri** — <https://www.cancerresearch.org/blog/mrna-covid-cancer-vaccines-ugur-sahin-ozlem-tureci>
- **paper** — <https://pmc.ncbi.nlm.nih.gov/articles/PMC8573597/>
- **time** — <https://time.com/collection-post/6270459/ozlem-tureci-and-ugur-sahin>

> 2022 Cesar Milstein Lecture (with Tureci) at MRC LMB. 'The Vaccine' was written with their cooperation plus 60+ interviews - effectively an authorised reconstruction of a year of decisions. BioNTech founded 2008 with Christoph Huber.

#### Barney S. Graham  `verified`

Prefusion-stabilised antigen design (RSV F, spike-2P) — structure-based vaccinology

- **profile** — <https://www.msm.edu/about_us/FacultyDirectory/MicrobiologyBiochemistryImmunology/BarneyGraham/index.php>
- **inventors_hall** — <https://www.invent.org/inductees/barney-graham>
- **lecture_abstract** — <https://dc.engconfintl.org/vt_vii/138/>
- **cen_account** — <https://cen.acs.org/pharmaceuticals/vaccines/tiny-tweak-behind-COVID-19/98/i38>
- **natgeo** — <https://www.nationalgeographic.com/science/article/these-scientists-spent-twelve-years-solving-puzzle-yielded-coronavirus-vaccines>

> The 2P proline-stabilisation story is the cleanest structure-based design reasoning in modern vaccinology. C&EN 'The tiny tweak behind COVID-19 vaccines' reconstructs the decision. Lecture 'Structure-based vaccines for respiratory viruses'. Video not yet located - check NIH VideoCast.

#### Stanley T. Crooke  `verified`

Antisense oligonucleotides as a durable drug platform

- **podcast_own** — <https://podcasts.apple.com/us/podcast/patient-empowerment-program-a-rare-disease-podcast/id1624577541>
- **podcast_waves** — <https://podcasts.apple.com/us/podcast/s2-e3-a-between-the-biotech-waves-conversation/id1626193282?i=1000694389567>
- **podcast_vital** — <https://www.criver.com/insights/vital-science-podcast/s4-e07-free-for-life-the-story-of-n-lorem-foundation>
- **interview_cen** — <https://cen.acs.org/pharmaceuticals/Stanley-Crooke-finally-making-sense/97/i18>
- **interview_bx** — <https://www.bioxconomy.com/modalities/dose-of-discovery-stanley-crooke-on-fixing-nano-rare-disease-with-oligos>

> Hosts his own podcast (Patient Empowerment Program) - a continuous first-person feed. Founded Ionis 1989; previously Bristol Labs and head of R&D at SKB. n-Lorem treats n-of-1 patients.

#### David R. Liu  `verified`

Base editing and prime editing; Beam, Prime, Editas

- **broad_talk** — <https://www.broadinstitute.org/videos/base-editing-and-prime-editing-precise-chemistry-genome-without-double-strand-dna-breaks>
- **youtube_1** — <https://www.youtube.com/watch?v=rdL3lpo7ftQ>
- **youtube_2** — <https://www.youtube.com/watch?v=ml1svbRo7Lg>
- **podcast_ark** — <https://www.ark-invest.com/podcast/ep-99-david-liu>
- **podcast_gv** — <https://podcast.gv.com/gene-editing/>
- **podcast_bios** — <https://www.bios.community/podcast/56-future-of-gene-editing>
- **podcast_ipm** — <https://www.insideprecisionmedicine.com/multimedia/podcasts/behind-the-breakthroughs/david-liu-performing-chemistry-on-dna-to-unlock-personalized-gene-editing/>
- **topol** — <https://erictopol.substack.com/p/david-liu-a-master-class-on-the-future>
- **interview_genen** — <https://www.genengnews.com/topics/genome-editing/feel-that-base-an-interview-with-base-editing-pioneer-david-liu/>

> Six+ long podcast interviews plus recorded lectures. Founder of nine companies incl. Editas, Beam, Prime. His lectures narrate design reasoning step by step - the richest single target in the genetic-medicine group.

#### Fyodor Urnov  `verified`

Genome editing as medicine; bespoke CRISPR therapies for n-of-1 patients

- **profile** — <https://innovativegenomics.org/people/fyodor-urnov/>
- **interview_1** — <https://www.genengnews.com/topics/genome-editing/engineering-crispr-cures-an-interview-with-fyodor-urnov/>
- **interview_2** — <https://www.genengnews.com/topics/genome-editing/fyodor-urnov-discusses-crispr-cures/>
- **topol** — <https://erictopol.substack.com/p/on-genome-editing-with-fyodor-urnov>
- **podcast_ge** — <https://www.genomicsengland.co.uk/podcasts/fyodor-urnov-putting-our-ancestors-in-a-tesla>
- **biotechtv** — <https://www.biotechtv.com/post/innovative-genomics-institute-fyodor-urnov-december-13-2023>
- **npf** — <https://nationalpress.org/topic/fyodor-urnov-innovative-genomics-institute-berkely-crispr-health-equity/>

> Coined 'genome editing' in 2005 at Sangamo. 100+ papers, 130+ patents. Also writes NYT op-eds. Known for extended automotive metaphors - his explanatory style is itself the artifact.

### Antiviral

#### Michael J. Sofia  `verified`

Sofosbuvir — phosphoramidate prodrug design that cured HCV

- **lasker_essay** — <https://laskerfoundation.org/wp-content/uploads/2021/01/2016_cell_article_-_sofia.pdf>
- **lasker_page** — <https://laskerfoundation.org/winners/hepatitis-c-replicon-system-and-drug-development/>
- **jci** — <https://www.jci.org/articles/view/90179>
- **discovery_chapter** — <https://link.springer.com/chapter/10.1007/7355_2018_37>
- **discovery_paper** — <https://www2.chem.wisc.edu/deptfiles/chem345-gellman/Sp13/Antiviral_Drug/Sofosbuvir%20discovery%2010.pdf>
- **stat** — <https://www.statnews.com/2016/09/13/lab-breakthrough-hepatitis-c/>

> 'Enter Sofosbuvir: The Path to Curing HCV' (Cell 2016, Lasker essay, free PDF) is a first-person design narrative - liver-targeted nucleotide prodrug logic laid out in full. Plus a book chapter 'The Discovery of Sofosbuvir'. Best-documented single molecule on the list.

### Metabolic Cv

#### Michael S. Brown  `partly-constructed`

LDL receptor pathway — the mechanistic basis for statins and PCSK9 drugs

- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/1985/brown/lecture/>
- **lasker_partnership** — <https://laskerfoundation.org/brown-goldstein/>
- **utsw_50yr** — <https://www.utsouthwestern.edu/ctplus/stories/2022/brown-goldstein-fifty-year-celebration.html>

> Nobel 1985 with Goldstein. Their joint Nobel lecture and 50-year retrospective document a scientific partnership as a working method. A 2020 book covers their NIH start.

#### Joseph L. Goldstein  `verified`

Co-discoverer of LDL-receptor regulation; sharp essayist on scientific taste

- **nobel_lecture** — <https://www.nobelprize.org/prizes/medicine/1985/goldstein/lecture/>
- **biographical** — <https://www.nobelprize.org/prizes/medicine/1985/goldstein/biographical/>
- **profile** — <https://profiles.utsouthwestern.edu/profile/12645/joseph-goldstein.html>
- **essay_series** — Annual Nature Medicine Lasker supplement essays, 2000/2001-present

> KEY: chairs the Lasker Awards jury since 1996 and has written an annual Nature Medicine essay series since ~2000 on creativity, elegance and taste in science - what makes an experiment 'elegant' or a body of work 'beautiful'. That series is one of the best explicit statements of scientific judgement in the corpus and needs collecting in full.

#### Helen H. Hobbs  `verified`

PCSK9 and ANGPTL3 loss-of-function humans — genetics as target validation

- **lab** — <https://labs.utsouthwestern.edu/hobbs-cohen-lab/people>
- **jci_conversation** — <https://www.jci.org/articles/view/84086>
- **tnq_lectures** — <https://www.tnqdistinguishedlectures.org/about-speaker/helen-hobbs.html>
- **bloch_lecture** — <https://www.mcb.harvard.edu/department/news/march-14-helen-hobbs-presents-2019-bloch-lecture/>
- **ricketts_lecture** — <https://biologicalsciences.uchicago.edu/news/helen-hobbs-ricketts-lecture>

> JCI 'A conversation with Helen Hobbs' includes video. Named lecture series: TNQ Distinguished Lectures 2019 (three cities), Harvard Bloch Lecture 2019, 107th Ricketts Lecture 2022. Dallas Heart Study outlier method is the reasoning to capture.

#### Sekar Kathiresan  `verified`

Human genetics to base-edited PCSK9/ANGPTL3 therapies

- **podcast_external_medicine** — <https://externalmedicinepodcast.com/sekar-kathiresan/>
- **podcast_biotech2050** — <https://www.biotech2050.com/episodes/single-course-gene-editing-for-cardiovascular-disease-sekar-kathiresan-co-founder-amp-ceo-verve-tx>
- **podcast_long_run** — <https://timmermanreport.com/2021/02/a-single-shot-for-heart-disease-sekar-kathiresan-on-the-long-run/>
- **interview** — <https://crisprmedicinenews.com/news/first-patient-is-dosed-with-base-editor-to-treat-familial-hypercholesterolemia-interview-sekar-kat/>
- **substack** — <https://breakingground.substack.com/p/head-of-obesity-research-at-eli-lilly>
- **wikipedia** — <https://en.wikipedia.org/wiki/Sekar_Kathiresan>

> Four+ long podcast interviews - unusually good for transcript mining. Targets from human genetics: NPC1L1, APOC3, ANGPTL3, PCSK9. Active on X.

#### Daniel J. Drucker  `verified`

GLP-1 biology; the intellectual through-line to incretin drugs

- **home** — <https://glucagon.com/druckerlab>
- **site** — <https://glucagon.com/>
- **jci_conversation** — <https://www.jci.org/articles/view/154150>
- **qa** — <https://www.cell.com/med/fulltext/S2666-6340(24)00293-9>
- **interview_utmj** — <https://jps.library.utoronto.ca/index.php/utmj/article/view/47411>
- **profile** — <https://www.utoronto.ca/news/setback-lizard-and-decades-work-impact-daniel-drucker-s-research-extends-far-beyond-ozempic>
- **topol** — Ground Truths podcast interview

> glucagon.com has served for years as the field's central repository - his own curated archive of foundational studies and integrative reviews. Highest-value self-maintained resource of anyone in the metabolic group.

#### Lotte Bjerre Knudsen  `verified`

Acylation design giving liraglutide and semaglutide their half-lives

- **podcast_acquired** — <https://www.acquired.fm/acq2-episodes/the-scientific-journey-behind-ozempic-with-lotte-bjerre-knudsen-novo-nordisks-chief-scientific-advisor>
- **first_person_paper** — <https://pubs.acs.org/aptsfn/article/2/6/468/1383356/Inventing-Liraglutide-a-Glucagon-Like-Peptide-1>
- **paper_pmc** — <https://pmc.ncbi.nlm.nih.gov/articles/PMC7088919/>
- **topol** — <https://erictopol.substack.com/p/lotte-bjerre-knudsen-the-scientist>
- **stat** — <https://www.statnews.com/2023/10/17/lotte-knudsen-novo-nordisk-obesity-drug-liraglutide-ozempic-wegovy/>
- **profile** — <https://pharmatimes.com/magazine/2019/march/smartpeople_lotte_bjerre_knudsen/>

> 'Inventing Liraglutide' (ACS Pharmacol Transl Sci 2019) is a first-person invention account - C16 albumin-binding fatty acid side chain, then C18 diacid plus a DPP-4-resistant substitution for semaglutide. Acquired ACQ2 episode is a long-form design narrative. 2024 Lasker.

#### Richard D. DiMarchi  `partial`

Insulin analogues (lispro); GIP/GLP-1 multi-agonist concept behind tirzepatide

- **profile** — <https://news.iu.edu/live/news/48708-richard-dimarchi-pioneering-iu-peptide-chemist>
- **story** — <https://www.myiu.org/news-stories/behind-the-ozempic-headlines.html>
- **award** — <https://www.aaas.org/news/innovators-glp-1-obesity-bhaumik-breakthrough>
- **science_piece** — <https://www.science.org/doi/10.1126/science.adq6452>
- **review** — <https://www.sciencedirect.com/science/article/pii/S1550413123002693>
- **researchgate** — <https://www.researchgate.net/profile/Richard-Dimarchi>

> 20 years at Lilly Research Labs; discovered the active peptide of Humalog. The GLP-1/GIP single-molecule dual-agonist insight became tirzepatide. Shared the 2024 Bhaumik award with Knudsen. No dedicated lecture video located.

### Cns

#### Steven M. Paul  `verified`

Muscarinic agonism for psychosis (KarXT); candid on CNS attrition

- **interview_fierce** — <https://www.fiercebiotech.com/biotech/jpm-conversation-steve-paul-ceo-karuna-therapeutics>
- **profile** — <https://www.pharmavoice.com/news/karuna-therapeutics-neuroscience-steve-paul/625509/>
- **program_history** — <https://www.fiercebiotech.com/biotech/how-karunas-schizophrenia-med-karxt-went-serendipitous-clinical-finding-fda-25-not-so-short>

> The KarXT story is a clean case of reasoning about a shelved asset: xanomeline's M1/M4 agonism worked but peripheral cholinergic side effects killed it at Lilly; pairing with trospium (does not cross the BBB) rescued it 25 years later. Paul inherited the molecule at Lilly and later built the company around it. Ex-Lilly EVP science and technology / president of Lilly Research Labs; also co-founded Sage.

#### John Hardy  `verified`

Amyloid cascade hypothesis from APP genetics; genetics-first neurodegeneration

- **profile_ukdri** — <https://www.ukdri.ac.uk/team/john-hardy>
- **breakthrough** — <https://breakthroughprize.org/Laureates/2/L168>
- **ucl** — <https://www.ucl.ac.uk/brain-sciences/news/2015/nov/ucl-institute-neurology-professor-john-hardy-first-uk-winner-3m-breakthrough-prize-life-sciences>
- **feature** — <https://www.ucl.ac.uk/brain-sciences/news/2022/dec/feature-historic-alzheimers-breakthrough-30-years-making>
- **alzforum** — <https://www.alzforum.org/news/community-news/introducing-sir-john>
- **editorial** — <https://onlinelibrary.wiley.com/doi/10.1111/jnc.15593>

> 1991 first APP mutation implicated in Alzheimer's, leading to the amyloid cascade hypothesis. ALZFORUM is the place his running commentary and revisions live - worth crawling as a venue, not just his page. Breakthrough Prize 2016, Brain Prize 2018, knighted 2022.

### Computational

#### David Baker  `verified`

De novo protein design; designed binders and minibinder therapeutics

- **nobel_interview** — <https://www.nobelprize.org/prizes/chemistry/2024/baker/interview/>
- **nobel_lecture** — <https://www.nobelprize.org/prizes/chemistry/2024/baker/lecture/>
- **nih_lecture** — <https://videocast.nih.gov/watch=46050>
- **ted** — <https://www.youtube.com/watch?v=k-9sQXhHHmk>
- **talk_deep_learning** — <https://www.youtube.com/watch?v=EcPCQC1_4Ks>
- **talk_bios** — <https://www.youtube.com/watch?v=WioAzuaybok>
- **explainer** — <https://www.youtube.com/watch?v=g96tXNwrYXc>
- **podcast_ebrc** — <https://ebrcintranslation.buzzsprout.com/1581817/episodes/10251245-11-protein-design-and-the-communal-brain-w-david-baker>
- **qa** — <https://journals.sagepub.com/doi/10.1089/genbio.2025.0004>

> NIH VideoCast 'The Coming of Age of De Novo Protein Design' (Dec 2022) is downloadable. The 'communal brain' framing of how his lab works recurs across interviews and is itself a reasoning artifact about running a research group.

#### John M. Jumper  `verified`

AlphaFold2 — structure prediction at usable accuracy

- **nobel_podcast** — <https://www.nobelprize.org/prizes/chemistry/2024/jumper/podcast/>
- **nobel_lecture** — <https://www.nobelprize.org/prizes/chemistry/2024/jumper/lecture/>
- **podcast_yc** — <https://podcasts.apple.com/za/podcast/john-jumper-alphafold-and-the-future-of-science/id1236907421?i=1000717377311>
- **podcast_dm** — <https://podcasts.apple.com/gb/podcast/alphafold-grand-challenge-to-nobel-prize-with-john-jumper/id1476316441?i=1000738797143>
- **bloch_lecture** — <https://datascience.uchicago.edu/events/john-jumper-google-deepmind-bloch-lecture/>
- **tnq** — <https://www.tnqdistinguishedlectures.org/about-speaker/john-jumper.php>

> Google DeepMind podcast episode (47 min, Hannah Fry) traces AlphaFold 1 to 3. Y Combinator episode covers the CASP14 turn. EBI talk covers the history of AlphaFold. Strong on what the model does NOT solve - useful negative reasoning.

#### Mohammed AlQuraishi  `verified`

Protein structure prediction; the field's most analytical essayist on ML in bio

- **blog** — <https://moalquraishi.wordpress.com/>
- **author_index** — <https://moalquraishi.wordpress.com/author/moalquraishi/>
- **feed** — <https://moalquraishi.wordpress.com/feed/>
- **key_post_1** — <https://moalquraishi.wordpress.com/2020/12/08/alphafold2-casp14-it-feels-like-ones-child-has-left-home/>

> Long-form essays: 'AlphaFold2 @ CASP14', 'The AlphaFold2 Method Paper: A Fount of Good Ideas', 'The Future of Protein Science will not be Supervised'. WordPress feed makes the whole archive machine-readable.

#### Gregory Landrum  `verified`

RDKit — the open cheminformatics substrate of modern discovery

- **blog** — <https://greglandrum.github.io/rdkit-blog/>
- **about** — <https://greglandrum.github.io/rdkit-blog/about.html>
- **repo** — <https://github.com/greglandrum/rdkit-blog>
- **old_repo** — <https://github.com/greglandrum/rdkit_blog>
- **archive** — <https://rdkit.blogspot.com/>
- **move_notice** — <https://rdkit.blogspot.com/2022/01/the-rdkit-blog-has-moved.html>

> Blog moved from Blogspot to GitHub Pages in Jan 2022; both halves needed for the full archive. Posts are Jupyter notebooks in the repo - reasoning as executable code, same as Pat Walters.

### Strategy

#### Roger M. Perlmutter  `verified`

Backed pembrolizumab when it was shelved; explicit about R&D portfolio reasoning

- **bio** — <https://www.eikontx.com/team/roger-perlmutter/>
- **isb** — <https://isbscience.org/people/roger-perlmutter-md-phd/>
- **podcast_approved** — <https://www.approved.fm/p/keytruda-how-mercks-pembrolizumab>
- **podcast_leaders** — <https://podcasts.apple.com/us/podcast/leaders-legends/id1779154155>
- **profile** — <https://www.innovationendeavors.com/insights/meet-super-evolution-driver-roger-perlmutter-president-and-ceo-of-eikon-therapeutics>
- **wikipedia** — <https://en.wikipedia.org/wiki/Roger_M._Perlmutter>

> The 'Approved' podcast traces Keytruda from origin to approval with interviews from the program leads; 'Leaders & Legends' covers rebuilding Merck's clinical development org across 140+ approvals. Both are decision-reasoning gold. Now CEO of Eikon.

#### Mene Pangalos  `verified`

The '5R framework' — an explicit, published decision rubric for projects

- **paper_2014** — <https://www.nature.com/articles/nrd4309>
- **paper_2018** — <https://www.nature.com/articles/nrd.2017.244>
- **az_page** — <https://www.astrazeneca.com/what-science-can-do/topics/disease-understanding/transforming-astrazenecas-rd-productivity.html>
- **biocentury** — <https://www.biocentury.com/article/292629/astrazeneca-says-5r-framework-increased-productivity>
- **ddw** — <https://www.ddw-online.com/media/32/(2)-improving-productivity-with-better-predictivity.pdf>
- **wikipedia** — <https://en.wikipedia.org/wiki/Mene_Pangalos>

> The 5R rubric (right target, tissue, safety, patient, commercial potential) plus a measured before/after: 4% of candidates completing Phase III in 2005-2010 vs 19% in 2012-2016. A rare case of a published decision framework with its own outcome audit. Two papers: NRD 2014 and NRD 2018.

#### Aled M. Edwards  `verified`

Open-science target discovery; argues publicly about incentives and duplication

- **profile** — <https://moleculargenetics.utoronto.ca/faculty/aled-edwards>
- **royal_society** — <https://royalsociety.org/people/aled-edwards-36787/>
- **interview_elife** — <https://elifesciences.org/interviews/89c121b4/the-structural-genomics-consortium>
- **conversation** — <https://link.springer.com/article/10.1038/scibx.2014.604>
- **talk_1** — <https://www.youtube.com/watch?v=Nt_0w7CNcyI>
- **talk_2** — <https://www.youtube.com/watch?v=1_dN3dQ3GsI>
- **interview_fe** — <https://thefutureeconomy.ca/interviews/aled-edwards/>

> Founded SGC in 2004; with Richard Gold wrote the 2007 SGC Open Science Principles - the first biomedical research org to mandate sharing and eschew patenting, including on novel chemistry. The eLife open-notebook interview (with Rachel Harding and Matthieu Schapira) is the clearest statement of the position.

#### Chas Bountra  `verified`

Open target validation and pre-competitive collaboration

- **profile** — <https://www.ndm.ox.ac.uk/team/chas-bountra>
- **innovation** — <https://innovation.ox.ac.uk/about/people/chas-bountra/>
- **podcasts** — <https://podcasts.ox.ac.uk/people/chas-bountra>
- **expert** — <https://www.ox.ac.uk/news-and-events/find-an-expert/professor-chas-bountra>
- **repro_lecture** — <http://neuroanatody.com/2017/12/oxford-reproducibility-lectures-chas-bountra/>
- **podcast_bf** — <https://www.hitgenpod.com/1929512/episodes/10316473-chas-bountra-innovation-at-oxford>
- **martin** — <https://www.oxfordmartin.ox.ac.uk/people/professor-chas-bountra>

> KEY: University of Oxford Podcasts hosts a dedicated speaker page - a whole archive of his recorded talks in one place. 80+ papers, 10 patents, 100+ invited lectures. Ran SGC-Oxford 2008-2020 pooling 9 pharma companies, 5 patient groups and academic labs, all data free. 19 years in industry before Oxford.

#### Paul Workman  `verified`

HSP90 and other programs; prolific writer on how to run drug discovery well

- **blog** — <https://www.icr.ac.uk/research-and-discoveries/cancer-blogs/lab-research-blogs/the-drug-discoverer-blog>
- **blog_post_probes** — <https://www.icr.ac.uk/research-and-discoveries/cancer-blogs/detail/the-drug-discoverer/more-on-chemical-probes-from-indiana-jones-to-open-science>
- **blog_post_probes2** — <https://www.icr.ac.uk/blogs/the-drug-discoverer/page-details/call-to-bioscientists-choose-and-use-your-chemicai-probes-very-carefully>
- **probes_portal** — <https://www.chemicalprobes.org/people/paul-workman>
- **paper** — <https://www.cell.com/trends/cancer/fulltext/S2405-8033(16)30137-6>
- **profile** — <https://oncodaily.com/insight/156731>

> CONFIRMED: he runs a blog, 'The Drug Discoverer', at the ICR. That plus the Chemical Probes Portal ('fitness factors for small molecule tools') makes him the closest thing to a Derek Lowe inside an academic drug discovery unit. Crawl the whole blog.
