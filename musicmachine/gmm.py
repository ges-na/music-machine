import ipdb
import os
from shutil import copy2

FILE_CATEGORY_MAP = {'mp3': 'mp3', 'flac': 'lossless', 'wav': 'lossless'}


class MusicMachine(object):
    def __init__(self):

        abs_path = os.path.dirname(os.path.abspath(__file__))
        self.input_dir = os.path.join(abs_path, 'test_data', 'input')
        self.output_dir = os.path.join(abs_path, 'test_data', 'output')

    def prompt(self):
        print('1: Change input directory.')
        print('2: Change output directory.')
        #todo: step 3
        print('3: See state.')
        print('4: Do the thing.')
        decision = input('What do you want to do? ')
        if decision == '1':
            self.set_input_dir()
        elif decision == '2':
            self.set_output_dir()
        elif decision == '3':
            pass
        elif decision == '4':
            self.the_thing()
        else:
            print('Use a numeral dummy.')
            self.prompt()

    def set_input_dir(self):
        print('Your input directory is: {}'.format(self.input_dir))
        string_input = input('Enter input directory: ')
        if string_input:
            self.input_dir = string_input
            print('Your new input directory is: {}'.format(self.input_dir))
        else:
            print('The input directory is unchanged.')
        self.prompt()

    def set_output_dir(self):
        print('Your output directory is: {}'.format(self.output_dir))
        string_input = input('Enter output directory: ')
        if string_input:
            self.output_dir = string_input
            print('Your new output directory is: {}'.format(self.output_dir))
        else:
            print('The output directory is unchanged.')
        self.prompt()

    def the_thing(self):
        """compares input and output dirs
        copies files not present in output from input"""
        for root, dirs, files in os.walk(self.input_dir):
            ##input_dir_appended = 
            trunc_root = os.path.relpath(root, self.input_dir)
            split_trunc_root = trunc_root.split(os.sep)
            array_length = len(split_trunc_root)
            if array_length == 2:
                self.copy_album(files, trunc_root)

    def copy_album(self, songs, path):
        for filename in songs:
            relative_path = os.path.join(path, filename)
            norm_path = self.custom_normalize(relative_path)
            file_extension = filename.split('.').pop().lower()
            category = FILE_CATEGORY_MAP.get(file_extension)
            if category:
                file_from = os.path.join(self.input_dir, relative_path)
                file_to = os.path.join(self.output_dir, category, norm_path)
                self.create_output_dirs(file_to)
                copy2(file_from, file_to)
            #todo: check whether file exists already

    def custom_normalize(self, pathname):
        return pathname.replace(" ", "_")

    def create_output_dirs(self, file_to):
        artist_album_folders = file_to.replace(self.output_dir, '').split(os.sep)
        artist_album_folders.pop()
        root = self.output_dir
        for folder in artist_album_folders:
            path = os.path.join(root, folder)
            if os.path.isdir(path):
                pass
            else:
                os.mkdir(path)
            root = path

music_machine = MusicMachine()
music_machine.prompt()
