#!/usr/bin/env python3

from fuzzywuzzy import fuzz
from csv_utils import *

nz_active_file = "/home/kurt/alchemy-workspace/Product Information Tables/New Zealand Active Products.csv"
aus_active_file = "/home/kurt/alchemy-workspace/Product Information Tables/Australia Active Products.csv"
nav_list_file = "/home/kurt/alchemy-workspace/Product Information Tables/NAV product list.csv"



nz_active = []
tmp = read_csv(nz_active_file, skip_first=True)
for item in tmp:
    nz_active.append([item[0], item[1], "NZ"])

aus_active = []
tmp = read_csv(aus_active_file, skip_first=True)
for item in tmp:
    aus_active.append([item[0], item[1], "AUS"])

nav = []
tmp = read_csv(nav_list_file, skip_first=True)
for item in tmp:
    nav.append([item[0], item[9]])

all_active = nz_active + aus_active
all_active.insert(0, ["ID", "Description", "Database", "NAV ID", "Vendor ID"])
        
for i in range(len(all_active)):
    all_active[i] = all_active[i] + get_closest_match(all_active[i][0], nav)

print_csv(all_active)

