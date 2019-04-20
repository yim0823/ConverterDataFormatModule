'''
Created on 2018. 12. 30.

@author: Taehyoung Yim
'''

import unittest
import validators
# import re
import pathlib

class TestValidator(unittest.TestCase):
    '''
    All validation test is here.
    '''
    
    def test_check_type_of_value_in_json(self):
        dict_json = [
                        {'Name': '\xcf\x80-zza', 'Hire Date': '03/15/14', 'Salary': 50000.0, 'Sick Days remaining': 10}, 
                        {'Name': 'John Cleese', 'Hire Date': '06/01/15', 'Salary': 65000.0, 'Sick Days remaining': 8}, 
                        {'Name': 'Eric Idle', 'Hire Date': '05/12/14', 'Salary': 45000.0, 'Sick Days remaining': 10}, 
                        {'Name': 'Terry Jones', 'Hire Date': '11/01/13', 'Salary': 70000.0, 'Sick Days remaining': 3}, 
                        {'Name': 'Terry Gilliam', 'Hire Date': '08/12/14', 'Salary': 48000.0, 'Sick Days remaining': 7}, 
                        {'Name': 'Michael Palin', 'Hire Date': '05/23/13', 'Salary': 66000.0, 'Sick Days remaining': 8}
                    ]
        
        for h in dict_json:
            self.assertTrue(isinstance(h['Name'], str), 'This value is ascii')
    
    # Doesn't work. It needs to modify the code in the future.
#     def test_validate_url_regex(self):
#         regex = re.compile(
#             r'^(?:http|ftp)s?://' # http:// or https://
#             r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
#             r'localhost|' #localhost...
#             r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
#             r'(?::\d+)?' # optional port
#             r'(?:/?|[/?]\S+)$')
#         
#         print(re.match(regex, "http://www.naver.com"))
#         print(re.match(regex, "http://www.naver.//"))
    
    def test_simple_validate_url_using_validator(self):
        url1 = "www.naver.com" # ValidationFailure
        result = validators.url(url1)
        if result:
            self.assertTrue(result, 'It is invalid.')
        else:
            self.assertFalse(result, 'It is not invalid.')
            
        url2 = "http://www.naver." # ValidationFailure
        result = validators.url(url2)
        if result:
            self.assertTrue(result, 'It is invalid.')
        else:
            self.assertFalse(result, 'It is not invalid.')
        
        url3 = "http://www.naver.com/" # True
        result = validators.url(url3)
        if result:
            self.assertTrue(result, 'It is invalid.')
        else:
            self.assertFalse(result, 'It is not invalid.')
            
        url4 = "http://naver.com" # True
        result = validators.url(url4)
        if result:
            self.assertTrue(result, 'It is invalid.')
        else:
            self.assertFalse(result, 'It is not invalid.')
            
        url5 = "http://www.naver.com." # ValidationFailure
        result = validators.url(url5)
        if result:
            self.assertTrue(result, 'It is invalid.')
        else:
            self.assertFalse(result, 'It is not invalid.')
            
        url6 = "http://www.naver.codm" # True
        result = validators.url(url6)
        if result:
            self.assertTrue(result, 'It is invalid.')
        else:
            self.assertFalse(result, 'It is not invalid.')
        
    def test_validate_url_using_validator(self):
        dict_json = [
                        {'hotel_name': 'Luxor Las Vegas', 'hotel_url': 'www.vegas-hotel.com', 'price': 5000, 'rate': 5}, 
                        {'hotel_name': 'Izmailovo Hotel', 'hotel_url': 'www.izmalove.l/', 'price': 4426, 'rate': 5}, 
                        {'hotel_name': 'Shinagawa Prince Hotel', 'hotel_url': 'prince.jp', 'price': 3680, 'rate': 3}, 
                        {'hotel_name': 'Marina Bay Sands', 'hotel_url': 'www.marina.', 'price': 2561, 'rate': 1}, 
                        {'hotel_name': 'Galaxy Macau', 'hotel_url': 'http://www.galaxy-macau.com', 'price': 2200, 'rate': 7}, 
                        {'hotel_name': 'Dacheng International', 'hotel_url': 'w.hotels.com', 'price': 2000, 'rate': -2}
                    ]
         
        valid_list = []
        invalid_list = []
        for h in dict_json:
            tmp_dict = {}
            if validators.url(h['hotel_url']):
                tmp_dict.update(h)
                valid_list.append(tmp_dict)
            else:
                tmp_dict.update(h)
                invalid_list.append(tmp_dict)
                
        self.assertEqual(len(valid_list), 1)
        self.assertEqual(len(invalid_list), 5)
                  
    def test_check_integer_type_and_number_range(self):
        integer_value = 5
        self.assertEqual(type(integer_value) == int, True, 'ginven value is number')
        
        string_value = '4'
        self.assertEqual(type(string_value) != 'int', True, 'ginven value is number')
        
        self.assertEqual(integer_value in range(0, 6), True)
        
        negative_value = -1
        self.assertEqual(negative_value in range(0, 6), False)
            
    def test_compare_strings(self):
        str1 = 'yim'
        str2 = 'yIm'
        
        self.assertEqual(str1.lower() == str2.lower(), True)
        
    def test_check_relative_path(self):
        print(pathlib.Path(__file__).resolve().parents[1] )
        print(pathlib.Path.cwd())
            
if __name__ == '__main__':
    unittest.main()