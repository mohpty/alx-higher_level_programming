#!/bin/bash
# Display all methods that a url accepts
curl -sI OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
