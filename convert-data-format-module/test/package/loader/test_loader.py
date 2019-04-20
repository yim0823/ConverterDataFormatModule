# coding: utf-8

'''
Created on 2018. 12. 30.

@author: Taehyoung Yim
'''

import unittest
import pandas
from pandas.core.frame import DataFrame as _DataFrame

def read_csv(file, separator, sortCols=None, sortTypes=None, groupbyCols=None):
    try:
        dataframe = pandas.read_csv(file, encoding='utf-8', sep=separator)
    except FileNotFoundError:
        print("File Not Found.")
        raise 
        
    if sortCols is not None: # need sort by column 
        return dataframe.sort_values(by=sortCols, axis=0, ascending=sortTypes, na_position='first')
    elif groupbyCols is not None: 
        return dataframe.groupby(by=groupbyCols, sort=True, group_keys=True).apply(lambda x: x.to_json(orient='records', date_format="epoch", double_precision=10, force_ascii=True, date_unit="ms"))
    else:
        return dataframe

class TestLoader(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.path = '../../../data'
    
    def test_read_csv(self):
        filePathNameExt = self.path + '/' + 'test.csv'
        data = read_csv(filePathNameExt, separator=',')
        print(data)
        self.assertIsInstance(data, _DataFrame, '')
        return data
    
    def test_read_csv_sortby(self):
        filePathNameExt = self.path + '/' + 'test.csv'
        data = read_csv(filePathNameExt, sortCols=['Name', 'Sick Days remaining'], sortTypes=[True, False], separator=',')
        print(data)
        self.assertIsInstance(data, _DataFrame, '')
        return data
    
    def test_read_csv_groupby(self):
        filePathNameExt = self.path + '/' + 'test.csv'
        data = read_csv(filePathNameExt, groupbyCols=['Sick Days remaining'], separator=',')
        print(data)
        self.assertIsInstance(data, _DataFrame, '')
        return data
    
if __name__ == '__main__':
    unittest.main()