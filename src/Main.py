import requests
from TVMaze import TVMaze
from ShowFileFormat import ShowFileFormat
from Util.ArgvUtil import manage_command_line
from Util.FilesManagementFunctions import *


def get_episodes_list(show, seasonNum):
    response = requests.get(TVMaze.get_search_url(show))
    if response.status_code == requests.codes.ok:
        show_id = TVMaze.get_show_id(response.json())

        show_episodes_url = TVMaze.get_episodes(show_id)
        response = requests.get(show_episodes_url)

        if response.status_code == requests.codes.ok:
            return TVMaze.get_episodes_list(response.json(), seasonNum)

    return []


def reorder():
    # TODO
    pass


# Main.py
if __name__ == "__main__":
    directory, fileEx, subEx = manage_command_line()
    print(
        "Dir is {}, FileEx is {}, SubEx is {}".format(directory, fileEx, subEx))

    # get the list of files from the directory
    try:
        listOfFile = get_list_of_files(directory)
        test_remove_temp_files(directory)
        test_create_temp_dir(directory, listOfFile)

    except OSError as e:
        print(e)
        exit(0)

    # get the show name and the season number
    print("Insert the name of the show")
    show = input("> ")
    print("Insert the season number")
    seasonNum = input("> ")

    print(show + " season #" + seasonNum)
    episodesList = get_episodes_list(show, seasonNum)

    # check if the list is correct
    for episode in episodesList:
        print(episode)
    print("Is the list correctly ordered? [y/n]")
    resp = input("> ")
    if resp != 'y':
        reorder()

    listOfNewFilesName = ShowFileFormat.get_S0xE0x_format(episodesList, show,
                                                          seasonNum)
    curr_dir = os.getcwd()
    os.chdir(directory)
    os.chdir("./temp")

    count = 1
    for file in listOfFile:
        # is a
        if str(file).endswith(fileEx):
            epname = episodesList[count-1]
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
