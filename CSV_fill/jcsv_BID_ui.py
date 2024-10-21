import csv
import os
import json
import sys

def append_json_to_csv(json_data, csv_file):
    directory = os.path.dirname(csv_file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    if isinstance(json_data, str):
        try:
            json_dict = json.loads(json_data)
        except json.JSONDecodeError:
            print("Error: The provided string is not valid JSON.")
            return
    elif isinstance(json_data, dict):
        json_dict = json_data
    else:
        print("Error: The input data is neither a JSON string nor a dictionary.")
        return

    file_exists = os.path.isfile(csv_file)
    with open(csv_file, 'a+', newline='') as cfile:
        cfile.seek(0)
        reader = csv.DictReader(cfile)
        
        fieldnames = ['nome', 'filiciao', 'data de expedicao', 'Naturalidade',
                      'Data de nascimento', 'CPF']

        if not file_exists or not reader.fieldnames:
            writer = csv.DictWriter(cfile, fieldnames=fieldnames)
            writer.writeheader()
            print("Created new CSV with headers.")
        else:
            writer = csv.DictWriter(cfile, fieldnames=fieldnames)

        data = json_dict  # Use the entire JSON directly

        data = {k: (v if v is not None and v != 'null' else '') for k, v in data.items()}

        row = {
            'nome': data.get('nome', ''),
            'filiciao': data.get('filiciao', ''),
            'data de expedicao': data.get('data de expedicao', ''),
            'Naturalidade': data.get('Naturalidade', ''),
            'Data de nascimento': data.get('Data de nascimento', ''),
            'CPF': data.get('CPF', '')
        }
        writer.writerow(row)

json_file = rf'{sys.argv[1]}'
csv_file = rf'D:\Grad\OCR-RPA\CSV_fill\data_BID.csv'
append_json_to_csv(json_file, csv_file)
