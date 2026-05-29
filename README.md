<p align="center">
  <img src="src/docs/soma-logo.svg" alt="SOMA Logo" width="700">
</p>

<p align="center">
  A <a href="https://linkml.io/">LinkML</a> schema for representing Key Event and Outcome measurements, assays, and experimental protocols in the context of environmental health sciences (EHS) outcomes research.
</p>

<p align="center">
  <a href="https://EHS-Data-Standards.github.io/soma"><strong>Documentation</strong></a> &middot;
  <a href="https://EHS-Data-Standards.github.io/soma/elements/"><strong>Schema</strong></a> &middot;
  <a href="https://EHS-Data-Standards.github.io/soma/examples.html"><strong>Examples</strong></a> &middot;
  <a href="https://EHS-Data-Standards.github.io/soma/artifacts.html"><strong>Artifacts</strong></a>
</p>

---

## Purpose

This data model provides a standardized way to capture and exchange data about airway biology
assays relevant to respiratory health outcomes, including:

- **Ciliary function** - Beat frequency, active area, morphology
- **Airway surface liquid** - ASL height, periciliary layer depth, ion composition
- **Mucociliary clearance** - Transport rates, directionality, clearance efficiency
- **Oxidative stress** - ROS, lipid peroxidation, antioxidant capacity
- **Ion channel function** - CFTR chloride secretion, sweat chloride
- **Signaling pathways** - EGFR phosphorylation, downstream kinases
- **Mucin biology** - Goblet cells, MUC5AC/MUC5B expression
- **Inflammatory markers** - BALF/sputum cell counts, cytokines
- **Lung function** - Spirometry outcomes (FEV1, FVC)
- **Gene expression** - Target gene mRNA levels

## Key Features

- **Assay-centric architecture** with domain-specific assay classes using named measurement slots
- **StudySubject hierarchy** for describing biological systems: cell cultures, human/animal subjects, populations
- **Typed protocol hierarchy**: ImagingProtocol, MolecularAssayProtocol, StainingProtocol, SpirometryProtocol
- **AOP Framework integration**: KeyEvent and AdverseOutcomePathway classes with assay linkage
- **Ontology-backed** entities mapped to GO, ChEBI, CL, UO, OBI, and other biomedical ontologies

## Getting Started

The schema can be used to:

1. **Validate data** - Ensure your data conforms to the model
2. **Generate code** - Create Python dataclasses, Pydantic models, JSON Schema
3. **Transform data** - Convert between JSON, YAML, RDF, and other formats

## Development Workflow

For local development, use `uv` and `just` as the canonical entry points.
The repository may contain underlying Python, npm, and LinkML commands, but contributors
should treat the `just` recipes as the supported interface for routine setup, testing,
and generation tasks.

### Prerequisites

- `uv` for Python environment and dependency management
- `just` for repository task automation
- `node` and `npm` for DataHarmonizer frontend builds

### Setup

Install the Python dependencies managed by the repo:

```bash
just install
```

### Common Commands

- Run the full validation workflow: `just test`
- Regenerate project artifacts: `just gen-project`
- Regenerate schema documentation: `just gen-doc`
- Build the DataHarmonizer assets: `just build-dh`
- List all available recipes: `just --list`

If you need to run a Python tool directly, prefer `uv run ...` so it executes inside the
managed project environment.

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (auto-generated, do not edit)
* [src/soma/schema/](src/soma/schema) - LinkML schema (edit this)
* [src/soma/datamodel/](src/soma/datamodel) - generated Python datamodel
* [tests/](tests/) - Python tests

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
