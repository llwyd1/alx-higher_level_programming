#!/bin/bash
# takes a URL, then displays all HTTP methods the server will accept
curl -Is "$1" | grep -oP '(?<=Allow: ).*'
