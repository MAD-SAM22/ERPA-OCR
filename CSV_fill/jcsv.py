import csv
import os
import sys

# Function to append data to the last empty row of a CSV file
def append_json_to_csv(json_data, csv_file):
    # Create directory if it does not exist
    directory = os.path.dirname(csv_file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Open CSV file in append mode
    with open(csv_file, 'a+', newline='') as cfile:
        # Extract the 'invoice' and 'subtotal' keys for CSV rows
        invoice_data = json_data.get('invoice', {})
        items_data = json_data.get('items', [])
        subtotal_data = json_data.get('subtotal', {})
        payment_data = json_data.get('payment_instructions', {})

        # Replace None (null) values with empty strings in each dictionary
        invoice_data = {k: (v if v is not None else '') for k, v in invoice_data.items()}
        subtotal_data = {k: (v if v is not None else '') for k, v in subtotal_data.items()}
        payment_data = {k: (v if v is not None else '') for k, v in payment_data.items()}

        # Define fieldnames for CSV based on the structure of JSON
        fieldnames = ['client_name', 'invoice_number', 'invoice_date', 'due_date',
                      'item_description', 'item_quantity', 'item_total_price',
                      'tax', 'discount', 'total', 'payment_due_date', 'bank_name', 'account_number', 'payment_method']

        # Move to the start of the file to check if it's empty or not
        cfile.seek(0)
        reader = csv.DictReader(cfile)

        # If the CSV is empty, write the headers
        if not reader.fieldnames:
            writer = csv.DictWriter(cfile, fieldnames=fieldnames)
            writer.writeheader()

        writer = csv.DictWriter(cfile, fieldnames=fieldnames)

        # Write each item in 'items' array as a separate row
        for item in items_data:
            item = {k: (v if v is not None else '') for k, v in item.items()}  # Replace None with empty string
            row = {
                'client_name': invoice_data.get('client_name', ''),
                'invoice_number': invoice_data.get('invoice_number', ''),
                'invoice_date': invoice_data.get('invoice_date', ''),
                'due_date': invoice_data.get('due_date', ''),
                'item_description': item.get('description', ''),
                'item_quantity': item.get('quantity', ''),
                'item_total_price': item.get('total_price', ''),
                'tax': subtotal_data.get('tax', ''),
                'discount': subtotal_data.get('discount', ''),
                'total': subtotal_data.get('total', ''),
                'payment_due_date': payment_data.get('due_date', ''),
                'bank_name': payment_data.get('bank_name', ''),
                'account_number': payment_data.get('account_number', ''),
                'payment_method': payment_data.get('payment_method', '')
            }
            writer.writerow(row)

# Example usage
json_file = rf'{sys.argv[1]}'

csv_file = rf'C:\Users\Osama hosam\Desktop\gg\OCR+FormatFilling\OCR+FormatFilling\CSV_fill\data.csv'  # Specify folder in the path

append_json_to_csv(json_file, csv_file)
