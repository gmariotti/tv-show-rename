import os
import shutil


# TODO - change of directory must be done outside as a decorator
def get_list_of_files(dirname):
    curr_dir = os.getcwd()
    os.chdir(dirname)
    files = [name for name in os.listdir(".") if os.path.isfile(name)]
    os.chdir(curr_dir)  # return to the script directory

    return files


def test_function(list_of_files):
    i = 0
    for filename in list_of_files:
        if os.path.isfile(filename):
            shutil.copy2(filename, filename + str(i))
            i += 1

    print("New list of file")
    for filename in os.listdir("."):
        print(filename)


def test_remove_temp_files(directory):
    curr_dir = os.getcwd()
    temp_dir = "./temp"
    os.chdir(directory)

    # remove the temporary directory and its files if exists
    if os.path.exists(temp_dir) and os.path.isdir(temp_dir):
        for file_to_remove in os.listdir(temp_dir):
            os.remove(temp_dir + "/" + file_to_remove)
        os.removedirs(temp_dir)
    print("Removed temp dir and/or files")
    os.chdir(curr_dir)


def test_create_temp_dir(directory, list_of_files):
    curr_dir = os.getcwd()
    temp_dir = "./temp"
    os.chdir(directory)

    # make a temporary directory and save a list of fake empty files
    os.makedirs(temp_dir)
    os.chdir(temp_dir)
    for file_name in list_of_files:
        tmp = open(file_name, "w+")
        tmp.close()

    os.chdir(curr_dir)
