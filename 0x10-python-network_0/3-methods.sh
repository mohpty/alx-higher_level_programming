#!/bin/bash
# Display all methods that a url accepts
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
