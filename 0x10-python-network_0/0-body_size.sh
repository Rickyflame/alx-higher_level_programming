#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the byte size of the HTTP response header
curl -s "$1" | wc -c
