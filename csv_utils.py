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

    for item in table_a:
        result.append(item + get_closest_match2(item[index_a], table_b, index_b))

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
    ratios = dict()
    for x in listing:
        ratios[x[0]] = (fuzz.ratio(item_id, x[0]), x)

    max_ratio = 0
    max_value = None
    for k in ratios.keys():
        if ratios[k][0] > max_ratio:
            max_ratio = ratios[k][0]
            max_value = ratios[k][1]

    return max_value

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
