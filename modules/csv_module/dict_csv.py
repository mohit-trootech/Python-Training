import csv

with open("timezone.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        # if line_count == 0:
        #     i, j, k = row.keys()
        #     print(f"Sr.No \t{i} \t{j} \t{k}".expandtabs(30))
        #     line_count += 1
        # print(
        #     f'{line_count} \t{row["Value"]} \t{row["Label"]} \t{row["Group"]}.'.expandtabs(
        #         30
        #     )
        # )
        if row["Label"].lower() == "kolkata":
            print(row)
            break
        line_count += 1
    print(f"Processed {line_count} lines.")
