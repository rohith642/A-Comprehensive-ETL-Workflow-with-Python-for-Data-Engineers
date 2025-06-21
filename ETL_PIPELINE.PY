import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

# --- Configuration ---
source_dir = r'C:\Users\ROHITH.M\OneDrive\Desktop\A Comprehensive ETL Workflow with Python for Data Engineers\UNZIPPED'
log_file = 'log_file.txt'
output_file = 'transformed_data.csv'

# --- Logging Utility ---
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

# --- Extraction Functions ---
def extract_from_csv(file_path):
    return pd.read_csv(file_path)

def extract_from_json(file_path):
    return pd.read_json(file_path, lines=True)

def extract_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    for record in root.findall('record'):
        entry = {
            'name': record.find('name').text,
            'height': float(record.find('height').text),
            'weight': float(record.find('weight').text)
        }
        data.append(entry)
    return pd.DataFrame(data)

def extract():
    log("Extraction phase started.")
    extracted_data = pd.DataFrame()
    for file in glob.glob(f"{source_dir}/*"):
        if file.endswith('.csv'):
            log(f"Extracting from CSV: {file}")
            extracted_data = pd.concat([extracted_data, extract_from_csv(file)], ignore_index=True)
        elif file.endswith('.json'):
            log(f"Extracting from JSON: {file}")
            extracted_data = pd.concat([extracted_data, extract_from_json(file)], ignore_index=True)
        elif file.endswith('.xml'):
            log(f"Extracting from XML: {file}")
            extracted_data = pd.concat([extracted_data, extract_from_xml(file)], ignore_index=True)
    log("Extraction phase completed.")
    return extracted_data

# --- Transformation Function ---
def transform(data):
    log("Transformation phase started.")
    # Convert height from inches to meters (1 inch = 0.0254 meters)
    data['height'] = data['height'] * 0.0254
    # Convert weight from pounds to kilograms (1 pound = 0.453592 kilograms)
    data['weight'] = data['weight'] * 0.453592
    log("Transformation phase completed.")
    return data

# --- Load Function ---
def load(data):
    log("Loading phase started.")
    data.to_csv(output_file, index=False)
    log(f"Data successfully written to {output_file}.")
    log("Loading phase completed.")

# --- ETL Pipeline ---
def run_etl():
    log("ETL job started.")
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load(transformed_data)
    log("ETL job finished.")

if __name__ == "__main__":
    run_etl()
