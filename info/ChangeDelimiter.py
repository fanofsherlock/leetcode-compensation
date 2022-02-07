import csv

with open("./data/out/lc_updated.csv", "rU") as og_file:
    reader = csv.reader(og_file, delimiter=',')
    with open("./data/out/lc_updated_delimiter.csv", "w") as new_file:
        writer = csv.writer(new_file, delimiter='#')
        writer.writerows(reader)
        print("Delimiter successfully changed")
