# Bell S, Daskalopoulou M, Rapsomaniki E, George J, Britton A, Bobak M, Casas JP, Dale CE, Denaxas S, Shah AD, Hemingway H, 2024.

import sys, csv, re

codes = [{"code":"E250.13","system":"readv2"},{"code":"E250.11","system":"readv2"},{"code":"13ZY.00","system":"readv2"},{"code":"136V.00","system":"readv2"},{"code":"1368","system":"readv2"},{"code":"1D19.00","system":"readv2"},{"code":"136Z.00","system":"readv2"},{"code":"136W.00","system":"readv2"},{"code":"136S.00","system":"readv2"},{"code":"G555.00","system":"readv2"},{"code":"J153.00","system":"readv2"},{"code":"F144000","system":"readv2"},{"code":"F394100","system":"readv2"},{"code":"Eu10512","system":"readv2"},{"code":"F375.00","system":"readv2"},{"code":"E01..00","system":"readv2"},{"code":"J613000","system":"readv2"},{"code":"Eu10511","system":"readv2"},{"code":"F11x011","system":"readv2"},{"code":"F11x000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcohol-consumption-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcohol-consumption---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcohol-consumption---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcohol-consumption---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
