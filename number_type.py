# Split contacts with phone numbers into fixed and mobile

import csv

mobile_codes = ["70", "71", "72", "73", "74", "75", "76", "77", "78"]

fixed_line_codes = ["63", "25", "36", "55", "57", "65", "32", "11", "91", "33", "47", "51", "21", "67", "34", "81", "35", "37", "23", "66", "41", "54", "31", "52", "38", "27", "45", "26", "24"]

def split_by_type():
    input_file = "cd_telephone_final.csv"
    output_file = "cd_mobile_final.csv"
    output_file2 = "cd_fixed_final.csv"

    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile, open(output_file2, "w", newline="") as outfile2:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer2 = csv.writer(outfile2)

        header = next(reader)
        writer.writerow(header)
        writer2.writerow(header)

        for row in reader:
            number = row[1].strip()
            if (len(number) == 11):
                if (number[2:4] in mobile_codes):
                    writer.writerow(row)
                elif (number[2:4] in fixed_line_codes):
                    writer2.writerow(row)
            
split_by_type()