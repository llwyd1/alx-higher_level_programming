#!/bin/bash
# Sends a DELETE request to a URL and sends the body of the response
curl -s "$1" -X DELETE
