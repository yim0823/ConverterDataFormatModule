# coding: utf-8

'''
Created on 2018. 12. 30.

@author: Taehyoung Yim
'''

from src.package.converter.converter_algorithm import ConverterAlgorithm
import src.package.utils.logger as my_logger

import yaml
import codecs

logger = my_logger.get_logger()

class YamlConverter(ConverterAlgorithm):
    '''
    Convert to YAML file at specific path.
    '''

    def writeTo(self, filePathNameExt, dataframe):
        '''
        Write to YAML file.
        
        @param filePathNameExt: The path where the YAML file will be created.
        @param dataframe: Data loaded from the source file.
        '''
        try:
            logger.info('Writing data to %s...', filePathNameExt)
            with codecs.open(filePathNameExt, 'w', encoding='utf-8') as fp:
                yaml.dump(dataframe, fp, default_flow_style=False, allow_unicode=True)
        except Exception as e:
            logger.error('%s-%s', e.code, e.read())
            raise
            
    