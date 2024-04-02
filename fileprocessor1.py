# fileprocessor1.py

# Open the file
with open('fileprocessor.input', 'r') as file:
    # Read each line into a list
    lines = file.readlines()

# Initialize an empty list to store user data
user_data = []

# Process each line
for line in lines:
    # Skip lines starting with #
    if line.startswith('#'):
        continue
    
    # Split the line into a list using ':' as delimiter
    user_info = line.strip().split(':')
    
    # Append user information to the user_data list
    user_data.append(user_info)

# Print user data
print("Printing out User Data:")
for user_info in user_data:
    username, password, userid, groupid = user_info
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("End of User Data")
