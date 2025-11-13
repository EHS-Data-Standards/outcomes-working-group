#!/usr/bin/env python3
"""
Generate ontology mappings for schema slots with proper PATO terms and labels.
This script creates a comprehensive CSV with ontology mappings excluding UO terms
from measurement slots (UO should only constrain the unit slot in QuantityValue).
"""

import csv
import json
import os
import requests
import time

OLS_API_BASE = "https://www.ebi.ac.uk/ols4/api"

def get_term_label(term_id: str) -> str:
    """Get the label for an ontology term from OLS."""
    if ":" in term_id:
        parts = term_id.split(":")
        ontology = parts[0].lower()
        
        url = f"{OLS_API_BASE}/ontologies/{ontology}/terms"
        params = {"obo_id": term_id}
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "_embedded" in data and "terms" in data["_embedded"]:
                terms = data["_embedded"]["terms"]
                if terms and len(terms) > 0:
                    return terms[0].get("label", "")
        except Exception as e:
            print(f"  Warning: Could not fetch label for {term_id}: {e}")
    
    return ""

def get_fallback_label(term_id: str) -> str:
    """Fallback labels for common terms if OLS lookup fails."""
    fallback_labels = {
        "OBI:0000011": "planned process",
        "OBI:0000070": "assay",
        "OBI:0000079": "culture medium",
        "OBI:0000185": "imaging assay",
        "OBI:0000272": "protocol",
        "OBI:0000424": "transcription profiling assay",
        "OBI:0000747": "material sample",
        "OBI:0000968": "device",
        "OBI:0100051": "specimen",
        "OBI:0302887": "staining",
        "IAO:0000109": "measurement datum",
        "IAO:0000310": "document",
        "PATO:0000001": "quality",
        "PATO:0000033": "concentration of",
        "PATO:0000044": "frequency",
        "PATO:0000070": "amount",
        "PATO:0000119": "height",
        "PATO:0000122": "length",
        "PATO:0000146": "temperature",
        "PATO:0000161": "rate",
        "PATO:0000165": "time",
        "PATO:0000915": "thickness",
        "PATO:0000918": "volume",
        "PATO:0001018": "physical quality",
        "PATO:0001025": "pressure",
        "PATO:0001309": "duration",
        "PATO:0001421": "alive",
        "PATO:0001470": "ratio",
        "PATO:0001527": "quiet",
        "PATO:0001555": "has number of",
        "PATO:0001595": "depth",
        "PATO:0015009": "humidity",
        "UO:0000000": "unit",
        "CHEBI:16526": "carbon dioxide",
        "CHEBI:16991": "deoxyribonucleic acid",
        "CHEBI:17660": "N(6)-dimethylallyladenine",
        "CHEBI:23530": "cytokinin",
        "CHEBI:26523": "reactive oxygen species",
        "CHEBI:33699": "messenger RNA",
        "CHEBI:36080": "protein",
        "CHEBI:51217": "fluorochrome",
        "CL:0000064": "ciliated cell",
        "CL:0000160": "goblet cell",
        "GO:0003341": "cilium movement",
        "GO:0016491": "oxidoreductase activity",
        "GO:0070254": "mucus secretion",
        "GO:0120197": "mucociliary clearance",
        "ENVO:01000254": "environmental system",
    }
    
    return fallback_labels.get(term_id, "")

def generate_slot_mappings():
    """
    Generate improved mappings using PATO for qualities and excluding UO from measurement slots.
    """
    
    mappings = {
        "input_sample": {
            "exact_mappings": ["OBI:0100051"],
            "related_mappings": ["OBI:0000747"]
        },
        "method_assay": {
            "exact_mappings": ["OBI:0000070"],
        },
        "protocol_notes": {
            "broad_mappings": ["OBI:0000272"],
            "related_mappings": ["IAO:0000310"]
        },
        "assay_type": {
            "exact_mappings": ["OBI:0000070"],
        },
        "instrumentation": {
            "broad_mappings": ["OBI:0000968"],
        },
        "environmental_conditions": {
            "related_mappings": ["ENVO:01000254", "PATO:0001018"]
        },
        "sop_reference": {
            "broad_mappings": ["OBI:0000272"],
            "related_mappings": ["IAO:0000310"]
        },
        "sample_type": {
            "broad_mappings": ["OBI:0100051"],
        },
        "manipulation": {
            "broad_mappings": ["OBI:0000011"],
        },
        "exposure_conditions": {
            "related_mappings": ["ENVO:01000254", "PATO:0001018"]
        },
        "has_numeric_value": {
            "broad_mappings": ["IAO:0000109"],
        },
        "has_unit": {
            "exact_mappings": ["UO:0000000"],
        },
        "has_minimum_numeric_value": {
            "broad_mappings": ["IAO:0000109"],
        },
        "has_maximum_numeric_value": {
            "broad_mappings": ["IAO:0000109"],
        },
        "imaging_modality": {
            "broad_mappings": ["OBI:0000185"],
        },
        "imaging_protocol": {
            "exact_mappings": ["OBI:0000272"],
        },
        "frame_rate": {
            "broad_mappings": ["IAO:0000109"],
            "related_mappings": ["PATO:0000161"]
        },
        "imaging_duration": {
            "broad_mappings": ["IAO:0000109"],
            "related_mappings": ["PATO:0001309"]
        },
        "spatial_resolution": {
            "broad_mappings": ["IAO:0000109"],
            "related_mappings": ["PATO:0001018"]
        },
        "fluorescent_labeling": {
            "related_mappings": ["CHEBI:51217"]
        },
        "fluorophore_type": {
            "broad_mappings": ["CHEBI:51217"],
        },
        "culture_medium": {
            "exact_mappings": ["OBI:0000079"],
        },
        "days_at_ali": {
            "broad_mappings": ["IAO:0000109"],
            "related_mappings": ["PATO:0000165"]
        },
        "passage_number": {
            "broad_mappings": ["IAO:0000109"],
        },
        "temperature": {
            "exact_mappings": ["PATO:0000146"],
        },
        "humidity": {
            "exact_mappings": ["PATO:0015009"],
        },
        "co2_percentage": {
            "broad_mappings": ["PATO:0000033"],
            "related_mappings": ["CHEBI:16526"]
        },
        "donor_count": {
            "broad_mappings": ["IAO:0000109"],
            "related_mappings": ["PATO:0000070"]
        },
        "staining_type": {
            "broad_mappings": ["OBI:0302887"],
        },
        "staining_protocol": {
            "exact_mappings": ["OBI:0000272"],
        },
        "fixation_method": {
            "broad_mappings": ["OBI:0000011"],
            "related_mappings": ["OBI:0302887"]
        },
        "analysis_method": {
            "broad_mappings": ["OBI:0000070"],
        },
        "gene_expression_analysis": {
            "broad_mappings": ["OBI:0000070"],
            "related_mappings": ["OBI:0000424"]
        },
        "mrna_level": {
            "broad_mappings": ["PATO:0000070"],
            "related_mappings": ["CHEBI:33699"]
        },
        "protein_level": {
            "broad_mappings": ["PATO:0000070"],
            "related_mappings": ["CHEBI:36080"]
        },
        "percentage_positive_cells": {
            "broad_mappings": ["PATO:0001555"],
        },
        "collection_method": {
            "broad_mappings": ["OBI:0000011"],
        },
        "storage_conditions": {
            "related_mappings": ["PATO:0000146", "PATO:0015009"]
        },
        "processing_time": {
            "broad_mappings": ["PATO:0000165"],
        },
        "detection_type": {
            "broad_mappings": ["OBI:0000070"],
        },
        "detection_method_details": {
            "broad_mappings": ["OBI:0000070"],
        },
        "beat_frequency_hz": {
            "broad_mappings": ["PATO:0000044"],
            "related_mappings": ["GO:0003341"]
        },
        "asl_height_um": {
            "broad_mappings": ["PATO:0000119"],
        },
        "periciliary_layer_depth": {
            "broad_mappings": ["PATO:0001595"],
        },
        "cilia_length": {
            "broad_mappings": ["PATO:0000122"],
        },
        "cilia_per_cell": {
            "broad_mappings": ["PATO:0000070"],
            "related_mappings": ["CL:0000064"]
        },
        "transport_rate": {
            "broad_mappings": ["PATO:0000161"],
            "related_mappings": ["GO:0120197"]
        },
        "goblet_cell_count": {
            "broad_mappings": ["PATO:0000070"],
            "related_mappings": ["CL:0000160"]
        },
        "mucin_expression_level": {
            "broad_mappings": ["PATO:0000070"],
            "related_mappings": ["GO:0070254"]
        },
        "mucin_protein_concentration": {
            "broad_mappings": ["PATO:0000033"],
            "related_mappings": ["CHEBI:36080"]
        },
        "ros_level": {
            "broad_mappings": ["PATO:0000070"],
            "related_mappings": ["CHEBI:26523"]
        },
        "lipid_peroxidation": {
            "broad_mappings": ["PATO:0000001"],
            "related_mappings": ["GO:0016491"]
        },
        "antioxidant_capacity": {
            "broad_mappings": ["PATO:0000001"],
        },
        "percentage_ciliated_cells": {
            "broad_mappings": ["PATO:0001555"],
            "related_mappings": ["CL:0000064"]
        },
        "active_area_percentage": {
            "broad_mappings": ["PATO:0001555"],
        },
        "goblet_to_ciliated_ratio": {
            "broad_mappings": ["PATO:0001470"],
            "related_mappings": ["CL:0000160", "CL:0000064"]
        },
        "fev1": {
            "broad_mappings": ["PATO:0000918"],
        },
        "fvc": {
            "broad_mappings": ["PATO:0000918"],
        },
        "fev1_fvc_ratio": {
            "broad_mappings": ["PATO:0001470"],
        },
        "viability_percentage": {
            "broad_mappings": ["PATO:0001421"],
        },
        "cytokine_levels": {
            "broad_mappings": ["PATO:0000033"],
            "related_mappings": ["CHEBI:23530"]
        },
        "protein_concentration": {
            "broad_mappings": ["PATO:0000033"],
            "related_mappings": ["CHEBI:36080"]
        },
        "cell_free_dna": {
            "broad_mappings": ["PATO:0000033"],
            "related_mappings": ["CHEBI:16991"]
        },
        "mucus_layer_thickness": {
            "broad_mappings": ["PATO:0000915"],
        },
        "bacterial_load": {
            "broad_mappings": ["PATO:0000070"],
        },
        "biofilm_clearance_rate": {
            "broad_mappings": ["PATO:0000161"],
        },
        "viral_spread_rate": {
            "broad_mappings": ["PATO:0000161"],
        },
        "teer_value": {
            "broad_mappings": ["PATO:0001025"],
        },
        "permeability_coefficient": {
            "broad_mappings": ["PATO:0000001"],
        },
        "ldh_release": {
            "broad_mappings": ["PATO:0000070"],
            "related_mappings": ["CHEBI:17660"]
        },
        "directionality": {
            "broad_mappings": ["PATO:0001527"],
        },
        "ciliary_motion_patterns": {
            "broad_mappings": ["PATO:0000001"],
            "related_mappings": ["GO:0003341"]
        },
    }
    
    return mappings

def main():
    print("Generating ontology mappings for schema slots...")
    print("=" * 70)
    
    mappings = generate_slot_mappings()
    
    output_dir = "examples/ontology_mappings"
    os.makedirs(output_dir, exist_ok=True)
    
    json_path = f"{output_dir}/slot_mappings_improved.json"
    with open(json_path, 'w') as f:
        json.dump(mappings, f, indent=2)
    print(f"\n✓ Saved JSON to: {json_path}")
    
    all_terms = set()
    for slot_data in mappings.values():
        for mapping_list in slot_data.values():
            all_terms.update(mapping_list)
    
    print(f"\nFetching labels for {len(all_terms)} unique ontology terms...")
    print("(This may take a minute...)")
    
    term_labels = {}
    for i, term_id in enumerate(sorted(all_terms), 1):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(all_terms)}")
        
        label = get_term_label(term_id)
        if label:
            term_labels[term_id] = label
        else:
            term_labels[term_id] = get_fallback_label(term_id)
        
        time.sleep(0.3)
    
    csv_path = f"{output_dir}/slot_mappings_improved.csv"
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Slot Name", "Mapping Type", "Ontology Term ID", "Term Label"])
        
        for slot_name, mapping_data in sorted(mappings.items()):
            for mapping_type in ["exact_mappings", "narrow_mappings", "broad_mappings", "related_mappings"]:
                if mapping_type in mapping_data:
                    for term_id in mapping_data[mapping_type]:
                        label = term_labels.get(term_id, "")
                        writer.writerow([slot_name, mapping_type, term_id, label])
    
    print(f"✓ Saved CSV with labels to: {csv_path}")
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total slots mapped: {len(mappings)}")
    print(f"Total ontology terms: {len(all_terms)}")
    print(f"\nKey improvements:")
    print("  • Uses PATO terms for qualities (height, concentration, frequency, etc.)")
    print("  • UO terms only for has_unit slot in QuantityValue")
    print("  • Labels fetched from OLS API")
    print("\nDone!")

if __name__ == "__main__":
    main()
