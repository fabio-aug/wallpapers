import os

path = '<wallpaper_folder>'

files = os.listdir(path)

for index, file in enumerate(files):
    name = str(index + 1)

    for i in range(0, (4 - len(name)), 1):
        name = "0" + name

    oldName = file.split(".")

    name = name + '.' + oldName[len(oldName) - 1]

    print(name)
    print(''.join([str(index), '.jpg']) + "\n")

    os.rename(os.path.join(path, file), os.path.join(path, name))

exit()
