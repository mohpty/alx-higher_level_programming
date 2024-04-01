#!/bin/bash
# Script that sends GET request to a url with a variable in the header
curl -s "$1" -H "X-School-User-Id: 98"
