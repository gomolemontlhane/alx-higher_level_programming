#!/bin/bash
# Sends a GET request to the URL and displays the body of the response if status code is 200
curl -sL -w "%{http_code}" -o /dev/null "$1" | {
    read -r status
    if [[ $status == 200 ]]; then
        curl -s "$1"
    fi
}

