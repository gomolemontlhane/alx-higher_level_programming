#!/bin/bash
# Sends a POST request with specific parameters to a given URL and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
