# A-Comprehensive-ETL-Workflow-with-Python-for-Data-Engineers
# ETL Pipeline with Python

This project implements a simple ETL (Extract, Transform, Load) pipeline using Python. It extracts data from multiple file formats (CSV, JSON, and XML), transforms the data (converting height and weight units), and then loads the cleaned data into a CSV file. The pipeline also maintains a log of all operations.

## 📁 Project Structure

project/
├── etl_pipeline.py # Main ETL script
├── log_file.txt # Log file (auto-generated)
├── transformed_data.csv # Output file (auto-generated)
├── README.md # This file
└── UNZIPPED/ # Source folder containing CSV, JSON, XML files

markdown
Copy
Edit

## ⚙️ Features

- **Extract** data from:
  - `.csv` files using `pandas`
  - `.json` (newline-delimited) files using `pandas`
  - `.xml` files using `xml.etree.ElementTree`
- **Transform** the data:
  - Height from inches to meters
  - Weight from pounds to kilograms
- **Load** the transformed data into a single `.csv` output
- Logs each step of the pipeline with timestamps

## 🛠️ Requirements

- Python 3.7+
- `pandas`

Install dependencies using pip (if not already installed):

```bash
pip install pandas
🚀 How to Run
Place your input files (.csv, .json, .xml) inside the UNZIPPED directory.

Run the ETL script:

bash
Copy
Edit
python etl_pipeline.py
After execution:

Transformed data will be saved to transformed_data.csv

Logs will be written to log_file.txt

📝 Logging
The script logs important messages to log_file.txt with timestamps, including:

Extraction start and completion

File-specific extraction messages

Transformation and loading stages

Final completion notice
