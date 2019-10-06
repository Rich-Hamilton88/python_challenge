import csv
import os


Candidates = []
Votes = []
Vote_Count = 0
Winner_Votes = 0

data = os.path.join('C:\\Users\\richn\\Desktop\\', 'LearnPython', 'election_data.csv')

with open(data, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    for row in csvreader:
        
        Vote_Count += 1
        
        if Candidates.count(row[2]) == 0:
            Candidates.append(row[2])
            Votes.append(1)
        else:
            
            Votes[Candidates.index(row[2])] += 1


print("Election Results")
print("--------------------------")
print(f"Total Votes: {Vote_Count}")
print("--------------------------")

for n in range(len(Candidates)):
    
    print(f"{Candidates[n]}: {(100*Votes[n]/Vote_Count):.3f}% ({Votes[n]})")
    
    if Votes[n] > Winner_Votes:
        WinnerName = Candidates[n]
        WinnerVotes = Votes[n]
print("--------------------------")

print(f"Winner: {WinnerName}")
print("--------------------------")


with open("Poll_Results.txt","w") as txtfile:
    txtfile.write("Poll Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {Vote_Count}\n")
    txtfile.write("--------------------------\n")
    for n in range(len(Candidates)):
        txtfile.write(f"{Candidates[n]}: {(100*Votes[n]/Vote_Count):.3f}% ({Votes[n]})\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Winner: {WinnerName}\n")
    txtfile.write("--------------------------\n")