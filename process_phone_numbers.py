import csv

def single_number(phone_number):
    if len(phone_number) == 9:
            if (phone_number.isdigit() and not phone_number.startswith("0")):
                return "94" + phone_number

    elif len(phone_number) == 10:
        if phone_number.isdigit():
            if phone_number.startswith("0"):
                return "94" + phone_number[1:]
        else:
            if not phone_number.startswith("0") and phone_number[3] in ["-", " "] and phone_number[:3].isdigit() and phone_number[4:].isdigit():
                phone_number = phone_number.replace("-", "").replace(" ", "")
                return "94" + phone_number

    elif len(phone_number) == 11:
        if phone_number.startswith("0") and phone_number[3] in ["-", " "] and phone_number[:3].isdigit() and phone_number[4:].isdigit():
            phone_number = phone_number.replace("-", "").replace(" ", "")
            return "94" + phone_number[1:]

    return None

def is_valid_phone_number(phone_number):
    phone_numbers = []

    if (len(phone_number) >= 9):
        if (len(phone_number) <= 11):
            phone_number = single_number(phone_number)
            if (phone_number):
                phone_numbers.append(phone_number)

        else:
            numbers = []

            if "/" in phone_number:
                numbers = phone_number.split("/")
            elif " " in phone_number:
                numbers = phone_number.split(maxsplit=1)

            numbers = [number.strip() for number in numbers]

            for n in numbers:
                if (len(n) >= 9 and len(n) <= 11):
                    number = single_number(n)
                    if (number):
                        phone_numbers.append(number)

    return phone_numbers

def process_csv(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)

        header[0] = "Name"
        header[1] = "Phone"

        writer.writerow(header)

        for row in reader:
            phone_number = row[1].strip()
            phone_numbers = is_valid_phone_number(phone_number)
            
            for number in phone_numbers:
                row[1] = number
                writer.writerow(row)

# Example usage
input_file = "cd_mobile_f1.csv"
output_file = "cd_telephone_final.csv"
process_csv(input_file, output_file)
