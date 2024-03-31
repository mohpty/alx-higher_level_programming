#!/bin/bash
# Script that sends GET request to a url with a variable in the header
curl -H "X-School-Student-Id: 98" -s "$1"
