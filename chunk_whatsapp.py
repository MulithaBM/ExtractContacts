# Separate contacts into groups of fixed size to create Whatsapp groups

import csv
import os

input_file = 'cd_mobile_final.csv'
output_folder = 'Mobile Groups'
chunk_size = 1000

os.makedirs(output_folder, exist_ok=True)

with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)[:2]

    chunk_num = 1
    chunk = []
    for row in reader:
        row[0] = "WGM" + str(chunk_num) + " - " + row[0]
        chunk.append([row[0], row[1]])
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