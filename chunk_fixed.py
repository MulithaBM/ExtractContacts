import csv
import os

input_file = 'cd_fixed_final.csv'
output_folder = 'Chunked'
chunk_size = 1000

os.makedirs(output_folder, exist_ok=True)

with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)

    chunk_num = 1
    chunk = []
    for row in reader:
        chunk.append(row)
        if len(chunk) == chunk_size:
            output_file = f'{output_folder}/file_{chunk_num}.csv'
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)
                writer.writerows(chunk)
            chunk = []
            chunk_num += 1

    if chunk:
        output_file = f'{output_folder}/file_{chunk_num}.csv'
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(chunk)
