# coding: utf-8

'''
Created on 2018. 12. 30.

@author: Taehyoung Yim
'''

import abc

class ConverterAlgorithm(object):
    '''
    Abstract class that used as an interface
    this class makes sure that child classes have implemented
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def writeTo(self, filePathNameExt, dataframe):
        '''
        Write the data object to the output.
        '''
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, TestConverterAlgorithm is supposed to be an interface / abstract class!')
        