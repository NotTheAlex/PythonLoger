import os
import datetime
import shutil


class log():

    def __init__(self, log_folder: str='logs'):
        '''Вы можите изменить папку для сохранения логов
        log_folder = ""'''
        if not os.path.isdir(log_folder):
            os.mkdir (log_folder)
        self.log_folder = log_folder
    
    def add (self, text: str):
        '''Добавляет в лог данные'''
        current_date = datetime.date.today()
        
        file = f'{current_date.day}-{current_date.month}-{current_date.year}.log'
        file = f'{self.log_folder}/' + file
        
        if not os.path.isfile (file):
            open(file, 'w').write("")

        with open (file, 'a') as f:
            now = datetime.datetime.now()
            current_time = now.strftime("[%H:%M:%S] ")
            f.write(f'\n{current_time}{text}')
    
    def clear (self):
        '''Удаляет папку с логами'''
        shutil.rmtree (self.log_folder)
        