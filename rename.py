""" Script for rename files """
import os

# Path folder images
PATH = './images'


def rename_file(name, file_data):
    """ Function get file types and create new name """

    old_name = file_data.split(".")
    return name + '.' + old_name[len(old_name) - 1]


files = os.listdir(PATH)
for index, file in enumerate(files):
    temp_name = rename_file(str(index + 1), file)
    os.rename(os.path.join(PATH, file), os.path.join(PATH, temp_name))

files = os.listdir(PATH)
for index, file in enumerate(files):
    new_name = str(index + 1)

    for i in range(0, (4 - len(new_name)), 1):
        new_name = "0" + new_name

    final_name = rename_file(new_name, file)
    os.rename(os.path.join(PATH, file), os.path.join(PATH, final_name))
