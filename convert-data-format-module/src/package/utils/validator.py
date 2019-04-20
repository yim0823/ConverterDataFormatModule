# -*- coding: utf-8 -*-

'''
Created on 2018. 12. 30.

@author: gtrus
'''

import validators

class Validator(object):
    '''
    class that collect validation for several conditions.
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def validate_unicode_for_value(self, value: str) -> bool:
        '''
        A function that checks if the value is Unicode.
        
        @value the value to be validated.
        '''
        if isinstance(value, str):
            return True
        else:
            return False
            
    def validate_url(self, url: str) -> bool:
        '''
        A function that validates the url using validators library.
        
        @url the value to be validated.
        '''
        if validators.url(url):
            return True
        else:
            return False
        
    def check_hotel_rate(self, rate: int) -> bool:
        '''
        A function that checks the hotel rate to specific conditions.
          - as a number from 0 to 5
          - no negative numbers
        
        @rate the value to be checked.
        '''
        if rate in range(0, 6):
            return True
        else:
            return False
        
    
    