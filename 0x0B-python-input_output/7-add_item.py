#!/usr/bin/python3
"""Load, add, save module"""

import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists, if not, create it
if not os.path.isfile(filename):
    save_to_json_file([], filename)

# Load the current list from the file
my_list = load_from_json_file(filename)

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
