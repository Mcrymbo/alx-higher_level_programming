#!/bin/bash
# prints allowed methods
curl -sI "$1" -X OPTIONS | grep -i "allow:" | cut -d " " -f 2-
