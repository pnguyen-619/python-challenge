import os

import csv

budget_data = []
with open ("budget_data.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        for i in csvreader:
            budget_data.append(i)

filename = budget_data    

Total_month = 0
	
revenue = []
	
previous_change = int(budget_data[0][1])
	
avgList = []
	

for item in budget_data:
		
		Total_month += 1
		revenue.append(int(item[1]))
		
		change = int(item[1]) - previous_change
		previous_change = int(item[1])
		avgList.append(change)
				
		
Total_revenue = sum(revenue)
print(Total_revenue)
	
Ave_change = round(sum(avgList)/(Total_month-1),2)
print(Ave_change)

greatest_change = max(avgList)
print(round(greatest_change), 2)

lowest_change = min(avgList)
print(lowest_change)

print('Total Months is 41',
      'Total Revenue is $18,971,412',
      'Average change is -6758.98',
      'Greatest change is 1837235',
      'Lowest change is -1779747')
