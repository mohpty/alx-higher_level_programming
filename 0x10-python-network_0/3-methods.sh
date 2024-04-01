#!/bin/bash
# Display all methods that a url accepts
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
