#!/usr/bin/python3
"""
module that adds all arguments to a python list
saves them to file
"""

import sys
import os.path


save_file = __import__("5-save_to_json_file").save_to_json_file
load_file = __import__("6-load_from_json_file").load_from_json_file

file_list = []
if os.path.exists("add_item.json"):
    file_list = load_file("add_item.json")

for ac in sys.argv[1:]:
    file_list.append(ac)

save_file(file_list, "add_item.json")
