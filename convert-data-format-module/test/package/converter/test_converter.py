# coding: utf-8

'''
Created on 2018. 12. 30.

@author: Taehyoung Yim
'''

import unittest
import json
import yaml
import codecs
from pathlib import Path

from datetime import datetime
from test.package.loader.test_loader import TestLoader

class TestConverter(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

        self.path = '../../../data'
        self.filePathNameExt = None
        
        loader = TestLoader()
        self.csv = loader.test_read_csv()
        

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
        try:
            Path(self.filePathNameExt).unlink()
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        
    def test_write_list_into_json(self):
        fileName = 'test_' + datetime.now().strftime('%Y%m%d%H%M%S')
        data = {}
        data['policyID'] = 119736
        data['statecode'] = 'FL'
        data['county'] = 'SUWANNEE'
        
        self.filePathNameExt = self.path + '/' + fileName + '.json'
        with codecs.open(self.filePathNameExt, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)
        self.assertTrue(Path(self.filePathNameExt).is_file())
    
    def test_write_list_into_yaml(self):
        fileName = 'test_' + datetime.now().strftime('%Y%m%d%H%M%S')
        data = {}
        data['policyID'] = 119736
        data['statecode'] = 'FL'
        data['county'] = 'SUWANNEE'
        
        self.filePathNameExt = self.path + '/' + fileName + '.yaml'
        with codecs.open(self.filePathNameExt, 'w', encoding='utf-8') as fp:
            yaml.dump(data, fp, default_flow_style=False, allow_unicode=True)
        self.assertTrue(Path(self.filePathNameExt).is_file())
    
    def test_write_conversion_of_csv_to_json(self):
        fileName = 'test'
        dataframe = self.csv;
        
        self.filePathNameExt = self.path + '/' + fileName + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.json'
        dataframe.to_json(self.filePathNameExt, orient="records", date_format="epoch", double_precision=10, force_ascii=False, date_unit="ms")
        self.assertTrue(Path(self.filePathNameExt).is_file())
            
    def test_write_conversion_of_csv_into_yaml(self):
        fileName = 'test'
        dataframe = self.csv;
        
        self.filePathNameExt = self.path + '/' + fileName + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.yml'
        with open(self.filePathNameExt, 'w') as fp:
            yaml.dump({'result': dataframe.to_dict(orient='records')}, fp, default_flow_style=False, allow_unicode=True)
        self.assertTrue(Path(self.filePathNameExt).is_file())

class TestConverterWithoutFileProcess(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        loader = TestLoader()
        self.csv = loader.test_read_csv()
    
    def test_convert_csv_dataframe_to_json_dataframe(self):
        dataframe = self.csv;
        
        json_string = dataframe.to_json(orient='records', date_format="epoch", double_precision=10, force_ascii=True, date_unit="ms")
        self.assertIsNotNone(json_string, 'It would be fail to convert data.')
        
        dict_json = json.loads(json_string)
        self.assertIsNotNone(dict_json, 'It would be fail to load json string to json.')
        self.assertIsInstance(dict_json, list, 'It would be fail to load json string to json.')
    
    def test_example_vaild_and_convert_other_format(self):
        dict_json = [
                        {'Name': 'Graham Chapman', 'Hire Date': '03/15/14', 'Salary': 50000.0, 'Sick Days remaining': 10}, 
                        {'Name': 'John Cleese', 'Hire Date': '06/01/15', 'Salary': 65000.0, 'Sick Days remaining': 8}, 
                        {'Name': 'Eric Idle', 'Hire Date': '05/12/14', 'Salary': 45000.0, 'Sick Days remaining': 10}, 
                        {'Name': 'Terry Jones', 'Hire Date': '11/01/13', 'Salary': 70000.0, 'Sick Days remaining': 3}, 
                        {'Name': 'Terry Gilliam', 'Hire Date': '08/12/14', 'Salary': 48000.0, 'Sick Days remaining': 7}, 
                        {'Name': 'Michael Palin', 'Hire Date': '05/23/13', 'Salary': 66000.0, 'Sick Days remaining': 8}
                    ]
        
        valid_list = list()
        for h in dict_json:
#             valid_dict = {}
            if h['Salary'] >= 50000:
#                 valid_dict.update(h)
                valid_list.append(h)
                
        self.assertIsInstance(json.dumps(valid_list), str)
        print("json :\n %s" %json.dumps(valid_list))
        
        self.assertIsInstance(yaml.dump(valid_list), str)
        print("yaml :\n %s" %yaml.dump(valid_list))
        
if __name__ == '__main__':
    unittest.main()