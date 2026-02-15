#!/usr/bin/env python3
"""
Export Room Profiles to OTA-compatible CSV formats
Usage: python3 export-ota.py [expedia|booking|all]

Extracts data from rooms.md YAML blocks + OTA fields
"""

import re
import csv
import sys
from pathlib import Path

ROOMS_FILE = Path(__file__).resolve().parents[2] / "data/core/property/inventory/rooms/rooms.md"
OUTPUT_DIR = Path(__file__).parent

def extract_yaml_data(content):
    """Extract key fields from all YAML blocks"""
    # Find all YAML blocks
    pattern = r'### (R\d+).*?```yaml\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    rooms = []
    for room_id, yaml_block in matches:
        # Parse max_occupancy
        occ_match = re.search(r'max_occupancy:\s*(\d+)', yaml_block)
        max_occupancy = occ_match.group(1) if occ_match else ''
        
        # Parse beds - handle multi-line format
        beds = []
        # Find all bed entries
        bed_blocks = re.findall(r'- type:\s*(\w+)(?:.*?size_cm:\s*(\d+))?.*?count:\s*(\d+)', yaml_block, re.DOTALL)
        for bed_type, size_cm, count in bed_blocks:
            bed_type_clean = bed_type.replace('_', ' ').title()
            beds.append(f"{count}x {bed_type_clean}")
        
        # Parse size
        size_match = re.search(r'size_m2:\s*(\d+)', yaml_block)
        size = size_match.group(1) if size_match else ''
        
        rooms.append({
            'room_id': room_id,
            'max_occupancy': max_occupancy,
            'bed_type': '; '.join(beds) if beds else '',
            'size_m2': size
        })
    
    return rooms

def extract_ota_fields(content):
    """Extract OTA-specific fields from rooms.md"""
    # Match each room section's OTA fields
    pattern = r'### (R\d+ — [^\n]+)\n.*?\*\*Expedia Title\*\*:\s*([^(\n]+)\s*\((\d+) chars\).*?\*\*Booking\.com Title\*\*:\s*([^(\n]+)\s*\((\d+) chars\).*?\*\*Short Description \(EN\)\*\*:\s*([^(\n]+)\s*\((\d+) chars\).*?\*\*Short Description \(FR\)\*\*:\s*([^(\n]+)\s*\((\d+) chars\)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    return [{
        'room_id': m[0].split()[0],
        'room_name': m[0].split(' — ')[1] if ' — ' in m[0] else m[0],
        'expedia_title': m[1].strip(),
        'booking_title': m[3].strip(),
        'short_desc_en': m[5].strip(),
        'short_desc_fr': m[7].strip()
    } for m in matches]

def merge_data(ota_data, yaml_data):
    """Merge OTA fields with YAML data"""
    yaml_lookup = {r['room_id']: r for r in yaml_data}
    merged = []
    for ota in ota_data:
        room_id = ota['room_id']
        yaml_info = yaml_lookup.get(room_id, {})
        merged.append({
            **ota,
            'max_occupancy': yaml_info.get('max_occupancy', ''),
            'bed_type': yaml_info.get('bed_type', ''),
            'size_m2': yaml_info.get('size_m2', '')
        })
    return merged

def export_expedia(merged_data):
    """Export Expedia-compatible CSV"""
    output_file = OUTPUT_DIR / "expedia-room-listings.csv"
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Room ID', 
            'Room Name', 
            'Title', 
            'Description (EN)', 
            'Description (FR)', 
            'Max Occupancy', 
            'Bed Type',
            'Size (m²)'
        ])
        
        for room in merged_data:
            writer.writerow([
                room['room_id'],
                room['room_name'],
                room['expedia_title'],
                room['short_desc_en'],
                room['short_desc_fr'],
                room['max_occupancy'],
                room['bed_type'],
                room['size_m2']
            ])
    
    print(f"✓ Exported Expedia CSV: {output_file}")
    return output_file

def export_booking(merged_data):
    """Export Booking.com-compatible CSV"""
    output_file = OUTPUT_DIR / "booking-room-listings.csv"
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Room ID', 
            'Room Name', 
            'Title (FR)', 
            'Description (EN)', 
            'Description (FR)', 
            'Max Guests', 
            'Bed Configuration',
            'Size (m²)'
        ])
        
        for room in merged_data:
            writer.writerow([
                room['room_id'],
                room['room_name'],
                room['booking_title'],
                room['short_desc_en'],
                room['short_desc_fr'],
                room['max_occupancy'],
                room['bed_type'],
                room['size_m2']
            ])
    
    print(f"✓ Exported Booking.com CSV: {output_file}")
    return output_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 export-ota.py [expedia|booking|all]")
        sys.exit(1)
    
    platform = sys.argv[1].lower()
    
    with open(ROOMS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    ota_data = extract_ota_fields(content)
    yaml_data = extract_yaml_data(content)
    merged_data = merge_data(ota_data, yaml_data)
    
    if not merged_data:
        print("ERROR: No data found in rooms.md")
        sys.exit(1)
    
    print(f"Found {len(merged_data)} room profiles")
    print(f"  OTA fields: {len(ota_data)}")
    print(f"  YAML blocks: {len(yaml_data)}\n")
    
    if platform in ('expedia', 'all'):
        export_expedia(merged_data)
    
    if platform in ('booking', 'all'):
        export_booking(merged_data)
    
    print("\nDone. CSV files ready for OTA upload.")

if __name__ == '__main__':
    main()
