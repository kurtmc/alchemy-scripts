#!/usr/bin/env python3

import csv
from fuzzywuzzy import fuzz

# Prints a list of lists in CSV format
def print_csv(csv_list):
    for item in csv_list:
        p = item
        for i in range(len(p) - 1):
            v = p[i]
            if v == None:
                v = ""
            if "," in v or "\n" in v:
                print('"' + v + '"', end="")
            else:
                print(v, sep="", end="")

            print(",", end="")

        v = p[-1]
        if "," in v or "\n" in v:
            print('"' + v + '"')
        else:
            print(v, sep="")

nz_active_file = "New Zealand Active Products.csv"
aus_active_file = "Australia Active Products.csv"
paths_file = "File Paths (tab delimited).csv"
nav_list_file = "NAV product list.csv"

active_products = []
for active_product_file in [nz_active_file, aus_active_file]:
    
    with open(active_product_file, newline='') as csvfile:
        active_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        first = True
        for row in active_reader:
            if not first:
                active_products.append(row)
            else:
                first = False

data_sheet_paths = []


with open(paths_file, newline='') as csvfile:
    active_reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    first = True
    for row in active_reader:
        if not first:
            data_sheet_paths.append(row)
        else:
            first = False

#print(data_sheet_paths[0])

not_found = []

relation = []

for item in data_sheet_paths:
    found = False
    for product in active_products:
        product_id = product[0]

        if (item[0] == product_id):
            relation.append((item, product))
            found = True
            break


    if not found:
        not_found.append(item)

#print("Relation length:", len(relation))
#print("Not found length:", len(not_found))


for item in not_found:
    ratios = dict()
    for product in active_products:
        product_id = product[0]
    
        ratios[product_id] = fuzz.ratio(item[0], product_id)

    max_ratio = 0
    max_ratio_key = None
    for k in ratios.keys():
        if max_ratio < ratios[k]:
            max_ratio = ratios[k]
            max_ratio_key = k

    for product in active_products:
        if max_ratio_key  == product[0]:
            relation.append((item, product))
            break

rows = [["Rubbish ID", "SDS", "PDS", "NAV ID", "DESCRIPTION"]]
for r in relation:

    row = [None] * 5
    for i in range(1, len(rows)):
        if rows[i][0] == r[0][0]:
            row = rows[i]
            break
        
    row[0] = r[0][0]
    if r[0][1].startswith("SDS"):
        row[1] = r[0][1]
    elif r[0][1].startswith("PDS"):
        row[2] = r[0][1]

    row[3] = r[1][0]
    row[4] = r[1][1]

    rows.append(row)

print_csv(rows)
