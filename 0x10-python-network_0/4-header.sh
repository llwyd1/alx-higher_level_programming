#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of the response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
