import json
import csv
import sys
import os

# Get JSON filename from user
if len(sys.argv) > 1:
    json_filename = sys.argv[1]
else:
    json_filename = input("Enter the JSON filename (e.g., search_results.json): ").strip()

# Validate file exists
if not os.path.exists(json_filename):
    print(f"Error: File '{json_filename}' not found.")
    sys.exit(1)

# Validate file has .json extension
if not json_filename.lower().endswith('.json'):
    print(f"Warning: File '{json_filename}' does not have a .json extension.")
    proceed = input("Continue anyway? (y/n): ").strip().lower()
    if proceed != 'y':
        sys.exit(0)

# Read the JSON file
try:
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON format in '{json_filename}': {e}")
    sys.exit(1)

# Define CSV output file (replace .json with .csv)
csv_filename = json_filename.rsplit('.', 1)[0] + '.csv'

# Extract all unique keys from the nested structure
# We'll flatten the result_metadata into separate columns
fieldnames = ['title', 'body', 'score', 'document_retrieval_source']

# Write to CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write data rows
    for item in data:
        row = {
            'title': item.get('title', ''),
            'body': item.get('body', ''),
            'score': item.get('result_metadata', {}).get('score', ''),
            'document_retrieval_source': item.get('result_metadata', {}).get('document_retrieval_source', '')
        }
        writer.writerow(row)

print(f"Successfully converted {json_filename} to {csv_filename}")
print(f"Total records: {len(data)}")

# Made with Bob
