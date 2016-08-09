import unittest
from sys import argv
from src.Util.ArgvUtil import manage_command_line


class TestArgvUtil(unittest.TestCase):
    def setUp(self):
        argv[1] = "C:\\Users\\guido\\Downloads\\Torrent\\"

    def test_directory_argument_existence(self):
        dir, fileEx, subEx = manage_command_line()
        self.assertEqual(argv[1], dir)

    def test_dir_file_and_sub_existence(self):
        dir, fileEx, subEx = manage_command_line()
        self.assertEqual([argv[1], ".mkv", ".srt"], [dir, fileEx, subEx])

    # def test_file_ex_other_values(self):
    #     argv[2] = "-exf"
    #     argv[3] = "mp4"
    #     dir, fileEx, subEx = manage_command_line()
    #     self.assertEqual(argv[3], fileEx)


if __name__ == '__main__':
    unittest.main()
