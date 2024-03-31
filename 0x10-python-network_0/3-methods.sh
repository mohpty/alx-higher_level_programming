#!/bin/bash
# Display all methods that a url accepts
curl -X OPTIONS -i "$1"
