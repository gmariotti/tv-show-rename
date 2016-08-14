import requests
from tv_maze_api import TVMaze
from show_files_format import ShowFileFormat
from utils.argv_utils import manage_command_line
from utils.files_management import *


def get_episodes_list(show_name, season_num):
    response = requests.get(TVMaze.get_search_url(show_name))
    if response.status_code == requests.codes.ok:
        show_id = TVMaze.get_show_id(response.json())
        show_episodes_url = TVMaze.get_episodes(show_id)
        response = requests.get(show_episodes_url)

        if response.status_code == requests.codes.ok:
            return TVMaze.get_episodes_list(response.json(), season_num)
        else:
            print("Error in requesting list of episodes...")
            print("Status code received {]".format(response.status_code))
            exit(0)
    else:
        print("Error in request to server...")
        print("Status code received {}".format(response.status_code))
        exit(0)

    return []


def reorder():
    # TODO
    pass


# main.py
if __name__ == "__main__":
    directory, show, fileEx, subEx = manage_command_line()
    print("Working directory = {}".format(directory))
    print("Name of the TV Show = {}".format(show))
    print("List of file extensions = {}".format(fileEx))
    print("List of subtitle extensions = {}".format(subEx))

    # get the list of files from the directory
    try:
        listOfFiles = get_list_of_files(directory)
        print("File found in directory")
        for filename in listOfFiles:
            print("- {}".format(filename))
        # test_remove_temp_files(directory)
        # test_create_temp_dir(directory, listOfFiles)

    except OSError as e:
        print(e)
        exit(0)

    # insert the season number
    # TODO - move to terminal arguments
    print("\nInsert the season number")
    seasonNum = input("> ")

    listOfEpisodes = get_episodes_list(show, seasonNum)

    # check if the list is correct
    print("Episodes of {} - season {}".format(show, seasonNum))
    for episode in listOfEpisodes:
        print(episode)
    print("Is the list ok? [y/n]")
    resp = input("> ")
    if resp != 'y':
        print("Something has gone wrong")
        exit(0)

    # TODO - strategy pattern
    listOfNewFilesName = ShowFileFormat.get_S0xE0x_format(listOfEpisodes, show,
                                                          seasonNum)
    print("New list of file names")
    for newFilename in listOfNewFilesName:
        print("- {}".format(newFilename))
    # TODO - start from here
    exit(0)

    curr_dir = os.getcwd()
    os.chdir(directory)
    os.chdir("./temp")

    count = 1
    for file in listOfFiles:
        # is a
        if str(file).endswith(fileEx):
            epname = listOfEpisodes[count - 1]
            epnumBigE = "E{}".format(count)
            epnumSmallE = "e{}".format(count)
            if count < 10:
                epnumBigE = "E0{}".format(count)
                epnumSmallE = "e0{}".format(count)
            print(file)
            print(listOfNewFilesName[count - 1])
            if file.__contains__(epname) or file.__contains__(epnumBigE) or \
                    file.__contains__(epnumSmallE):
                os.rename(file, listOfNewFilesName[count - 1] + fileEx)
                count += 1
