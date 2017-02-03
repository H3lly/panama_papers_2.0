import csv
dictionnaire = {}
list = []

with open('neo4j-community-3.1.1/import/all_edges.csv', "r+") as edges:
    r = csv.reader(edges)
    w = csv.writer(edges, delimiter=',')
    for line in r:
        if line[1] not in list:
            list.append(line[1])

for l in list:
    print(l)
