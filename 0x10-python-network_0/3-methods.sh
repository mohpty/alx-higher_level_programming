#!/bin/bash
# Display all methods that a url accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
