import csv
with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Year","Class"])

import csv
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
