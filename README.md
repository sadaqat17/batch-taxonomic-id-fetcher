# Batch Taxonomic ID Fetcher

This repository contains a Python script to fetch taxonomic IDs from NCBI in batch. It is designed for users who need to process multiple species or genera efficiently.

## Features
- Fetch taxonomic IDs for species or genera using the NCBI taxonomy database.
- Batch processing from an input file.
- Outputs results to a CSV file for easy analysis.

## Prerequisites
- Python 3.x
- [Biopython](https://biopython.org/) library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/batch-taxonomic-id-fetcher.git
   cd batch-taxonomic-id-fetcher
   ```
2. Install the required Python library:
   ```bash
   pip install biopython
   ```

## Usage
1. Prepare an input file `species_list.txt` with a list of species or genera (one per line). Example:
   ```
   Homo sapiens
   Canis lupus
   Felis catus
   Panthera leo
   ```
2. Run the script:
   ```bash
   python fetch_tax_ids.py
   ```
3. The script will generate a CSV file `taxonomic_ids.csv` with the results.

## Output Format
The output CSV file will have two columns:
- **Species/Genus**: The name of the species or genus queried.
- **Taxonomic ID**: The corresponding NCBI Taxonomic ID, or `Not Found` if the species/genus is not in the database.

Example output:
Species/Genus,Taxonomic ID Homo sapiens,9606 Canis lupus,9612 Felis catus,9685 Panthera leo,9689


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

## Acknowledgments
- Developed using the [Biopython](https://biopython.org/) library.
- Data retrieved from the [NCBI Taxonomy Database](https://www.ncbi.nlm.nih.gov/taxonomy).

