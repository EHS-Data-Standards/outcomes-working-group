# Auto generated from outcomes_working_group.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-11T18:15:33
# Schema: aop-model
#
# id: https://w3id.org/EHS-Data-Standards/aop-model
# description: A LinkML data model for representing Adverse Outcome Pathways (AOPs),
#   Key Events (KEs), and Key Event Relationships (KERs) in the context of
#   the Source-to-Outcome (S2O) continuum.
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

from linkml_runtime.linkml_model.types import Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
AOP_MODEL = CurieNamespace('aop_model', 'https://w3id.org/EHS-Data-Standards/aop-model/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = AOP_MODEL


# Types

# Class references
class NamedEntityId(URIorCURIE):
    pass


class AdverseOutcomePathwayId(NamedEntityId):
    pass


class KeyEventId(NamedEntityId):
    pass


class OxidativeStressEventId(KeyEventId):
    pass


class EGFRActivationEventId(KeyEventId):
    pass


class CFTRFunctionEventId(KeyEventId):
    pass


class FoxJ1ExpressionEventId(KeyEventId):
    pass


class CiliaNumberEventId(KeyEventId):
    pass


class GobletCellEventId(KeyEventId):
    pass


class ASLHeightEventId(KeyEventId):
    pass


class CiliaryBeatFrequencyEventId(KeyEventId):
    pass


class MucinProductionEventId(KeyEventId):
    pass


class MucociliaryClearanceEventId(KeyEventId):
    pass


class LungFunctionEventId(KeyEventId):
    pass


class AssociationId(NamedEntityId):
    pass


class KeyEventAssociationId(AssociationId):
    pass


class MeasurementProcessId(NamedEntityId):
    pass


class InputSampleId(NamedEntityId):
    pass


class AssayId(NamedEntityId):
    pass


class OutputMeasurementId(NamedEntityId):
    pass


class ContextFieldId(NamedEntityId):
    pass


class CFTRFunctionMeasurementId(MeasurementProcessId):
    pass


class CiliaBeatFrequencyMeasurementId(MeasurementProcessId):
    pass


class ASLHeightMeasurementId(MeasurementProcessId):
    pass


class MucociliaryClearanceMeasurementId(MeasurementProcessId):
    pass


class GobletCellMeasurementId(MeasurementProcessId):
    pass


class OxidativeStressMeasurementId(MeasurementProcessId):
    pass


class ScientificEvidenceId(NamedEntityId):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Base class for all named entities in the model
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["NamedEntity"]
    class_class_curie: ClassVar[str] = "aop_model:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseOutcomePathway(NamedEntity):
    """
    A structured representation of biological events linking a molecular initiating event (MIE)
    to an adverse outcome through a series of key events.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["AdverseOutcomePathway"]
    class_class_curie: ClassVar[str] = "aop_model:AdverseOutcomePathway"
    class_name: ClassVar[str] = "AdverseOutcomePathway"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.AdverseOutcomePathway

    id: Union[str, AdverseOutcomePathwayId] = None
    adverse_outcome: Union[str, KeyEventId] = None
    molecular_initiating_events: Optional[Union[dict[Union[str, KeyEventId], Union[dict, "KeyEvent"]], list[Union[dict, "KeyEvent"]]]] = empty_dict()
    key_events: Optional[Union[dict[Union[str, KeyEventId], Union[dict, "KeyEvent"]], list[Union[dict, "KeyEvent"]]]] = empty_dict()
    key_event_relationships: Optional[Union[dict[Union[str, KeyEventAssociationId], Union[dict, "KeyEventAssociation"]], list[Union[dict, "KeyEventAssociation"]]]] = empty_dict()
    aop_network_members: Optional[Union[Union[str, AdverseOutcomePathwayId], list[Union[str, AdverseOutcomePathwayId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseOutcomePathwayId):
            self.id = AdverseOutcomePathwayId(self.id)

        if self._is_empty(self.adverse_outcome):
            self.MissingRequiredField("adverse_outcome")
        if not isinstance(self.adverse_outcome, KeyEventId):
            self.adverse_outcome = KeyEventId(self.adverse_outcome)

        self._normalize_inlined_as_dict(slot_name="molecular_initiating_events", slot_type=KeyEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="key_events", slot_type=KeyEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="key_event_relationships", slot_type=KeyEventAssociation, key_name="id", keyed=True)

        if not isinstance(self.aop_network_members, list):
            self.aop_network_members = [self.aop_network_members] if self.aop_network_members is not None else []
        self.aop_network_members = [v if isinstance(v, AdverseOutcomePathwayId) else AdverseOutcomePathwayId(v) for v in self.aop_network_members]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEvent(NamedEntity):
    """
    A measurable change in biological state that is a necessary step in a pathway from
    a molecular initiating event to an adverse outcome. Key Events can represent molecular,
    cellular, tissue, organ, or organism-level changes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["KeyEvent"]
    class_class_curie: ClassVar[str] = "aop_model:KeyEvent"
    class_name: ClassVar[str] = "KeyEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.KeyEvent

    id: Union[str, KeyEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None
    direction_of_change: Optional[Union[str, "DirectionEnum"]] = None
    measurement_processes: Optional[Union[dict[Union[str, MeasurementProcessId], Union[dict, "MeasurementProcess"]], list[Union[dict, "MeasurementProcess"]]]] = empty_dict()
    biomarkers: Optional[Union[str, list[str]]] = empty_list()
    upstream_events: Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]] = empty_list()
    downstream_events: Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.event_type):
            self.MissingRequiredField("event_type")
        if not isinstance(self.event_type, KeyEventTypeEnum):
            self.event_type = KeyEventTypeEnum(self.event_type)

        if self._is_empty(self.biological_level):
            self.MissingRequiredField("biological_level")
        if not isinstance(self.biological_level, BiologicalLevelEnum):
            self.biological_level = BiologicalLevelEnum(self.biological_level)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventId):
            self.id = KeyEventId(self.id)

        if self.direction_of_change is not None and not isinstance(self.direction_of_change, DirectionEnum):
            self.direction_of_change = DirectionEnum(self.direction_of_change)

        self._normalize_inlined_as_dict(slot_name="measurement_processes", slot_type=MeasurementProcess, key_name="id", keyed=True)

        if not isinstance(self.biomarkers, list):
            self.biomarkers = [self.biomarkers] if self.biomarkers is not None else []
        self.biomarkers = [v if isinstance(v, str) else str(v) for v in self.biomarkers]

        if not isinstance(self.upstream_events, list):
            self.upstream_events = [self.upstream_events] if self.upstream_events is not None else []
        self.upstream_events = [v if isinstance(v, KeyEventId) else KeyEventId(v) for v in self.upstream_events]

        if not isinstance(self.downstream_events, list):
            self.downstream_events = [self.downstream_events] if self.downstream_events is not None else []
        self.downstream_events = [v if isinstance(v, KeyEventId) else KeyEventId(v) for v in self.downstream_events]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OxidativeStressEvent(KeyEvent):
    """
    Molecular initiating event involving oxidative stress
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["OxidativeStressEvent"]
    class_class_curie: ClassVar[str] = "aop_model:OxidativeStressEvent"
    class_name: ClassVar[str] = "OxidativeStressEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.OxidativeStressEvent

    id: Union[str, OxidativeStressEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OxidativeStressEventId):
            self.id = OxidativeStressEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EGFRActivationEvent(KeyEvent):
    """
    Molecular initiating event involving EGFR activation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["EGFRActivationEvent"]
    class_class_curie: ClassVar[str] = "aop_model:EGFRActivationEvent"
    class_name: ClassVar[str] = "EGFRActivationEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.EGFRActivationEvent

    id: Union[str, EGFRActivationEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EGFRActivationEventId):
            self.id = EGFRActivationEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CFTRFunctionEvent(KeyEvent):
    """
    Key event representing changes in CFTR function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["CFTRFunctionEvent"]
    class_class_curie: ClassVar[str] = "aop_model:CFTRFunctionEvent"
    class_name: ClassVar[str] = "CFTRFunctionEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.CFTRFunctionEvent

    id: Union[str, CFTRFunctionEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CFTRFunctionEventId):
            self.id = CFTRFunctionEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FoxJ1ExpressionEvent(KeyEvent):
    """
    Key event representing changes in FoxJ1 expression
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["FoxJ1ExpressionEvent"]
    class_class_curie: ClassVar[str] = "aop_model:FoxJ1ExpressionEvent"
    class_name: ClassVar[str] = "FoxJ1ExpressionEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.FoxJ1ExpressionEvent

    id: Union[str, FoxJ1ExpressionEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoxJ1ExpressionEventId):
            self.id = FoxJ1ExpressionEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CiliaNumberEvent(KeyEvent):
    """
    Key event representing changes in cilia number or length
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["CiliaNumberEvent"]
    class_class_curie: ClassVar[str] = "aop_model:CiliaNumberEvent"
    class_name: ClassVar[str] = "CiliaNumberEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.CiliaNumberEvent

    id: Union[str, CiliaNumberEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CiliaNumberEventId):
            self.id = CiliaNumberEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GobletCellEvent(KeyEvent):
    """
    Key event representing changes in goblet cell number
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["GobletCellEvent"]
    class_class_curie: ClassVar[str] = "aop_model:GobletCellEvent"
    class_name: ClassVar[str] = "GobletCellEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.GobletCellEvent

    id: Union[str, GobletCellEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GobletCellEventId):
            self.id = GobletCellEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ASLHeightEvent(KeyEvent):
    """
    Key event representing changes in airway surface liquid height
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["ASLHeightEvent"]
    class_class_curie: ClassVar[str] = "aop_model:ASLHeightEvent"
    class_name: ClassVar[str] = "ASLHeightEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.ASLHeightEvent

    id: Union[str, ASLHeightEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ASLHeightEventId):
            self.id = ASLHeightEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CiliaryBeatFrequencyEvent(KeyEvent):
    """
    Key event representing changes in ciliary beat frequency
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["CiliaryBeatFrequencyEvent"]
    class_class_curie: ClassVar[str] = "aop_model:CiliaryBeatFrequencyEvent"
    class_name: ClassVar[str] = "CiliaryBeatFrequencyEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.CiliaryBeatFrequencyEvent

    id: Union[str, CiliaryBeatFrequencyEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CiliaryBeatFrequencyEventId):
            self.id = CiliaryBeatFrequencyEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MucinProductionEvent(KeyEvent):
    """
    Key event representing changes in mucin production
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["MucinProductionEvent"]
    class_class_curie: ClassVar[str] = "aop_model:MucinProductionEvent"
    class_name: ClassVar[str] = "MucinProductionEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.MucinProductionEvent

    id: Union[str, MucinProductionEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MucinProductionEventId):
            self.id = MucinProductionEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MucociliaryClearanceEvent(KeyEvent):
    """
    Key event representing changes in mucociliary clearance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["MucociliaryClearanceEvent"]
    class_class_curie: ClassVar[str] = "aop_model:MucociliaryClearanceEvent"
    class_name: ClassVar[str] = "MucociliaryClearanceEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.MucociliaryClearanceEvent

    id: Union[str, MucociliaryClearanceEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MucociliaryClearanceEventId):
            self.id = MucociliaryClearanceEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LungFunctionEvent(KeyEvent):
    """
    Adverse outcome representing decreased lung function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["LungFunctionEvent"]
    class_class_curie: ClassVar[str] = "aop_model:LungFunctionEvent"
    class_name: ClassVar[str] = "LungFunctionEvent"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.LungFunctionEvent

    id: Union[str, LungFunctionEventId] = None
    event_type: Union[str, "KeyEventTypeEnum"] = None
    biological_level: Union[str, "BiologicalLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LungFunctionEventId):
            self.id = LungFunctionEventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Association(NamedEntity):
    """
    Base class for associations/relationships in the model.
    Uses subject-predicate-object pattern similar to Biolink model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["Association"]
    class_class_curie: ClassVar[str] = "aop_model:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.Association

    id: Union[str, AssociationId] = None
    subject: Optional[Union[str, KeyEventId]] = None
    predicate: Optional[Union[str, URIorCURIE]] = None
    object: Optional[Union[str, KeyEventId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, KeyEventId):
            self.subject = KeyEventId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, URIorCURIE):
            self.predicate = URIorCURIE(self.predicate)

        if self.object is not None and not isinstance(self.object, KeyEventId):
            self.object = KeyEventId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEventAssociation(Association):
    """
    A causal or associative relationship between two key events in an adverse outcome pathway.
    Represents the connection showing how one event leads to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["KeyEventAssociation"]
    class_class_curie: ClassVar[str] = "aop_model:KeyEventAssociation"
    class_name: ClassVar[str] = "KeyEventAssociation"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.KeyEventAssociation

    id: Union[str, KeyEventAssociationId] = None
    subject: Union[str, KeyEventId] = None
    predicate: Union[str, "KeyEventPredicateEnum"] = None
    object: Union[str, KeyEventId] = None
    evidence_strength: Optional[Union[str, "EvidenceStrengthEnum"]] = None
    supporting_evidence: Optional[Union[dict[Union[str, ScientificEvidenceId], Union[dict, "ScientificEvidence"]], list[Union[dict, "ScientificEvidence"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventAssociationId):
            self.id = KeyEventAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, KeyEventId):
            self.subject = KeyEventId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, KeyEventPredicateEnum):
            self.predicate = KeyEventPredicateEnum(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, KeyEventId):
            self.object = KeyEventId(self.object)

        if self.evidence_strength is not None and not isinstance(self.evidence_strength, EvidenceStrengthEnum):
            self.evidence_strength = EvidenceStrengthEnum(self.evidence_strength)

        self._normalize_inlined_as_dict(slot_name="supporting_evidence", slot_type=ScientificEvidence, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasurementProcess(NamedEntity):
    """
    A generic class representing the process of measuring a biological key event.
    Includes information about input samples, methods, outputs, and contextual metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["MeasurementProcess"]
    class_class_curie: ClassVar[str] = "aop_model:MeasurementProcess"
    class_name: ClassVar[str] = "MeasurementProcess"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.MeasurementProcess

    id: Union[str, MeasurementProcessId] = None
    input_sample: Optional[Union[str, InputSampleId]] = None
    method_assay: Optional[Union[str, AssayId]] = None
    output_measurement: Optional[Union[str, OutputMeasurementId]] = None
    context_fields: Optional[Union[dict[Union[str, ContextFieldId], Union[dict, "ContextField"]], list[Union[dict, "ContextField"]]]] = empty_dict()
    protocol_notes: Optional[str] = None
    ontology_mappings: Optional[Union[str, list[str]]] = empty_list()
    exemplar_manuscripts: Optional[Union[dict[Union[str, ScientificEvidenceId], Union[dict, "ScientificEvidence"]], list[Union[dict, "ScientificEvidence"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementProcessId):
            self.id = MeasurementProcessId(self.id)

        if self.input_sample is not None and not isinstance(self.input_sample, InputSampleId):
            self.input_sample = InputSampleId(self.input_sample)

        if self.method_assay is not None and not isinstance(self.method_assay, AssayId):
            self.method_assay = AssayId(self.method_assay)

        if self.output_measurement is not None and not isinstance(self.output_measurement, OutputMeasurementId):
            self.output_measurement = OutputMeasurementId(self.output_measurement)

        self._normalize_inlined_as_dict(slot_name="context_fields", slot_type=ContextField, key_name="id", keyed=True)

        if self.protocol_notes is not None and not isinstance(self.protocol_notes, str):
            self.protocol_notes = str(self.protocol_notes)

        if not isinstance(self.ontology_mappings, list):
            self.ontology_mappings = [self.ontology_mappings] if self.ontology_mappings is not None else []
        self.ontology_mappings = [v if isinstance(v, str) else str(v) for v in self.ontology_mappings]

        self._normalize_inlined_as_dict(slot_name="exemplar_manuscripts", slot_type=ScientificEvidence, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InputSample(NamedEntity):
    """
    Description of the biological sample or experimental manipulation used as input
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["InputSample"]
    class_class_curie: ClassVar[str] = "aop_model:InputSample"
    class_name: ClassVar[str] = "InputSample"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.InputSample

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
    The specific method or assay used to measure a key event
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["Assay"]
    class_class_curie: ClassVar[str] = "aop_model:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.Assay

    id: Union[str, AssayId] = None
    assay_type: Optional[Union[str, "AssayTypeEnum"]] = None
    instrumentation: Optional[str] = None
    environmental_conditions: Optional[str] = None
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

        if self.environmental_conditions is not None and not isinstance(self.environmental_conditions, str):
            self.environmental_conditions = str(self.environmental_conditions)

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

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["QuantityValue"]
    class_class_curie: ClassVar[str] = "aop_model:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.QuantityValue

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
class OutputMeasurement(NamedEntity):
    """
    The quantitative or qualitative output from a measurement process
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["OutputMeasurement"]
    class_class_curie: ClassVar[str] = "aop_model:OutputMeasurement"
    class_name: ClassVar[str] = "OutputMeasurement"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.OutputMeasurement

    id: Union[str, OutputMeasurementId] = None
    measurement_type: Optional[str] = None
    has_quantity_value: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OutputMeasurementId):
            self.id = OutputMeasurementId(self.id)

        if self.measurement_type is not None and not isinstance(self.measurement_type, str):
            self.measurement_type = str(self.measurement_type)

        if self.has_quantity_value is not None and not isinstance(self.has_quantity_value, QuantityValue):
            self.has_quantity_value = QuantityValue(**as_dict(self.has_quantity_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContextField(NamedEntity):
    """
    Metadata fields that capture important contextual information for reproducibility
    and cross-study comparison
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["ContextField"]
    class_class_curie: ClassVar[str] = "aop_model:ContextField"
    class_name: ClassVar[str] = "ContextField"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.ContextField

    id: Union[str, ContextFieldId] = None
    field_name: Optional[str] = None
    field_value: Optional[str] = None
    field_category: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContextFieldId):
            self.id = ContextFieldId(self.id)

        if self.field_name is not None and not isinstance(self.field_name, str):
            self.field_name = str(self.field_name)

        if self.field_value is not None and not isinstance(self.field_value, str):
            self.field_value = str(self.field_value)

        if self.field_category is not None and not isinstance(self.field_category, str):
            self.field_category = str(self.field_category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CFTRFunctionMeasurement(MeasurementProcess):
    """
    Measurement of CFTR-mediated ion transport function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["CFTRFunctionMeasurement"]
    class_class_curie: ClassVar[str] = "aop_model:CFTRFunctionMeasurement"
    class_name: ClassVar[str] = "CFTRFunctionMeasurement"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.CFTRFunctionMeasurement

    id: Union[str, CFTRFunctionMeasurementId] = None
    cftr_specific_current: Optional[Union[dict, QuantityValue]] = None
    inhibitor_sensitive_current: Optional[Union[dict, QuantityValue]] = None
    cell_culture_conditions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CFTRFunctionMeasurementId):
            self.id = CFTRFunctionMeasurementId(self.id)

        if self.cftr_specific_current is not None and not isinstance(self.cftr_specific_current, QuantityValue):
            self.cftr_specific_current = QuantityValue(**as_dict(self.cftr_specific_current))

        if self.inhibitor_sensitive_current is not None and not isinstance(self.inhibitor_sensitive_current, QuantityValue):
            self.inhibitor_sensitive_current = QuantityValue(**as_dict(self.inhibitor_sensitive_current))

        if self.cell_culture_conditions is not None and not isinstance(self.cell_culture_conditions, str):
            self.cell_culture_conditions = str(self.cell_culture_conditions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CiliaBeatFrequencyMeasurement(MeasurementProcess):
    """
    Measurement of ciliary beat frequency
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["CiliaBeatFrequencyMeasurement"]
    class_class_curie: ClassVar[str] = "aop_model:CiliaBeatFrequencyMeasurement"
    class_name: ClassVar[str] = "CiliaBeatFrequencyMeasurement"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.CiliaBeatFrequencyMeasurement

    id: Union[str, CiliaBeatFrequencyMeasurementId] = None
    beat_frequency_hz: Optional[Union[dict, QuantityValue]] = None
    active_area_percentage: Optional[Union[dict, QuantityValue]] = None
    imaging_conditions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CiliaBeatFrequencyMeasurementId):
            self.id = CiliaBeatFrequencyMeasurementId(self.id)

        if self.beat_frequency_hz is not None and not isinstance(self.beat_frequency_hz, QuantityValue):
            self.beat_frequency_hz = QuantityValue(**as_dict(self.beat_frequency_hz))

        if self.active_area_percentage is not None and not isinstance(self.active_area_percentage, QuantityValue):
            self.active_area_percentage = QuantityValue(**as_dict(self.active_area_percentage))

        if self.imaging_conditions is not None and not isinstance(self.imaging_conditions, str):
            self.imaging_conditions = str(self.imaging_conditions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ASLHeightMeasurement(MeasurementProcess):
    """
    Measurement of airway surface liquid height
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["ASLHeightMeasurement"]
    class_class_curie: ClassVar[str] = "aop_model:ASLHeightMeasurement"
    class_name: ClassVar[str] = "ASLHeightMeasurement"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.ASLHeightMeasurement

    id: Union[str, ASLHeightMeasurementId] = None
    asl_height_um: Optional[Union[dict, QuantityValue]] = None
    periciliary_layer_depth: Optional[Union[dict, QuantityValue]] = None
    imaging_modality: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ASLHeightMeasurementId):
            self.id = ASLHeightMeasurementId(self.id)

        if self.asl_height_um is not None and not isinstance(self.asl_height_um, QuantityValue):
            self.asl_height_um = QuantityValue(**as_dict(self.asl_height_um))

        if self.periciliary_layer_depth is not None and not isinstance(self.periciliary_layer_depth, QuantityValue):
            self.periciliary_layer_depth = QuantityValue(**as_dict(self.periciliary_layer_depth))

        if self.imaging_modality is not None and not isinstance(self.imaging_modality, str):
            self.imaging_modality = str(self.imaging_modality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MucociliaryClearanceMeasurement(MeasurementProcess):
    """
    Measurement of mucociliary clearance/transport
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["MucociliaryClearanceMeasurement"]
    class_class_curie: ClassVar[str] = "aop_model:MucociliaryClearanceMeasurement"
    class_name: ClassVar[str] = "MucociliaryClearanceMeasurement"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.MucociliaryClearanceMeasurement

    id: Union[str, MucociliaryClearanceMeasurementId] = None
    transport_rate: Optional[Union[dict, QuantityValue]] = None
    directionality: Optional[str] = None
    particle_tracking_method: Optional[str] = None

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GobletCellMeasurement(MeasurementProcess):
    """
    Measurement of goblet cell number or mucin production
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["GobletCellMeasurement"]
    class_class_curie: ClassVar[str] = "aop_model:GobletCellMeasurement"
    class_name: ClassVar[str] = "GobletCellMeasurement"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.GobletCellMeasurement

    id: Union[str, GobletCellMeasurementId] = None
    goblet_cell_count: Optional[Union[dict, QuantityValue]] = None
    mucin_expression_level: Optional[Union[dict, QuantityValue]] = None
    staining_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GobletCellMeasurementId):
            self.id = GobletCellMeasurementId(self.id)

        if self.goblet_cell_count is not None and not isinstance(self.goblet_cell_count, QuantityValue):
            self.goblet_cell_count = QuantityValue(**as_dict(self.goblet_cell_count))

        if self.mucin_expression_level is not None and not isinstance(self.mucin_expression_level, QuantityValue):
            self.mucin_expression_level = QuantityValue(**as_dict(self.mucin_expression_level))

        if self.staining_method is not None and not isinstance(self.staining_method, str):
            self.staining_method = str(self.staining_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OxidativeStressMeasurement(MeasurementProcess):
    """
    Measurement of oxidative stress markers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["OxidativeStressMeasurement"]
    class_class_curie: ClassVar[str] = "aop_model:OxidativeStressMeasurement"
    class_name: ClassVar[str] = "OxidativeStressMeasurement"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.OxidativeStressMeasurement

    id: Union[str, OxidativeStressMeasurementId] = None
    ros_level: Optional[Union[dict, QuantityValue]] = None
    lipid_peroxidation: Optional[Union[dict, QuantityValue]] = None
    antioxidant_capacity: Optional[Union[dict, QuantityValue]] = None

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScientificEvidence(NamedEntity):
    """
    Published scientific evidence supporting an AOP component
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_MODEL["ScientificEvidence"]
    class_class_curie: ClassVar[str] = "aop_model:ScientificEvidence"
    class_name: ClassVar[str] = "ScientificEvidence"
    class_model_uri: ClassVar[URIRef] = AOP_MODEL.ScientificEvidence

    id: Union[str, ScientificEvidenceId] = None
    publication_reference: Optional[str] = None
    evidence_type: Optional[str] = None
    study_design: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificEvidenceId):
            self.id = ScientificEvidenceId(self.id)

        if self.publication_reference is not None and not isinstance(self.publication_reference, str):
            self.publication_reference = str(self.publication_reference)

        if self.evidence_type is not None and not isinstance(self.evidence_type, str):
            self.evidence_type = str(self.evidence_type)

        if self.study_design is not None and not isinstance(self.study_design, str):
            self.study_design = str(self.study_design)

        super().__post_init__(**kwargs)


# Enumerations
class BiologicalLevelEnum(EnumDefinitionImpl):
    """
    The level of biological organization at which an event occurs
    """
    MOLECULAR = PermissibleValue(
        text="MOLECULAR",
        description="Macro-molecular interactions (e.g., receptor binding, protein modification)")
    CELLULAR = PermissibleValue(
        text="CELLULAR",
        description="Cellular response (e.g., cell signaling, gene expression, cell death)")
    TISSUE = PermissibleValue(
        text="TISSUE",
        description="Tissue-level response (e.g., inflammation, tissue damage)")
    ORGAN = PermissibleValue(
        text="ORGAN",
        description="Organ-level response (e.g., impaired organ function)")
    ORGANISM = PermissibleValue(
        text="ORGANISM",
        description="Organism-level outcome (e.g., disease, mortality)")
    POPULATION = PermissibleValue(
        text="POPULATION",
        description="Population-level outcome (e.g., disease incidence, public health impact)")

    _defn = EnumDefinition(
        name="BiologicalLevelEnum",
        description="The level of biological organization at which an event occurs",
    )

class KeyEventTypeEnum(EnumDefinitionImpl):
    """
    Classification of key events in an AOP
    """
    MIE = PermissibleValue(
        text="MIE",
        description="""Molecular Initiating Event - the initial interaction between a stressor and a biological target""")
    KE = PermissibleValue(
        text="KE",
        description="Key Event - a measurable change in biological state along the pathway")
    AO = PermissibleValue(
        text="AO",
        description="Adverse Outcome - the endpoint of regulatory concern")

    _defn = EnumDefinition(
        name="KeyEventTypeEnum",
        description="Classification of key events in an AOP",
    )

class DirectionEnum(EnumDefinitionImpl):
    """
    Direction of change for a key event
    """
    INCREASED = PermissibleValue(
        text="INCREASED",
        description="The measured parameter is increased")
    DECREASED = PermissibleValue(
        text="DECREASED",
        description="The measured parameter is decreased")
    ALTERED = PermissibleValue(
        text="ALTERED",
        description="The measured parameter is changed in either direction")

    _defn = EnumDefinition(
        name="DirectionEnum",
        description="Direction of change for a key event",
    )

class EvidenceStrengthEnum(EnumDefinitionImpl):
    """
    Strength of evidence supporting a relationship
    """
    STRONG = PermissibleValue(
        text="STRONG",
        description="Strong empirical evidence from multiple independent studies")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Moderate evidence with some consistency")
    WEAK = PermissibleValue(
        text="WEAK",
        description="Limited or inconsistent evidence")
    NOT_SPECIFIED = PermissibleValue(
        text="NOT_SPECIFIED",
        description="Evidence strength not specified")

    _defn = EnumDefinition(
        name="EvidenceStrengthEnum",
        description="Strength of evidence supporting a relationship",
    )

class KeyEventPredicateEnum(EnumDefinitionImpl):
    """
    Types of relationships between key events in an AOP
    """
    has_input = PermissibleValue(
        text="has_input",
        description="The subject key event has the object key event as input",
        meaning=BIOLINK["has_input"])
    has_output = PermissibleValue(
        text="has_output",
        description="The subject key event has the object key event as output",
        meaning=BIOLINK["has_output"])
    leads_to = PermissibleValue(
        text="leads_to",
        description="The subject key event leads to the object key event",
        meaning=BIOLINK["causes"])
    regulates = PermissibleValue(
        text="regulates",
        description="The subject key event regulates the object key event",
        meaning=BIOLINK["regulates"])
    positively_regulates = PermissibleValue(
        text="positively_regulates",
        description="The subject key event positively regulates the object key event",
        meaning=BIOLINK["positively_regulates"])
    negatively_regulates = PermissibleValue(
        text="negatively_regulates",
        description="The subject key event negatively regulates the object key event",
        meaning=BIOLINK["negatively_regulates"])
    causes = PermissibleValue(
        text="causes",
        description="The subject key event directly causes the object key event",
        meaning=BIOLINK["causes"])
    contributes_to = PermissibleValue(
        text="contributes_to",
        description="The subject key event contributes to the object key event",
        meaning=BIOLINK["contributes_to"])

    _defn = EnumDefinition(
        name="KeyEventPredicateEnum",
        description="Types of relationships between key events in an AOP",
    )

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

slots.id = Slot(uri=AOP_MODEL.id, name="id", curie=AOP_MODEL.curie('id'),
                   model_uri=AOP_MODEL.id, domain=None, range=URIRef)

slots.name = Slot(uri=AOP_MODEL.name, name="name", curie=AOP_MODEL.curie('name'),
                   model_uri=AOP_MODEL.name, domain=None, range=Optional[str])

slots.description = Slot(uri=AOP_MODEL.description, name="description", curie=AOP_MODEL.curie('description'),
                   model_uri=AOP_MODEL.description, domain=None, range=Optional[str])

slots.molecular_initiating_events = Slot(uri=AOP_MODEL.molecular_initiating_events, name="molecular_initiating_events", curie=AOP_MODEL.curie('molecular_initiating_events'),
                   model_uri=AOP_MODEL.molecular_initiating_events, domain=None, range=Optional[Union[dict[Union[str, KeyEventId], Union[dict, KeyEvent]], list[Union[dict, KeyEvent]]]])

slots.key_events = Slot(uri=AOP_MODEL.key_events, name="key_events", curie=AOP_MODEL.curie('key_events'),
                   model_uri=AOP_MODEL.key_events, domain=None, range=Optional[Union[dict[Union[str, KeyEventId], Union[dict, KeyEvent]], list[Union[dict, KeyEvent]]]])

slots.adverse_outcome = Slot(uri=AOP_MODEL.adverse_outcome, name="adverse_outcome", curie=AOP_MODEL.curie('adverse_outcome'),
                   model_uri=AOP_MODEL.adverse_outcome, domain=None, range=Union[str, KeyEventId])

slots.key_event_relationships = Slot(uri=AOP_MODEL.key_event_relationships, name="key_event_relationships", curie=AOP_MODEL.curie('key_event_relationships'),
                   model_uri=AOP_MODEL.key_event_relationships, domain=None, range=Optional[Union[dict[Union[str, KeyEventAssociationId], Union[dict, KeyEventAssociation]], list[Union[dict, KeyEventAssociation]]]])

slots.aop_network_members = Slot(uri=AOP_MODEL.aop_network_members, name="aop_network_members", curie=AOP_MODEL.curie('aop_network_members'),
                   model_uri=AOP_MODEL.aop_network_members, domain=None, range=Optional[Union[Union[str, AdverseOutcomePathwayId], list[Union[str, AdverseOutcomePathwayId]]]])

slots.event_type = Slot(uri=AOP_MODEL.event_type, name="event_type", curie=AOP_MODEL.curie('event_type'),
                   model_uri=AOP_MODEL.event_type, domain=None, range=Union[str, "KeyEventTypeEnum"])

slots.biological_level = Slot(uri=AOP_MODEL.biological_level, name="biological_level", curie=AOP_MODEL.curie('biological_level'),
                   model_uri=AOP_MODEL.biological_level, domain=None, range=Union[str, "BiologicalLevelEnum"])

slots.direction_of_change = Slot(uri=AOP_MODEL.direction_of_change, name="direction_of_change", curie=AOP_MODEL.curie('direction_of_change'),
                   model_uri=AOP_MODEL.direction_of_change, domain=None, range=Optional[Union[str, "DirectionEnum"]])

slots.measurement_processes = Slot(uri=AOP_MODEL.measurement_processes, name="measurement_processes", curie=AOP_MODEL.curie('measurement_processes'),
                   model_uri=AOP_MODEL.measurement_processes, domain=None, range=Optional[Union[dict[Union[str, MeasurementProcessId], Union[dict, MeasurementProcess]], list[Union[dict, MeasurementProcess]]]])

slots.biomarkers = Slot(uri=AOP_MODEL.biomarkers, name="biomarkers", curie=AOP_MODEL.curie('biomarkers'),
                   model_uri=AOP_MODEL.biomarkers, domain=None, range=Optional[Union[str, list[str]]])

slots.upstream_events = Slot(uri=AOP_MODEL.upstream_events, name="upstream_events", curie=AOP_MODEL.curie('upstream_events'),
                   model_uri=AOP_MODEL.upstream_events, domain=None, range=Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]])

slots.downstream_events = Slot(uri=AOP_MODEL.downstream_events, name="downstream_events", curie=AOP_MODEL.curie('downstream_events'),
                   model_uri=AOP_MODEL.downstream_events, domain=None, range=Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=AOP_MODEL.subject, domain=None, range=Optional[Union[str, KeyEventId]])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=AOP_MODEL.predicate, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=AOP_MODEL.object, domain=None, range=Optional[Union[str, KeyEventId]])

slots.evidence_strength = Slot(uri=AOP_MODEL.evidence_strength, name="evidence_strength", curie=AOP_MODEL.curie('evidence_strength'),
                   model_uri=AOP_MODEL.evidence_strength, domain=None, range=Optional[Union[str, "EvidenceStrengthEnum"]])

slots.supporting_evidence = Slot(uri=AOP_MODEL.supporting_evidence, name="supporting_evidence", curie=AOP_MODEL.curie('supporting_evidence'),
                   model_uri=AOP_MODEL.supporting_evidence, domain=None, range=Optional[Union[dict[Union[str, ScientificEvidenceId], Union[dict, ScientificEvidence]], list[Union[dict, ScientificEvidence]]]])

slots.input_sample = Slot(uri=AOP_MODEL.input_sample, name="input_sample", curie=AOP_MODEL.curie('input_sample'),
                   model_uri=AOP_MODEL.input_sample, domain=None, range=Optional[Union[str, InputSampleId]])

slots.method_assay = Slot(uri=AOP_MODEL.method_assay, name="method_assay", curie=AOP_MODEL.curie('method_assay'),
                   model_uri=AOP_MODEL.method_assay, domain=None, range=Optional[Union[str, AssayId]])

slots.output_measurement = Slot(uri=AOP_MODEL.output_measurement, name="output_measurement", curie=AOP_MODEL.curie('output_measurement'),
                   model_uri=AOP_MODEL.output_measurement, domain=None, range=Optional[Union[str, OutputMeasurementId]])

slots.context_fields = Slot(uri=AOP_MODEL.context_fields, name="context_fields", curie=AOP_MODEL.curie('context_fields'),
                   model_uri=AOP_MODEL.context_fields, domain=None, range=Optional[Union[dict[Union[str, ContextFieldId], Union[dict, ContextField]], list[Union[dict, ContextField]]]])

slots.protocol_notes = Slot(uri=AOP_MODEL.protocol_notes, name="protocol_notes", curie=AOP_MODEL.curie('protocol_notes'),
                   model_uri=AOP_MODEL.protocol_notes, domain=None, range=Optional[str])

slots.ontology_mappings = Slot(uri=AOP_MODEL.ontology_mappings, name="ontology_mappings", curie=AOP_MODEL.curie('ontology_mappings'),
                   model_uri=AOP_MODEL.ontology_mappings, domain=None, range=Optional[Union[str, list[str]]])

slots.exemplar_manuscripts = Slot(uri=AOP_MODEL.exemplar_manuscripts, name="exemplar_manuscripts", curie=AOP_MODEL.curie('exemplar_manuscripts'),
                   model_uri=AOP_MODEL.exemplar_manuscripts, domain=None, range=Optional[Union[dict[Union[str, ScientificEvidenceId], Union[dict, ScientificEvidence]], list[Union[dict, ScientificEvidence]]]])

slots.sample_type = Slot(uri=AOP_MODEL.sample_type, name="sample_type", curie=AOP_MODEL.curie('sample_type'),
                   model_uri=AOP_MODEL.sample_type, domain=None, range=Optional[str])

slots.manipulation = Slot(uri=AOP_MODEL.manipulation, name="manipulation", curie=AOP_MODEL.curie('manipulation'),
                   model_uri=AOP_MODEL.manipulation, domain=None, range=Optional[str])

slots.exposure_conditions = Slot(uri=AOP_MODEL.exposure_conditions, name="exposure_conditions", curie=AOP_MODEL.curie('exposure_conditions'),
                   model_uri=AOP_MODEL.exposure_conditions, domain=None, range=Optional[str])

slots.assay_type = Slot(uri=AOP_MODEL.assay_type, name="assay_type", curie=AOP_MODEL.curie('assay_type'),
                   model_uri=AOP_MODEL.assay_type, domain=None, range=Optional[Union[str, "AssayTypeEnum"]])

slots.instrumentation = Slot(uri=AOP_MODEL.instrumentation, name="instrumentation", curie=AOP_MODEL.curie('instrumentation'),
                   model_uri=AOP_MODEL.instrumentation, domain=None, range=Optional[str])

slots.environmental_conditions = Slot(uri=AOP_MODEL.environmental_conditions, name="environmental_conditions", curie=AOP_MODEL.curie('environmental_conditions'),
                   model_uri=AOP_MODEL.environmental_conditions, domain=None, range=Optional[str])

slots.sop_reference = Slot(uri=AOP_MODEL.sop_reference, name="sop_reference", curie=AOP_MODEL.curie('sop_reference'),
                   model_uri=AOP_MODEL.sop_reference, domain=None, range=Optional[str])

slots.measurement_type = Slot(uri=AOP_MODEL.measurement_type, name="measurement_type", curie=AOP_MODEL.curie('measurement_type'),
                   model_uri=AOP_MODEL.measurement_type, domain=None, range=Optional[str])

slots.has_quantity_value = Slot(uri=AOP_MODEL.has_quantity_value, name="has_quantity_value", curie=AOP_MODEL.curie('has_quantity_value'),
                   model_uri=AOP_MODEL.has_quantity_value, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.has_numeric_value = Slot(uri=AOP_MODEL.has_numeric_value, name="has_numeric_value", curie=AOP_MODEL.curie('has_numeric_value'),
                   model_uri=AOP_MODEL.has_numeric_value, domain=None, range=Optional[float])

slots.has_unit = Slot(uri=AOP_MODEL.has_unit, name="has_unit", curie=AOP_MODEL.curie('has_unit'),
                   model_uri=AOP_MODEL.has_unit, domain=None, range=Optional[str])

slots.has_minimum_numeric_value = Slot(uri=AOP_MODEL.has_minimum_numeric_value, name="has_minimum_numeric_value", curie=AOP_MODEL.curie('has_minimum_numeric_value'),
                   model_uri=AOP_MODEL.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.has_maximum_numeric_value = Slot(uri=AOP_MODEL.has_maximum_numeric_value, name="has_maximum_numeric_value", curie=AOP_MODEL.curie('has_maximum_numeric_value'),
                   model_uri=AOP_MODEL.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.field_name = Slot(uri=AOP_MODEL.field_name, name="field_name", curie=AOP_MODEL.curie('field_name'),
                   model_uri=AOP_MODEL.field_name, domain=None, range=Optional[str])

slots.field_value = Slot(uri=AOP_MODEL.field_value, name="field_value", curie=AOP_MODEL.curie('field_value'),
                   model_uri=AOP_MODEL.field_value, domain=None, range=Optional[str])

slots.field_category = Slot(uri=AOP_MODEL.field_category, name="field_category", curie=AOP_MODEL.curie('field_category'),
                   model_uri=AOP_MODEL.field_category, domain=None, range=Optional[str])

slots.cftr_specific_current = Slot(uri=AOP_MODEL.cftr_specific_current, name="cftr_specific_current", curie=AOP_MODEL.curie('cftr_specific_current'),
                   model_uri=AOP_MODEL.cftr_specific_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inhibitor_sensitive_current = Slot(uri=AOP_MODEL.inhibitor_sensitive_current, name="inhibitor_sensitive_current", curie=AOP_MODEL.curie('inhibitor_sensitive_current'),
                   model_uri=AOP_MODEL.inhibitor_sensitive_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cell_culture_conditions = Slot(uri=AOP_MODEL.cell_culture_conditions, name="cell_culture_conditions", curie=AOP_MODEL.curie('cell_culture_conditions'),
                   model_uri=AOP_MODEL.cell_culture_conditions, domain=None, range=Optional[str])

slots.beat_frequency_hz = Slot(uri=AOP_MODEL.beat_frequency_hz, name="beat_frequency_hz", curie=AOP_MODEL.curie('beat_frequency_hz'),
                   model_uri=AOP_MODEL.beat_frequency_hz, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.active_area_percentage = Slot(uri=AOP_MODEL.active_area_percentage, name="active_area_percentage", curie=AOP_MODEL.curie('active_area_percentage'),
                   model_uri=AOP_MODEL.active_area_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_conditions = Slot(uri=AOP_MODEL.imaging_conditions, name="imaging_conditions", curie=AOP_MODEL.curie('imaging_conditions'),
                   model_uri=AOP_MODEL.imaging_conditions, domain=None, range=Optional[str])

slots.asl_height_um = Slot(uri=AOP_MODEL.asl_height_um, name="asl_height_um", curie=AOP_MODEL.curie('asl_height_um'),
                   model_uri=AOP_MODEL.asl_height_um, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.periciliary_layer_depth = Slot(uri=AOP_MODEL.periciliary_layer_depth, name="periciliary_layer_depth", curie=AOP_MODEL.curie('periciliary_layer_depth'),
                   model_uri=AOP_MODEL.periciliary_layer_depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_modality = Slot(uri=AOP_MODEL.imaging_modality, name="imaging_modality", curie=AOP_MODEL.curie('imaging_modality'),
                   model_uri=AOP_MODEL.imaging_modality, domain=None, range=Optional[str])

slots.transport_rate = Slot(uri=AOP_MODEL.transport_rate, name="transport_rate", curie=AOP_MODEL.curie('transport_rate'),
                   model_uri=AOP_MODEL.transport_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.directionality = Slot(uri=AOP_MODEL.directionality, name="directionality", curie=AOP_MODEL.curie('directionality'),
                   model_uri=AOP_MODEL.directionality, domain=None, range=Optional[str])

slots.particle_tracking_method = Slot(uri=AOP_MODEL.particle_tracking_method, name="particle_tracking_method", curie=AOP_MODEL.curie('particle_tracking_method'),
                   model_uri=AOP_MODEL.particle_tracking_method, domain=None, range=Optional[str])

slots.goblet_cell_count = Slot(uri=AOP_MODEL.goblet_cell_count, name="goblet_cell_count", curie=AOP_MODEL.curie('goblet_cell_count'),
                   model_uri=AOP_MODEL.goblet_cell_count, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mucin_expression_level = Slot(uri=AOP_MODEL.mucin_expression_level, name="mucin_expression_level", curie=AOP_MODEL.curie('mucin_expression_level'),
                   model_uri=AOP_MODEL.mucin_expression_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.staining_method = Slot(uri=AOP_MODEL.staining_method, name="staining_method", curie=AOP_MODEL.curie('staining_method'),
                   model_uri=AOP_MODEL.staining_method, domain=None, range=Optional[str])

slots.ros_level = Slot(uri=AOP_MODEL.ros_level, name="ros_level", curie=AOP_MODEL.curie('ros_level'),
                   model_uri=AOP_MODEL.ros_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lipid_peroxidation = Slot(uri=AOP_MODEL.lipid_peroxidation, name="lipid_peroxidation", curie=AOP_MODEL.curie('lipid_peroxidation'),
                   model_uri=AOP_MODEL.lipid_peroxidation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.antioxidant_capacity = Slot(uri=AOP_MODEL.antioxidant_capacity, name="antioxidant_capacity", curie=AOP_MODEL.curie('antioxidant_capacity'),
                   model_uri=AOP_MODEL.antioxidant_capacity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.publication_reference = Slot(uri=AOP_MODEL.publication_reference, name="publication_reference", curie=AOP_MODEL.curie('publication_reference'),
                   model_uri=AOP_MODEL.publication_reference, domain=None, range=Optional[str])

slots.evidence_type = Slot(uri=AOP_MODEL.evidence_type, name="evidence_type", curie=AOP_MODEL.curie('evidence_type'),
                   model_uri=AOP_MODEL.evidence_type, domain=None, range=Optional[str])

slots.study_design = Slot(uri=AOP_MODEL.study_design, name="study_design", curie=AOP_MODEL.curie('study_design'),
                   model_uri=AOP_MODEL.study_design, domain=None, range=Optional[str])

slots.AdverseOutcomePathway_id = Slot(uri=AOP_MODEL.id, name="AdverseOutcomePathway_id", curie=AOP_MODEL.curie('id'),
                   model_uri=AOP_MODEL.AdverseOutcomePathway_id, domain=AdverseOutcomePathway, range=Union[str, AdverseOutcomePathwayId],
                   pattern=re.compile(r'^AOP:\d+$'))

slots.KeyEvent_id = Slot(uri=AOP_MODEL.id, name="KeyEvent_id", curie=AOP_MODEL.curie('id'),
                   model_uri=AOP_MODEL.KeyEvent_id, domain=KeyEvent, range=Union[str, KeyEventId],
                   pattern=re.compile(r'^(MIE|KE|AO):\d+$'))

slots.KeyEventAssociation_id = Slot(uri=AOP_MODEL.id, name="KeyEventAssociation_id", curie=AOP_MODEL.curie('id'),
                   model_uri=AOP_MODEL.KeyEventAssociation_id, domain=KeyEventAssociation, range=Union[str, KeyEventAssociationId],
                   pattern=re.compile(r'^KER:\d+$'))

slots.KeyEventAssociation_subject = Slot(uri=RDF.subject, name="KeyEventAssociation_subject", curie=RDF.curie('subject'),
                   model_uri=AOP_MODEL.KeyEventAssociation_subject, domain=KeyEventAssociation, range=Union[str, KeyEventId])

slots.KeyEventAssociation_predicate = Slot(uri=RDF.predicate, name="KeyEventAssociation_predicate", curie=RDF.curie('predicate'),
                   model_uri=AOP_MODEL.KeyEventAssociation_predicate, domain=KeyEventAssociation, range=Union[str, "KeyEventPredicateEnum"])

slots.KeyEventAssociation_object = Slot(uri=RDF.object, name="KeyEventAssociation_object", curie=RDF.curie('object'),
                   model_uri=AOP_MODEL.KeyEventAssociation_object, domain=KeyEventAssociation, range=Union[str, KeyEventId])
