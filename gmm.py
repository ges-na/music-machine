import os
from shutil import copy2

FILE_CATEGORY_MAP = {'mp3': 'mp3', 'flac': 'lossless', 'wav': 'lossless'}


class MusicMachine(object):
    def __init__(self):

        relative_path = os.path.dirname(os.path.abspath(__file__))
        self.input_dir = '{}/test_data/input'.format(relative_path)
        self.output_dir = '{}/test_data/output'.format(relative_path)

    def prompt(self):
        print('1: Change input directory.')
        print('2: Change output directory.')
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
            trunc_root = root.replace(self.input_dir, "")
            split_trunc_root = trunc_root.split("/")
            array_length = len(split_trunc_root)
            if array_length == 3:
                self.copy_album(files, trunc_root)

    def copy_album(self, songs, path):
        for filename in songs:
            relative_path = '{}/{}'.format(path, filename)
            norm_path = self.normalize_pathnames(relative_path)
            file_extension = filename.split('.').pop().lower()
            category = FILE_CATEGORY_MAP.get(file_extension)
            if category:
                category_dir = '{}/{}'.format(self.output_dir, category)
                #todo: create subdirs recursively
                if not os.path.isdir(category_dir):
                    os.makedirs(category_dir)
                copy2('{}{}'.format(self.input_dir, relative_path), '{}/{}{}'.format(self.output_dir, category, norm_path))
            #todo: check whether file exists already

    def normalize_pathnames(self, pathname):
        return pathname.replace(" ", "_")

music_machine = MusicMachine()
music_machine.prompt()
