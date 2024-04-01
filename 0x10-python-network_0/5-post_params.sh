#!/bin/bash
# Script sends POST to url, pre set key:val pair sent
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
