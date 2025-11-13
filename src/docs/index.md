# Outcomes Data Model

A LinkML data model for representing biological measurements, assays, and experimental protocols.

## Overview

This schema provides a structured framework for capturing biological measurement data with rich 
contextual information to support reproducibility and cross-study comparison. The model is designed 
to represent various types of measurements relevant to respiratory AOPs (adverse outcome pathways).

## Core Architecture

### Base Classes

#### NamedEntity
The base class for all entities in the model, providing:
- `id`: Unique identifier (required)
- `description`: Detailed description

#### Measurement
The central class representing a biological measurement process, extending `NamedEntity` with:
- `input_sample`: The biological sample or experimental setup (InputSample)
- `method_assay`: The assay or method used (Assay)
- `protocol_notes`: Protocol or SOP notes

#### InputSample
Describes the biological sample or experimental manipulation:
- `sample_type`: Type of biological sample (e.g., "Primary human airway epithelial cells at ALI")
- `manipulation`: Experimental manipulation applied
- `exposure_conditions`: Exposure or treatment conditions

#### Assay
The specific method used to measure an endpoint:
- `assay_type`: Type of assay (constrained to OBI ontology terms via AssayTypeEnum)
- `instrumentation`: Specific instruments or equipment used
- `environmental_conditions`: Environmental parameters during measurement (EnvironmentalCondition)
- `sop_reference`: Reference to standard operating procedure

#### QuantityValue
A reusable pattern for expressing measurements with units (based on NMDC Schema):
- `has_numeric_value`: The numeric value
- `has_unit`: The unit of measurement (e.g., "Hz", "�m", "mm/min", "%")
- `has_minimum_numeric_value`: Minimum value in a range
- `has_maximum_numeric_value`: Maximum value in a range

## Specialized Measurement Classes

All specialized measurement classes extend the base `Measurement` class:

### CFTRFunctionMeasurement
Measurement of CFTR-mediated ion transport function
- CFTR-specific current measurements
- Inhibitor-sensitive current data
- Cell culture details

### BALFSputumMeasurement
Measurement of bronchoalveolar lavage fluid or sputum components
- Sample collection details
- Inflammatory cell profiles
- Microbiome analysis
- Cytokine levels
- Protein concentration
- Cell-free DNA

### LungFunctionMeasurement
Measurement of lung function parameters
- FEV1, FVC, FEV1/FVC ratio
- FEF25-75
- Bronchodilator response
- Decline rate
- DLCO, FeNO

### EGFRSignalingMeasurement
Measurement of EGFR pathway activation and signaling
- EGFR phosphorylation levels
- Downstream kinase activation
- Ligand expression levels
- Pathway biomarkers

### TranscriptionFactorExpressionMeasurement
Measurement of transcription factor expression (generalized for any transcription factor)
- mRNA expression level
- Protein expression level
- Percentage of positive cells
- Staining protocol details
- Gene expression analysis methodology

### CiliaBeatFrequencyMeasurement
Measurement of ciliary beat frequency
- Beat frequency in Hz
- Active area percentage
- Imaging protocol
- Cilia per cell, cilia length
- Percentage ciliated cells
- Ciliary motion patterns
- Cell type ratios

### ASLHeightMeasurement
Measurement of airway surface liquid height
- ASL height in micrometers
- Periciliary layer depth
- Imaging protocol
- Ion composition
- Fluorescent labeling
- Evaporation prevention methods

### MucociliaryClearanceMeasurement
Measurement of mucociliary clearance/transport
- Transport rate
- Directionality
- Particle tracking methods
- Fluorescent tracers
- Mucus layer thickness
- Bacterial biofilm and viral infection details
- Biofilm clearance rate, bacterial load, viral spread rate

### GobletCellMeasurement
Measurement of goblet cell number or mucin production
- Goblet cell count
- Mucin expression level
- Staining protocol
- Gene expression analysis
- Mucin protein concentration
- Goblet-to-ciliated cell ratio
- Pathway enrichment scores
- Dose-response data

### OxidativeStressMeasurement
Measurement of oxidative stress markers
- ROS level
- Lipid peroxidation markers
- Antioxidant capacity
- ROS probe details
- Detection method details
- Protein oxidation markers
- DNA damage markers
- Antioxidant enzyme activities
- Barrier integrity
- Cytotoxicity metrics

## Supporting Classes

### EnvironmentalCondition
Environmental parameters during measurement:
- Temperature
- Humidity
- CO� percentage

### ImagingProtocol
Details about imaging parameters and protocols:
- Imaging modality (confocal, OCT, etc.)
- Frame rate
- Imaging duration and intervals
- Spatial resolution
- Probe positioning

### CellCultureConditions
Detailed cell culture parameters:
- Culture medium formulation
- Days at air-liquid interface (ALI)
- Passage number
- Substrate type
- Temperature, humidity, CO� percentage
- Donor count and replicates per donor

### StainingProtocol
Histological or immunofluorescence staining protocol:
- Staining type
- Antibodies used
- Fixation method
- Incubation conditions

### GeneExpressionAnalysis
Gene expression measurement methodology:
- Analysis method (qRT-PCR, RNA-seq)
- Normalization genes
- Primers used
- Sequencing platform and depth

### Publication
Scientific publication information (following Biolink model):
- Authors
- Pages
- Summary/abstract
- Keywords
- MeSH terms
- Publication type
- Cross-references (xref)

### Additional Supporting Classes

- **FluorescentLabel**: Fluorescent labeling or tracer details
- **EvaporationControl**: Methods to prevent evaporation
- **ROSProbe**: Reactive oxygen species probe details
- **DetectionMethod**: Method for detecting/measuring analytes
- **SampleCollection**: Biological sample collection details
- **InflammatoryCellProfile**: Profile of inflammatory cell types
- **MicrobiomeAnalysis**: Microbiome composition analysis
- **BarrierIntegrity**: Epithelial barrier integrity measurements
- **CytotoxicityMetrics**: Cell viability and cytotoxicity measurements

## Ontology Integration

The schema integrates with standard ontologies:
- **OBI** (Ontology for Biomedical Investigations): Assay types
- **CHEBI**: Chemical entities
- **ENVO**: Environmental ontology terms
- **Biolink**: Publication and entity modeling patterns

### AssayTypeEnum
Assay types are constrained to OBI terms via dynamic enumeration:
- Source ontology: `obo:obi`
- Root node: `OBI:0000070` (assay)
- Relationship: `rdfs:subClassOf`

## Design Principles

1. **Modularity**: Specialized measurement classes inherit from a common base
2. **Reusability**: Common patterns like QuantityValue are used throughout
3. **Rich Context**: Environmental conditions, protocols, and methodological details are captured
4. **Ontology-Driven**: Use of standard ontologies for interoperability
5. **Flexibility**: Support for various measurement types while maintaining consistency

## License

MIT

## More Information

- Schema repository: https://EHS-Data-Standards.github.io/outcomes-working-group
- Schema ID: https://w3id.org/EHS-Data-Standards/outcomes-model
