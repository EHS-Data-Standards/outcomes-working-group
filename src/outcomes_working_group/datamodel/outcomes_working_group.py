# Auto generated from outcomes_working_group.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-12T16:19:55
# Schema: outcomes-model
#
# id: https://w3id.org/EHS-Data-Standards/outcomes-model
# description: A LinkML data model for representing biological measurements, assays, and experimental protocols
#   in the context of outcomes research.
#
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OUTCOMES_MODEL = CurieNamespace('outcomes_model', 'https://w3id.org/EHS-Data-Standards/outcomes-model/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OUTCOMES_MODEL


# Types

# Class references
class NamedEntityId(URIorCURIE):
    pass


class MeasurementId(NamedEntityId):
    pass


class InputSampleId(NamedEntityId):
    pass


class AssayId(NamedEntityId):
    pass


class CFTRFunctionMeasurementId(MeasurementId):
    pass


class BALFSputumMeasurementId(MeasurementId):
    pass


class LungFunctionMeasurementId(MeasurementId):
    pass


class EGFRSignalingMeasurementId(MeasurementId):
    pass


class TranscriptionFactorExpressionMeasurementId(MeasurementId):
    pass


class CiliaBeatFrequencyMeasurementId(MeasurementId):
    pass


class ASLHeightMeasurementId(MeasurementId):
    pass


class MucociliaryClearanceMeasurementId(MeasurementId):
    pass


class GobletCellMeasurementId(MeasurementId):
    pass


class OxidativeStressMeasurementId(MeasurementId):
    pass


class PublicationId(NamedEntityId):
    pass


class ImagingProtocolId(NamedEntityId):
    pass


class FluorescentLabelId(NamedEntityId):
    pass


class EvaporationControlId(NamedEntityId):
    pass


class ROSProbeId(NamedEntityId):
    pass


class DetectionMethodId(NamedEntityId):
    pass


class SampleCollectionId(NamedEntityId):
    pass


class CellCultureConditionsId(NamedEntityId):
    pass


class StainingProtocolId(NamedEntityId):
    pass


class GeneExpressionAnalysisId(NamedEntityId):
    pass


class InflammatoryCellProfileId(NamedEntityId):
    pass


class MicrobiomeAnalysisId(NamedEntityId):
    pass


class BarrierIntegrityId(NamedEntityId):
    pass


class CytotoxicityMetricsId(NamedEntityId):
    pass


class EnvironmentalConditionId(NamedEntityId):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Base class for all named entities in the model
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["NamedEntity"]
    class_class_curie: ClassVar[str] = "outcomes_model:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.NamedEntity

    id: Union[str, NamedEntityId] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(NamedEntity):
    """
    A generic class representing the process of measuring a biological endpoint.
    Includes information about input samples, methods, and contextual metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["Measurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.Measurement

    id: Union[str, MeasurementId] = None
    input_sample: Optional[Union[str, InputSampleId]] = None
    method_assay: Optional[Union[str, AssayId]] = None
    protocol_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementId):
            self.id = MeasurementId(self.id)

        if self.input_sample is not None and not isinstance(self.input_sample, InputSampleId):
            self.input_sample = InputSampleId(self.input_sample)

        if self.method_assay is not None and not isinstance(self.method_assay, AssayId):
            self.method_assay = AssayId(self.method_assay)

        if self.protocol_notes is not None and not isinstance(self.protocol_notes, str):
            self.protocol_notes = str(self.protocol_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InputSample(NamedEntity):
    """
    Description of the biological sample or experimental manipulation used as input
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["InputSample"]
    class_class_curie: ClassVar[str] = "outcomes_model:InputSample"
    class_name: ClassVar[str] = "InputSample"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.InputSample

    id: Union[str, InputSampleId] = None
    sample_type: Optional[str] = None
    manipulation: Optional[str] = None
    exposure_conditions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InputSampleId):
            self.id = InputSampleId(self.id)

        if self.sample_type is not None and not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.manipulation is not None and not isinstance(self.manipulation, str):
            self.manipulation = str(self.manipulation)

        if self.exposure_conditions is not None and not isinstance(self.exposure_conditions, str):
            self.exposure_conditions = str(self.exposure_conditions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(NamedEntity):
    """
    The specific method or assay used to measure an endpoint
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["Assay"]
    class_class_curie: ClassVar[str] = "outcomes_model:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.Assay

    id: Union[str, AssayId] = None
    assay_type: Optional[Union[str, "AssayTypeEnum"]] = None
    instrumentation: Optional[str] = None
    environmental_conditions: Optional[Union[dict[Union[str, EnvironmentalConditionId], Union[dict, "EnvironmentalCondition"]], list[Union[dict, "EnvironmentalCondition"]]]] = empty_dict()
    sop_reference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayId):
            self.id = AssayId(self.id)

        if self.assay_type is not None and not isinstance(self.assay_type, AssayTypeEnum):
            self.assay_type = AssayTypeEnum(self.assay_type)

        if self.instrumentation is not None and not isinstance(self.instrumentation, str):
            self.instrumentation = str(self.instrumentation)

        self._normalize_inlined_as_dict(slot_name="environmental_conditions", slot_type=EnvironmentalCondition, key_name="id", keyed=True)

        if self.sop_reference is not None and not isinstance(self.sop_reference, str):
            self.sop_reference = str(self.sop_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    A quantity value expresses a measurement with a numeric value and a unit.
    Based on NMDC Schema QuantityValue pattern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["QuantityValue"]
    class_class_curie: ClassVar[str] = "outcomes_model:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.QuantityValue

    has_numeric_value: Optional[float] = None
    has_unit: Optional[str] = None
    has_minimum_numeric_value: Optional[float] = None
    has_maximum_numeric_value: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_minimum_numeric_value is not None and not isinstance(self.has_minimum_numeric_value, float):
            self.has_minimum_numeric_value = float(self.has_minimum_numeric_value)

        if self.has_maximum_numeric_value is not None and not isinstance(self.has_maximum_numeric_value, float):
            self.has_maximum_numeric_value = float(self.has_maximum_numeric_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CFTRFunctionMeasurement(Measurement):
    """
    Measurement of CFTR-mediated ion transport function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["CFTRFunctionMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:CFTRFunctionMeasurement"
    class_name: ClassVar[str] = "CFTRFunctionMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.CFTRFunctionMeasurement

    id: Union[str, CFTRFunctionMeasurementId] = None
    cftr_specific_current: Optional[Union[dict, QuantityValue]] = None
    inhibitor_sensitive_current: Optional[Union[dict, QuantityValue]] = None
    cell_culture_details: Optional[Union[dict, "CellCultureConditions"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CFTRFunctionMeasurementId):
            self.id = CFTRFunctionMeasurementId(self.id)

        if self.cftr_specific_current is not None and not isinstance(self.cftr_specific_current, QuantityValue):
            self.cftr_specific_current = QuantityValue(**as_dict(self.cftr_specific_current))

        if self.inhibitor_sensitive_current is not None and not isinstance(self.inhibitor_sensitive_current, QuantityValue):
            self.inhibitor_sensitive_current = QuantityValue(**as_dict(self.inhibitor_sensitive_current))

        if self.cell_culture_details is not None and not isinstance(self.cell_culture_details, CellCultureConditions):
            self.cell_culture_details = CellCultureConditions(**as_dict(self.cell_culture_details))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BALFSputumMeasurement(Measurement):
    """
    Measurement of bronchoalveolar lavage fluid or sputum components
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["BALFSputumMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:BALFSputumMeasurement"
    class_name: ClassVar[str] = "BALFSputumMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.BALFSputumMeasurement

    id: Union[str, BALFSputumMeasurementId] = None
    sample_collection_details: Optional[Union[dict, "SampleCollection"]] = None
    inflammatory_cell_profile: Optional[Union[dict, "InflammatoryCellProfile"]] = None
    microbiome_analysis: Optional[Union[dict, "MicrobiomeAnalysis"]] = None
    cytokine_levels: Optional[Union[str, list[str]]] = empty_list()
    protein_concentration: Optional[Union[dict, QuantityValue]] = None
    cell_free_dna: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BALFSputumMeasurementId):
            self.id = BALFSputumMeasurementId(self.id)

        if self.sample_collection_details is not None and not isinstance(self.sample_collection_details, SampleCollection):
            self.sample_collection_details = SampleCollection(**as_dict(self.sample_collection_details))

        if self.inflammatory_cell_profile is not None and not isinstance(self.inflammatory_cell_profile, InflammatoryCellProfile):
            self.inflammatory_cell_profile = InflammatoryCellProfile(**as_dict(self.inflammatory_cell_profile))

        if self.microbiome_analysis is not None and not isinstance(self.microbiome_analysis, MicrobiomeAnalysis):
            self.microbiome_analysis = MicrobiomeAnalysis(**as_dict(self.microbiome_analysis))

        if not isinstance(self.cytokine_levels, list):
            self.cytokine_levels = [self.cytokine_levels] if self.cytokine_levels is not None else []
        self.cytokine_levels = [v if isinstance(v, str) else str(v) for v in self.cytokine_levels]

        if self.protein_concentration is not None and not isinstance(self.protein_concentration, QuantityValue):
            self.protein_concentration = QuantityValue(**as_dict(self.protein_concentration))

        if self.cell_free_dna is not None and not isinstance(self.cell_free_dna, QuantityValue):
            self.cell_free_dna = QuantityValue(**as_dict(self.cell_free_dna))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LungFunctionMeasurement(Measurement):
    """
    Measurement of lung function parameters
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["LungFunctionMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:LungFunctionMeasurement"
    class_name: ClassVar[str] = "LungFunctionMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.LungFunctionMeasurement

    id: Union[str, LungFunctionMeasurementId] = None
    fev1: Optional[Union[dict, QuantityValue]] = None
    fvc: Optional[Union[dict, QuantityValue]] = None
    fev1_fvc_ratio: Optional[Union[dict, QuantityValue]] = None
    fef25_75: Optional[Union[dict, QuantityValue]] = None
    bronchodilator_response: Optional[Union[dict, QuantityValue]] = None
    decline_rate: Optional[Union[dict, QuantityValue]] = None
    dlco: Optional[Union[dict, QuantityValue]] = None
    feno: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LungFunctionMeasurementId):
            self.id = LungFunctionMeasurementId(self.id)

        if self.fev1 is not None and not isinstance(self.fev1, QuantityValue):
            self.fev1 = QuantityValue(**as_dict(self.fev1))

        if self.fvc is not None and not isinstance(self.fvc, QuantityValue):
            self.fvc = QuantityValue(**as_dict(self.fvc))

        if self.fev1_fvc_ratio is not None and not isinstance(self.fev1_fvc_ratio, QuantityValue):
            self.fev1_fvc_ratio = QuantityValue(**as_dict(self.fev1_fvc_ratio))

        if self.fef25_75 is not None and not isinstance(self.fef25_75, QuantityValue):
            self.fef25_75 = QuantityValue(**as_dict(self.fef25_75))

        if self.bronchodilator_response is not None and not isinstance(self.bronchodilator_response, QuantityValue):
            self.bronchodilator_response = QuantityValue(**as_dict(self.bronchodilator_response))

        if self.decline_rate is not None and not isinstance(self.decline_rate, QuantityValue):
            self.decline_rate = QuantityValue(**as_dict(self.decline_rate))

        if self.dlco is not None and not isinstance(self.dlco, QuantityValue):
            self.dlco = QuantityValue(**as_dict(self.dlco))

        if self.feno is not None and not isinstance(self.feno, QuantityValue):
            self.feno = QuantityValue(**as_dict(self.feno))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EGFRSignalingMeasurement(Measurement):
    """
    Measurement of EGFR pathway activation and signaling
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["EGFRSignalingMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:EGFRSignalingMeasurement"
    class_name: ClassVar[str] = "EGFRSignalingMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.EGFRSignalingMeasurement

    id: Union[str, EGFRSignalingMeasurementId] = None
    egfr_phosphorylation: Optional[Union[dict, QuantityValue]] = None
    downstream_kinase_activation: Optional[str] = None
    ligand_expression_levels: Optional[Union[str, list[str]]] = empty_list()
    pathway_biomarkers: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EGFRSignalingMeasurementId):
            self.id = EGFRSignalingMeasurementId(self.id)

        if self.egfr_phosphorylation is not None and not isinstance(self.egfr_phosphorylation, QuantityValue):
            self.egfr_phosphorylation = QuantityValue(**as_dict(self.egfr_phosphorylation))

        if self.downstream_kinase_activation is not None and not isinstance(self.downstream_kinase_activation, str):
            self.downstream_kinase_activation = str(self.downstream_kinase_activation)

        if not isinstance(self.ligand_expression_levels, list):
            self.ligand_expression_levels = [self.ligand_expression_levels] if self.ligand_expression_levels is not None else []
        self.ligand_expression_levels = [v if isinstance(v, str) else str(v) for v in self.ligand_expression_levels]

        if not isinstance(self.pathway_biomarkers, list):
            self.pathway_biomarkers = [self.pathway_biomarkers] if self.pathway_biomarkers is not None else []
        self.pathway_biomarkers = [v if isinstance(v, str) else str(v) for v in self.pathway_biomarkers]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TranscriptionFactorExpressionMeasurement(Measurement):
    """
    Measurement of transcription factor expression
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["TranscriptionFactorExpressionMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:TranscriptionFactorExpressionMeasurement"
    class_name: ClassVar[str] = "TranscriptionFactorExpressionMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.TranscriptionFactorExpressionMeasurement

    id: Union[str, TranscriptionFactorExpressionMeasurementId] = None
    mrna_level: Optional[Union[dict, QuantityValue]] = None
    protein_level: Optional[Union[dict, QuantityValue]] = None
    percentage_positive_cells: Optional[Union[dict, QuantityValue]] = None
    staining_protocol: Optional[Union[dict, "StainingProtocol"]] = None
    gene_expression_analysis: Optional[Union[dict, "GeneExpressionAnalysis"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TranscriptionFactorExpressionMeasurementId):
            self.id = TranscriptionFactorExpressionMeasurementId(self.id)

        if self.mrna_level is not None and not isinstance(self.mrna_level, QuantityValue):
            self.mrna_level = QuantityValue(**as_dict(self.mrna_level))

        if self.protein_level is not None and not isinstance(self.protein_level, QuantityValue):
            self.protein_level = QuantityValue(**as_dict(self.protein_level))

        if self.percentage_positive_cells is not None and not isinstance(self.percentage_positive_cells, QuantityValue):
            self.percentage_positive_cells = QuantityValue(**as_dict(self.percentage_positive_cells))

        if self.staining_protocol is not None and not isinstance(self.staining_protocol, StainingProtocol):
            self.staining_protocol = StainingProtocol(**as_dict(self.staining_protocol))

        if self.gene_expression_analysis is not None and not isinstance(self.gene_expression_analysis, GeneExpressionAnalysis):
            self.gene_expression_analysis = GeneExpressionAnalysis(**as_dict(self.gene_expression_analysis))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CiliaBeatFrequencyMeasurement(Measurement):
    """
    Measurement of ciliary beat frequency
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["CiliaBeatFrequencyMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:CiliaBeatFrequencyMeasurement"
    class_name: ClassVar[str] = "CiliaBeatFrequencyMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.CiliaBeatFrequencyMeasurement

    id: Union[str, CiliaBeatFrequencyMeasurementId] = None
    beat_frequency_hz: Optional[Union[dict, QuantityValue]] = None
    active_area_percentage: Optional[Union[dict, QuantityValue]] = None
    imaging_protocol: Optional[Union[dict, "ImagingProtocol"]] = None
    cilia_per_cell: Optional[Union[dict, QuantityValue]] = None
    cilia_length: Optional[Union[dict, QuantityValue]] = None
    percentage_ciliated_cells: Optional[Union[dict, QuantityValue]] = None
    ciliary_motion_patterns: Optional[str] = None
    cell_type_ratios: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CiliaBeatFrequencyMeasurementId):
            self.id = CiliaBeatFrequencyMeasurementId(self.id)

        if self.beat_frequency_hz is not None and not isinstance(self.beat_frequency_hz, QuantityValue):
            self.beat_frequency_hz = QuantityValue(**as_dict(self.beat_frequency_hz))

        if self.active_area_percentage is not None and not isinstance(self.active_area_percentage, QuantityValue):
            self.active_area_percentage = QuantityValue(**as_dict(self.active_area_percentage))

        if self.imaging_protocol is not None and not isinstance(self.imaging_protocol, ImagingProtocol):
            self.imaging_protocol = ImagingProtocol(**as_dict(self.imaging_protocol))

        if self.cilia_per_cell is not None and not isinstance(self.cilia_per_cell, QuantityValue):
            self.cilia_per_cell = QuantityValue(**as_dict(self.cilia_per_cell))

        if self.cilia_length is not None and not isinstance(self.cilia_length, QuantityValue):
            self.cilia_length = QuantityValue(**as_dict(self.cilia_length))

        if self.percentage_ciliated_cells is not None and not isinstance(self.percentage_ciliated_cells, QuantityValue):
            self.percentage_ciliated_cells = QuantityValue(**as_dict(self.percentage_ciliated_cells))

        if self.ciliary_motion_patterns is not None and not isinstance(self.ciliary_motion_patterns, str):
            self.ciliary_motion_patterns = str(self.ciliary_motion_patterns)

        if self.cell_type_ratios is not None and not isinstance(self.cell_type_ratios, str):
            self.cell_type_ratios = str(self.cell_type_ratios)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ASLHeightMeasurement(Measurement):
    """
    Measurement of airway surface liquid height
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["ASLHeightMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:ASLHeightMeasurement"
    class_name: ClassVar[str] = "ASLHeightMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.ASLHeightMeasurement

    id: Union[str, ASLHeightMeasurementId] = None
    asl_height_um: Optional[Union[dict, QuantityValue]] = None
    periciliary_layer_depth: Optional[Union[dict, QuantityValue]] = None
    imaging_protocol: Optional[Union[dict, "ImagingProtocol"]] = None
    ion_composition: Optional[str] = None
    fluorescent_labeling: Optional[Union[dict, "FluorescentLabel"]] = None
    evaporation_prevention: Optional[Union[dict, "EvaporationControl"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ASLHeightMeasurementId):
            self.id = ASLHeightMeasurementId(self.id)

        if self.asl_height_um is not None and not isinstance(self.asl_height_um, QuantityValue):
            self.asl_height_um = QuantityValue(**as_dict(self.asl_height_um))

        if self.periciliary_layer_depth is not None and not isinstance(self.periciliary_layer_depth, QuantityValue):
            self.periciliary_layer_depth = QuantityValue(**as_dict(self.periciliary_layer_depth))

        if self.imaging_protocol is not None and not isinstance(self.imaging_protocol, ImagingProtocol):
            self.imaging_protocol = ImagingProtocol(**as_dict(self.imaging_protocol))

        if self.ion_composition is not None and not isinstance(self.ion_composition, str):
            self.ion_composition = str(self.ion_composition)

        if self.fluorescent_labeling is not None and not isinstance(self.fluorescent_labeling, FluorescentLabel):
            self.fluorescent_labeling = FluorescentLabel(**as_dict(self.fluorescent_labeling))

        if self.evaporation_prevention is not None and not isinstance(self.evaporation_prevention, EvaporationControl):
            self.evaporation_prevention = EvaporationControl(**as_dict(self.evaporation_prevention))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MucociliaryClearanceMeasurement(Measurement):
    """
    Measurement of mucociliary clearance/transport
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["MucociliaryClearanceMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:MucociliaryClearanceMeasurement"
    class_name: ClassVar[str] = "MucociliaryClearanceMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.MucociliaryClearanceMeasurement

    id: Union[str, MucociliaryClearanceMeasurementId] = None
    transport_rate: Optional[Union[dict, QuantityValue]] = None
    directionality: Optional[str] = None
    particle_tracking_method: Optional[str] = None
    fluorescent_tracers: Optional[Union[dict[Union[str, FluorescentLabelId], Union[dict, "FluorescentLabel"]], list[Union[dict, "FluorescentLabel"]]]] = empty_dict()
    mucus_layer_thickness: Optional[Union[dict, QuantityValue]] = None
    bacterial_biofilm_details: Optional[str] = None
    viral_infection_details: Optional[str] = None
    biofilm_clearance_rate: Optional[Union[dict, QuantityValue]] = None
    bacterial_load: Optional[Union[dict, QuantityValue]] = None
    viral_spread_rate: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MucociliaryClearanceMeasurementId):
            self.id = MucociliaryClearanceMeasurementId(self.id)

        if self.transport_rate is not None and not isinstance(self.transport_rate, QuantityValue):
            self.transport_rate = QuantityValue(**as_dict(self.transport_rate))

        if self.directionality is not None and not isinstance(self.directionality, str):
            self.directionality = str(self.directionality)

        if self.particle_tracking_method is not None and not isinstance(self.particle_tracking_method, str):
            self.particle_tracking_method = str(self.particle_tracking_method)

        self._normalize_inlined_as_dict(slot_name="fluorescent_tracers", slot_type=FluorescentLabel, key_name="id", keyed=True)

        if self.mucus_layer_thickness is not None and not isinstance(self.mucus_layer_thickness, QuantityValue):
            self.mucus_layer_thickness = QuantityValue(**as_dict(self.mucus_layer_thickness))

        if self.bacterial_biofilm_details is not None and not isinstance(self.bacterial_biofilm_details, str):
            self.bacterial_biofilm_details = str(self.bacterial_biofilm_details)

        if self.viral_infection_details is not None and not isinstance(self.viral_infection_details, str):
            self.viral_infection_details = str(self.viral_infection_details)

        if self.biofilm_clearance_rate is not None and not isinstance(self.biofilm_clearance_rate, QuantityValue):
            self.biofilm_clearance_rate = QuantityValue(**as_dict(self.biofilm_clearance_rate))

        if self.bacterial_load is not None and not isinstance(self.bacterial_load, QuantityValue):
            self.bacterial_load = QuantityValue(**as_dict(self.bacterial_load))

        if self.viral_spread_rate is not None and not isinstance(self.viral_spread_rate, QuantityValue):
            self.viral_spread_rate = QuantityValue(**as_dict(self.viral_spread_rate))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GobletCellMeasurement(Measurement):
    """
    Measurement of goblet cell number or mucin production
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["GobletCellMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:GobletCellMeasurement"
    class_name: ClassVar[str] = "GobletCellMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.GobletCellMeasurement

    id: Union[str, GobletCellMeasurementId] = None
    goblet_cell_count: Optional[Union[dict, QuantityValue]] = None
    mucin_expression_level: Optional[Union[dict, QuantityValue]] = None
    staining_protocol: Optional[Union[dict, "StainingProtocol"]] = None
    gene_expression_analysis: Optional[Union[dict, "GeneExpressionAnalysis"]] = None
    mucin_protein_concentration: Optional[Union[dict, QuantityValue]] = None
    goblet_to_ciliated_ratio: Optional[Union[dict, QuantityValue]] = None
    pathway_enrichment_scores: Optional[Union[str, list[str]]] = empty_list()
    dose_response_data: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GobletCellMeasurementId):
            self.id = GobletCellMeasurementId(self.id)

        if self.goblet_cell_count is not None and not isinstance(self.goblet_cell_count, QuantityValue):
            self.goblet_cell_count = QuantityValue(**as_dict(self.goblet_cell_count))

        if self.mucin_expression_level is not None and not isinstance(self.mucin_expression_level, QuantityValue):
            self.mucin_expression_level = QuantityValue(**as_dict(self.mucin_expression_level))

        if self.staining_protocol is not None and not isinstance(self.staining_protocol, StainingProtocol):
            self.staining_protocol = StainingProtocol(**as_dict(self.staining_protocol))

        if self.gene_expression_analysis is not None and not isinstance(self.gene_expression_analysis, GeneExpressionAnalysis):
            self.gene_expression_analysis = GeneExpressionAnalysis(**as_dict(self.gene_expression_analysis))

        if self.mucin_protein_concentration is not None and not isinstance(self.mucin_protein_concentration, QuantityValue):
            self.mucin_protein_concentration = QuantityValue(**as_dict(self.mucin_protein_concentration))

        if self.goblet_to_ciliated_ratio is not None and not isinstance(self.goblet_to_ciliated_ratio, QuantityValue):
            self.goblet_to_ciliated_ratio = QuantityValue(**as_dict(self.goblet_to_ciliated_ratio))

        if not isinstance(self.pathway_enrichment_scores, list):
            self.pathway_enrichment_scores = [self.pathway_enrichment_scores] if self.pathway_enrichment_scores is not None else []
        self.pathway_enrichment_scores = [v if isinstance(v, str) else str(v) for v in self.pathway_enrichment_scores]

        if self.dose_response_data is not None and not isinstance(self.dose_response_data, str):
            self.dose_response_data = str(self.dose_response_data)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OxidativeStressMeasurement(Measurement):
    """
    Measurement of oxidative stress markers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["OxidativeStressMeasurement"]
    class_class_curie: ClassVar[str] = "outcomes_model:OxidativeStressMeasurement"
    class_name: ClassVar[str] = "OxidativeStressMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.OxidativeStressMeasurement

    id: Union[str, OxidativeStressMeasurementId] = None
    ros_level: Optional[Union[dict, QuantityValue]] = None
    lipid_peroxidation: Optional[Union[dict, QuantityValue]] = None
    antioxidant_capacity: Optional[Union[dict, QuantityValue]] = None
    ros_probe: Optional[Union[dict, "ROSProbe"]] = None
    detection_method_details: Optional[Union[dict[Union[str, DetectionMethodId], Union[dict, "DetectionMethod"]], list[Union[dict, "DetectionMethod"]]]] = empty_dict()
    protein_oxidation_markers: Optional[Union[str, list[str]]] = empty_list()
    dna_damage_markers: Optional[Union[dict, QuantityValue]] = None
    antioxidant_enzyme_activities: Optional[str] = None
    barrier_integrity: Optional[Union[dict, "BarrierIntegrity"]] = None
    cytotoxicity_metrics: Optional[Union[dict, "CytotoxicityMetrics"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OxidativeStressMeasurementId):
            self.id = OxidativeStressMeasurementId(self.id)

        if self.ros_level is not None and not isinstance(self.ros_level, QuantityValue):
            self.ros_level = QuantityValue(**as_dict(self.ros_level))

        if self.lipid_peroxidation is not None and not isinstance(self.lipid_peroxidation, QuantityValue):
            self.lipid_peroxidation = QuantityValue(**as_dict(self.lipid_peroxidation))

        if self.antioxidant_capacity is not None and not isinstance(self.antioxidant_capacity, QuantityValue):
            self.antioxidant_capacity = QuantityValue(**as_dict(self.antioxidant_capacity))

        if self.ros_probe is not None and not isinstance(self.ros_probe, ROSProbe):
            self.ros_probe = ROSProbe(**as_dict(self.ros_probe))

        self._normalize_inlined_as_dict(slot_name="detection_method_details", slot_type=DetectionMethod, key_name="id", keyed=True)

        if not isinstance(self.protein_oxidation_markers, list):
            self.protein_oxidation_markers = [self.protein_oxidation_markers] if self.protein_oxidation_markers is not None else []
        self.protein_oxidation_markers = [v if isinstance(v, str) else str(v) for v in self.protein_oxidation_markers]

        if self.dna_damage_markers is not None and not isinstance(self.dna_damage_markers, QuantityValue):
            self.dna_damage_markers = QuantityValue(**as_dict(self.dna_damage_markers))

        if self.antioxidant_enzyme_activities is not None and not isinstance(self.antioxidant_enzyme_activities, str):
            self.antioxidant_enzyme_activities = str(self.antioxidant_enzyme_activities)

        if self.barrier_integrity is not None and not isinstance(self.barrier_integrity, BarrierIntegrity):
            self.barrier_integrity = BarrierIntegrity(**as_dict(self.barrier_integrity))

        if self.cytotoxicity_metrics is not None and not isinstance(self.cytotoxicity_metrics, CytotoxicityMetrics):
            self.cytotoxicity_metrics = CytotoxicityMetrics(**as_dict(self.cytotoxicity_metrics))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(NamedEntity):
    """
    Any published piece of information, following Biolink model.
    Represents scientific evidence supporting research.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["Publication"]
    class_class_curie: ClassVar[str] = "outcomes_model:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.Publication

    id: Union[str, PublicationId] = None
    authors: Optional[Union[str, list[str]]] = empty_list()
    pages: Optional[str] = None
    summary: Optional[str] = None
    keywords: Optional[Union[str, list[str]]] = empty_list()
    mesh_terms: Optional[Union[str, list[str]]] = empty_list()
    publication_type: Optional[str] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.pages is not None and not isinstance(self.pages, str):
            self.pages = str(self.pages)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if not isinstance(self.mesh_terms, list):
            self.mesh_terms = [self.mesh_terms] if self.mesh_terms is not None else []
        self.mesh_terms = [v if isinstance(v, str) else str(v) for v in self.mesh_terms]

        if self.publication_type is not None and not isinstance(self.publication_type, str):
            self.publication_type = str(self.publication_type)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImagingProtocol(NamedEntity):
    """
    Details about imaging parameters and protocols
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["ImagingProtocol"]
    class_class_curie: ClassVar[str] = "outcomes_model:ImagingProtocol"
    class_name: ClassVar[str] = "ImagingProtocol"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.ImagingProtocol

    id: Union[str, ImagingProtocolId] = None
    imaging_modality: Optional[str] = None
    frame_rate: Optional[Union[dict, QuantityValue]] = None
    imaging_duration: Optional[Union[dict, QuantityValue]] = None
    imaging_intervals: Optional[str] = None
    spatial_resolution: Optional[Union[dict, QuantityValue]] = None
    probe_positioning: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImagingProtocolId):
            self.id = ImagingProtocolId(self.id)

        if self.imaging_modality is not None and not isinstance(self.imaging_modality, str):
            self.imaging_modality = str(self.imaging_modality)

        if self.frame_rate is not None and not isinstance(self.frame_rate, QuantityValue):
            self.frame_rate = QuantityValue(**as_dict(self.frame_rate))

        if self.imaging_duration is not None and not isinstance(self.imaging_duration, QuantityValue):
            self.imaging_duration = QuantityValue(**as_dict(self.imaging_duration))

        if self.imaging_intervals is not None and not isinstance(self.imaging_intervals, str):
            self.imaging_intervals = str(self.imaging_intervals)

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, QuantityValue):
            self.spatial_resolution = QuantityValue(**as_dict(self.spatial_resolution))

        if self.probe_positioning is not None and not isinstance(self.probe_positioning, str):
            self.probe_positioning = str(self.probe_positioning)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FluorescentLabel(NamedEntity):
    """
    Fluorescent labeling or tracer used in measurement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["FluorescentLabel"]
    class_class_curie: ClassVar[str] = "outcomes_model:FluorescentLabel"
    class_name: ClassVar[str] = "FluorescentLabel"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.FluorescentLabel

    id: Union[str, FluorescentLabelId] = None
    fluorophore_type: Optional[str] = None
    concentration: Optional[Union[dict, QuantityValue]] = None
    wavelength: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FluorescentLabelId):
            self.id = FluorescentLabelId(self.id)

        if self.fluorophore_type is not None and not isinstance(self.fluorophore_type, str):
            self.fluorophore_type = str(self.fluorophore_type)

        if self.concentration is not None and not isinstance(self.concentration, QuantityValue):
            self.concentration = QuantityValue(**as_dict(self.concentration))

        if self.wavelength is not None and not isinstance(self.wavelength, QuantityValue):
            self.wavelength = QuantityValue(**as_dict(self.wavelength))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaporationControl(NamedEntity):
    """
    Method used to prevent evaporation during measurement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["EvaporationControl"]
    class_class_curie: ClassVar[str] = "outcomes_model:EvaporationControl"
    class_name: ClassVar[str] = "EvaporationControl"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.EvaporationControl

    id: Union[str, EvaporationControlId] = None
    control_method: Optional[str] = None
    material_used: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaporationControlId):
            self.id = EvaporationControlId(self.id)

        if self.control_method is not None and not isinstance(self.control_method, str):
            self.control_method = str(self.control_method)

        if self.material_used is not None and not isinstance(self.material_used, str):
            self.material_used = str(self.material_used)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ROSProbe(NamedEntity):
    """
    Reactive oxygen species probe and detection details
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["ROSProbe"]
    class_class_curie: ClassVar[str] = "outcomes_model:ROSProbe"
    class_name: ClassVar[str] = "ROSProbe"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.ROSProbe

    id: Union[str, ROSProbeId] = None
    probe_type: Optional[str] = None
    loading_conditions: Optional[str] = None
    detection_wavelength: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ROSProbeId):
            self.id = ROSProbeId(self.id)

        if self.probe_type is not None and not isinstance(self.probe_type, str):
            self.probe_type = str(self.probe_type)

        if self.loading_conditions is not None and not isinstance(self.loading_conditions, str):
            self.loading_conditions = str(self.loading_conditions)

        if self.detection_wavelength is not None and not isinstance(self.detection_wavelength, QuantityValue):
            self.detection_wavelength = QuantityValue(**as_dict(self.detection_wavelength))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DetectionMethod(NamedEntity):
    """
    Method used for detecting or measuring analytes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["DetectionMethod"]
    class_class_curie: ClassVar[str] = "outcomes_model:DetectionMethod"
    class_name: ClassVar[str] = "DetectionMethod"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.DetectionMethod

    id: Union[str, DetectionMethodId] = None
    detection_type: Optional[str] = None
    instrumentation: Optional[str] = None
    sensitivity: Optional[str] = None
    technical_replicates: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DetectionMethodId):
            self.id = DetectionMethodId(self.id)

        if self.detection_type is not None and not isinstance(self.detection_type, str):
            self.detection_type = str(self.detection_type)

        if self.instrumentation is not None and not isinstance(self.instrumentation, str):
            self.instrumentation = str(self.instrumentation)

        if self.sensitivity is not None and not isinstance(self.sensitivity, str):
            self.sensitivity = str(self.sensitivity)

        if self.technical_replicates is not None and not isinstance(self.technical_replicates, int):
            self.technical_replicates = int(self.technical_replicates)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleCollection(NamedEntity):
    """
    Details about biological sample collection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["SampleCollection"]
    class_class_curie: ClassVar[str] = "outcomes_model:SampleCollection"
    class_name: ClassVar[str] = "SampleCollection"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.SampleCollection

    id: Union[str, SampleCollectionId] = None
    collection_method: Optional[str] = None
    processing_time: Optional[Union[dict, QuantityValue]] = None
    storage_conditions: Optional[str] = None
    sample_volume: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleCollectionId):
            self.id = SampleCollectionId(self.id)

        if self.collection_method is not None and not isinstance(self.collection_method, str):
            self.collection_method = str(self.collection_method)

        if self.processing_time is not None and not isinstance(self.processing_time, QuantityValue):
            self.processing_time = QuantityValue(**as_dict(self.processing_time))

        if self.storage_conditions is not None and not isinstance(self.storage_conditions, str):
            self.storage_conditions = str(self.storage_conditions)

        if self.sample_volume is not None and not isinstance(self.sample_volume, QuantityValue):
            self.sample_volume = QuantityValue(**as_dict(self.sample_volume))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellCultureConditions(NamedEntity):
    """
    Detailed cell culture parameters
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["CellCultureConditions"]
    class_class_curie: ClassVar[str] = "outcomes_model:CellCultureConditions"
    class_name: ClassVar[str] = "CellCultureConditions"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.CellCultureConditions

    id: Union[str, CellCultureConditionsId] = None
    culture_medium: Optional[str] = None
    days_at_ali: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    humidity: Optional[Union[dict, QuantityValue]] = None
    co2_percentage: Optional[Union[dict, QuantityValue]] = None
    donor_count: Optional[int] = None
    replicates_per_donor: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellCultureConditionsId):
            self.id = CellCultureConditionsId(self.id)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        if self.days_at_ali is not None and not isinstance(self.days_at_ali, int):
            self.days_at_ali = int(self.days_at_ali)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if self.humidity is not None and not isinstance(self.humidity, QuantityValue):
            self.humidity = QuantityValue(**as_dict(self.humidity))

        if self.co2_percentage is not None and not isinstance(self.co2_percentage, QuantityValue):
            self.co2_percentage = QuantityValue(**as_dict(self.co2_percentage))

        if self.donor_count is not None and not isinstance(self.donor_count, int):
            self.donor_count = int(self.donor_count)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StainingProtocol(NamedEntity):
    """
    Histological or immunofluorescence staining protocol
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["StainingProtocol"]
    class_class_curie: ClassVar[str] = "outcomes_model:StainingProtocol"
    class_name: ClassVar[str] = "StainingProtocol"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.StainingProtocol

    id: Union[str, StainingProtocolId] = None
    staining_type: Optional[str] = None
    antibodies_used: Optional[Union[str, list[str]]] = empty_list()
    fixation_method: Optional[str] = None
    incubation_conditions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StainingProtocolId):
            self.id = StainingProtocolId(self.id)

        if self.staining_type is not None and not isinstance(self.staining_type, str):
            self.staining_type = str(self.staining_type)

        if not isinstance(self.antibodies_used, list):
            self.antibodies_used = [self.antibodies_used] if self.antibodies_used is not None else []
        self.antibodies_used = [v if isinstance(v, str) else str(v) for v in self.antibodies_used]

        if self.fixation_method is not None and not isinstance(self.fixation_method, str):
            self.fixation_method = str(self.fixation_method)

        if self.incubation_conditions is not None and not isinstance(self.incubation_conditions, str):
            self.incubation_conditions = str(self.incubation_conditions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneExpressionAnalysis(NamedEntity):
    """
    Gene expression measurement methodology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["GeneExpressionAnalysis"]
    class_class_curie: ClassVar[str] = "outcomes_model:GeneExpressionAnalysis"
    class_name: ClassVar[str] = "GeneExpressionAnalysis"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.GeneExpressionAnalysis

    id: Union[str, GeneExpressionAnalysisId] = None
    analysis_method: Optional[str] = None
    normalization_genes: Optional[Union[str, list[str]]] = empty_list()
    primers_used: Optional[Union[str, list[str]]] = empty_list()
    sequencing_platform: Optional[str] = None
    sequencing_depth: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneExpressionAnalysisId):
            self.id = GeneExpressionAnalysisId(self.id)

        if self.analysis_method is not None and not isinstance(self.analysis_method, str):
            self.analysis_method = str(self.analysis_method)

        if not isinstance(self.normalization_genes, list):
            self.normalization_genes = [self.normalization_genes] if self.normalization_genes is not None else []
        self.normalization_genes = [v if isinstance(v, str) else str(v) for v in self.normalization_genes]

        if not isinstance(self.primers_used, list):
            self.primers_used = [self.primers_used] if self.primers_used is not None else []
        self.primers_used = [v if isinstance(v, str) else str(v) for v in self.primers_used]

        if self.sequencing_platform is not None and not isinstance(self.sequencing_platform, str):
            self.sequencing_platform = str(self.sequencing_platform)

        if self.sequencing_depth is not None and not isinstance(self.sequencing_depth, int):
            self.sequencing_depth = int(self.sequencing_depth)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InflammatoryCellProfile(NamedEntity):
    """
    Profile of inflammatory cell types and counts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["InflammatoryCellProfile"]
    class_class_curie: ClassVar[str] = "outcomes_model:InflammatoryCellProfile"
    class_name: ClassVar[str] = "InflammatoryCellProfile"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.InflammatoryCellProfile

    id: Union[str, InflammatoryCellProfileId] = None
    neutrophil_percentage: Optional[Union[dict, QuantityValue]] = None
    eosinophil_percentage: Optional[Union[dict, QuantityValue]] = None
    macrophage_percentage: Optional[Union[dict, QuantityValue]] = None
    lymphocyte_percentage: Optional[Union[dict, QuantityValue]] = None
    total_cell_count: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InflammatoryCellProfileId):
            self.id = InflammatoryCellProfileId(self.id)

        if self.neutrophil_percentage is not None and not isinstance(self.neutrophil_percentage, QuantityValue):
            self.neutrophil_percentage = QuantityValue(**as_dict(self.neutrophil_percentage))

        if self.eosinophil_percentage is not None and not isinstance(self.eosinophil_percentage, QuantityValue):
            self.eosinophil_percentage = QuantityValue(**as_dict(self.eosinophil_percentage))

        if self.macrophage_percentage is not None and not isinstance(self.macrophage_percentage, QuantityValue):
            self.macrophage_percentage = QuantityValue(**as_dict(self.macrophage_percentage))

        if self.lymphocyte_percentage is not None and not isinstance(self.lymphocyte_percentage, QuantityValue):
            self.lymphocyte_percentage = QuantityValue(**as_dict(self.lymphocyte_percentage))

        if self.total_cell_count is not None and not isinstance(self.total_cell_count, QuantityValue):
            self.total_cell_count = QuantityValue(**as_dict(self.total_cell_count))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrobiomeAnalysis(NamedEntity):
    """
    Microbiome composition analysis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["MicrobiomeAnalysis"]
    class_class_curie: ClassVar[str] = "outcomes_model:MicrobiomeAnalysis"
    class_name: ClassVar[str] = "MicrobiomeAnalysis"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.MicrobiomeAnalysis

    id: Union[str, MicrobiomeAnalysisId] = None
    alpha_diversity: Optional[Union[dict, QuantityValue]] = None
    beta_diversity: Optional[str] = None
    taxonomic_abundance: Optional[Union[str, list[str]]] = empty_list()
    sequencing_primers: Optional[Union[str, list[str]]] = empty_list()
    dna_extraction_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicrobiomeAnalysisId):
            self.id = MicrobiomeAnalysisId(self.id)

        if self.alpha_diversity is not None and not isinstance(self.alpha_diversity, QuantityValue):
            self.alpha_diversity = QuantityValue(**as_dict(self.alpha_diversity))

        if self.beta_diversity is not None and not isinstance(self.beta_diversity, str):
            self.beta_diversity = str(self.beta_diversity)

        if not isinstance(self.taxonomic_abundance, list):
            self.taxonomic_abundance = [self.taxonomic_abundance] if self.taxonomic_abundance is not None else []
        self.taxonomic_abundance = [v if isinstance(v, str) else str(v) for v in self.taxonomic_abundance]

        if not isinstance(self.sequencing_primers, list):
            self.sequencing_primers = [self.sequencing_primers] if self.sequencing_primers is not None else []
        self.sequencing_primers = [v if isinstance(v, str) else str(v) for v in self.sequencing_primers]

        if self.dna_extraction_method is not None and not isinstance(self.dna_extraction_method, str):
            self.dna_extraction_method = str(self.dna_extraction_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BarrierIntegrity(NamedEntity):
    """
    Epithelial barrier integrity measurements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["BarrierIntegrity"]
    class_class_curie: ClassVar[str] = "outcomes_model:BarrierIntegrity"
    class_name: ClassVar[str] = "BarrierIntegrity"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.BarrierIntegrity

    id: Union[str, BarrierIntegrityId] = None
    teer_value: Optional[Union[dict, QuantityValue]] = None
    permeability_coefficient: Optional[Union[dict, QuantityValue]] = None
    measurement_timepoint: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BarrierIntegrityId):
            self.id = BarrierIntegrityId(self.id)

        if self.teer_value is not None and not isinstance(self.teer_value, QuantityValue):
            self.teer_value = QuantityValue(**as_dict(self.teer_value))

        if self.permeability_coefficient is not None and not isinstance(self.permeability_coefficient, QuantityValue):
            self.permeability_coefficient = QuantityValue(**as_dict(self.permeability_coefficient))

        if self.measurement_timepoint is not None and not isinstance(self.measurement_timepoint, str):
            self.measurement_timepoint = str(self.measurement_timepoint)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CytotoxicityMetrics(NamedEntity):
    """
    Cell viability and cytotoxicity measurements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["CytotoxicityMetrics"]
    class_class_curie: ClassVar[str] = "outcomes_model:CytotoxicityMetrics"
    class_name: ClassVar[str] = "CytotoxicityMetrics"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.CytotoxicityMetrics

    id: Union[str, CytotoxicityMetricsId] = None
    ldh_release: Optional[Union[dict, QuantityValue]] = None
    mtt_reduction: Optional[Union[dict, QuantityValue]] = None
    viability_percentage: Optional[Union[dict, QuantityValue]] = None
    apoptosis_markers: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CytotoxicityMetricsId):
            self.id = CytotoxicityMetricsId(self.id)

        if self.ldh_release is not None and not isinstance(self.ldh_release, QuantityValue):
            self.ldh_release = QuantityValue(**as_dict(self.ldh_release))

        if self.mtt_reduction is not None and not isinstance(self.mtt_reduction, QuantityValue):
            self.mtt_reduction = QuantityValue(**as_dict(self.mtt_reduction))

        if self.viability_percentage is not None and not isinstance(self.viability_percentage, QuantityValue):
            self.viability_percentage = QuantityValue(**as_dict(self.viability_percentage))

        if not isinstance(self.apoptosis_markers, list):
            self.apoptosis_markers = [self.apoptosis_markers] if self.apoptosis_markers is not None else []
        self.apoptosis_markers = [v if isinstance(v, str) else str(v) for v in self.apoptosis_markers]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalCondition(NamedEntity):
    """
    Environmental parameters during measurement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_MODEL["EnvironmentalCondition"]
    class_class_curie: ClassVar[str] = "outcomes_model:EnvironmentalCondition"
    class_name: ClassVar[str] = "EnvironmentalCondition"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_MODEL.EnvironmentalCondition

    id: Union[str, EnvironmentalConditionId] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    humidity: Optional[Union[dict, QuantityValue]] = None
    co2_percentage: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalConditionId):
            self.id = EnvironmentalConditionId(self.id)

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if self.humidity is not None and not isinstance(self.humidity, QuantityValue):
            self.humidity = QuantityValue(**as_dict(self.humidity))

        if self.co2_percentage is not None and not isinstance(self.co2_percentage, QuantityValue):
            self.co2_percentage = QuantityValue(**as_dict(self.co2_percentage))

        super().__post_init__(**kwargs)


# Enumerations
class AssayTypeEnum(EnumDefinitionImpl):
    """
    Types of assays from the Ontology for Biomedical Investigations (OBI)
    """
    _defn = EnumDefinition(
        name="AssayTypeEnum",
        description="Types of assays from the Ontology for Biomedical Investigations (OBI)",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "OBI:0000070",
            PermissibleValue(
                text="OBI:0000070",
                description="assay",
                meaning=OBI["0000070"]))

# Slots
class slots:
    pass

slots.id = Slot(uri=OUTCOMES_MODEL.id, name="id", curie=OUTCOMES_MODEL.curie('id'),
                   model_uri=OUTCOMES_MODEL.id, domain=None, range=URIRef)

slots.description = Slot(uri=OUTCOMES_MODEL.description, name="description", curie=OUTCOMES_MODEL.curie('description'),
                   model_uri=OUTCOMES_MODEL.description, domain=None, range=Optional[str])

slots.input_sample = Slot(uri=OUTCOMES_MODEL.input_sample, name="input_sample", curie=OUTCOMES_MODEL.curie('input_sample'),
                   model_uri=OUTCOMES_MODEL.input_sample, domain=None, range=Optional[Union[str, InputSampleId]])

slots.method_assay = Slot(uri=OUTCOMES_MODEL.method_assay, name="method_assay", curie=OUTCOMES_MODEL.curie('method_assay'),
                   model_uri=OUTCOMES_MODEL.method_assay, domain=None, range=Optional[Union[str, AssayId]])

slots.protocol_notes = Slot(uri=OUTCOMES_MODEL.protocol_notes, name="protocol_notes", curie=OUTCOMES_MODEL.curie('protocol_notes'),
                   model_uri=OUTCOMES_MODEL.protocol_notes, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=OUTCOMES_MODEL.sample_type, name="sample_type", curie=OUTCOMES_MODEL.curie('sample_type'),
                   model_uri=OUTCOMES_MODEL.sample_type, domain=None, range=Optional[str])

slots.manipulation = Slot(uri=OUTCOMES_MODEL.manipulation, name="manipulation", curie=OUTCOMES_MODEL.curie('manipulation'),
                   model_uri=OUTCOMES_MODEL.manipulation, domain=None, range=Optional[str])

slots.exposure_conditions = Slot(uri=OUTCOMES_MODEL.exposure_conditions, name="exposure_conditions", curie=OUTCOMES_MODEL.curie('exposure_conditions'),
                   model_uri=OUTCOMES_MODEL.exposure_conditions, domain=None, range=Optional[str])

slots.assay_type = Slot(uri=OUTCOMES_MODEL.assay_type, name="assay_type", curie=OUTCOMES_MODEL.curie('assay_type'),
                   model_uri=OUTCOMES_MODEL.assay_type, domain=None, range=Optional[Union[str, "AssayTypeEnum"]])

slots.instrumentation = Slot(uri=OUTCOMES_MODEL.instrumentation, name="instrumentation", curie=OUTCOMES_MODEL.curie('instrumentation'),
                   model_uri=OUTCOMES_MODEL.instrumentation, domain=None, range=Optional[str])

slots.environmental_conditions = Slot(uri=OUTCOMES_MODEL.environmental_conditions, name="environmental_conditions", curie=OUTCOMES_MODEL.curie('environmental_conditions'),
                   model_uri=OUTCOMES_MODEL.environmental_conditions, domain=None, range=Optional[Union[dict[Union[str, EnvironmentalConditionId], Union[dict, EnvironmentalCondition]], list[Union[dict, EnvironmentalCondition]]]])

slots.sop_reference = Slot(uri=OUTCOMES_MODEL.sop_reference, name="sop_reference", curie=OUTCOMES_MODEL.curie('sop_reference'),
                   model_uri=OUTCOMES_MODEL.sop_reference, domain=None, range=Optional[str])

slots.has_numeric_value = Slot(uri=OUTCOMES_MODEL.has_numeric_value, name="has_numeric_value", curie=OUTCOMES_MODEL.curie('has_numeric_value'),
                   model_uri=OUTCOMES_MODEL.has_numeric_value, domain=None, range=Optional[float])

slots.has_unit = Slot(uri=OUTCOMES_MODEL.has_unit, name="has_unit", curie=OUTCOMES_MODEL.curie('has_unit'),
                   model_uri=OUTCOMES_MODEL.has_unit, domain=None, range=Optional[str])

slots.has_minimum_numeric_value = Slot(uri=OUTCOMES_MODEL.has_minimum_numeric_value, name="has_minimum_numeric_value", curie=OUTCOMES_MODEL.curie('has_minimum_numeric_value'),
                   model_uri=OUTCOMES_MODEL.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.has_maximum_numeric_value = Slot(uri=OUTCOMES_MODEL.has_maximum_numeric_value, name="has_maximum_numeric_value", curie=OUTCOMES_MODEL.curie('has_maximum_numeric_value'),
                   model_uri=OUTCOMES_MODEL.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.cftr_specific_current = Slot(uri=OUTCOMES_MODEL.cftr_specific_current, name="cftr_specific_current", curie=OUTCOMES_MODEL.curie('cftr_specific_current'),
                   model_uri=OUTCOMES_MODEL.cftr_specific_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inhibitor_sensitive_current = Slot(uri=OUTCOMES_MODEL.inhibitor_sensitive_current, name="inhibitor_sensitive_current", curie=OUTCOMES_MODEL.curie('inhibitor_sensitive_current'),
                   model_uri=OUTCOMES_MODEL.inhibitor_sensitive_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cell_culture_conditions = Slot(uri=OUTCOMES_MODEL.cell_culture_conditions, name="cell_culture_conditions", curie=OUTCOMES_MODEL.curie('cell_culture_conditions'),
                   model_uri=OUTCOMES_MODEL.cell_culture_conditions, domain=None, range=Optional[str])

slots.beat_frequency_hz = Slot(uri=OUTCOMES_MODEL.beat_frequency_hz, name="beat_frequency_hz", curie=OUTCOMES_MODEL.curie('beat_frequency_hz'),
                   model_uri=OUTCOMES_MODEL.beat_frequency_hz, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.active_area_percentage = Slot(uri=OUTCOMES_MODEL.active_area_percentage, name="active_area_percentage", curie=OUTCOMES_MODEL.curie('active_area_percentage'),
                   model_uri=OUTCOMES_MODEL.active_area_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_conditions = Slot(uri=OUTCOMES_MODEL.imaging_conditions, name="imaging_conditions", curie=OUTCOMES_MODEL.curie('imaging_conditions'),
                   model_uri=OUTCOMES_MODEL.imaging_conditions, domain=None, range=Optional[str])

slots.asl_height_um = Slot(uri=OUTCOMES_MODEL.asl_height_um, name="asl_height_um", curie=OUTCOMES_MODEL.curie('asl_height_um'),
                   model_uri=OUTCOMES_MODEL.asl_height_um, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.periciliary_layer_depth = Slot(uri=OUTCOMES_MODEL.periciliary_layer_depth, name="periciliary_layer_depth", curie=OUTCOMES_MODEL.curie('periciliary_layer_depth'),
                   model_uri=OUTCOMES_MODEL.periciliary_layer_depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_modality = Slot(uri=OUTCOMES_MODEL.imaging_modality, name="imaging_modality", curie=OUTCOMES_MODEL.curie('imaging_modality'),
                   model_uri=OUTCOMES_MODEL.imaging_modality, domain=None, range=Optional[str])

slots.transport_rate = Slot(uri=OUTCOMES_MODEL.transport_rate, name="transport_rate", curie=OUTCOMES_MODEL.curie('transport_rate'),
                   model_uri=OUTCOMES_MODEL.transport_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.directionality = Slot(uri=OUTCOMES_MODEL.directionality, name="directionality", curie=OUTCOMES_MODEL.curie('directionality'),
                   model_uri=OUTCOMES_MODEL.directionality, domain=None, range=Optional[str])

slots.particle_tracking_method = Slot(uri=OUTCOMES_MODEL.particle_tracking_method, name="particle_tracking_method", curie=OUTCOMES_MODEL.curie('particle_tracking_method'),
                   model_uri=OUTCOMES_MODEL.particle_tracking_method, domain=None, range=Optional[str])

slots.goblet_cell_count = Slot(uri=OUTCOMES_MODEL.goblet_cell_count, name="goblet_cell_count", curie=OUTCOMES_MODEL.curie('goblet_cell_count'),
                   model_uri=OUTCOMES_MODEL.goblet_cell_count, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mucin_expression_level = Slot(uri=OUTCOMES_MODEL.mucin_expression_level, name="mucin_expression_level", curie=OUTCOMES_MODEL.curie('mucin_expression_level'),
                   model_uri=OUTCOMES_MODEL.mucin_expression_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.staining_method = Slot(uri=OUTCOMES_MODEL.staining_method, name="staining_method", curie=OUTCOMES_MODEL.curie('staining_method'),
                   model_uri=OUTCOMES_MODEL.staining_method, domain=None, range=Optional[str])

slots.ros_level = Slot(uri=OUTCOMES_MODEL.ros_level, name="ros_level", curie=OUTCOMES_MODEL.curie('ros_level'),
                   model_uri=OUTCOMES_MODEL.ros_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lipid_peroxidation = Slot(uri=OUTCOMES_MODEL.lipid_peroxidation, name="lipid_peroxidation", curie=OUTCOMES_MODEL.curie('lipid_peroxidation'),
                   model_uri=OUTCOMES_MODEL.lipid_peroxidation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.antioxidant_capacity = Slot(uri=OUTCOMES_MODEL.antioxidant_capacity, name="antioxidant_capacity", curie=OUTCOMES_MODEL.curie('antioxidant_capacity'),
                   model_uri=OUTCOMES_MODEL.antioxidant_capacity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_protocol = Slot(uri=OUTCOMES_MODEL.imaging_protocol, name="imaging_protocol", curie=OUTCOMES_MODEL.curie('imaging_protocol'),
                   model_uri=OUTCOMES_MODEL.imaging_protocol, domain=None, range=Optional[Union[dict, ImagingProtocol]])

slots.ion_composition = Slot(uri=OUTCOMES_MODEL.ion_composition, name="ion_composition", curie=OUTCOMES_MODEL.curie('ion_composition'),
                   model_uri=OUTCOMES_MODEL.ion_composition, domain=None, range=Optional[str])

slots.fluorescent_labeling = Slot(uri=OUTCOMES_MODEL.fluorescent_labeling, name="fluorescent_labeling", curie=OUTCOMES_MODEL.curie('fluorescent_labeling'),
                   model_uri=OUTCOMES_MODEL.fluorescent_labeling, domain=None, range=Optional[Union[dict, FluorescentLabel]])

slots.evaporation_prevention = Slot(uri=OUTCOMES_MODEL.evaporation_prevention, name="evaporation_prevention", curie=OUTCOMES_MODEL.curie('evaporation_prevention'),
                   model_uri=OUTCOMES_MODEL.evaporation_prevention, domain=None, range=Optional[Union[dict, EvaporationControl]])

slots.cilia_per_cell = Slot(uri=OUTCOMES_MODEL.cilia_per_cell, name="cilia_per_cell", curie=OUTCOMES_MODEL.curie('cilia_per_cell'),
                   model_uri=OUTCOMES_MODEL.cilia_per_cell, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cilia_length = Slot(uri=OUTCOMES_MODEL.cilia_length, name="cilia_length", curie=OUTCOMES_MODEL.curie('cilia_length'),
                   model_uri=OUTCOMES_MODEL.cilia_length, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.percentage_ciliated_cells = Slot(uri=OUTCOMES_MODEL.percentage_ciliated_cells, name="percentage_ciliated_cells", curie=OUTCOMES_MODEL.curie('percentage_ciliated_cells'),
                   model_uri=OUTCOMES_MODEL.percentage_ciliated_cells, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ciliary_motion_patterns = Slot(uri=OUTCOMES_MODEL.ciliary_motion_patterns, name="ciliary_motion_patterns", curie=OUTCOMES_MODEL.curie('ciliary_motion_patterns'),
                   model_uri=OUTCOMES_MODEL.ciliary_motion_patterns, domain=None, range=Optional[str])

slots.cell_type_ratios = Slot(uri=OUTCOMES_MODEL.cell_type_ratios, name="cell_type_ratios", curie=OUTCOMES_MODEL.curie('cell_type_ratios'),
                   model_uri=OUTCOMES_MODEL.cell_type_ratios, domain=None, range=Optional[str])

slots.fluorescent_tracers = Slot(uri=OUTCOMES_MODEL.fluorescent_tracers, name="fluorescent_tracers", curie=OUTCOMES_MODEL.curie('fluorescent_tracers'),
                   model_uri=OUTCOMES_MODEL.fluorescent_tracers, domain=None, range=Optional[Union[dict[Union[str, FluorescentLabelId], Union[dict, FluorescentLabel]], list[Union[dict, FluorescentLabel]]]])

slots.mucus_layer_thickness = Slot(uri=OUTCOMES_MODEL.mucus_layer_thickness, name="mucus_layer_thickness", curie=OUTCOMES_MODEL.curie('mucus_layer_thickness'),
                   model_uri=OUTCOMES_MODEL.mucus_layer_thickness, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bacterial_biofilm_details = Slot(uri=OUTCOMES_MODEL.bacterial_biofilm_details, name="bacterial_biofilm_details", curie=OUTCOMES_MODEL.curie('bacterial_biofilm_details'),
                   model_uri=OUTCOMES_MODEL.bacterial_biofilm_details, domain=None, range=Optional[str])

slots.viral_infection_details = Slot(uri=OUTCOMES_MODEL.viral_infection_details, name="viral_infection_details", curie=OUTCOMES_MODEL.curie('viral_infection_details'),
                   model_uri=OUTCOMES_MODEL.viral_infection_details, domain=None, range=Optional[str])

slots.biofilm_clearance_rate = Slot(uri=OUTCOMES_MODEL.biofilm_clearance_rate, name="biofilm_clearance_rate", curie=OUTCOMES_MODEL.curie('biofilm_clearance_rate'),
                   model_uri=OUTCOMES_MODEL.biofilm_clearance_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bacterial_load = Slot(uri=OUTCOMES_MODEL.bacterial_load, name="bacterial_load", curie=OUTCOMES_MODEL.curie('bacterial_load'),
                   model_uri=OUTCOMES_MODEL.bacterial_load, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.viral_spread_rate = Slot(uri=OUTCOMES_MODEL.viral_spread_rate, name="viral_spread_rate", curie=OUTCOMES_MODEL.curie('viral_spread_rate'),
                   model_uri=OUTCOMES_MODEL.viral_spread_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.staining_protocol = Slot(uri=OUTCOMES_MODEL.staining_protocol, name="staining_protocol", curie=OUTCOMES_MODEL.curie('staining_protocol'),
                   model_uri=OUTCOMES_MODEL.staining_protocol, domain=None, range=Optional[Union[dict, StainingProtocol]])

slots.gene_expression_analysis = Slot(uri=OUTCOMES_MODEL.gene_expression_analysis, name="gene_expression_analysis", curie=OUTCOMES_MODEL.curie('gene_expression_analysis'),
                   model_uri=OUTCOMES_MODEL.gene_expression_analysis, domain=None, range=Optional[Union[dict, GeneExpressionAnalysis]])

slots.mucin_protein_concentration = Slot(uri=OUTCOMES_MODEL.mucin_protein_concentration, name="mucin_protein_concentration", curie=OUTCOMES_MODEL.curie('mucin_protein_concentration'),
                   model_uri=OUTCOMES_MODEL.mucin_protein_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.goblet_to_ciliated_ratio = Slot(uri=OUTCOMES_MODEL.goblet_to_ciliated_ratio, name="goblet_to_ciliated_ratio", curie=OUTCOMES_MODEL.curie('goblet_to_ciliated_ratio'),
                   model_uri=OUTCOMES_MODEL.goblet_to_ciliated_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pathway_enrichment_scores = Slot(uri=OUTCOMES_MODEL.pathway_enrichment_scores, name="pathway_enrichment_scores", curie=OUTCOMES_MODEL.curie('pathway_enrichment_scores'),
                   model_uri=OUTCOMES_MODEL.pathway_enrichment_scores, domain=None, range=Optional[Union[str, list[str]]])

slots.dose_response_data = Slot(uri=OUTCOMES_MODEL.dose_response_data, name="dose_response_data", curie=OUTCOMES_MODEL.curie('dose_response_data'),
                   model_uri=OUTCOMES_MODEL.dose_response_data, domain=None, range=Optional[str])

slots.cell_culture_details = Slot(uri=OUTCOMES_MODEL.cell_culture_details, name="cell_culture_details", curie=OUTCOMES_MODEL.curie('cell_culture_details'),
                   model_uri=OUTCOMES_MODEL.cell_culture_details, domain=None, range=Optional[Union[dict, CellCultureConditions]])

slots.ros_probe = Slot(uri=OUTCOMES_MODEL.ros_probe, name="ros_probe", curie=OUTCOMES_MODEL.curie('ros_probe'),
                   model_uri=OUTCOMES_MODEL.ros_probe, domain=None, range=Optional[Union[dict, ROSProbe]])

slots.detection_method_details = Slot(uri=OUTCOMES_MODEL.detection_method_details, name="detection_method_details", curie=OUTCOMES_MODEL.curie('detection_method_details'),
                   model_uri=OUTCOMES_MODEL.detection_method_details, domain=None, range=Optional[Union[dict[Union[str, DetectionMethodId], Union[dict, DetectionMethod]], list[Union[dict, DetectionMethod]]]])

slots.protein_oxidation_markers = Slot(uri=OUTCOMES_MODEL.protein_oxidation_markers, name="protein_oxidation_markers", curie=OUTCOMES_MODEL.curie('protein_oxidation_markers'),
                   model_uri=OUTCOMES_MODEL.protein_oxidation_markers, domain=None, range=Optional[Union[str, list[str]]])

slots.dna_damage_markers = Slot(uri=OUTCOMES_MODEL.dna_damage_markers, name="dna_damage_markers", curie=OUTCOMES_MODEL.curie('dna_damage_markers'),
                   model_uri=OUTCOMES_MODEL.dna_damage_markers, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.antioxidant_enzyme_activities = Slot(uri=OUTCOMES_MODEL.antioxidant_enzyme_activities, name="antioxidant_enzyme_activities", curie=OUTCOMES_MODEL.curie('antioxidant_enzyme_activities'),
                   model_uri=OUTCOMES_MODEL.antioxidant_enzyme_activities, domain=None, range=Optional[str])

slots.barrier_integrity = Slot(uri=OUTCOMES_MODEL.barrier_integrity, name="barrier_integrity", curie=OUTCOMES_MODEL.curie('barrier_integrity'),
                   model_uri=OUTCOMES_MODEL.barrier_integrity, domain=None, range=Optional[Union[dict, BarrierIntegrity]])

slots.cytotoxicity_metrics = Slot(uri=OUTCOMES_MODEL.cytotoxicity_metrics, name="cytotoxicity_metrics", curie=OUTCOMES_MODEL.curie('cytotoxicity_metrics'),
                   model_uri=OUTCOMES_MODEL.cytotoxicity_metrics, domain=None, range=Optional[Union[dict, CytotoxicityMetrics]])

slots.sample_collection_details = Slot(uri=OUTCOMES_MODEL.sample_collection_details, name="sample_collection_details", curie=OUTCOMES_MODEL.curie('sample_collection_details'),
                   model_uri=OUTCOMES_MODEL.sample_collection_details, domain=None, range=Optional[Union[dict, SampleCollection]])

slots.inflammatory_cell_profile = Slot(uri=OUTCOMES_MODEL.inflammatory_cell_profile, name="inflammatory_cell_profile", curie=OUTCOMES_MODEL.curie('inflammatory_cell_profile'),
                   model_uri=OUTCOMES_MODEL.inflammatory_cell_profile, domain=None, range=Optional[Union[dict, InflammatoryCellProfile]])

slots.microbiome_analysis = Slot(uri=OUTCOMES_MODEL.microbiome_analysis, name="microbiome_analysis", curie=OUTCOMES_MODEL.curie('microbiome_analysis'),
                   model_uri=OUTCOMES_MODEL.microbiome_analysis, domain=None, range=Optional[Union[dict, MicrobiomeAnalysis]])

slots.cytokine_levels = Slot(uri=OUTCOMES_MODEL.cytokine_levels, name="cytokine_levels", curie=OUTCOMES_MODEL.curie('cytokine_levels'),
                   model_uri=OUTCOMES_MODEL.cytokine_levels, domain=None, range=Optional[Union[str, list[str]]])

slots.protein_concentration = Slot(uri=OUTCOMES_MODEL.protein_concentration, name="protein_concentration", curie=OUTCOMES_MODEL.curie('protein_concentration'),
                   model_uri=OUTCOMES_MODEL.protein_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cell_free_dna = Slot(uri=OUTCOMES_MODEL.cell_free_dna, name="cell_free_dna", curie=OUTCOMES_MODEL.curie('cell_free_dna'),
                   model_uri=OUTCOMES_MODEL.cell_free_dna, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fev1 = Slot(uri=OUTCOMES_MODEL.fev1, name="fev1", curie=OUTCOMES_MODEL.curie('fev1'),
                   model_uri=OUTCOMES_MODEL.fev1, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fvc = Slot(uri=OUTCOMES_MODEL.fvc, name="fvc", curie=OUTCOMES_MODEL.curie('fvc'),
                   model_uri=OUTCOMES_MODEL.fvc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fev1_fvc_ratio = Slot(uri=OUTCOMES_MODEL.fev1_fvc_ratio, name="fev1_fvc_ratio", curie=OUTCOMES_MODEL.curie('fev1_fvc_ratio'),
                   model_uri=OUTCOMES_MODEL.fev1_fvc_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fef25_75 = Slot(uri=OUTCOMES_MODEL.fef25_75, name="fef25_75", curie=OUTCOMES_MODEL.curie('fef25_75'),
                   model_uri=OUTCOMES_MODEL.fef25_75, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bronchodilator_response = Slot(uri=OUTCOMES_MODEL.bronchodilator_response, name="bronchodilator_response", curie=OUTCOMES_MODEL.curie('bronchodilator_response'),
                   model_uri=OUTCOMES_MODEL.bronchodilator_response, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.decline_rate = Slot(uri=OUTCOMES_MODEL.decline_rate, name="decline_rate", curie=OUTCOMES_MODEL.curie('decline_rate'),
                   model_uri=OUTCOMES_MODEL.decline_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dlco = Slot(uri=OUTCOMES_MODEL.dlco, name="dlco", curie=OUTCOMES_MODEL.curie('dlco'),
                   model_uri=OUTCOMES_MODEL.dlco, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.feno = Slot(uri=OUTCOMES_MODEL.feno, name="feno", curie=OUTCOMES_MODEL.curie('feno'),
                   model_uri=OUTCOMES_MODEL.feno, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.egfr_phosphorylation = Slot(uri=OUTCOMES_MODEL.egfr_phosphorylation, name="egfr_phosphorylation", curie=OUTCOMES_MODEL.curie('egfr_phosphorylation'),
                   model_uri=OUTCOMES_MODEL.egfr_phosphorylation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.downstream_kinase_activation = Slot(uri=OUTCOMES_MODEL.downstream_kinase_activation, name="downstream_kinase_activation", curie=OUTCOMES_MODEL.curie('downstream_kinase_activation'),
                   model_uri=OUTCOMES_MODEL.downstream_kinase_activation, domain=None, range=Optional[str])

slots.ligand_expression_levels = Slot(uri=OUTCOMES_MODEL.ligand_expression_levels, name="ligand_expression_levels", curie=OUTCOMES_MODEL.curie('ligand_expression_levels'),
                   model_uri=OUTCOMES_MODEL.ligand_expression_levels, domain=None, range=Optional[Union[str, list[str]]])

slots.pathway_biomarkers = Slot(uri=OUTCOMES_MODEL.pathway_biomarkers, name="pathway_biomarkers", curie=OUTCOMES_MODEL.curie('pathway_biomarkers'),
                   model_uri=OUTCOMES_MODEL.pathway_biomarkers, domain=None, range=Optional[Union[str, list[str]]])

slots.mrna_level = Slot(uri=OUTCOMES_MODEL.mrna_level, name="mrna_level", curie=OUTCOMES_MODEL.curie('mrna_level'),
                   model_uri=OUTCOMES_MODEL.mrna_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.protein_level = Slot(uri=OUTCOMES_MODEL.protein_level, name="protein_level", curie=OUTCOMES_MODEL.curie('protein_level'),
                   model_uri=OUTCOMES_MODEL.protein_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.percentage_positive_cells = Slot(uri=OUTCOMES_MODEL.percentage_positive_cells, name="percentage_positive_cells", curie=OUTCOMES_MODEL.curie('percentage_positive_cells'),
                   model_uri=OUTCOMES_MODEL.percentage_positive_cells, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.frame_rate = Slot(uri=OUTCOMES_MODEL.frame_rate, name="frame_rate", curie=OUTCOMES_MODEL.curie('frame_rate'),
                   model_uri=OUTCOMES_MODEL.frame_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_duration = Slot(uri=OUTCOMES_MODEL.imaging_duration, name="imaging_duration", curie=OUTCOMES_MODEL.curie('imaging_duration'),
                   model_uri=OUTCOMES_MODEL.imaging_duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_intervals = Slot(uri=OUTCOMES_MODEL.imaging_intervals, name="imaging_intervals", curie=OUTCOMES_MODEL.curie('imaging_intervals'),
                   model_uri=OUTCOMES_MODEL.imaging_intervals, domain=None, range=Optional[str])

slots.spatial_resolution = Slot(uri=OUTCOMES_MODEL.spatial_resolution, name="spatial_resolution", curie=OUTCOMES_MODEL.curie('spatial_resolution'),
                   model_uri=OUTCOMES_MODEL.spatial_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.probe_positioning = Slot(uri=OUTCOMES_MODEL.probe_positioning, name="probe_positioning", curie=OUTCOMES_MODEL.curie('probe_positioning'),
                   model_uri=OUTCOMES_MODEL.probe_positioning, domain=None, range=Optional[str])

slots.fluorophore_type = Slot(uri=OUTCOMES_MODEL.fluorophore_type, name="fluorophore_type", curie=OUTCOMES_MODEL.curie('fluorophore_type'),
                   model_uri=OUTCOMES_MODEL.fluorophore_type, domain=None, range=Optional[str])

slots.concentration = Slot(uri=OUTCOMES_MODEL.concentration, name="concentration", curie=OUTCOMES_MODEL.curie('concentration'),
                   model_uri=OUTCOMES_MODEL.concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.wavelength = Slot(uri=OUTCOMES_MODEL.wavelength, name="wavelength", curie=OUTCOMES_MODEL.curie('wavelength'),
                   model_uri=OUTCOMES_MODEL.wavelength, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.control_method = Slot(uri=OUTCOMES_MODEL.control_method, name="control_method", curie=OUTCOMES_MODEL.curie('control_method'),
                   model_uri=OUTCOMES_MODEL.control_method, domain=None, range=Optional[str])

slots.material_used = Slot(uri=OUTCOMES_MODEL.material_used, name="material_used", curie=OUTCOMES_MODEL.curie('material_used'),
                   model_uri=OUTCOMES_MODEL.material_used, domain=None, range=Optional[str])

slots.probe_type = Slot(uri=OUTCOMES_MODEL.probe_type, name="probe_type", curie=OUTCOMES_MODEL.curie('probe_type'),
                   model_uri=OUTCOMES_MODEL.probe_type, domain=None, range=Optional[str])

slots.loading_conditions = Slot(uri=OUTCOMES_MODEL.loading_conditions, name="loading_conditions", curie=OUTCOMES_MODEL.curie('loading_conditions'),
                   model_uri=OUTCOMES_MODEL.loading_conditions, domain=None, range=Optional[str])

slots.detection_wavelength = Slot(uri=OUTCOMES_MODEL.detection_wavelength, name="detection_wavelength", curie=OUTCOMES_MODEL.curie('detection_wavelength'),
                   model_uri=OUTCOMES_MODEL.detection_wavelength, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.detection_type = Slot(uri=OUTCOMES_MODEL.detection_type, name="detection_type", curie=OUTCOMES_MODEL.curie('detection_type'),
                   model_uri=OUTCOMES_MODEL.detection_type, domain=None, range=Optional[str])

slots.sensitivity = Slot(uri=OUTCOMES_MODEL.sensitivity, name="sensitivity", curie=OUTCOMES_MODEL.curie('sensitivity'),
                   model_uri=OUTCOMES_MODEL.sensitivity, domain=None, range=Optional[str])

slots.technical_replicates = Slot(uri=OUTCOMES_MODEL.technical_replicates, name="technical_replicates", curie=OUTCOMES_MODEL.curie('technical_replicates'),
                   model_uri=OUTCOMES_MODEL.technical_replicates, domain=None, range=Optional[int])

slots.collection_method = Slot(uri=OUTCOMES_MODEL.collection_method, name="collection_method", curie=OUTCOMES_MODEL.curie('collection_method'),
                   model_uri=OUTCOMES_MODEL.collection_method, domain=None, range=Optional[str])

slots.processing_time = Slot(uri=OUTCOMES_MODEL.processing_time, name="processing_time", curie=OUTCOMES_MODEL.curie('processing_time'),
                   model_uri=OUTCOMES_MODEL.processing_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.storage_conditions = Slot(uri=OUTCOMES_MODEL.storage_conditions, name="storage_conditions", curie=OUTCOMES_MODEL.curie('storage_conditions'),
                   model_uri=OUTCOMES_MODEL.storage_conditions, domain=None, range=Optional[str])

slots.sample_volume = Slot(uri=OUTCOMES_MODEL.sample_volume, name="sample_volume", curie=OUTCOMES_MODEL.curie('sample_volume'),
                   model_uri=OUTCOMES_MODEL.sample_volume, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.culture_medium = Slot(uri=OUTCOMES_MODEL.culture_medium, name="culture_medium", curie=OUTCOMES_MODEL.curie('culture_medium'),
                   model_uri=OUTCOMES_MODEL.culture_medium, domain=None, range=Optional[str])

slots.days_at_ali = Slot(uri=OUTCOMES_MODEL.days_at_ali, name="days_at_ali", curie=OUTCOMES_MODEL.curie('days_at_ali'),
                   model_uri=OUTCOMES_MODEL.days_at_ali, domain=None, range=Optional[int])

slots.passage_number = Slot(uri=OUTCOMES_MODEL.passage_number, name="passage_number", curie=OUTCOMES_MODEL.curie('passage_number'),
                   model_uri=OUTCOMES_MODEL.passage_number, domain=None, range=Optional[int])

slots.substrate_type = Slot(uri=OUTCOMES_MODEL.substrate_type, name="substrate_type", curie=OUTCOMES_MODEL.curie('substrate_type'),
                   model_uri=OUTCOMES_MODEL.substrate_type, domain=None, range=Optional[str])

slots.temperature = Slot(uri=OUTCOMES_MODEL.temperature, name="temperature", curie=OUTCOMES_MODEL.curie('temperature'),
                   model_uri=OUTCOMES_MODEL.temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity = Slot(uri=OUTCOMES_MODEL.humidity, name="humidity", curie=OUTCOMES_MODEL.curie('humidity'),
                   model_uri=OUTCOMES_MODEL.humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.co2_percentage = Slot(uri=OUTCOMES_MODEL.co2_percentage, name="co2_percentage", curie=OUTCOMES_MODEL.curie('co2_percentage'),
                   model_uri=OUTCOMES_MODEL.co2_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.donor_count = Slot(uri=OUTCOMES_MODEL.donor_count, name="donor_count", curie=OUTCOMES_MODEL.curie('donor_count'),
                   model_uri=OUTCOMES_MODEL.donor_count, domain=None, range=Optional[int])

slots.replicates_per_donor = Slot(uri=OUTCOMES_MODEL.replicates_per_donor, name="replicates_per_donor", curie=OUTCOMES_MODEL.curie('replicates_per_donor'),
                   model_uri=OUTCOMES_MODEL.replicates_per_donor, domain=None, range=Optional[int])

slots.staining_type = Slot(uri=OUTCOMES_MODEL.staining_type, name="staining_type", curie=OUTCOMES_MODEL.curie('staining_type'),
                   model_uri=OUTCOMES_MODEL.staining_type, domain=None, range=Optional[str])

slots.antibodies_used = Slot(uri=OUTCOMES_MODEL.antibodies_used, name="antibodies_used", curie=OUTCOMES_MODEL.curie('antibodies_used'),
                   model_uri=OUTCOMES_MODEL.antibodies_used, domain=None, range=Optional[Union[str, list[str]]])

slots.fixation_method = Slot(uri=OUTCOMES_MODEL.fixation_method, name="fixation_method", curie=OUTCOMES_MODEL.curie('fixation_method'),
                   model_uri=OUTCOMES_MODEL.fixation_method, domain=None, range=Optional[str])

slots.incubation_conditions = Slot(uri=OUTCOMES_MODEL.incubation_conditions, name="incubation_conditions", curie=OUTCOMES_MODEL.curie('incubation_conditions'),
                   model_uri=OUTCOMES_MODEL.incubation_conditions, domain=None, range=Optional[str])

slots.analysis_method = Slot(uri=OUTCOMES_MODEL.analysis_method, name="analysis_method", curie=OUTCOMES_MODEL.curie('analysis_method'),
                   model_uri=OUTCOMES_MODEL.analysis_method, domain=None, range=Optional[str])

slots.normalization_genes = Slot(uri=OUTCOMES_MODEL.normalization_genes, name="normalization_genes", curie=OUTCOMES_MODEL.curie('normalization_genes'),
                   model_uri=OUTCOMES_MODEL.normalization_genes, domain=None, range=Optional[Union[str, list[str]]])

slots.primers_used = Slot(uri=OUTCOMES_MODEL.primers_used, name="primers_used", curie=OUTCOMES_MODEL.curie('primers_used'),
                   model_uri=OUTCOMES_MODEL.primers_used, domain=None, range=Optional[Union[str, list[str]]])

slots.sequencing_platform = Slot(uri=OUTCOMES_MODEL.sequencing_platform, name="sequencing_platform", curie=OUTCOMES_MODEL.curie('sequencing_platform'),
                   model_uri=OUTCOMES_MODEL.sequencing_platform, domain=None, range=Optional[str])

slots.sequencing_depth = Slot(uri=OUTCOMES_MODEL.sequencing_depth, name="sequencing_depth", curie=OUTCOMES_MODEL.curie('sequencing_depth'),
                   model_uri=OUTCOMES_MODEL.sequencing_depth, domain=None, range=Optional[int])

slots.neutrophil_percentage = Slot(uri=OUTCOMES_MODEL.neutrophil_percentage, name="neutrophil_percentage", curie=OUTCOMES_MODEL.curie('neutrophil_percentage'),
                   model_uri=OUTCOMES_MODEL.neutrophil_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.eosinophil_percentage = Slot(uri=OUTCOMES_MODEL.eosinophil_percentage, name="eosinophil_percentage", curie=OUTCOMES_MODEL.curie('eosinophil_percentage'),
                   model_uri=OUTCOMES_MODEL.eosinophil_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.macrophage_percentage = Slot(uri=OUTCOMES_MODEL.macrophage_percentage, name="macrophage_percentage", curie=OUTCOMES_MODEL.curie('macrophage_percentage'),
                   model_uri=OUTCOMES_MODEL.macrophage_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lymphocyte_percentage = Slot(uri=OUTCOMES_MODEL.lymphocyte_percentage, name="lymphocyte_percentage", curie=OUTCOMES_MODEL.curie('lymphocyte_percentage'),
                   model_uri=OUTCOMES_MODEL.lymphocyte_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_cell_count = Slot(uri=OUTCOMES_MODEL.total_cell_count, name="total_cell_count", curie=OUTCOMES_MODEL.curie('total_cell_count'),
                   model_uri=OUTCOMES_MODEL.total_cell_count, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.alpha_diversity = Slot(uri=OUTCOMES_MODEL.alpha_diversity, name="alpha_diversity", curie=OUTCOMES_MODEL.curie('alpha_diversity'),
                   model_uri=OUTCOMES_MODEL.alpha_diversity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.beta_diversity = Slot(uri=OUTCOMES_MODEL.beta_diversity, name="beta_diversity", curie=OUTCOMES_MODEL.curie('beta_diversity'),
                   model_uri=OUTCOMES_MODEL.beta_diversity, domain=None, range=Optional[str])

slots.taxonomic_abundance = Slot(uri=OUTCOMES_MODEL.taxonomic_abundance, name="taxonomic_abundance", curie=OUTCOMES_MODEL.curie('taxonomic_abundance'),
                   model_uri=OUTCOMES_MODEL.taxonomic_abundance, domain=None, range=Optional[Union[str, list[str]]])

slots.sequencing_primers = Slot(uri=OUTCOMES_MODEL.sequencing_primers, name="sequencing_primers", curie=OUTCOMES_MODEL.curie('sequencing_primers'),
                   model_uri=OUTCOMES_MODEL.sequencing_primers, domain=None, range=Optional[Union[str, list[str]]])

slots.dna_extraction_method = Slot(uri=OUTCOMES_MODEL.dna_extraction_method, name="dna_extraction_method", curie=OUTCOMES_MODEL.curie('dna_extraction_method'),
                   model_uri=OUTCOMES_MODEL.dna_extraction_method, domain=None, range=Optional[str])

slots.teer_value = Slot(uri=OUTCOMES_MODEL.teer_value, name="teer_value", curie=OUTCOMES_MODEL.curie('teer_value'),
                   model_uri=OUTCOMES_MODEL.teer_value, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.permeability_coefficient = Slot(uri=OUTCOMES_MODEL.permeability_coefficient, name="permeability_coefficient", curie=OUTCOMES_MODEL.curie('permeability_coefficient'),
                   model_uri=OUTCOMES_MODEL.permeability_coefficient, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.measurement_timepoint = Slot(uri=OUTCOMES_MODEL.measurement_timepoint, name="measurement_timepoint", curie=OUTCOMES_MODEL.curie('measurement_timepoint'),
                   model_uri=OUTCOMES_MODEL.measurement_timepoint, domain=None, range=Optional[str])

slots.ldh_release = Slot(uri=OUTCOMES_MODEL.ldh_release, name="ldh_release", curie=OUTCOMES_MODEL.curie('ldh_release'),
                   model_uri=OUTCOMES_MODEL.ldh_release, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mtt_reduction = Slot(uri=OUTCOMES_MODEL.mtt_reduction, name="mtt_reduction", curie=OUTCOMES_MODEL.curie('mtt_reduction'),
                   model_uri=OUTCOMES_MODEL.mtt_reduction, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.viability_percentage = Slot(uri=OUTCOMES_MODEL.viability_percentage, name="viability_percentage", curie=OUTCOMES_MODEL.curie('viability_percentage'),
                   model_uri=OUTCOMES_MODEL.viability_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.apoptosis_markers = Slot(uri=OUTCOMES_MODEL.apoptosis_markers, name="apoptosis_markers", curie=OUTCOMES_MODEL.curie('apoptosis_markers'),
                   model_uri=OUTCOMES_MODEL.apoptosis_markers, domain=None, range=Optional[Union[str, list[str]]])

slots.authors = Slot(uri=OUTCOMES_MODEL.authors, name="authors", curie=OUTCOMES_MODEL.curie('authors'),
                   model_uri=OUTCOMES_MODEL.authors, domain=None, range=Optional[Union[str, list[str]]])

slots.pages = Slot(uri=OUTCOMES_MODEL.pages, name="pages", curie=OUTCOMES_MODEL.curie('pages'),
                   model_uri=OUTCOMES_MODEL.pages, domain=None, range=Optional[str])

slots.summary = Slot(uri=OUTCOMES_MODEL.summary, name="summary", curie=OUTCOMES_MODEL.curie('summary'),
                   model_uri=OUTCOMES_MODEL.summary, domain=None, range=Optional[str])

slots.keywords = Slot(uri=OUTCOMES_MODEL.keywords, name="keywords", curie=OUTCOMES_MODEL.curie('keywords'),
                   model_uri=OUTCOMES_MODEL.keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.mesh_terms = Slot(uri=OUTCOMES_MODEL.mesh_terms, name="mesh_terms", curie=OUTCOMES_MODEL.curie('mesh_terms'),
                   model_uri=OUTCOMES_MODEL.mesh_terms, domain=None, range=Optional[Union[str, list[str]]])

slots.publication_type = Slot(uri=OUTCOMES_MODEL.publication_type, name="publication_type", curie=OUTCOMES_MODEL.curie('publication_type'),
                   model_uri=OUTCOMES_MODEL.publication_type, domain=None, range=Optional[str])

slots.xref = Slot(uri=OUTCOMES_MODEL.xref, name="xref", curie=OUTCOMES_MODEL.curie('xref'),
                   model_uri=OUTCOMES_MODEL.xref, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Publication_id = Slot(uri=OUTCOMES_MODEL.id, name="Publication_id", curie=OUTCOMES_MODEL.curie('id'),
                   model_uri=OUTCOMES_MODEL.Publication_id, domain=Publication, range=Union[str, PublicationId])
