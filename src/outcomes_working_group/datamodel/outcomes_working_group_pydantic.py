from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'outcomes_model',
     'default_range': 'string',
     'description': 'A LinkML data model for representing biological measurements, '
                    'assays, and experimental protocols\n'
                    'in the context of outcomes research.\n',
     'id': 'https://w3id.org/EHS-Data-Standards/outcomes-model',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'outcomes-model',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'IAO': {'prefix_prefix': 'IAO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'outcomes_model': {'prefix_prefix': 'outcomes_model',
                                     'prefix_reference': 'https://w3id.org/EHS-Data-Standards/outcomes-model/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://EHS-Data-Standards.github.io/outcomes-working-group'],
     'source_file': 'src/outcomes_working_group/schema/outcomes_working_group.yaml',
     'title': 'Outcomes Data Model'} )

class AssayTypeEnum(str, Enum):
    """
    Types of assays from the Ontology for Biomedical Investigations (OBI)
    """
    OBICOLON0000070 = "OBI:0000070"
    """
    assay
    """



class NamedEntity(ConfiguredBaseModel):
    """
    Base class for all named entities in the model
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class Measurement(NamedEntity):
    """
    A generic class representing the process of measuring a biological endpoint.
    Includes information about input samples, methods, and contextual metadata.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class InputSample(NamedEntity):
    """
    Description of the biological sample or experimental manipulation used as input
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    sample_type: Optional[str] = Field(default=None, description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0100051'],
         'domain_of': ['InputSample'],
         'examples': [{'value': 'Primary human airway epithelial cells at ALI'},
                      {'value': 'MucilAir 3D tissue model'}]} })
    manipulation: Optional[str] = Field(default=None, description="""Experimental manipulation applied""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000011'], 'domain_of': ['InputSample']} })
    exposure_conditions: Optional[str] = Field(default=None, description="""Exposure or treatment conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSample'],
         'related_mappings': ['ENVO:01000254', 'PATO:0001018']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class Assay(NamedEntity):
    """
    The specific method or assay used to measure an endpoint
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    assay_type: Optional[AssayTypeEnum] = Field(default=None, description="""Type of assay or method, constrained to OBI assay terms""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000070']} })
    instrumentation: Optional[str] = Field(default=None, description="""Specific instruments or equipment used""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000968'], 'domain_of': ['Assay', 'DetectionMethod']} })
    environmental_conditions: Optional[dict[str, EnvironmentalCondition]] = Field(default=None, description="""Environmental conditions during measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'related_mappings': ['ENVO:01000254', 'PATO:0001018']} })
    sop_reference: Optional[str] = Field(default=None, description="""Reference to standard operating procedure""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Assay'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class QuantityValue(ConfiguredBaseModel):
    """
    A quantity value expresses a measurement with a numeric value and a unit. Based on NMDC Schema QuantityValue pattern.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    has_numeric_value: Optional[float] = Field(default=None, description="""The numeric value of a quantity""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'], 'domain_of': ['QuantityValue']} })
    has_unit: Optional[str] = Field(default=None, description="""The unit of measurement for the quantity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'],
         'exact_mappings': ['UO:0000000'],
         'examples': [{'value': 'Hz'},
                      {'value': 'µm'},
                      {'value': 'mm/min'},
                      {'value': '%'}]} })
    has_minimum_numeric_value: Optional[float] = Field(default=None, description="""The minimum value in a range""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'], 'domain_of': ['QuantityValue']} })
    has_maximum_numeric_value: Optional[float] = Field(default=None, description="""The maximum value in a range""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'], 'domain_of': ['QuantityValue']} })


class CFTRFunctionMeasurement(Measurement):
    """
    Measurement of CFTR-mediated ion transport function
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    cftr_specific_current: Optional[QuantityValue] = Field(default=None, description="""CFTR-mediated chloride secretory current""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionMeasurement']} })
    inhibitor_sensitive_current: Optional[QuantityValue] = Field(default=None, description="""Inhibitor-sensitive current measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionMeasurement']} })
    cell_culture_details: Optional[CellCultureConditions] = Field(default=None, description="""Detailed cell culture conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class BALFSputumMeasurement(Measurement):
    """
    Measurement of bronchoalveolar lavage fluid or sputum components
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    sample_collection_details: Optional[SampleCollection] = Field(default=None, description="""Sample collection protocol details""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumMeasurement']} })
    inflammatory_cell_profile: Optional[InflammatoryCellProfile] = Field(default=None, description="""Inflammatory cell type profile""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumMeasurement']} })
    microbiome_analysis: Optional[MicrobiomeAnalysis] = Field(default=None, description="""Microbiome composition analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumMeasurement']} })
    cytokine_levels: Optional[list[str]] = Field(default=[], description="""Cytokine and chemokine levels""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000033'],
         'domain_of': ['BALFSputumMeasurement'],
         'related_mappings': ['CHEBI:23530']} })
    protein_concentration: Optional[QuantityValue] = Field(default=None, description="""Total protein concentration""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000033'],
         'domain_of': ['BALFSputumMeasurement'],
         'related_mappings': ['CHEBI:36080']} })
    cell_free_dna: Optional[QuantityValue] = Field(default=None, description="""Cell-free DNA measurement""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000033'],
         'domain_of': ['BALFSputumMeasurement'],
         'related_mappings': ['CHEBI:16991']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class LungFunctionMeasurement(Measurement):
    """
    Measurement of lung function parameters
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    fev1: Optional[QuantityValue] = Field(default=None, description="""Forced expiratory volume in 1 second""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000918'], 'domain_of': ['LungFunctionMeasurement']} })
    fvc: Optional[QuantityValue] = Field(default=None, description="""Forced vital capacity""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000918'], 'domain_of': ['LungFunctionMeasurement']} })
    fev1_fvc_ratio: Optional[QuantityValue] = Field(default=None, description="""Ratio of FEV1 to FVC""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001470'], 'domain_of': ['LungFunctionMeasurement']} })
    fef25_75: Optional[QuantityValue] = Field(default=None, description="""Forced expiratory flow 25-75%""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionMeasurement']} })
    bronchodilator_response: Optional[QuantityValue] = Field(default=None, description="""Response to bronchodilator""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionMeasurement']} })
    decline_rate: Optional[QuantityValue] = Field(default=None, description="""Longitudinal decline rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionMeasurement']} })
    dlco: Optional[QuantityValue] = Field(default=None, description="""Diffusing capacity of the lung for carbon monoxide""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionMeasurement']} })
    feno: Optional[QuantityValue] = Field(default=None, description="""Fractional exhaled nitric oxide""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class EGFRSignalingMeasurement(Measurement):
    """
    Measurement of EGFR pathway activation and signaling
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    egfr_phosphorylation: Optional[QuantityValue] = Field(default=None, description="""EGFR phosphorylation levels""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingMeasurement']} })
    downstream_kinase_activation: Optional[str] = Field(default=None, description="""Activation levels of downstream kinases (ERK, AKT)""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingMeasurement']} })
    ligand_expression_levels: Optional[list[str]] = Field(default=[], description="""Expression levels of EGFR ligands""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingMeasurement']} })
    pathway_biomarkers: Optional[list[str]] = Field(default=[], description="""Pathway-specific biomarker signatures""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class TranscriptionFactorExpressionMeasurement(Measurement):
    """
    Measurement of transcription factor expression
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    mrna_level: Optional[QuantityValue] = Field(default=None, description="""mRNA expression level""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['TranscriptionFactorExpressionMeasurement'],
         'related_mappings': ['CHEBI:33699']} })
    protein_level: Optional[QuantityValue] = Field(default=None, description="""Protein expression level""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['TranscriptionFactorExpressionMeasurement'],
         'related_mappings': ['CHEBI:36080']} })
    percentage_positive_cells: Optional[QuantityValue] = Field(default=None, description="""Percentage of positive cells""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001555'],
         'domain_of': ['TranscriptionFactorExpressionMeasurement']} })
    staining_protocol: Optional[StainingProtocol] = Field(default=None, description="""Staining protocol details""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorExpressionMeasurement',
                       'GobletCellMeasurement'],
         'exact_mappings': ['OBI:0000272']} })
    gene_expression_analysis: Optional[GeneExpressionAnalysis] = Field(default=None, description="""Gene expression analysis methodology""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000070'],
         'domain_of': ['TranscriptionFactorExpressionMeasurement',
                       'GobletCellMeasurement'],
         'related_mappings': ['OBI:0000424']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class CiliaBeatFrequencyMeasurement(Measurement):
    """
    Measurement of ciliary beat frequency
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    beat_frequency_hz: Optional[QuantityValue] = Field(default=None, description="""Ciliary beat frequency in Hz""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000044'],
         'domain_of': ['CiliaBeatFrequencyMeasurement'],
         'related_mappings': ['GO:0003341']} })
    active_area_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of active ciliated area""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001555'],
         'domain_of': ['CiliaBeatFrequencyMeasurement']} })
    imaging_protocol: Optional[ImagingProtocol] = Field(default=None, description="""Imaging protocol and parameters""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaBeatFrequencyMeasurement', 'ASLHeightMeasurement'],
         'exact_mappings': ['OBI:0000272']} })
    cilia_per_cell: Optional[QuantityValue] = Field(default=None, description="""Number of cilia per cell""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['CiliaBeatFrequencyMeasurement'],
         'related_mappings': ['CL:0000064']} })
    cilia_length: Optional[QuantityValue] = Field(default=None, description="""Length of cilia""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000122'],
         'domain_of': ['CiliaBeatFrequencyMeasurement']} })
    percentage_ciliated_cells: Optional[QuantityValue] = Field(default=None, description="""Percentage of cells that are ciliated""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001555'],
         'domain_of': ['CiliaBeatFrequencyMeasurement'],
         'related_mappings': ['CL:0000064']} })
    ciliary_motion_patterns: Optional[str] = Field(default=None, description="""Patterns of ciliary motion""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000001'],
         'domain_of': ['CiliaBeatFrequencyMeasurement'],
         'related_mappings': ['GO:0003341']} })
    cell_type_ratios: Optional[str] = Field(default=None, description="""Ratios between different cell types""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaBeatFrequencyMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class ASLHeightMeasurement(Measurement):
    """
    Measurement of airway surface liquid height
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    asl_height_um: Optional[QuantityValue] = Field(default=None, description="""Airway surface liquid height in micrometers""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000119'], 'domain_of': ['ASLHeightMeasurement']} })
    periciliary_layer_depth: Optional[QuantityValue] = Field(default=None, description="""Depth of periciliary layer in micrometers""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001595'], 'domain_of': ['ASLHeightMeasurement']} })
    imaging_protocol: Optional[ImagingProtocol] = Field(default=None, description="""Imaging protocol and parameters""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaBeatFrequencyMeasurement', 'ASLHeightMeasurement'],
         'exact_mappings': ['OBI:0000272']} })
    ion_composition: Optional[str] = Field(default=None, description="""Ionic composition (Cl⁻, Na⁺, K⁺)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLHeightMeasurement']} })
    fluorescent_labeling: Optional[FluorescentLabel] = Field(default=None, description="""Fluorescent label or tracer used""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLHeightMeasurement'], 'related_mappings': ['CHEBI:51217']} })
    evaporation_prevention: Optional[EvaporationControl] = Field(default=None, description="""Method used to prevent evaporation""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLHeightMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class MucociliaryClearanceMeasurement(Measurement):
    """
    Measurement of mucociliary clearance/transport
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    transport_rate: Optional[QuantityValue] = Field(default=None, description="""Mucociliary transport rate""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000161'],
         'domain_of': ['MucociliaryClearanceMeasurement'],
         'related_mappings': ['GO:0120197']} })
    directionality: Optional[str] = Field(default=None, description="""Directionality of mucociliary transport""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001527'],
         'domain_of': ['MucociliaryClearanceMeasurement']} })
    particle_tracking_method: Optional[str] = Field(default=None, description="""Method used for tracking particles or mucus""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceMeasurement']} })
    fluorescent_tracers: Optional[dict[str, FluorescentLabel]] = Field(default=None, description="""Fluorescent tracers used for tracking""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceMeasurement']} })
    mucus_layer_thickness: Optional[QuantityValue] = Field(default=None, description="""Thickness of mucus layer""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000915'],
         'domain_of': ['MucociliaryClearanceMeasurement']} })
    bacterial_biofilm_details: Optional[str] = Field(default=None, description="""Details about bacterial biofilm preparation and characteristics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceMeasurement']} })
    viral_infection_details: Optional[str] = Field(default=None, description="""Details about viral infection protocol""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceMeasurement']} })
    biofilm_clearance_rate: Optional[QuantityValue] = Field(default=None, description="""Rate of bacterial biofilm clearance""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000161'],
         'domain_of': ['MucociliaryClearanceMeasurement']} })
    bacterial_load: Optional[QuantityValue] = Field(default=None, description="""Bacterial load (CFU or similar)""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['MucociliaryClearanceMeasurement']} })
    viral_spread_rate: Optional[QuantityValue] = Field(default=None, description="""Rate of viral spread""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000161'],
         'domain_of': ['MucociliaryClearanceMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class GobletCellMeasurement(Measurement):
    """
    Measurement of goblet cell number or mucin production
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    goblet_cell_count: Optional[QuantityValue] = Field(default=None, description="""Number or percentage of goblet cells""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['GobletCellMeasurement'],
         'related_mappings': ['CL:0000160']} })
    mucin_expression_level: Optional[QuantityValue] = Field(default=None, description="""Level of mucin gene or protein expression""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['GobletCellMeasurement'],
         'related_mappings': ['GO:0070254']} })
    staining_protocol: Optional[StainingProtocol] = Field(default=None, description="""Staining protocol details""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorExpressionMeasurement',
                       'GobletCellMeasurement'],
         'exact_mappings': ['OBI:0000272']} })
    gene_expression_analysis: Optional[GeneExpressionAnalysis] = Field(default=None, description="""Gene expression analysis methodology""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000070'],
         'domain_of': ['TranscriptionFactorExpressionMeasurement',
                       'GobletCellMeasurement'],
         'related_mappings': ['OBI:0000424']} })
    mucin_protein_concentration: Optional[QuantityValue] = Field(default=None, description="""Concentration of mucin protein""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000033'],
         'domain_of': ['GobletCellMeasurement'],
         'related_mappings': ['CHEBI:36080']} })
    goblet_to_ciliated_ratio: Optional[QuantityValue] = Field(default=None, description="""Ratio of goblet cells to ciliated cells""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001470'],
         'domain_of': ['GobletCellMeasurement'],
         'related_mappings': ['CL:0000160', 'CL:0000064']} })
    pathway_enrichment_scores: Optional[list[str]] = Field(default=[], description="""Enrichment scores for biological pathways""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellMeasurement']} })
    dose_response_data: Optional[str] = Field(default=None, description="""Dose-response relationship data""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class OxidativeStressMeasurement(Measurement):
    """
    Measurement of oxidative stress markers
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    ros_level: Optional[QuantityValue] = Field(default=None, description="""Reactive oxygen species level""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['OxidativeStressMeasurement'],
         'related_mappings': ['CHEBI:26523']} })
    lipid_peroxidation: Optional[QuantityValue] = Field(default=None, description="""Lipid peroxidation markers (MDA, 8-isoprostane, etc.)""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000001'],
         'domain_of': ['OxidativeStressMeasurement'],
         'related_mappings': ['GO:0016491']} })
    antioxidant_capacity: Optional[QuantityValue] = Field(default=None, description="""Antioxidant capacity (GSH/GSSG ratio, enzyme activity)""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000001'],
         'domain_of': ['OxidativeStressMeasurement']} })
    ros_probe: Optional[ROSProbe] = Field(default=None, description="""ROS probe details""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    detection_method_details: Optional[dict[str, DetectionMethod]] = Field(default=None, description="""Detection method details""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000070'], 'domain_of': ['OxidativeStressMeasurement']} })
    protein_oxidation_markers: Optional[list[str]] = Field(default=[], description="""Protein oxidation markers (carbonyls, nitrotyrosine)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    dna_damage_markers: Optional[QuantityValue] = Field(default=None, description="""DNA damage markers (8-OHdG)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    antioxidant_enzyme_activities: Optional[str] = Field(default=None, description="""Antioxidant enzyme activities (SOD, catalase, GPx)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    barrier_integrity: Optional[BarrierIntegrity] = Field(default=None, description="""Epithelial barrier integrity measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    cytotoxicity_metrics: Optional[CytotoxicityMetrics] = Field(default=None, description="""Cytotoxicity measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'],
         'exact_mappings': ['OBI:0100051'],
         'related_mappings': ['OBI:0000747']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'exact_mappings': ['OBI:0000070']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000272'],
         'domain_of': ['Measurement'],
         'related_mappings': ['IAO:0000310']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class Publication(NamedEntity):
    """
    Any published piece of information, following Biolink model.
    Represents scientific evidence supporting research.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model',
         'slot_usage': {'id': {'description': 'Preferentially a PMID, DOI, or '
                                              'industry-standard identifier (ISBN, '
                                              'ISSN)',
                               'examples': [{'value': 'PMID:12345678'},
                                            {'value': 'DOI:10.1234/example'}],
                               'name': 'id'}}})

    authors: Optional[list[str]] = Field(default=[], description="""Connects publications to contributor lists, formatted as comma-delimited names""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    pages: Optional[str] = Field(default=None, description="""Page numbers (start and end) or total pages""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    summary: Optional[str] = Field(default=None, description="""Executive summary or abstract of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    keywords: Optional[list[str]] = Field(default=[], description="""Keywords or tags for the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    mesh_terms: Optional[list[str]] = Field(default=[], description="""Medical Subject Headings (MeSH) terms for indexing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    publication_type: Optional[str] = Field(default=None, description="""Ontology term for categorizing publication format (e.g., journal article, book chapter, review)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    xref: Optional[list[str]] = Field(default=[], description="""Cross-references to supporting databases or webpages""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    id: str = Field(default=..., description="""Preferentially a PMID, DOI, or industry-standard identifier (ISBN, ISSN)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'PMID:12345678'}, {'value': 'DOI:10.1234/example'}]} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class ImagingProtocol(NamedEntity):
    """
    Details about imaging parameters and protocols
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    imaging_modality: Optional[str] = Field(default=None, description="""Imaging modality used (confocal, OCT, etc.)""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000185'], 'domain_of': ['ImagingProtocol']} })
    frame_rate: Optional[QuantityValue] = Field(default=None, description="""Image acquisition frame rate""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'],
         'domain_of': ['ImagingProtocol'],
         'related_mappings': ['PATO:0000161']} })
    imaging_duration: Optional[QuantityValue] = Field(default=None, description="""Duration of imaging session""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'],
         'domain_of': ['ImagingProtocol'],
         'related_mappings': ['PATO:0001309']} })
    imaging_intervals: Optional[str] = Field(default=None, description="""Time intervals between image acquisitions""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    spatial_resolution: Optional[QuantityValue] = Field(default=None, description="""Spatial resolution of imaging""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'],
         'domain_of': ['ImagingProtocol'],
         'related_mappings': ['PATO:0001018']} })
    probe_positioning: Optional[str] = Field(default=None, description="""Probe or sensor positioning protocol""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class FluorescentLabel(NamedEntity):
    """
    Fluorescent labeling or tracer used in measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    fluorophore_type: Optional[str] = Field(default=None, description="""Type of fluorophore used""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['CHEBI:51217'], 'domain_of': ['FluorescentLabel']} })
    concentration: Optional[QuantityValue] = Field(default=None, description="""Concentration of reagent or compound""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescentLabel']} })
    wavelength: Optional[QuantityValue] = Field(default=None, description="""Wavelength for excitation or emission""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescentLabel']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class EvaporationControl(NamedEntity):
    """
    Method used to prevent evaporation during measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    control_method: Optional[str] = Field(default=None, description="""Method used for control""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaporationControl']} })
    material_used: Optional[str] = Field(default=None, description="""Material used in protocol""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaporationControl']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class ROSProbe(NamedEntity):
    """
    Reactive oxygen species probe and detection details
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    probe_type: Optional[str] = Field(default=None, description="""Type of probe used""", json_schema_extra = { "linkml_meta": {'domain_of': ['ROSProbe']} })
    loading_conditions: Optional[str] = Field(default=None, description="""Conditions for loading probe or dye""", json_schema_extra = { "linkml_meta": {'domain_of': ['ROSProbe']} })
    detection_wavelength: Optional[QuantityValue] = Field(default=None, description="""Wavelength for detection""", json_schema_extra = { "linkml_meta": {'domain_of': ['ROSProbe']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class DetectionMethod(NamedEntity):
    """
    Method used for detecting or measuring analytes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    detection_type: Optional[str] = Field(default=None, description="""Type of detection method""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000070'], 'domain_of': ['DetectionMethod']} })
    instrumentation: Optional[str] = Field(default=None, description="""Specific instruments or equipment used""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000968'], 'domain_of': ['Assay', 'DetectionMethod']} })
    sensitivity: Optional[str] = Field(default=None, description="""Sensitivity of detection method""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod']} })
    technical_replicates: Optional[int] = Field(default=None, description="""Number of technical replicates""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class SampleCollection(NamedEntity):
    """
    Details about biological sample collection
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    collection_method: Optional[str] = Field(default=None, description="""Method for sample collection""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000011'], 'domain_of': ['SampleCollection']} })
    processing_time: Optional[QuantityValue] = Field(default=None, description="""Time from collection to processing""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000165'], 'domain_of': ['SampleCollection']} })
    storage_conditions: Optional[str] = Field(default=None, description="""Storage temperature and conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleCollection'],
         'related_mappings': ['PATO:0000146', 'PATO:0015009']} })
    sample_volume: Optional[QuantityValue] = Field(default=None, description="""Volume of sample collected""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleCollection']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class CellCultureConditions(NamedEntity):
    """
    Detailed cell culture parameters
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    culture_medium: Optional[str] = Field(default=None, description="""Cell culture medium formulation""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions'], 'exact_mappings': ['OBI:0000079']} })
    days_at_ali: Optional[int] = Field(default=None, description="""Days at air-liquid interface""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'],
         'domain_of': ['CellCultureConditions'],
         'related_mappings': ['PATO:0000165']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'], 'domain_of': ['CellCultureConditions']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions']} })
    temperature: Optional[QuantityValue] = Field(default=None, description="""Temperature setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'EnvironmentalCondition'],
         'exact_mappings': ['PATO:0000146']} })
    humidity: Optional[QuantityValue] = Field(default=None, description="""Humidity level""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'EnvironmentalCondition'],
         'exact_mappings': ['PATO:0015009']} })
    co2_percentage: Optional[QuantityValue] = Field(default=None, description="""CO2 percentage in incubator""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000033'],
         'domain_of': ['CellCultureConditions', 'EnvironmentalCondition'],
         'related_mappings': ['CHEBI:16526']} })
    donor_count: Optional[int] = Field(default=None, description="""Number of unique donors""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['IAO:0000109'],
         'domain_of': ['CellCultureConditions'],
         'related_mappings': ['PATO:0000070']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicates per donor""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class StainingProtocol(NamedEntity):
    """
    Histological or immunofluorescence staining protocol
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    staining_type: Optional[str] = Field(default=None, description="""Type of staining (histological, immunofluorescence)""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0302887'], 'domain_of': ['StainingProtocol']} })
    antibodies_used: Optional[list[str]] = Field(default=[], description="""Antibodies used in staining""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol']} })
    fixation_method: Optional[str] = Field(default=None, description="""Method for tissue/cell fixation""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000011'],
         'domain_of': ['StainingProtocol'],
         'related_mappings': ['OBI:0302887']} })
    incubation_conditions: Optional[str] = Field(default=None, description="""Incubation time and temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class GeneExpressionAnalysis(NamedEntity):
    """
    Gene expression measurement methodology
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    analysis_method: Optional[str] = Field(default=None, description="""Method for analysis (qRT-PCR, RNA-seq)""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['OBI:0000070'], 'domain_of': ['GeneExpressionAnalysis']} })
    normalization_genes: Optional[list[str]] = Field(default=[], description="""Genes used for normalization""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAnalysis']} })
    primers_used: Optional[list[str]] = Field(default=[], description="""PCR primers used""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAnalysis']} })
    sequencing_platform: Optional[str] = Field(default=None, description="""Platform used for sequencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAnalysis']} })
    sequencing_depth: Optional[int] = Field(default=None, description="""Sequencing depth or read count""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAnalysis']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class InflammatoryCellProfile(NamedEntity):
    """
    Profile of inflammatory cell types and counts
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    neutrophil_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of neutrophils""", json_schema_extra = { "linkml_meta": {'domain_of': ['InflammatoryCellProfile']} })
    eosinophil_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of eosinophils""", json_schema_extra = { "linkml_meta": {'domain_of': ['InflammatoryCellProfile']} })
    macrophage_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of macrophages""", json_schema_extra = { "linkml_meta": {'domain_of': ['InflammatoryCellProfile']} })
    lymphocyte_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of lymphocytes""", json_schema_extra = { "linkml_meta": {'domain_of': ['InflammatoryCellProfile']} })
    total_cell_count: Optional[QuantityValue] = Field(default=None, description="""Total cell count""", json_schema_extra = { "linkml_meta": {'domain_of': ['InflammatoryCellProfile']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class MicrobiomeAnalysis(NamedEntity):
    """
    Microbiome composition analysis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    alpha_diversity: Optional[QuantityValue] = Field(default=None, description="""Alpha diversity metric""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicrobiomeAnalysis']} })
    beta_diversity: Optional[str] = Field(default=None, description="""Beta diversity metric""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicrobiomeAnalysis']} })
    taxonomic_abundance: Optional[list[str]] = Field(default=[], description="""Taxonomic abundance data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicrobiomeAnalysis']} })
    sequencing_primers: Optional[list[str]] = Field(default=[], description="""Primers used for sequencing (16S, ITS)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicrobiomeAnalysis']} })
    dna_extraction_method: Optional[str] = Field(default=None, description="""Method for DNA extraction""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicrobiomeAnalysis']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class BarrierIntegrity(NamedEntity):
    """
    Epithelial barrier integrity measurements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    teer_value: Optional[QuantityValue] = Field(default=None, description="""Transepithelial electrical resistance value""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001025'], 'domain_of': ['BarrierIntegrity']} })
    permeability_coefficient: Optional[QuantityValue] = Field(default=None, description="""Permeability coefficient""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000001'], 'domain_of': ['BarrierIntegrity']} })
    measurement_timepoint: Optional[str] = Field(default=None, description="""Timepoint of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['BarrierIntegrity']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class CytotoxicityMetrics(NamedEntity):
    """
    Cell viability and cytotoxicity measurements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    ldh_release: Optional[QuantityValue] = Field(default=None, description="""Lactate dehydrogenase release""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000070'],
         'domain_of': ['CytotoxicityMetrics'],
         'related_mappings': ['CHEBI:17660']} })
    mtt_reduction: Optional[QuantityValue] = Field(default=None, description="""MTT reduction assay result""", json_schema_extra = { "linkml_meta": {'domain_of': ['CytotoxicityMetrics']} })
    viability_percentage: Optional[QuantityValue] = Field(default=None, description="""Cell viability percentage""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0001421'], 'domain_of': ['CytotoxicityMetrics']} })
    apoptosis_markers: Optional[list[str]] = Field(default=[], description="""Apoptosis marker levels""", json_schema_extra = { "linkml_meta": {'domain_of': ['CytotoxicityMetrics']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class EnvironmentalCondition(NamedEntity):
    """
    Environmental parameters during measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes-model'})

    temperature: Optional[QuantityValue] = Field(default=None, description="""Temperature setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'EnvironmentalCondition'],
         'exact_mappings': ['PATO:0000146']} })
    humidity: Optional[QuantityValue] = Field(default=None, description="""Humidity level""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'EnvironmentalCondition'],
         'exact_mappings': ['PATO:0015009']} })
    co2_percentage: Optional[QuantityValue] = Field(default=None, description="""CO2 percentage in incubator""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['PATO:0000033'],
         'domain_of': ['CellCultureConditions', 'EnvironmentalCondition'],
         'related_mappings': ['CHEBI:16526']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
Measurement.model_rebuild()
InputSample.model_rebuild()
Assay.model_rebuild()
QuantityValue.model_rebuild()
CFTRFunctionMeasurement.model_rebuild()
BALFSputumMeasurement.model_rebuild()
LungFunctionMeasurement.model_rebuild()
EGFRSignalingMeasurement.model_rebuild()
TranscriptionFactorExpressionMeasurement.model_rebuild()
CiliaBeatFrequencyMeasurement.model_rebuild()
ASLHeightMeasurement.model_rebuild()
MucociliaryClearanceMeasurement.model_rebuild()
GobletCellMeasurement.model_rebuild()
OxidativeStressMeasurement.model_rebuild()
Publication.model_rebuild()
ImagingProtocol.model_rebuild()
FluorescentLabel.model_rebuild()
EvaporationControl.model_rebuild()
ROSProbe.model_rebuild()
DetectionMethod.model_rebuild()
SampleCollection.model_rebuild()
CellCultureConditions.model_rebuild()
StainingProtocol.model_rebuild()
GeneExpressionAnalysis.model_rebuild()
InflammatoryCellProfile.model_rebuild()
MicrobiomeAnalysis.model_rebuild()
BarrierIntegrity.model_rebuild()
CytotoxicityMetrics.model_rebuild()
EnvironmentalCondition.model_rebuild()
