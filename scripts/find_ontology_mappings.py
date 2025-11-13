#!/usr/bin/env python3
"""
Find ontology terms for slot definitions and value constraints using OLS API.
"""

import requests
import json
import csv
import time
from typing import Dict, List, Optional

OLS_API_BASE = "https://www.ebi.ac.uk/ols4/api"

def search_ols(query: str, ontologies: List[str] = None, exact: bool = False) -> List[Dict]:
    """Search OLS for terms matching the query."""
    url = f"{OLS_API_BASE}/search"
    params = {
        "q": query,
        "rows": 10,
        "exact": str(exact).lower()
    }
    if ontologies:
        params["ontology"] = ",".join(ontologies)
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        results = []
        if "response" in data and "docs" in data["response"]:
            for doc in data["response"]["docs"]:
                results.append({
                    "iri": doc.get("iri"),
                    "obo_id": doc.get("obo_id"),
                    "label": doc.get("label"),
                    "description": doc.get("description", [""])[0] if doc.get("description") else "",
                    "ontology_name": doc.get("ontology_name"),
                    "ontology_prefix": doc.get("ontology_prefix")
                })
        return results
    except Exception as e:
        print(f"Error searching for '{query}': {e}")
        return []

def find_slot_definition_terms():
    """Find ontology terms that define what slots ARE."""
    slot_searches = [
        # Measurement process concepts
        ("assay", ["OBI"], "assay_type slot definition"),
        ("measurement datum", ["IAO", "OBI"], "measurement value slot definition"),
        ("protocol", ["OBI", "IAO"], "protocol_notes slot definition"),
        ("material entity", ["OBI", "BFO"], "input_sample slot definition"),
        ("instrument", ["OBI"], "instrumentation slot definition"),
        ("data item", ["IAO"], "generic data slot definition"),
        
        # Sample-related
        ("specimen", ["OBI"], "sample_type slot definition"),
        ("biological sample", ["OBI"], "biological sample slot"),
        
        # Method-related
        ("planned process", ["OBI"], "method slot definition"),
        ("assay", ["OBI"], "method_assay slot definition"),
        
        # Documentation
        ("document", ["IAO"], "documentation slot definition"),
        ("standard operating procedure", ["OBI"], "sop_reference slot definition"),
    ]
    
    results = {}
    for query, ontologies, purpose in slot_searches:
        print(f"Searching for: {query} ({purpose})")
        terms = search_ols(query, ontologies)
        if terms:
            results[purpose] = terms[:3]  # Top 3 results
        time.sleep(0.5)  # Be nice to the API
    
    return results

def find_value_constraint_terms():
    """Find ontology terms that can constrain slot VALUES."""
    value_searches = [
        # Imaging modalities
        ("confocal microscopy", ["OBI"], "imaging_modality value"),
        ("optical coherence tomography", ["OBI"], "imaging_modality value"),
        ("fluorescence microscopy", ["OBI"], "imaging_modality value"),
        
        # Cell types
        ("epithelial cell", ["CL"], "sample_type value"),
        ("airway epithelial cell", ["CL"], "sample_type value"),
        ("ciliated cell", ["CL"], "sample_type value"),
        ("goblet cell", ["CL"], "sample_type value"),
        
        # Tissue types
        ("airway epithelium", ["UBERON"], "sample_type value"),
        ("respiratory system", ["UBERON"], "sample_type value"),
        
        # Staining methods
        ("immunofluorescence assay", ["OBI"], "staining_type value"),
        ("histological staining", ["OBI"], "staining_type value"),
        
        # Fixation methods
        ("fixation", ["OBI"], "fixation_method value"),
        ("paraformaldehyde", ["CHEBI"], "fixation_method value"),
        
        # Analysis methods
        ("reverse transcription polymerase chain reaction", ["OBI"], "analysis_method value"),
        ("RNA-seq", ["OBI"], "analysis_method value"),
        ("quantitative PCR", ["OBI"], "analysis_method value"),
        
        # Culture conditions
        ("cell culture", ["OBI"], "culture condition"),
        ("culture medium", ["OBI"], "culture_medium value"),
        
        # Units
        ("micrometer", ["UO"], "distance unit"),
        ("hertz", ["UO"], "frequency unit"),
        ("percentage", ["UO"], "ratio unit"),
        
        # Environmental conditions
        ("temperature", ["PATO", "ENVO"], "environmental parameter"),
        ("humidity", ["PATO", "ENVO"], "environmental parameter"),
        
        # Biological processes
        ("cilium movement", ["GO"], "biological process"),
        ("mucus secretion", ["GO"], "biological process"),
    ]
    
    results = {}
    for query, ontologies, purpose in value_searches:
        print(f"Searching for: {query} ({purpose})")
        terms = search_ols(query, ontologies)
        if terms:
            results[purpose] = terms[:3]  # Top 3 results
        time.sleep(0.5)  # Be nice to the API
    
    return results

def format_results_as_csv(slot_defs: Dict, value_constraints: Dict, output_file: str):
    """Format results as CSV."""
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Category",
            "Slot/Value Purpose",
            "Ontology Term Label",
            "Ontology ID",
            "Ontology",
            "Description"
        ])
        
        # Write slot definitions
        for purpose, terms in slot_defs.items():
            for term in terms:
                writer.writerow([
                    "Slot Definition",
                    purpose,
                    term.get("label", ""),
                    term.get("obo_id", term.get("iri", "")),
                    term.get("ontology_prefix", ""),
                    term.get("description", "")[:200]  # Truncate long descriptions
                ])
        
        # Write value constraints
        for purpose, terms in value_constraints.items():
            for term in terms:
                writer.writerow([
                    "Value Constraint",
                    purpose,
                    term.get("label", ""),
                    term.get("obo_id", term.get("iri", "")),
                    term.get("ontology_prefix", ""),
                    term.get("description", "")[:200]
                ])

def format_results_as_markdown(slot_defs: Dict, value_constraints: Dict, output_file: str):
    """Format results as Markdown."""
    with open(output_file, 'w') as f:
        f.write("# Ontology Mappings for Outcomes Schema\n\n")
        
        f.write("## Slot Definition Terms\n\n")
        f.write("These ontology terms define what the slots themselves represent.\n\n")
        
        for purpose, terms in slot_defs.items():
            f.write(f"### {purpose}\n\n")
            for term in terms:
                f.write(f"- **{term.get('label')}** (`{term.get('obo_id', term.get('iri'))}`) - {term.get('ontology_prefix')}\n")
                if term.get('description'):
                    f.write(f"  - {term.get('description')[:200]}\n")
            f.write("\n")
        
        f.write("## Value Constraint Terms\n\n")
        f.write("These ontology terms can be used to constrain the values allowed in slots.\n\n")
        
        # Group by slot type
        grouped_values = {}
        for purpose, terms in value_constraints.items():
            slot_type = purpose.split(" value")[0].split(" ")[-1]
            if slot_type not in grouped_values:
                grouped_values[slot_type] = {}
            grouped_values[slot_type][purpose] = terms
        
        for slot_type, purposes in grouped_values.items():
            f.write(f"### {slot_type}\n\n")
            for purpose, terms in purposes.items():
                f.write(f"**{purpose}**:\n\n")
                for term in terms:
                    f.write(f"- {term.get('label')} (`{term.get('obo_id', term.get('iri'))}`) - {term.get('ontology_prefix')}\n")
                f.write("\n")

def main():
    print("Finding ontology terms for slot definitions...")
    slot_definitions = find_slot_definition_terms()
    
    print("\nFinding ontology terms for value constraints...")
    value_constraints = find_value_constraint_terms()
    
    print("\nGenerating output files...")
    
    # Create output directory
    import os
    output_dir = "examples/ontology_mappings"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save as CSV
    csv_file = f"{output_dir}/ontology_mappings.csv"
    format_results_as_csv(slot_definitions, value_constraints, csv_file)
    print(f"CSV saved to: {csv_file}")
    
    # Save as Markdown
    md_file = f"{output_dir}/ontology_mappings.md"
    format_results_as_markdown(slot_definitions, value_constraints, md_file)
    print(f"Markdown saved to: {md_file}")
    
    # Save raw JSON for reference
    json_file = f"{output_dir}/ontology_mappings.json"
    with open(json_file, 'w') as f:
        json.dump({
            "slot_definitions": slot_definitions,
            "value_constraints": value_constraints
        }, f, indent=2)
    print(f"JSON saved to: {json_file}")
    
    print("\nDone!")

if __name__ == "__main__":
    main()
