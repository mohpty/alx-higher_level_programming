#!/bin/bash
# Script that sends GET request to a url with a variable in the header
curl -s -X GET -H "X-School-Student-Id: 98" "$1"
