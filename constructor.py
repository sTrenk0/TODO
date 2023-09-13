from package_TODO import punctuation
from package_TODO import datetime


class Constructor:

    def __init__(self, name_file, author):
        self.__valid_name_file(name_file)
        self._name_file = name_file
        self.author = author
        self.__check_file_before_create()

    @staticmethod
    def __valid_name_file(*args, **kwargs):
        if any(x for x in kwargs if str(x) in punctuation):
            raise ValueError('Type for name of file has to be string without digits')

    def __create_TODO_file(self, *args, **kwargs):
        time_now = datetime.now()
        with open(self._name_file, 'w') as file_c:
            file_c.write(str(time_now) + f':\t created by {self.author}.\n')

    def __check_file_before_create(self):
        try:
            with open(self._name_file, 'r') as f_test:
                print('sss')
                f_test.readlines()
        except(FileExistsError, FileNotFoundError):
            print('iii')
            with open(self._name_file, 'w') as f_create:
                self.__create_TODO_file()
