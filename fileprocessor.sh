#!/bin/bash

# Part1.sh
# Declare an array in BASH
mylist=("User1" "User2" "User3")

# Print the list using a for loop
for user in "${mylist[@]}"; do
    echo "$user"
done
