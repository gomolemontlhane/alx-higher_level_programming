#!/usr/bin/python3
"""Script that adds all command line arguments to a Python list
   and then saves them to a JSON file.
"""

import sys
from os.path import exists
from json import load

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if the file exists
file_path = "add_item.json"

if not exists(file_path):
    save_to_json_file([], file_path)

# Load the existing list from the JSON file
my_list = load_from_json_file(file_path)

# Add command line arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list to the JSON file
save_to_json_file(my_list, file_path)
