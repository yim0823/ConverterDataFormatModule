# coding: utf-8

'''
Created on 2018. 12. 30.

@author: Taehyoung Yim
'''

from src.package.converter.converter_algorithm import ConverterAlgorithm
import src.package.utils.logger as my_logger

import codecs
import json

logger = my_logger.get_logger()

class JsonConverter(ConverterAlgorithm):
    '''
    Convert to Json file at specific path.
    '''

    def writeTo(self, filePathNameExt, dataframe):
        '''
        Write to Json file.
        
        @param filePathNameExt: The path where the Json file will be created.
        @param dataframe: Data loaded from the source file.
        '''
        try:
            logger.info('  Writing data to "%s".', filePathNameExt)
            with codecs.open(filePathNameExt, 'w', encoding='utf-8') as fp:
                json.dump(dataframe, fp, ensure_ascii=False)
        except Exception as e:
            logger.error('%s-%s', e.code, e.read())
            raise
            
    def convert_csv_dataframe_to_json_dataframe(self, dataframe):
        logger.info('  to json: orient="records", date_format="epoch", double_precision=10, force_ascii=True, date_unit="ms"')
        try:
            json_string = dataframe.to_json(orient='records', date_format="epoch", double_precision=10, force_ascii=True, date_unit="ms")
            return json.loads(json_string)
        except ValueError as e:
            logger.error('%s-%s', e.code, e.read())
            raise
            
            