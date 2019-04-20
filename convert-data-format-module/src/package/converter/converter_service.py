# coding: utf-8

'''
Created on 2018. 12. 30.

@author: aehyoung Yim
'''

class ConverterService(object):
    '''
    Maintain a reference to a Strategy object.
    '''

    def __init__(self, converterAlgorithm):
        '''
        Constructor
        '''
        self._converterAlgorithm = converterAlgorithm
        
    def convert(self, filePathNameExt, dataframe):
        self._converterAlgorithm.writeTo(filePathNameExt, dataframe)
        