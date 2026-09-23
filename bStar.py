import csv
import math

CSV_NAME = "ResultsV1.csv"
RESULTS_NAME = "bStarResults"

def bin_search(nodes, depth):
    low = 1
    high = nodes
    
    total = 0
    while abs(nodes-total) > 0.0000001:
        total = 0
        bStar = high-((high-low)/2)

        for i in range(1, depth+1):
            total = total + bStar**i
            

        if total> nodes:
            high = bStar
        elif total < nodes:
            low = bStar

    return bStar
        
        


with open(CSV_NAME, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data_list = list(reader)

for i in range(len(data_list)):
    myList = data_list[i]
    h1BF = bin_search(float(myList["Heuristic 1 Average Nodes"]),int(myList["Solution Number"]))
    h2BF = bin_search(float(myList["Heuristic 2 Average Nodes"]),int(myList["Solution Number"]))
    h3BF = bin_search(float(myList["Heuristic 3 Average Nodes"]),int(myList["Solution Number"]))
    print(h1BF, h2BF, h3BF)

