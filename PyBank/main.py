import csv
import os
import pandas as pd
count = 0

budget_csv = os.path.join("budget_data.csv")

print("Financial Analysis")
print("-----------------------")

#Total Months
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        count += 1
print("Total Months: " + str(count - 1))

#Profit/Loss Total
a = []
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)

    for row in csvreader:
      a.append (int(row[1]))
    total = sum(a)
print("Total: $" + str(total))

#Average Change

for x in range(2,87)
    lastrowamount = int(row[1])
    currentavg = int(row[1]) - lastrowamount
#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period