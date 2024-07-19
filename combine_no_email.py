import csv
import re

input_file = "cd.csv"
output_file = "cd_no_email.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    for row in reader:
        email = row[3].strip()
        if not email or not re.match(email_regex, email):
            writer.writerow(row)

