# Ontology Mappings for Outcomes Schema

## Slot Definition Terms

These ontology terms define what the slots themselves represent.

### assay_type slot definition

- **assay** (`OBI:0000070`) - OBI
  - A planned process that has the objective to produce information about a material entity (the evaluant) by examining it.
- **comet assay** (`OBI:0302736`) - OBI
  - An assay that measures DNA damage (DNA breakage) in eucaryotic cells exposed to a challenge by determining the size and shape of DNA migration by detecting fluorescently labeled DNA from a cell placed
- **pyrosequencing assay** (`OBI:0000730`) - OBI
  - A DNA sequencing by synthesis assay which sequences a single strand of DNA by synthesizing the complementary strand along it, one base pair at a time, and detecting which base was actually added at ea

### measurement value slot definition

- **measurement datum** (`IAO:0000109`) - IAO
  - A measurement datum is an information content entity that is a recording of the output of a measurement such as produced by a device.
- **measurement datum** (`IAO:0000109`) - OBI
  - A measurement datum is an information content entity that is a recording of the output of a measurement such as produced by a device.
- **scalar measurement datum** (`IAO:0000032`) - IAO
  - A scalar measurement datum is a measurement datum that is composed of two parts, numerals and a unit label.

### protocol_notes slot definition

- **protocol** (`OBI:0000272`) - OBI
  - A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to i
- **sequencing protocol** (`OBI:0003069`) - OBI
  - A protocol that, when concretized, is realized in an assay that uses chemical or biological means to infer the sequence of a biomaterial.
- **rodent care protocol** (`OBI:0000688`) - OBI
  - A rodent care protocol is an animal protocol in which the animals being taken care of are rodents.

### input_sample slot definition

- **material entity** (`BFO:0000040`) - BFO
- **material entity** (`BFO:0000040`) - OBI
  - An independent continuant that is spatially extended whose identity is independent of that of other entities and can be maintained through time.
- **dissolved material entity** (`OBI:0302876`) - OBI
  - A material entity that has been going through a process of being put into solution

### instrumentation slot definition

- **PCR instrument** (`OBI:0000989`) - OBI
  - A device that is used to amplify a single or few copies of a piece of DNA across several orders of magnitude, generating thousands to millions of copies of a particular DNA sequence.
- **radiography instrument** (`OBI:0001085`) - OBI
  - An image acquisition device that uses ionizing electromagnetic radiation such as X-rays to view objects.
- **microdissection instrument** (`OBI:0001123`) - OBI
  - A device that is used for the dissection of tissues under magnification.

### generic data slot definition

- **data item** (`IAO:0000027`) - IAO
  - An information content entity that is intended to be a truthful statement about something (modulo, e.g., measurement precision or other systematic errors) and is constructed/acquired by a method which
- **data item extraction from journal article** (`IAO:0000443`) - IAO
  - A planned process in which journal articles are read or processed and data items are extracted, typically for further analysis or indexing
- **data set** (`IAO:0000100`) - IAO
  - A data item that is an aggregate of other data items of the same type that have something in common. Averages and distributions can be determined for data sets.

### sample_type slot definition

- **specimen** (`OBI:0100051`) - OBI
  - A material entity that is collected for potential use as an input upon which measurements or observations are performed.
- **urine specimen** (`OBI:0000651`) - OBI
  - a portion of urine collected from an organism
- **blood specimen** (`OBI:0000655`) - OBI
  - a material entity derived from a portion of blood collected from an organism

### biological sample slot

- **Exalpha Biological** (`OBI:0001287`) - OBI
- **material sample** (`OBI:0000747`) - OBI
  - A material entity that has the material sample role
- **sample inlet** (`OBI:0000497`) - OBI
  - The column inlet (or injector) provides the means to introduce a sample into a continuous flow of carrier gas. The inlet is a piece of hardware attached to the column head.

### method slot definition

- **planned process** (`OBI:0000011`) - OBI
  - A process that realizes a plan which is the concretization of a plan specification.
- **planned irradiation** (`OBI:0302889`) - OBI
  - A planned process by which a material entity is exposed to radiative energy, which could be ionizing radiation (such as gamma rays, X-rays, charged particles or neutrons) or non-ionizing radiation (su
- **unblinding process** (`OBI:0000840`) - OBI
  - A planned process that is the part of the study execution in which the subjects are told what study arm they are in and in which the investigators are told which subjects are in which trials.

### method_assay slot definition

- **assay** (`OBI:0000070`) - OBI
  - A planned process that has the objective to produce information about a material entity (the evaluant) by examining it.
- **comet assay** (`OBI:0302736`) - OBI
  - An assay that measures DNA damage (DNA breakage) in eucaryotic cells exposed to a challenge by determining the size and shape of DNA migration by detecting fluorescently labeled DNA from a cell placed
- **pyrosequencing assay** (`OBI:0000730`) - OBI
  - A DNA sequencing by synthesis assay which sequences a single strand of DNA by synthesizing the complementary strand along it, one base pair at a time, and detecting which base was actually added at ea

### documentation slot definition

- **document** (`IAO:0000310`) - IAO
  - A collection of information content entities intended to be understood together as a whole
- **document title** (`IAO:0000305`) - IAO
  - A textual entity that names a document
- **document part** (`IAO:0000314`) - IAO
  - An information content entity that is part of a document.

### sop_reference slot definition

- **standard error** (`OBI:0000235`) - OBI
  - A quantitative confidence value which is the standard deviations of the sample in a frequency distribution, obtained by dividing the standard deviation by the total number of cases in the frequency di
- **standard deviation calculation** (`OBI:0200121`) - OBI
  - A standard deviation calculation is a descriptive statistics calculation defined as the square root of the variance.  Also thought of as the average distance of each value to the mean.
- **standard compliance rule** (`OBI:0500024`) - OBI
  - a  standard compliance rule is a compliance rule which defines conformity to a representation standard

## Value Constraint Terms

These ontology terms can be used to constrain the values allowed in slots.

### imaging_modality

**imaging_modality value**:

- lightsheet fluorescence microscopy assay (`OBI:0003098`) - OBI
- fluorescence microscopy assay (`CHMO:0000087`) - OBI
- confocal fluorescence microscopy assay (`CHMO:0000089`) - OBI

### sample_type

**sample_type value**:

- respiratory system (`UBERON:0001004`) - UBERON
- respiratory system mucus (`UBERON:0016553`) - UBERON
- respiratory system gland (`UBERON:0036225`) - UBERON

### staining_type

**staining_type value**:

- histological assay (`OBI:0600020`) - OBI
- staining (`OBI:0302887`) - OBI
- histological sample preparation (`OBI:0000341`) - OBI

### fixation_method

**fixation_method value**:

- paraformaldehyde polymer (`CHEBI:61538`) - CHEBI
- paraformaldehyde macromolecule (`CHEBI:31962`) - CHEBI

### analysis_method

**analysis_method value**:

- PCR instrument (`OBI:0000989`) - OBI
- PCR program (`OBI:0001961`) - OBI
- PCR product (`OBI:0000406`) - OBI

### condition

**culture condition**:

- cell culture (`OBI:0001876`) - OBI
- cell culture expansion (`OBI:0001147`) - OBI
- primary cell culture (`OBI:0001910`) - OBI

### culture_medium

**culture_medium value**:

- culture medium (`OBI:0000079`) - OBI
- enrichment culture medium (`OBI:0002673`) - OBI
- Dulbecco's modified Eagle medium (`OBI:0000918`) - OBI

### unit

**distance unit**:

- micrometer (`UO:0000017`) - UO
- micrometer (`UO:0000017`) - UO
- square micrometer (`UO:0010001`) - UO

**frequency unit**:

- hertz (`UO:0000106`) - UO
- hertz (`UO:0000106`) - UO
- hertz based unit (`UO:1000106`) - UO

**ratio unit**:

- mass percentage (`UO:0000163`) - UO
- volume percentage (`UO:0000165`) - UO
- purity percentage (`UO:0000193`) - UO

### parameter

**environmental parameter**:

- humidity (`PATO:0015009`) - PATO
- humidity (`PATO:0015009`) - ENVO
- increased humidity (`PATO:0015010`) - PATO

### process

**biological process**:

- mucus secretion (`GO:0070254`) - GO
- regulation of mucus secretion (`GO:0070255`) - GO
- negative regulation of mucus secretion (`GO:0070256`) - GO

