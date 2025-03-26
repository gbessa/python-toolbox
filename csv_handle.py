import csv

file = open("data/intergalactic_trade.csv", "r")

csv_reader = csv.DictReader(file)

intergalactic_trade_list = []

for row in csv_reader:
    intergalactic_trade_list.append(row)

file.close()

for trade in intergalactic_trade_list:
    print(trade)

def read_csv(file):
    f = open(file, "r")

    csv_reader = csv.DictReader(f)
    data = []
    for row in csv_reader:
        data.append(row)
    f.close()

    return data

print(read_csv("data/intergalactic_trade.csv"))