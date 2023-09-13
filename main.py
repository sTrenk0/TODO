import datetime
from constructor import Constructor
from package_TODO import *


class MainTodoList(Constructor):


    def __init__(self, name_file, author):
        super().__init__(name_file, author)
        self.db = 'db_file'


    def add_note_to_TODO_file(self, name_task, date_until=None, entry_task=None, *context):
        if re.findall(r'[\d][\d][,.-][\d][\d][,.-][\d][\d]', date_until):
            unpack_data = (map(int, (x for x in re.split(r'[,.-]', date_until))))
            time_data = datetime(*unpack_data)
            with open(self._name_file, 'a') as file_add:
                file_add.write(f'\n\t{name_task}: until {time_data}:\n {entry_task} - {str(*context)}\n')

        elif date_until is None:
            with open(self._name_file, 'a') as file_add:
                file_add.write(f'\n\t{name_task}: until {date_until}:\n {entry_task} - {str(*context)}\n')

        else:
            print('Date_until has be in \'year-month-day\' format')




    def __call__(cls, *args, **kwargs):
        pass


cl1 = MainTodoList('name_file3', 'dArtem')
