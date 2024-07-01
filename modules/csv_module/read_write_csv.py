"""
read CSV files using the csv.reader object from Python’s csv module.
"""

import csv

with open("timezone.csv", "r") as f:
    csv_data = csv.reader(f)
    print(csv_data)
    with open("newtimezone1.csv", "w") as fw:
        writer_obj = csv.writer(fw)
        writer_obj.writerows(csv_data)

    # for row in x:
    #     print(row)
