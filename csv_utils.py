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


def fuzzy_join(table_a, table_b, index_a, index_b):
    result = []
    for row_a in table_a:
        id_a = row_a[index_a]
        closest = get_closest_match2(id_a, table_b, index_b)
        result.append(row_a + closest)

    return result

def get_closest_match2(item_id, listing, index):
    ratios = dict()
    for x in listing:
        ratios[x[index]] = (fuzz.ratio(item_id, x[index]), x)

    max_ratio = 0
    max_value = None
    for k in ratios.keys():
        if ratios[k][0] > max_ratio:
            max_ratio = ratios[k][0]
            max_value = ratios[k][1]

    return max_value

def get_closest_match(item_id, listing):
    return get_closest_match2(item_id, listing, 0)

def read_csv(file_name, skip_first=False, delimiter=',', quotechar='"'):
    csv_list = []
    with open(file_name, newline='') as csvfile:
        active_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        first = skip_first
        for row in active_reader:
            if not first:
                csv_list.append(row)
            else:
                first = False
    return csv_list

def get_columns(data, column_list):
    result = []
    for item in data:
        tmp = []
        for i in column_list:
            tmp = tmp + [item[i]]
        result.append(tmp)
    return result

def add_column(data, default=None):
    result = []
    for item in data:
        result.append(item + [default])

    return result

