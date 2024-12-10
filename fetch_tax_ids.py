from Bio import Entrez
import csv

# Set your email to comply with NCBI requirements
Entrez.email = "your_email@example.com"

# Function to fetch TaxID for a given query (species or genus)
def fetch_tax_id(query):
    try:
        handle = Entrez.esearch(db="taxonomy", term=query)
        record = Entrez.read(handle)
        handle.close()
        if record["IdList"]:
            return record["IdList"][0]  # Return the first TaxID
        else:
            return "Not Found"
    except Exception as e:
        return f"Error: {e}"

# Read species list from file
input_file = "species_list.txt"  # Update to your file path
output_file = "taxonomic_ids.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = infile.readlines()
    writer = csv.writer(outfile)
    writer.writerow(["Species/Genus", "Taxonomic ID"])  # Header

    for line in reader:
        query = line.strip()  # Remove whitespace
        if query:
            tax_id = fetch_tax_id(query)
            print(f"Processing: {query} -> TaxID: {tax_id}")
            writer.writerow([query, tax_id])  # Write to CSV

print(f"Taxonomic IDs saved to {output_file}")
