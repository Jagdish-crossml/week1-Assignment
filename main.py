#!/usr/bin/python3
import uuid
import datetime
import getpass
import os
import json

# Return time when the program gets executed

print("Time of execution is:", datetime.datetime.now().time().strftime("%H:%M:%S"))

# Return username of the system

print("Username is:", getpass.getuser())

# Getting path of the folder to access user files

PWD = os.getcwd()
users_folder = PWD + '/users/'

# Storing file names into a list

files_list = os.listdir(users_folder)

# Create a new list to get all users in one place
user_names_list = []

for file_name in files_list:
    with open(users_folder + file_name, 'r') as file:
        user_names_list.extend(file.readlines())  # Appending data of each file after unpacking
        for user in user_names_list:
            user.strip()  # Removing new line character from each line
user_names = [user.strip() for user in user_names_list]


# Generating universal unique ID for each user
def generate_uuid(user_names):
    return user_names[0] + str(uuid.uuid1())


# Creating email_id for each user
def generate_email(user_names):
    first_name, last_name = user_names.split()
    return first_name + last_name[:1] +"@email.com"


user_info = []
# collecting data in specified JSON format
for user_name in user_names:
    user_info.append({generate_uuid(user_name): {"name": user_name, "email": generate_email(user_name)}})

# writing data to a JSON file
with open('user_data.json', 'w') as j:
    j.write(json.dumps(user_info))
