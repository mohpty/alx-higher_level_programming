#!/bin/bash
# Script that takes a url and return the length of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
