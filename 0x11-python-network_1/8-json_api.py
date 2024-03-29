#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

def search_user(letter):
    payload = {'q': letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json.get("id"), response_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
