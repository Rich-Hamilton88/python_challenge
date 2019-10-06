import csv
import os

data = os.path.join('C:\\Users\\richn\\Desktop\\', 'LearnPython', 'budget_data.csv')

with open(data, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(reader)

    months = []
    profit_loss = []
    change =[]
    change_alt = []
    previous = 0

    for row in reader:
        months.append(row[0])
        profit_loss.append(row[1])
        
        diff = int(row[1]) - int(previous)
        previous = row[1]
        change.append(diff)

months_2 = zip(months, change)
months_3 = list(months_2)
change.remove(change[0])
months_3.remove(months_3[0])

   

total_months = len(months)
total = sum(map(int, profit_loss))
average_change = sum(change) / len(change)
increase = max(change)
decrease = min(change)

month_dec = 0
month_inc = 0

for row in months_3:
    if row[1] == increase:
        month_inc = row[0]
    if row[1] == decrease:
        month_dec = row[0]

print(f'Financial Analysis')
print(f'------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {month_inc} ({increase})')
print(f'Greatest Decrease in Profits: {month_dec} ({decrease})')

with open('budget_data', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total}', file=text_file)
    print(f'Average Change: ${average_change:.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {month_inc} ({increase})', file=text_file)
    print(f'Greatest Decrease in Profits: {month_dec} ({decrease})', file=text_file)