import json
import csv

# Read the JSON file
with open('search_results.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Define CSV output file
csv_filename = 'search_results.csv'

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

print(f"Successfully converted search_results.json to {csv_filename}")
print(f"Total records: {len(data)}")

# Made with Bob
