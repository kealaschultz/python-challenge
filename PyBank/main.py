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
    month = []
    temp = 0

    for row in csvreader:
        if temp!=0:
            total_pl.append(int(row[1])-temp)
            month.append(row[0])
        temp = int(row[1])


    print("Average  Change: $" + str(sum(total_pl)/ len(total_pl)))

#The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: " + str(month[total_pl.index(max(total_pl))]) + " ($" + str(max(total_pl)) + ")")

#The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Profits: " +  str(month[total_pl.index(min(total_pl))]) + " ($" + str(min(total_pl)) + ")")

#Export
totalTitles = ["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"]
totalAmounts = ["86", "$38382578", "$-2315.12","Feb-2012 ($1926159)","Sep-2013 ($-2196167)"]

results = zip(totalTitles, totalAmounts)

output_file = os.path.join("output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])

    writer.writerows(results)