# About

## The SOMA

The SOMA is part of the [EHS Data Standards](https://github.com/EHS-Data-Standards)
initiative, focused on developing standardized data models for environmental health sciences research.

## Project Goals

This project aims to:

1. **Standardize data representation** for exposure-outcome relationships in EHS research
2. **Enable data interoperability** across studies, cohorts, and institutions
3. **Support mechanistic understanding** through integration with Adverse Outcome Pathways (AOPs)
4. **Bridge epidemiological and toxicological data** from human studies and model systems

## The Data Model

### Design Principles

The SOMA follows these principles:

- **Ontology-first** - All entities are mapped to established biomedical ontologies
- **FAIR-compliant** - Supports Findable, Accessible, Interoperable, and Reusable data
- **Extensible** - New assay types can be added without breaking existing data
- **Multi-scale** - Captures data from molecular to population levels

### Technology Stack

The model is built using:

- [LinkML](https://linkml.io/) - Linked Data Modeling Language for schema definition
- [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/)
  for documentation
- Python for data validation and transformation

### Core Domains

| Domain | Description |
|--------|-------------|
| Assays | Domain-specific assay classes with named measurement slots (e.g., CiliaryFunctionAssay, LungFunctionAssay) |
| Study Subjects | Biological systems under study: cell cultures (CellularSystem), human/animal subjects (InVivoSubject), populations (PopulationSubject) |
| Protocols | Typed experimental procedures: ImagingProtocol, MolecularAssayProtocol, StainingProtocol, SpirometryProtocol |
| AOP Framework | Adverse Outcome Pathways: KeyEvent, AdverseOutcomePathway, with assay linkage via `informs_on_key_event` |

## Contributing

We welcome contributions from the community. To contribute:

1. Visit the [GitHub repository](https://github.com/EHS-Data-Standards/soma)
2. Review the existing schema in `src/soma/schema/`
3. Open an issue to discuss proposed changes
4. Submit a pull request with your contributions

## Development

For local development, use [uv](https://docs.astral.sh/uv/) and
[just](https://github.com/casey/just/) as the canonical entry points.
The repository may contain underlying Python, npm, and LinkML commands, but
contributors should treat the `just` recipes as the supported interface for
routine setup, testing, and generation tasks.

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for Python environment and dependency management
- [just](https://github.com/casey/just/) for repository task automation
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
- Run the local documentation server: `just testdoc`
- List all available recipes: `just --list`

If you need to run a Python tool directly, prefer `uv run ...` so it executes
inside the managed project environment.

### Project Structure

```
soma/
├── src/
│   ├── docs/                    # Documentation source files
│   └── soma/
│       ├── schema/              # LinkML schema definition
│       └── datamodel/           # Generated Python models
├── docs/
│   └── elements/                # Generated schema docs
├── project/                     # Generated artifacts
├── tests/
│   └── data/                    # Test data files
└── examples/                    # Usage examples
```

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

This project uses the [linkml-project-copier](https://github.com/dalito/linkml-project-copier)
template for project structure and build tooling.

## Contact

For questions or feedback, please open an issue on the
[GitHub repository](https://github.com/EHS-Data-Standards/soma/issues).
