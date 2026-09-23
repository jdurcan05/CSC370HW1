import csv

CSV_NAME = "ResultsV1.csv"
RESULTS_NAME = "bStarResults.csv"
ARBITRARY_LOW_NUMBER = 0.0000000001

def bin_search(nodes, depth):
    low = 1
    high = nodes
    
    total = 0
    while abs(nodes-total) > ARBITRARY_LOW_NUMBER:
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
    data_list[i]["H1 Branching Factor"] = h1BF
    data_list[i]["H2 Branching Factor"] = h2BF
    data_list[i]["H3 Branching Factor"] = h3BF


with open(RESULTS_NAME, "w", newline="", encoding="utf-8") as file:
    keys = data_list[0].keys()

    writer = csv.DictWriter(file, keys)

    writer.writeheader()

    writer.writerows(data_list)