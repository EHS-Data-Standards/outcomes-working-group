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


linkml_meta = LinkMLMeta({'default_prefix': 'aop_model',
     'default_range': 'string',
     'description': 'A LinkML data model for representing Adverse Outcome Pathways '
                    '(AOPs),\n'
                    'Key Events (KEs), and Key Event Relationships (KERs) in the '
                    'context of\n'
                    'the Source-to-Outcome (S2O) continuum.\n',
     'id': 'https://w3id.org/EHS-Data-Standards/aop-model',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'aop-model',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'aop_model': {'prefix_prefix': 'aop_model',
                                'prefix_reference': 'https://w3id.org/EHS-Data-Standards/aop-model/'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://EHS-Data-Standards.github.io/outcomes-working-group'],
     'source_file': 'src/outcomes_working_group/schema/outcomes_working_group.yaml',
     'title': 'AOP Data Model'} )

class BiologicalLevelEnum(str, Enum):
    """
    The level of biological organization at which an event occurs
    """
    MOLECULAR = "MOLECULAR"
    """
    Macro-molecular interactions (e.g., receptor binding, protein modification)
    """
    CELLULAR = "CELLULAR"
    """
    Cellular response (e.g., cell signaling, gene expression, cell death)
    """
    TISSUE = "TISSUE"
    """
    Tissue-level response (e.g., inflammation, tissue damage)
    """
    ORGAN = "ORGAN"
    """
    Organ-level response (e.g., impaired organ function)
    """
    ORGANISM = "ORGANISM"
    """
    Organism-level outcome (e.g., disease, mortality)
    """
    POPULATION = "POPULATION"
    """
    Population-level outcome (e.g., disease incidence, public health impact)
    """


class KeyEventTypeEnum(str, Enum):
    """
    Classification of key events in an AOP
    """
    MIE = "MIE"
    """
    Molecular Initiating Event - the initial interaction between a stressor and a biological target
    """
    KE = "KE"
    """
    Key Event - a measurable change in biological state along the pathway
    """
    AO = "AO"
    """
    Adverse Outcome - the endpoint of regulatory concern
    """


class DirectionEnum(str, Enum):
    """
    Direction of change for a key event
    """
    INCREASED = "INCREASED"
    """
    The measured parameter is increased
    """
    DECREASED = "DECREASED"
    """
    The measured parameter is decreased
    """
    ALTERED = "ALTERED"
    """
    The measured parameter is changed in either direction
    """


class EvidenceStrengthEnum(str, Enum):
    """
    Strength of evidence supporting a relationship
    """
    STRONG = "STRONG"
    """
    Strong empirical evidence from multiple independent studies
    """
    MODERATE = "MODERATE"
    """
    Moderate evidence with some consistency
    """
    WEAK = "WEAK"
    """
    Limited or inconsistent evidence
    """
    NOT_SPECIFIED = "NOT_SPECIFIED"
    """
    Evidence strength not specified
    """


class KeyEventPredicateEnum(str, Enum):
    """
    Types of relationships between key events in an AOP
    """
    has_input = "has_input"
    """
    The subject key event has the object key event as input
    """
    has_output = "has_output"
    """
    The subject key event has the object key event as output
    """
    leads_to = "leads_to"
    """
    The subject key event leads to the object key event
    """
    regulates = "regulates"
    """
    The subject key event regulates the object key event
    """
    positively_regulates = "positively_regulates"
    """
    The subject key event positively regulates the object key event
    """
    negatively_regulates = "negatively_regulates"
    """
    The subject key event negatively regulates the object key event
    """
    causes = "causes"
    """
    The subject key event directly causes the object key event
    """
    contributes_to = "contributes_to"
    """
    The subject key event contributes to the object key event
    """


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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class AdverseOutcomePathway(NamedEntity):
    """
    A structured representation of biological events linking a molecular initiating event (MIE)
    to an adverse outcome through a series of key events.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model',
         'slot_usage': {'id': {'examples': [{'description': 'Example AOP identifier',
                                             'value': 'AOP:424'}],
                               'name': 'id',
                               'pattern': '^AOP:\\d+$'}}})

    molecular_initiating_events: Optional[dict[str, KeyEvent]] = Field(default=None, description="""The molecular initiating event(s) that start this AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    key_events: Optional[dict[str, KeyEvent]] = Field(default=None, description="""All key events in this AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    adverse_outcome: str = Field(default=..., description="""The adverse outcome of regulatory concern""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    key_event_relationships: Optional[dict[str, KeyEventAssociation]] = Field(default=None, description="""Relationships between key events in this AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    aop_network_members: Optional[list[str]] = Field(default=[], description="""Other AOPs that are part of the same network""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'description': 'Example AOP identifier', 'value': 'AOP:424'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^AOP:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class KeyEvent(NamedEntity):
    """
    A measurable change in biological state that is a necessary step in a pathway from
    a molecular initiating event to an adverse outcome. Key Events can represent molecular,
    cellular, tissue, organ, or organism-level changes.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model',
         'slot_usage': {'id': {'examples': [{'value': 'MIE:1'},
                                            {'value': 'KE:1906'},
                                            {'value': 'AO:11'}],
                               'name': 'id',
                               'pattern': '^(MIE|KE|AO):\\d+$'}}})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class OxidativeStressEvent(KeyEvent):
    """
    Molecular initiating event involving oxidative stress
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class EGFRActivationEvent(KeyEvent):
    """
    Molecular initiating event involving EGFR activation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class CFTRFunctionEvent(KeyEvent):
    """
    Key event representing changes in CFTR function
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FoxJ1ExpressionEvent(KeyEvent):
    """
    Key event representing changes in FoxJ1 expression
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class CiliaNumberEvent(KeyEvent):
    """
    Key event representing changes in cilia number or length
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class GobletCellEvent(KeyEvent):
    """
    Key event representing changes in goblet cell number
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class ASLHeightEvent(KeyEvent):
    """
    Key event representing changes in airway surface liquid height
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class CiliaryBeatFrequencyEvent(KeyEvent):
    """
    Key event representing changes in ciliary beat frequency
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class MucinProductionEvent(KeyEvent):
    """
    Key event representing changes in mucin production
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class MucociliaryClearanceEvent(KeyEvent):
    """
    Key event representing changes in mucociliary clearance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class LungFunctionEvent(KeyEvent):
    """
    Adverse outcome representing decreased lung function
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    event_type: KeyEventTypeEnum = Field(default=..., description="""Classification of the key event (MIE, KE, or AO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_level: BiologicalLevelEnum = Field(default=..., description="""The level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    direction_of_change: Optional[DirectionEnum] = Field(default=None, description="""Direction of change for this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    measurement_processes: Optional[dict[str, MeasurementProcess]] = Field(default=None, description="""Measurement processes used to assess this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biomarkers: Optional[list[str]] = Field(default=[], description="""Biomarkers associated with this key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    upstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur before this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_events: Optional[list[str]] = Field(default=[], description="""Key events that occur after this one in the pathway""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'MIE:1'}, {'value': 'KE:1906'}, {'value': 'AO:11'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(MIE|KE|AO):\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class Association(NamedEntity):
    """
    Base class for associations/relationships in the model.
    Uses subject-predicate-object pattern similar to Biolink model.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    subject: Optional[str] = Field(default=None, description="""The subject of a relationship (e.g., upstream key event)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdf:subject'} })
    predicate: Optional[str] = Field(default=None, description="""The predicate/relationship type (e.g., leads_to, causes, regulates)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdf:predicate'} })
    object: Optional[str] = Field(default=None, description="""The object of a relationship (e.g., downstream key event)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdf:object'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class KeyEventAssociation(Association):
    """
    A causal or associative relationship between two key events in an adverse outcome pathway.
    Represents the connection showing how one event leads to another.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model',
         'slot_usage': {'id': {'examples': [{'value': 'KER:1907'}],
                               'name': 'id',
                               'pattern': '^KER:\\d+$'},
                        'object': {'description': 'The downstream key event (output '
                                                  'from the relationship)',
                                   'name': 'object',
                                   'range': 'KeyEvent',
                                   'required': True},
                        'predicate': {'description': 'The type of relationship',
                                      'name': 'predicate',
                                      'range': 'KeyEventPredicateEnum',
                                      'required': True},
                        'subject': {'description': 'The upstream key event (input to '
                                                   'the relationship)',
                                    'name': 'subject',
                                    'range': 'KeyEvent',
                                    'required': True}}})

    evidence_strength: Optional[EvidenceStrengthEnum] = Field(default=None, description="""Strength of evidence supporting this relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventAssociation']} })
    supporting_evidence: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Scientific evidence supporting this relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventAssociation']} })
    subject: str = Field(default=..., description="""The upstream key event (input to the relationship)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdf:subject'} })
    predicate: KeyEventPredicateEnum = Field(default=..., description="""The type of relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., description="""The downstream key event (output from the relationship)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdf:object'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'examples': [{'value': 'KER:1907'}]} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^KER:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class MeasurementProcess(NamedEntity):
    """
    A generic class representing the process of measuring a biological key event.
    Includes information about input samples, methods, outputs, and contextual metadata.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    output_measurement: Optional[str] = Field(default=None, description="""The output or measurement obtained""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    context_fields: Optional[dict[str, ContextField]] = Field(default=None, description="""Contextual metadata fields for reproducibility""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    ontology_mappings: Optional[list[str]] = Field(default=[], description="""Mappings to ontology terms (Biolink, OBI, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    exemplar_manuscripts: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Key peer-reviewed publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class InputSample(NamedEntity):
    """
    Description of the biological sample or experimental manipulation used as input
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    sample_type: Optional[str] = Field(default=None, description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSample'],
         'examples': [{'value': 'Primary human airway epithelial cells at ALI'},
                      {'value': 'MucilAir 3D tissue model'}]} })
    manipulation: Optional[str] = Field(default=None, description="""Experimental manipulation applied""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSample']} })
    exposure_conditions: Optional[str] = Field(default=None, description="""Exposure or treatment conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSample']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class Assay(NamedEntity):
    """
    The specific method or assay used to measure a key event
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    assay_type: Optional[AssayTypeEnum] = Field(default=None, description="""Type of assay or method, constrained to OBI assay terms""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    instrumentation: Optional[str] = Field(default=None, description="""Specific instruments or equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    environmental_conditions: Optional[str] = Field(default=None, description="""Environmental conditions during measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    sop_reference: Optional[str] = Field(default=None, description="""Reference to standard operating procedure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class QuantityValue(ConfiguredBaseModel):
    """
    A quantity value expresses a measurement with a numeric value and a unit.
    Based on NMDC Schema QuantityValue pattern.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    has_numeric_value: Optional[float] = Field(default=None, description="""The numeric value of a quantity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    has_unit: Optional[str] = Field(default=None, description="""The unit of measurement for the quantity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'],
         'examples': [{'value': 'Hz'},
                      {'value': 'µm'},
                      {'value': 'mm/min'},
                      {'value': '%'}]} })
    has_minimum_numeric_value: Optional[float] = Field(default=None, description="""The minimum value in a range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    has_maximum_numeric_value: Optional[float] = Field(default=None, description="""The maximum value in a range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })


class OutputMeasurement(NamedEntity):
    """
    The quantitative or qualitative output from a measurement process
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    measurement_type: Optional[str] = Field(default=None, description="""Type of measurement or readout""", json_schema_extra = { "linkml_meta": {'domain_of': ['OutputMeasurement']} })
    has_quantity_value: Optional[QuantityValue] = Field(default=None, description="""The quantity value associated with this measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['OutputMeasurement']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class ContextField(NamedEntity):
    """
    Metadata fields that capture important contextual information for reproducibility
    and cross-study comparison

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    field_name: Optional[str] = Field(default=None, description="""Name of the context field""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContextField']} })
    field_value: Optional[str] = Field(default=None, description="""Value of the context field""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContextField']} })
    field_category: Optional[str] = Field(default=None, description="""Category or grouping for the context field""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContextField']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class CFTRFunctionMeasurement(MeasurementProcess):
    """
    Measurement of CFTR-mediated ion transport function
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    cftr_specific_current: Optional[QuantityValue] = Field(default=None, description="""CFTR-mediated chloride secretory current""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionMeasurement']} })
    inhibitor_sensitive_current: Optional[QuantityValue] = Field(default=None, description="""Inhibitor-sensitive current measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionMeasurement']} })
    cell_culture_conditions: Optional[str] = Field(default=None, description="""Conditions for cell culture (ALI days, medium, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    output_measurement: Optional[str] = Field(default=None, description="""The output or measurement obtained""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    context_fields: Optional[dict[str, ContextField]] = Field(default=None, description="""Contextual metadata fields for reproducibility""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    ontology_mappings: Optional[list[str]] = Field(default=[], description="""Mappings to ontology terms (Biolink, OBI, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    exemplar_manuscripts: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Key peer-reviewed publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class CiliaBeatFrequencyMeasurement(MeasurementProcess):
    """
    Measurement of ciliary beat frequency
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    beat_frequency_hz: Optional[QuantityValue] = Field(default=None, description="""Ciliary beat frequency in Hz""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaBeatFrequencyMeasurement']} })
    active_area_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of active ciliated area""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaBeatFrequencyMeasurement']} })
    imaging_conditions: Optional[str] = Field(default=None, description="""Imaging parameters and conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaBeatFrequencyMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    output_measurement: Optional[str] = Field(default=None, description="""The output or measurement obtained""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    context_fields: Optional[dict[str, ContextField]] = Field(default=None, description="""Contextual metadata fields for reproducibility""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    ontology_mappings: Optional[list[str]] = Field(default=[], description="""Mappings to ontology terms (Biolink, OBI, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    exemplar_manuscripts: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Key peer-reviewed publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class ASLHeightMeasurement(MeasurementProcess):
    """
    Measurement of airway surface liquid height
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    asl_height_um: Optional[QuantityValue] = Field(default=None, description="""Airway surface liquid height in micrometers""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLHeightMeasurement']} })
    periciliary_layer_depth: Optional[QuantityValue] = Field(default=None, description="""Depth of periciliary layer in micrometers""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLHeightMeasurement']} })
    imaging_modality: Optional[str] = Field(default=None, description="""Imaging modality used (confocal, OCT, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLHeightMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    output_measurement: Optional[str] = Field(default=None, description="""The output or measurement obtained""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    context_fields: Optional[dict[str, ContextField]] = Field(default=None, description="""Contextual metadata fields for reproducibility""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    ontology_mappings: Optional[list[str]] = Field(default=[], description="""Mappings to ontology terms (Biolink, OBI, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    exemplar_manuscripts: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Key peer-reviewed publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class MucociliaryClearanceMeasurement(MeasurementProcess):
    """
    Measurement of mucociliary clearance/transport
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    transport_rate: Optional[QuantityValue] = Field(default=None, description="""Mucociliary transport rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceMeasurement']} })
    directionality: Optional[str] = Field(default=None, description="""Directionality of mucociliary transport""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceMeasurement']} })
    particle_tracking_method: Optional[str] = Field(default=None, description="""Method used for tracking particles or mucus""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    output_measurement: Optional[str] = Field(default=None, description="""The output or measurement obtained""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    context_fields: Optional[dict[str, ContextField]] = Field(default=None, description="""Contextual metadata fields for reproducibility""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    ontology_mappings: Optional[list[str]] = Field(default=[], description="""Mappings to ontology terms (Biolink, OBI, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    exemplar_manuscripts: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Key peer-reviewed publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class GobletCellMeasurement(MeasurementProcess):
    """
    Measurement of goblet cell number or mucin production
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    goblet_cell_count: Optional[QuantityValue] = Field(default=None, description="""Number or percentage of goblet cells""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellMeasurement']} })
    mucin_expression_level: Optional[QuantityValue] = Field(default=None, description="""Level of mucin gene or protein expression""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellMeasurement']} })
    staining_method: Optional[str] = Field(default=None, description="""Histological staining method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    output_measurement: Optional[str] = Field(default=None, description="""The output or measurement obtained""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    context_fields: Optional[dict[str, ContextField]] = Field(default=None, description="""Contextual metadata fields for reproducibility""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    ontology_mappings: Optional[list[str]] = Field(default=[], description="""Mappings to ontology terms (Biolink, OBI, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    exemplar_manuscripts: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Key peer-reviewed publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class OxidativeStressMeasurement(MeasurementProcess):
    """
    Measurement of oxidative stress markers
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    ros_level: Optional[QuantityValue] = Field(default=None, description="""Reactive oxygen species level""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    lipid_peroxidation: Optional[QuantityValue] = Field(default=None, description="""Lipid peroxidation markers (MDA, 8-isoprostane, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    antioxidant_capacity: Optional[QuantityValue] = Field(default=None, description="""Antioxidant capacity (GSH/GSSG ratio, enzyme activity)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressMeasurement']} })
    input_sample: Optional[str] = Field(default=None, description="""Description of input samples and manipulations""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    method_assay: Optional[str] = Field(default=None, description="""The method or assay used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    output_measurement: Optional[str] = Field(default=None, description="""The output or measurement obtained""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    context_fields: Optional[dict[str, ContextField]] = Field(default=None, description="""Contextual metadata fields for reproducibility""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    protocol_notes: Optional[str] = Field(default=None, description="""Protocol or SOP notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    ontology_mappings: Optional[list[str]] = Field(default=[], description="""Mappings to ontology terms (Biolink, OBI, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    exemplar_manuscripts: Optional[dict[str, ScientificEvidence]] = Field(default=None, description="""Key peer-reviewed publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementProcess']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


class ScientificEvidence(NamedEntity):
    """
    Published scientific evidence supporting an AOP component
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop-model'})

    publication_reference: Optional[str] = Field(default=None, description="""Citation or reference to publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScientificEvidence']} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of evidence (experimental, observational, computational)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScientificEvidence']} })
    study_design: Optional[str] = Field(default=None, description="""Study design or experimental approach""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScientificEvidence']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })
    description: Optional[str] = Field(default=None, description="""A detailed description""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
AdverseOutcomePathway.model_rebuild()
KeyEvent.model_rebuild()
OxidativeStressEvent.model_rebuild()
EGFRActivationEvent.model_rebuild()
CFTRFunctionEvent.model_rebuild()
FoxJ1ExpressionEvent.model_rebuild()
CiliaNumberEvent.model_rebuild()
GobletCellEvent.model_rebuild()
ASLHeightEvent.model_rebuild()
CiliaryBeatFrequencyEvent.model_rebuild()
MucinProductionEvent.model_rebuild()
MucociliaryClearanceEvent.model_rebuild()
LungFunctionEvent.model_rebuild()
Association.model_rebuild()
KeyEventAssociation.model_rebuild()
MeasurementProcess.model_rebuild()
InputSample.model_rebuild()
Assay.model_rebuild()
QuantityValue.model_rebuild()
OutputMeasurement.model_rebuild()
ContextField.model_rebuild()
CFTRFunctionMeasurement.model_rebuild()
CiliaBeatFrequencyMeasurement.model_rebuild()
ASLHeightMeasurement.model_rebuild()
MucociliaryClearanceMeasurement.model_rebuild()
GobletCellMeasurement.model_rebuild()
OxidativeStressMeasurement.model_rebuild()
ScientificEvidence.model_rebuild()
