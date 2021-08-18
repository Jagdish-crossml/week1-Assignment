import getpass
import uuid
import json
import os
import datetime


class JsonOutput:

    def generate_user_date(self):
        print(datetime.datetime.now().time().strftime("%H:%M:%S"))
        print(getpass.getuser())

    def display_names(self, users_folder):
        files_list = os.listdir(users_folder)
        for file_name in files_list:
            with open(users_folder + file_name, 'r') as file:
                user_names_list.extend(file.readlines())

        return (user_names_list)

    def gen_UUID(self, user):
        return user[0] + str(uuid.uuid1())

    def gen_email(self, user_name):
        first_name = user_name[0]
        last_name = user_name[1]
        return (last_name + first_name[:1] + "@email.com")

    def create_json(self, user_info):
        parsed = json.dumps(user_info)
        user_info = str(parsed)
        with open("file.json", "w") as file:
            file.write(user_info)

    def strip_data(self, user_names_list):
        user_names = [user.strip() for user in user_names_list]

        return user_names


if __name__ == "__main__":
    PWD = os.getcwd()
    users_folder = PWD + '/users/'
    user_names_list = []
    user_info = []
    obb = JsonOutput()
    obb.generate_user_date()
    obb.display_names(users_folder)
    user_names = obb.strip_data(user_names_list)
    obb.gen_UUID(user_names)
    for user_name in user_names:
        obb.gen_email(user_names)
        user_info.append({obb.gen_UUID(user_name): {"name": user_name, "email": obb.gen_email(user_name)}})
    print(user_info)
    obb.create_json(user_info)
