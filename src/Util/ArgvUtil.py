import os
import argparse

# list of options message
message_directory = "Allows to insert the directory in which the files are " \
                    "located."
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
ext_file_choices = ["mkv", "mp4", "avi"]
ext_sub_choices = ["srt"]


def manage_command_line():
    parser = argparse.ArgumentParser()
    # directory is mandatory
    parser.add_argument("directory", help=message_directory)
    # file extension is optional
    parser.add_argument("-exf", "--extensionfile", help=message_extension_file,
                        choices=ext_file_choices, default="mkv")
    # subtitle extension is optional
    parser.add_argument("-exs", "--extensionsub", help=message_extension_sub,
                        choices=ext_sub_choices, default="srt")

    args = parser.parse_args()
    # manage directory
    if not os.path.exists(args.directory):
        print("Directory {} doesn't exist".format(args.directory))
        exit()

    # manages extensions
    file_ext = "." + args.extensionfile
    sub_ext = "." + args.extensionsub

    return args.directory, file_ext, sub_ext


if __name__ == "__main__":
    manage_command_line()
