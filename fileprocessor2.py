# fileprocessor2.py

import sys

# Process each line from stdin (redirected file input)
for line in sys.stdin:
    # Skip lines starting with #
    if line.startswith('#'):
        continue
    
    # Split the line into a list using ':' as delimiter
    user_info = line.strip().split(':')
    
    # Print user data
    username, password, userid, groupid = user_info
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
