---
name: pdf-to-yaml
description: Extract structured data from a publication PDF into a SOMA-compliant Container YAML file
user_invocable: true
---

# /pdf-to-yaml - Publication to SOMA YAML

Use this skill to extract structured assay/measurement data from a publication PDF and produce a SOMA-compliant 
Container YAML file.

## Pipeline Overview

```
PDF --[Read tool]--> Extract data --> Map to SOMA schema --> Assign ontology terms --> Generate YAML --> Validate
```

## Phase 1: Read the PDF

Use the Read tool to read the PDF in 20-page chunks. Extract:
- Study design (in vitro / in vivo models)
- Assay types performed
- Measurements and quantitative results
- Protocols and methods
- Exposure conditions (agent, concentration, duration)
- Statistical results (p-values, sample sizes, fold changes)
- Species, cell types, anatomical sites

## Phase 2: Map to SOMA Schema

Reference these schema files to structure the data:
- **Main schema**: `src/soma/schema/soma.yaml` - Container class with collection slots
- **Assay base**: `src/soma/schema/assay_base.yaml` - Assay, StudySubject, Protocol
- **Microschemas**: `src/soma/schema/assay_microschemas.yaml` - Domain-specific assay + output classes

### Available Assay Types

| Assay Class | Output Class | Use For |
|-------------|-------------|---------|
| CiliaryFunctionAssay | CiliaryFunctionOutput | CBF, active area, cilia length |
| ASLAssay | ASLOutput | Airway surface liquid height/volume |
| MucociliaryClearanceAssay | MCCOutput | Mucociliary transport rate |
| OxidativeStressAssay | OxidativeStressOutput | ROS, GSH, 8-OHdG |
| CFTRFunctionAssay | CFTRFunctionOutput | Isc, chloride secretion |
| EGFRSignalingAssay | EGFRSignalingOutput | EGFR phosphorylation, activation |
| GobletCellAssay | GobletCellOutput | Goblet cell %, MUC5AC/MUC5B |
| BALFSputumAssay | BALFSputumOutput | BALF cytokines, cell counts |
| LungFunctionAssay | LungFunctionOutput | FEV1, sRaw, resistance |
| FoxJExpressionAssay | FoxJExpressionOutput | FOXJ1 mRNA/protein |
| GeneExpressionAssay | GeneExpressionOutput | Generic gene/protein expression |

## Phase 3: Assign Ontology Terms

Use `/oaklib` to find and verify CURIEs for:
- **Chemicals/agents**: CHEBI (e.g., CHEBI:74481 for PM2.5)
- **Cell types**: CL (e.g., CL:0002603 for nasal epithelial cell)
- **Species**: NCBITaxon (e.g., NCBITaxon:9606 for Homo sapiens)
- **Units**: UO (e.g., UO:0000032 for hour)
- **Anatomy**: UBERON (e.g., UBERON:0001707 for nasal cavity)
- **Proteins/genes**: PR, NCBIGene (e.g., PR:000003411 for CFTR protein, NCBIGene:1080 for CFTR genes)
- **Cell lines**: CLO (e.g., CLO:0003679 for Calu-3)

## Phase 4: Generate YAML

### File Naming Convention

```
Container-<firstauthor><year>-<agent>-<focus>.yaml
```

Examples:
- `Container-liu2024-pm25-cftr.yaml`
- `Container-montgomery2020-pm25-mucociliary.yaml`

### Output Location

Write to current working directory.

### YAML Structure

Follow the structure of the existing schema in YAML format.  Examples:
- `tests/data/valid/Container-liu2024-pm25-cftr.yaml`
- `tests/data/valid/Container-montgomery2020-pm25-mucociliary.yaml`

Key structural patterns:
- `protocols:` section with all protocols listed
- Each assay type as a top-level collection (e.g., `cftr_assays:`, `gene_expression_assays:`)
- Each assay has inline `has_specified_output:` with the measurement data
- Each assay has inline `study_subject:` with cell type / species info
- Each assay has inline `has_exposure_condition:` with agent/concentration/duration
- Each assay has inline `informs_on_key_event:` linking to the AOP
- Each assay has `follows_protocols:` referencing the protocols section

### ID Conventions

- Protocols: `PROTOCOL:<author>-<method>-<number>` (e.g., `PROTOCOL:liu-ussing-001`)
- Exposures: `EXPOSURE:<author>-<agent>-<detail>` (e.g., `EXPOSURE:liu-pm25-100ug-24h`)
- Key Events: `KE:<type>-<description>` (e.g., `KE:ke-decreased-cftr`)
- Assays: `<PREFIX>:<author>-<target>-<condition>` (e.g., `CFTR:liu-pm25-24h`)
- Outputs: `<assay-id>-output` (e.g., `CFTR:liu-pm25-24h-output`)
- Subjects: `soma:<author>-<type>-<number>` or `SUBJECT:<author>-<type>` for in vivo

## Critical Constraints

1. **ALL numeric values MUST come from the paper** - never hallucinate measurements
2. **Figure-derived values**: do not derive any specific measurements - never hallucinate measurements
3. **Missing data**: omit the slot entirely, do not guess values
4. **Include p-values and sample sizes** in description fields when available, but structure the data using more specific slots when available.
5. **Quote all numeric values** as strings in YAML (e.g., `value: "0.55"`)
6. **For every ontology id you suggest, validate that the string-value from the paper matches the label of the ontology term, or one of its synonyms using linkml-term-validator"

## Phase 5: Validate

After generating the YAML, run validation:

```bash
uv run linkml-validate -s src/soma/schema/soma.yaml tests/data/valid/<new-file>.yaml
uv run python -m pytest tests/test_data.py -v -k "<new-file-stem>"
```
