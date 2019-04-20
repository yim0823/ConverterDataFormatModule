# -*- coding: utf-8 -*-

'''
Created on 2018. 12. 30.

@author: Taehyoung Yim
'''

import pandas
import src.package.utils.logger as my_logger

logger = my_logger.get_logger()

class CsvLoader(object):
    '''
    Class for reading CSV files
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def loadCsv(self, filePathNameExt, separator, sortCols=None, sortTypes=None, groupbyCols=None):
        '''
        Load csv file at specific path.
        Depending on the option, the loaded data can be sorted or grouped.
        
        @param filePathNameExt: The path where the CSV file is located
        @param separator: Delimiter to use in csv file.
        @param sortCols: Specify columns if you want to sort. The form is a list.
        @param sortTypes: Specify list for multiple sort orders if you want to sort.
                        ascending is True, descending is False. The form is list of bool.
        @param groupbyCols: Specify columns if you want to groupby. 
        '''
        try:
            logger.info('  Reading data from "%s".', filePathNameExt)
            dataframe = pandas.read_csv(filePathNameExt, encoding='utf-8', sep=separator)
        except FileNotFoundError as e:
            logger.error('%s-%s', e.code, e.read())
            raise 
        
        logger.info('  Complete to read data from "%s".', filePathNameExt)
        
        if sortCols is not None: # when need sort by column 
            if sortTypes is None:
                raise ValueError(
                    "sortCols was not None but sortTypes was None. Determin the ascending or descending.")
            
            logger.info('  Processing to sort data by %s', sortCols)
            return dataframe.sort_values(by=sortCols, axis=0, ascending=sortTypes, na_position='first')
        
        if groupbyCols is not None: # when need group by column
            logger.info('  Processing to group data by %s', sortCols)
            return dataframe.groupby(by=groupbyCols, sort=True, group_keys=True).apply(lambda x: x.to_json(orient='records', date_format="epoch", double_precision=10, force_ascii=True, date_unit="ms"))
        
        if sortCols is None and groupbyCols is None: # when not need sort and group 
            return dataframe
        
