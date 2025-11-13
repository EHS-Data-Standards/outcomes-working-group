#!/usr/bin/env python3
"""
Apply ontology mappings from CSV to the LinkML schema.
"""

import csv
import yaml
from collections import defaultdict

def load_mappings_from_csv(csv_path: str) -> dict:
    """Load mappings from CSV into a structured dictionary."""
    mappings = defaultdict(lambda: defaultdict(list))
    
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slot_name = row['Slot Name']
            mapping_type = row['Mapping Type']
            term_id = row['Ontology Term ID']
            
            if term_id and slot_name and mapping_type:
                mappings[slot_name][mapping_type].append(term_id)
    
    return dict(mappings)

def apply_mappings_to_schema(schema_path: str, mappings: dict, output_path: str):
    """Apply mappings to schema slots."""
    
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)
    
    if 'slots' not in schema:
        print("ERROR: No slots section found in schema")
        return
    
    slots_updated = 0
    slots_not_found = []
    
    for slot_name, mapping_data in mappings.items():
        if slot_name in schema['slots']:
            for mapping_type, term_ids in mapping_data.items():
                schema['slots'][slot_name][mapping_type] = term_ids
            slots_updated += 1
        else:
            slots_not_found.append(slot_name)
    
    with open(output_path, 'w') as f:
        yaml.dump(schema, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"✓ Updated {slots_updated} slots with ontology mappings")
    
    if slots_not_found:
        print(f"\n⚠ Warning: {len(slots_not_found)} slots from CSV not found in schema:")
        for slot in sorted(slots_not_found):
            print(f"  - {slot}")
    
    print(f"\n✓ Schema saved to: {output_path}")

def main():
    csv_path = "examples/ontology_mappings/slot_mappings_improved.csv"
    schema_path = "src/outcomes_working_group/schema/outcomes_working_group.yaml"
    output_path = schema_path
    
    print("Applying ontology mappings to schema...")
    print("=" * 70)
    
    print(f"\nLoading mappings from: {csv_path}")
    mappings = load_mappings_from_csv(csv_path)
    print(f"✓ Loaded mappings for {len(mappings)} slots")
    
    mapping_type_counts = defaultdict(int)
    total_terms = 0
    for slot_data in mappings.values():
        for mapping_type, terms in slot_data.items():
            mapping_type_counts[mapping_type] += len(terms)
            total_terms += len(terms)
    
    print(f"\nMapping breakdown:")
    for mapping_type in ["exact_mappings", "narrow_mappings", "broad_mappings", "related_mappings"]:
        if mapping_type in mapping_type_counts:
            print(f"  {mapping_type}: {mapping_type_counts[mapping_type]}")
    print(f"  Total: {total_terms}")
    
    print(f"\nApplying to schema: {schema_path}")
    apply_mappings_to_schema(schema_path, mappings, output_path)
    
    print("\n" + "=" * 70)
    print("Done!")

if __name__ == "__main__":
    main()
