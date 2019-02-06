import csv
import os
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
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)

    total_pl = []
    temp = 0

    for row in csvreader:
        if temp!=0:
            total_pl.append(int(row[1])-temp)
        temp = int(row[1])
    print("Average  Change: $" + str(sum(total_pl)/ len(total_pl)))

#The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: " + str(max(total_pl)))
#The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Profits: " + str(min(total_pl)))