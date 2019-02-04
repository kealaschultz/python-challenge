import csv
import os
import collections
count = 0
count = count - 1

election_data_csv = os.path.join("election_data.csv")

print("Election Results")
print("-----------------------")

#Total Votes
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        count += 1
print("Total Votes: " + str(count))
print("-----------------------")

#Candidates

with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    candidatesRoster = []
    for row in csvreader:
        candidatesRoster.append(row[2])
    candidates = set(candidatesRoster)
#    print(*candidates, sep = "\n")

#The percentage of votes each candidate won

otooleyCount = 0
with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if  row[2] == "O'Tooley":
            otooleyCount += 1
#print(otooleyCount)

correyCount = 0
with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if  row[2] == "Correy":
            correyCount += 1
#print(correyCount)

liCount = 0
with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if  row[2] == "Li":
            liCount += 1
#print(liCount)

khanCount = 0
with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if  row[2] == "Khan":
            khanCount += 1
#print(khanCount)

khanPercentage = round(khanCount/count * 100,3)
correyPercentage = round(correyCount/count * 100,3)
liPercentage = round(liCount/count * 100,3)
otooleyPercentage = round(otooleyCount/count * 100,3)


#Final Results
print("Khan: " + str(khanPercentage) + '% (' + str(khanCount) + ')')
print("Correy: " + str(correyPercentage) + '% (' + str(correyCount) + ')')
print("Li: " + str(liPercentage) + '% (' + str(liCount) + ')')
print("O'Tooley: " + str(otooleyPercentage) + '% (' + str(otooleyCount) + ')')
print("-----------------------")

if khanCount > correyCount and khanCount > liCount and khanCount > otooleyCount:
    print("Winner: Khan")
elif correyCount > khanCount and correyCount > liCount and correyCount > otooleyCount:
    print("Winner: Correy")
elif liCount > khanCount and liCount > correyCount and liCount > otooleyCount:
    print("Winner: Li")
else:
    print("Winner: O'Tooley")
print("-----------------------")

Candidate = ["Khan", "Correy", "Li", "O'Tooley"]
PercentOfVotes = ["63.0%", "20.0%", "14.0%", "3.0%"]
TotalNumberOfVotes = ["2218231", "704200", "492940", "105630"]

results = zip(Candidate, PercentOfVotes, TotalNumberOfVotes)

output_file = os.path.join("output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Candidates", "Percent of Votes", "Total Number of Votes"])

    writer.writerows(results)
