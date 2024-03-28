#!/bin/bash
# Sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s "$1" -X GET -o /dev/null -w "%{http_code}" | {
    read status_code
    if [ $status_code -eq 200 ]; then
        curl -s "$1"
    fi
}
