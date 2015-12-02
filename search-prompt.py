#!/usr/bin/env python3
import readline
import sys
import os
from fuzzywuzzy import fuzz
import shutil
import inspect

# Constants
product_info_dir = "/home/kurt/alchemy-workspace/Product_Information"
sds_dir = "/home/kurt/alchemy-workspace/SDS-copy"
pds_dir = "/home/kurt/alchemy-workspace/PDS-copy"
current_product_file = "/home/kurt/alchemy-workspace/current-product.txt"
        

# globals
sds_search_results = []
pds_search_results = []

def get_current_product():
        f = open(current_product_file,'r')
        current_product = f.readline().strip()
        f.close();
        return current_product


class Commands:
    def search(args, fuzzy_threshold = 90):
        sds_list = os.listdir(sds_dir)
        pds_list = os.listdir(pds_dir)
        
        global sds_search_results
        sds_search_results = []
        global pds_search_results
        pds_search_results = []

        print("SDS results")
        print("="*20)

        for sds in sds_list:
            if fuzz.partial_ratio(args.lower(), sds.lower()) > fuzzy_threshold:
                sds_search_results.append(sds)
                print(sds)
        
        print("="*20)
        print("")
        print("PDS results")
        print("="*20)

        for pds in pds_list:
            if fuzz.partial_ratio(args.lower(), pds.lower()) > fuzzy_threshold:
                pds_search_results.append(pds)
                print(pds)
                
        print("="*20)

    def open(args):
        for  sds in sds_search_results:
            os.system("xdg-open \"" + sds_dir + "/" + sds + "\"")
        for  pds in pds_search_results:
            os.system("xdg-open \"" + pds_dir + "/" + pds + "\"")

    def copy(args):
        for  sds in sds_search_results:
            print("Copy: " + sds + " to " + product_info_dir + "/" + get_current_product() + "/")
            shutil.copy2(sds_dir + "/" + sds, product_info_dir + "/" + get_current_product() + "/")
        for  pds in pds_search_results:
            print("Copy: " + pds + " to " + product_info_dir + "/" + get_current_product() + "/")
            shutil.copy2(pds_dir + "/" + pds, product_info_dir + "/" + get_current_product() + "/")
        

    def help(args):
        print("no command selected, start with: " + ", ".join(commands))

    def exit(args):
        sys.exit()

    def next(args, jump=1):
        current_product = get_current_product()

        file_list = os.listdir(product_info_dir)
        file_list.sort()

        
        if current_product not in file_list:
            print("file: '" + current_product + "' is not in " + product_info_dir)
        else:
            current_product = file_list[file_list.index(current_product) + jump]
            f = open(current_product_file,'w')
            f.write(current_product)
            f.close();
            print("Current product: " + current_product)

    def previous(args):
        Commands.next(args, -1)



    def current(args):
        print("Current product: " + get_current_product())

    def index(args):
        file_list = os.listdir(product_info_dir)
        file_list.sort()
        print("At index", file_list.index(get_current_product()),"out of", len(file_list))

    def fuzzy(args):
        fuzz = int(args.split()[0])
        search_args = args[args.index(" ") + 1:]
        Commands.search(search_args, fuzz)

commands = []
for funct in inspect.getmembers(Commands, predicate=inspect.isfunction):
    commands.append(funct[0])


Commands.current(True)
while True:

    user_cmd = input("> ")

    cmd_option = ""
    if len(user_cmd.split()) > 0:
        cmd_option = user_cmd.split()[0]

    if cmd_option in commands:
        command = getattr(Commands, cmd_option)
        args = ""
        try:
            args = user_cmd[user_cmd.index(" ") + 1:]
        except ValueError:
            pass
        command(args)
    else:
        Commands.help(None)
