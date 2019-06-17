import os
import csv

BudgetData = open("budget_data.csv")

# print(BudgetData.read())
print("Financial Analysis")
print("-------------------")


# Count number of months
reader = csv.reader(BudgetData,delimiter = ",")
months = list(reader)
MoCount = len(months) - 1
print("Total number of Months:", MoCount)

with open("budget_data.csv", newline="") as BudgetData:
    budgetD = csv.reader(BudgetData)
    
    TotalPL = 0
    Ch = 0
    TotalCh = 0
    PLPrevious = 867884
    PLCurrent = 0
    
    
    next(budgetD)
    for row in budgetD:

        PLCurrent = int(row[1])
        TotalPL += int(row[1])
        
        Ch = (PLCurrent - PLPrevious)
        TotalCh += Ch
        PLPrevious = PLCurrent

        
#     print("Total Number of Months: ", MoCount)    
    print("Total Profits and Losses: ", TotalPL)
    print("   Average monthly change: ", round(TotalCh / (MoCount - 1),2))

with open("budget_data.csv", newline="") as BudgetData:
    budgetD = csv.reader(BudgetData)
    
    next(budgetD)
    for row in budgetD:
    
        PLMax = max(budgetD)

with open("budget_data.csv", newline="") as BudgetData:
    budgetD = csv.reader(BudgetData)
    
    PLMin = min(budgetD)

    print("Greatest Increase in Profits: ", PLMax)
    print("Greatest Decrease in Profits: ", PLMin)