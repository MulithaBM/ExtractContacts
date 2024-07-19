import pandas as pd
import csv

csv_files = ['data.csv', 'data0.csv', 'data1.csv', 'data2.csv']

combined_records = []

max_fields = 0
for file in csv_files:
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            max_fields = max(max_fields, len(row))

for file in csv_files:
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            row += [''] * (max_fields - len(row))
            combined_records.append(row)

combined_data = pd.DataFrame(combined_records)

combined_data.to_csv('combined_data.csv', index=False)

print(combined_data)