# -*- coding: utf-8 -*-

'''
Created on 2018. 12. 31.

@author: Taehyoung Yim
'''

import unittest
from pathlib import Path
import pathlib

class TestUtils(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.data_path = str(pathlib.Path(__file__).resolve().parents[3]) + '/data'
    
    def test_check_file_exists(self):
        file_path = self.data_path + '/' + 'test' + '.' + 'csv'
        self.assertTrue(Path(file_path).is_file(), 'That file is exists.')
    
    def test_check_file_size(self):
        file_path = self.data_path + '/' + 'test' + '.' + 'csv'
        self.assertNotEqual(Path(file_path).stat().st_size, 0)
        