# Ontology Mappings for Outcomes Schema

This directory contains ontology term mappings that can be used to:
1. **Define what slots represent** (slot definitions)
2. **Constrain the values** allowed in slots (value constraints)

## Files

- **ontology_mappings.csv** - All mappings in CSV format
- **ontology_mappings.md** - Human-readable markdown format
- **ontology_mappings.json** - Raw JSON data for programmatic use

## How to Use These Mappings

### 1. Slot Definitions (slot_uri)

These ontology terms define what a slot *is*. Add them to the schema using `slot_uri`:

```yaml
slots:
  assay_type:
    description: Type of assay or method, constrained to OBI assay terms
    slot_uri: OBI:0000070  # assay
    range: AssayTypeEnum
    
  protocol_notes:
    description: Protocol or SOP notes
    slot_uri: OBI:0000272  # protocol
    range: string
    
  input_sample:
    description: Description of input samples and manipulations
    slot_uri: OBI:0100051  # specimen
    range: InputSample
```

### 2. Value Constraints (Enumerations)

These ontology terms can be used to create enumerations that constrain slot values:

#### Example: Imaging Modality Enumeration

```yaml
enums:
  ImagingModalityEnum:
    description: Types of imaging modalities from OBI
    reachable_from:
      source_ontology: obo:obi
      source_nodes:
        - OBI:0003098  # lightsheet fluorescence microscopy assay
        - OBI:0000087  # fluorescence microscopy assay
        - OBI:0000089  # confocal fluorescence microscopy assay
      relationship_types:
        - rdfs:subClassOf

slots:
  imaging_modality:
    description: Imaging modality used
    range: ImagingModalityEnum
```

#### Example: Staining Type Enumeration

```yaml
enums:
  StainingTypeEnum:
    description: Types of staining assays from OBI
    reachable_from:
      source_ontology: obo:obi
      source_nodes:
        - OBI:0600020  # histological assay
        - OBI:0302887  # staining
      relationship_types:
        - rdfs:subClassOf

slots:
  staining_type:
    description: Type of staining
    range: StainingTypeEnum
```

### 3. Unit Constraints

Use Units of Ontology (UO) terms for measurement units:

```yaml
slots:
  has_unit:
    description: The unit of measurement for the quantity
    range: string
    pattern: "^UO:[0-9]{7}$"  # UO IDs
    examples:
      - value: "UO:0000017"  # micrometer
        description: "For distance measurements"
      - value: "UO:0000106"  # hertz
        description: "For frequency measurements"
```

## Key Ontology Terms by Slot Type

### Core Measurement Slots

| Slot | Slot URI | Description |
|------|----------|-------------|
| assay_type | OBI:0000070 | assay |
| method_assay | OBI:0000070 | assay |
| input_sample | OBI:0100051 | specimen |
| protocol_notes | OBI:0000272 | protocol |
| instrumentation | (various OBI instrument terms) | |

### Sample-Related Slots

| Slot | Recommended Values | Ontology |
|------|-------------------|----------|
| sample_type | Epithelial cells, tissue types | CL, UBERON |
| - epithelial cell | CL:0000066 | CL |
| - airway epithelial cell | CL:0002632 | CL |
| - ciliated cell | CL:0000064 | CL |
| - goblet cell | CL:0000160 | CL |

### Method-Related Slots

| Slot | Recommended Values | Ontology |
|------|-------------------|----------|
| imaging_modality | Microscopy types | OBI |
| - confocal fluorescence microscopy | OBI:0000089 | OBI |
| - fluorescence microscopy | OBI:0000087 | OBI |
| - lightsheet fluorescence microscopy | OBI:0003098 | OBI |
| staining_type | Staining assays | OBI |
| - histological assay | OBI:0600020 | OBI |
| - staining | OBI:0302887 | OBI |
| analysis_method | Analysis assays | OBI |
| - (various PCR and sequencing terms) | OBI | OBI |

### Culture-Related Slots

| Slot | Recommended Values | Ontology |
|------|-------------------|----------|
| culture_medium | Media types | OBI |
| - culture medium | OBI:0000079 | OBI |
| - Dulbecco's modified Eagle medium | OBI:0000918 | OBI |

### Environmental Slots

| Slot | Recommended Values | Ontology |
|------|-------------------|----------|
| temperature | Temperature quality | PATO |
| humidity | PATO:0015009 | PATO |

### Units

| Measurement Type | Unit Term | OBO ID |
|-----------------|-----------|---------|
| Distance/Height | micrometer | UO:0000017 |
| Frequency | hertz | UO:0000106 |
| Percentage | mass/volume percentage | UO:0000163, UO:0000165 |

## Ontologies Used

- **OBI** - Ontology for Biomedical Investigations
- **IAO** - Information Artifact Ontology
- **CL** - Cell Ontology
- **UBERON** - Uber Anatomy Ontology
- **UO** - Units of Ontology
- **PATO** - Phenotype and Trait Ontology
- **CHEBI** - Chemical Entities of Biological Interest
- **GO** - Gene Ontology
- **ENVO** - Environment Ontology
- **BFO** - Basic Formal Ontology

## Next Steps

1. **Add slot_uri annotations** to existing slots in the schema
2. **Create enumerations** for commonly-used value sets (imaging modalities, staining types, etc.)
3. **Use reachable_from** to dynamically pull ontology terms rather than hardcoding values
4. **Add examples** to slot definitions showing proper ontology term usage
5. **Document units** using UO terms in the has_unit slot

## References

- OLS API: https://www.ebi.ac.uk/ols4/
- LinkML Ontology Integration: https://linkml.io/linkml/schemas/enums.html#dynamic-enums
