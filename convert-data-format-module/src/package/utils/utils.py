# -*- coding: utf-8 -*-

'''
Created on 2018. 12. 31.

@author: Taehyoung Yim
'''

from datetime import datetime
from pathlib import Path

class Utils(object):
    '''
    A class that collects utilities.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def create_filepath(self, path, fileName, extension, isInputFile: bool):
        if isInputFile:
            return path + '/' + fileName + '.' + extension
        else:
            return path + '/' + fileName + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.' + extension
    
    def check_file_exists(self, file_path):
        return Path(file_path).is_file()
    
    def check_file_size(self, file_path):
        return Path(file_path).stat().st_size
    