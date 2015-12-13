#!/usr/bin/env python3

from csv_utils import *

nz_active_file = "/home/kurt/alchemy-workspace/Product Information Tables/New Zealand Active Products.csv"
aus_active_file = "/home/kurt/alchemy-workspace/Product Information Tables/Australia Active Products.csv"
nav_list_file = "/home/kurt/alchemy-workspace/Product Information Tables/NAV product list.csv"
sds_pds_file = "/home/kurt/alchemy-workspace/Product Information Tables/File Paths (tab delimited).csv"

nz_active = read_csv(nz_active_file, skip_first=True)
nz_active = get_columns(nz_active, [0, 1])
nz_active = add_column(nz_active, "NZ")

aus_active = read_csv(aus_active_file, skip_first=True)
aus_active = get_columns(aus_active, [0, 1])
aus_active = add_column(aus_active, "AUS")

nav = read_csv(nav_list_file, skip_first=True)
nav = get_columns(nav, [0, 9])

sds_pds = read_csv(sds_pds_file, skip_first=False, delimiter='\t')
sds = []
pds = []
for value in sds_pds:
    if value[1].startswith("SDS -"):
        sds.append(value)
    elif value[1].startswith("PDS -"):
        pds.append(value)
    else:
        pass

all_active = nz_active + aus_active

result = fuzzy_join(all_active, nav, 0, 0)
result = join(result, sds, 0, 0)
result = join(result, pds, 0, 0)

result = get_columns(result, [0, 1, 2, 3, 4, 6, 8])

tmp = []
for r in result:
    if len(r[5]) <= 0 or len(r[6]) <= 0:
        tmp.append(r)
result = tmp

result = [["ID", "Description", "Database", "NAV ID", "Vendor ID", "SDS", "PDS"]] + result
        
print_csv(result)
