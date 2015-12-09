#!/usr/bin/env python3

from csv_utils import *

def join_lists(list_a, list_b, criteria):
    joined_list = []
    for x in list_a:
        for y in list_b:
            if criteria(x, y):
                joined_list.append(x + y)
    return joined_list


root = "/home/kurt/alchemy-workspace/Product Information Tables/"
nz_active_file = root + "New Zealand Active Products.csv"
aus_active_file = root + "Australia Active Products.csv"
paths_file = root + "File Paths (tab delimited).csv"
nav_list_file = root + "NAV product list.csv"

active_products = []
for active_product_file in [nav_list_file]:
    active_products += read_csv(active_product_file, skip_first=True)

data_sheet_paths = []
data_sheet_paths += read_csv(paths_file, skip_first=True, delimiter='\t')

aus_id_list = []
tmp = read_csv(aus_active_file, skip_first=True)
for i in tmp:
    aus_id_list.append(i[0])

nz_id_list = []
tmp = read_csv(nz_active_file, skip_first=True)
for i in tmp:
    nz_id_list.append(i[0])

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

rows = [["Rubbish ID", "SDS", "PDS", "NAV ID", "DESCRIPTION", "VENDOR ID", "DATABASE"]]
for r in relation:

    row = [None] * 7
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
    row[5] = r[1][9]

    if row[0] in aus_id_list:
        row[6] = "AUS"
    else:
        row[6] = "NZ"

    rows.append(row)

print_csv(rows)
