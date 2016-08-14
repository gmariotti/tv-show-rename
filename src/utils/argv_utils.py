import os
import argparse

# TODO
# list of options message
message_directory = "Allows to insert the directory in which the files are " \
                    "located."
message_show = "TODO"
message_extension_file = """allows to define the extension of the file.
                            Insert the extension as a <ext>
                            Default value is .mkv
                            """
message_extension_sub = """Equals to -exf except that is referred to the
                           subtitle extension.
                           Default value is .srt
                           """

# List of error messages
error_message_dir = """
Insert a directory name after -dir
example --> -dir <dir>
"""

# possible values
ext_file_choices = ["mkv", "mp4", "avi", "m4v"]
ext_sub_choices = ["srt"]


def manage_command_line():
    global ext_file_choices
    global ext_sub_choices

    parser = argparse.ArgumentParser()
    # Directory where files are located is mandatory
    parser.add_argument("directory", help=message_directory)

    # Name of the tv show
    parser.add_argument("show", help=message_show)

    # Files extension is optional. Use it just to speed up the research
    parser.add_argument("-exf", "--extensionfile", help=message_extension_file)

    # Subtitles extension is optional. Use it just if new format arises
    parser.add_argument("-exs", "--extensionsub", help=message_extension_sub)

    args = parser.parse_args()
    # manage directory
    if not os.path.exists(args.directory):
        print("Directory {} doesn't exist".format(args.directory))
        exit(-1)

    # manages extensions
    if args.extensionfile is not None:
        ext_file_choices = [args.extensionfile]
    if args.extensionsub is not None:
        ext_sub_choices = [args.extensionsub]

    return args.directory, args.show, ext_file_choices, ext_sub_choices


if __name__ == "__main__":
    manage_command_line()
