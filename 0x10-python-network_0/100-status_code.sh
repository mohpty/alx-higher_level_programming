#!/bin/bash
# Script that sends a request to url passed as an argument, and displays only the status of the code.
curl -so /dev/null -w "%{http_code}" "$1"
