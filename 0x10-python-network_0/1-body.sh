#!/bin/bash
# Displays the body of a 200 status code response of a URL
curl -s "$1" -X GET -L
