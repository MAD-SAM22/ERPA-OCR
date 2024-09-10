# Append JSON Data to CSV

This Python script appends data from a JSON to a CSV file. It handles the creation of directories if they don't exist and writes data to a CSV file in append mode. It replaces any `None` (null) values in the JSON data with empty strings.

## Requirements

- Python 3.x
- No additional packages are required beyond the standard library.

## Script Overview

1. **Function Definition**: The `append_json_to_csv` function processes the JSON data and appends it to the specified CSV file.
2. **Directory Creation**: The script ensures that the directory for the CSV file exists.
3. **File Handling**: It opens the CSV file in append mode and writes the data.
4. **Data Processing**: It extracts relevant fields from the JSON data and writes them to the CSV file.

## Function: `append_json_to_csv`

### Parameters

- `json_data` (dict): The JSON data to be appended to the CSV.
- `csv_file` (str): The path to the CSV file.

### Process

1. **Create Directory**: Checks if the directory for the CSV file exists, and creates it if it does not.
2. **Open CSV File**: Opens the CSV file in append mode.
3. **Read Data**: Reads the JSON data and processes it.
4. **Handle Empty CSV**: If the CSV file is empty, writes headers.
5. **Write Data**: Writes each item from the `items` array in the JSON data as a separate row in the CSV.
6. **look for last row** : the code go directly to the last empty row and full-fill it with the data.

### Example Usage

```python
import sys

json_file = rf'{sys.argv[1]}'
csv_file = rf'{ur path}'

append_json_to_csv(json_file, csv_file)
