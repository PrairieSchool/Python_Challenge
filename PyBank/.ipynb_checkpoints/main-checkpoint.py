import os
import csv

ElectData = open("election_data.csv")
reader = csv.reader(ElectData,delimiter = ",")
ElectTable = list(reader)
VoteTot = len(ElectTable) - 1


Candidate = 0
KC = 0
LC = 0
CC = 0
OC = 0
KP = 0
LP = 0
CP = 0
OP = 0


for row in ElectTable:
    Candidate = str(row[2])
    K = Candidate.count("Khan")
    L = Candidate.count("Li")
    C = Candidate.count("Correy") 
    O = Candidate.count("O'Tooley")
    
    KC = KC + K
    LC = LC + L
    CC = CC + C
    OC = OC + O
    
    KP = round(KC / VoteTot*100,2)
    LP = round(LC / VoteTot*100,2)
    CP = round(CC / VoteTot*100,2)
    OP = round(OC / VoteTot*100,2)
    
print("--------------------------------")
print("Election Results")
print("--------------------------------")
print("Total number of Votes:", VoteTot)
print("--------------------------------")    
print("Khan: ",KP,"%", "(", KC,")")
print("Li: ",LP,"%", "(", LC,")")
print("Correy: ",CP,"%", "(", CC,")")
print("O'Tooley: ",OP,"%", "(", OC,")")
print("--------------------------------")  


WinList = [KC,LC,CC,OC]
Win = max(WinList)
if Win == KC:
    Winner = "Khan"
elif Win == LC:
    Winner = "Li"    
elif Win == KC:
    Winner = "Correy"
else:
    Winner = "O'Tooley"    
    
print("Winner: ",Winner)
print("--------------------------------") 

file = open("main_Poll.txt", "r")