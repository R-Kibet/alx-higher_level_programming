#!/usr/bin/python3
""" adds and save all arguments to a Python list """

import sys
import os

args = sys.argv[1:]

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

item = []

if os.path.exists("./add_item.json"):
    item = load("add_item.json")

save(item + args, "add_item.json")
