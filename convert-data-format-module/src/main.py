# coding: utf-8

'''
Created on 2018. 12. 31.

@author: Taehyoung Yim
'''
import sys
sys.path.append('../')
import argparse
import pathlib

from src.package.loader.csv_loader import CsvLoader
from src.package.converter.json_converter import JsonConverter
from src.package.converter.converter_service import ConverterService
from src.package.converter.yaml_converter import YamlConverter
from src.package.utils.utils import Utils
from src.package.utils.validator import Validator
import src.package.utils.logger as my_logger

logger = my_logger.get_logger()

"""
python3 main.py \
 --input_file_name hotels.csv \
 --sort_columns name stars \
 --sort_types True, False \
 --group_by_columns name address \
 --output_file_format json
 
or

python3 main.py \
 -i hotels.csv \
 -sc name stars \
 -st True, False \
 -g name address \
 -o json
"""

DATA_PATH = str(pathlib.Path(__file__).resolve().parents[1]) + '/data'

COLUMN_NAME_HOTEL_NAME = 'name'
COLUMN_NAME_HOTEL_ADDRESS = 'address'
COLUMN_NAME_HOTEL_STARS = 'stars'
COLUMN_NAME_HOTEL_CONTACT = 'contact'
COLUMN_NAME_HOTEL_PHONE = 'phone'
COLUMN_NAME_HOTEL_URI = 'uri'

SEPERATOR = ','

def main(unused_args):
    
    logger.info('::: Start Convert Data Format Module :::')
    
    file = FLAGS.input_file_name.split('.')
    file_name = file[0]
    given_file_format = file[1]
    
    sortCols = FLAGS.sort_columns
    sortTypes = FLAGS.sort_types
    groupbyCols = FLAGS.group_by_columns
    
    output_format = FLAGS.output_file_format.lower()
    
    utils = Utils()
    validator = Validator()
    
    logger.info('++++++++++++++++ Conditions +++++++++++++++')
    logger.info('+ Input file: %s' %file_name + '.' + given_file_format)
    logger.info('+ Output format: %s' %output_format)
    logger.info('+ Sort Columns: %s' %sortCols)
    logger.info('+ Sort Types: %s' %sortTypes)
    logger.info('+ Group by Columns: %s' %groupbyCols)
    logger.info('++++++++++++++++++++++++++++++++++++++++++')
    
    # 1. load csv file
    logger.info('Start loading csv file.')
    
    csv_loader = CsvLoader()
    dataframe = csv_loader.loadCsv(utils.create_filepath(DATA_PATH, file_name, given_file_format, True), SEPERATOR, sortCols, sortTypes, groupbyCols)
    
    # 2. convert csv dataframe to json dataframe to extract values.
    logger.info('Start converting csv dataframe to json dataframe to extract values.')

    jsonConverter = JsonConverter()
    dataframe = jsonConverter.convert_csv_dataframe_to_json_dataframe(dataframe)
    
    # 3. validate several conditions
    logger.info('Starting validate several conditions.')
    
    valid_list = list()
    invalid_list = list()
    for data in dataframe:
        #  - Hotel name validation
        if not validator.validate_unicode_for_value(data[COLUMN_NAME_HOTEL_NAME]):
            logger.debug('   The data is not valid for name UTF-8. %s', data)
            invalid_list.append(data)
            continue
          
        #  - Hotel URL validation
        if not validator.validate_url(data[COLUMN_NAME_HOTEL_URI]):
            logger.debug('   The data is not valid for URL. %s', data)
            invalid_list.append(data)
            continue
         
        #  - Hotel rating validation
        if not validator.check_hotel_rate(data[COLUMN_NAME_HOTEL_STARS]):
            logger.debug('   The data is not valid for stars. %s', data)
            invalid_list.append(data)
            continue
        
        valid_list.append(data)
        
    logger.info('   Seperate valid and invalid data.')
        
    # 4. Write dataframe to files.
    logger.info('Start converting data to other format.')
    
    if output_format == 'json':
        logger.info('   Preparing to convert data to JSON format.')
        jsonConverter = JsonConverter()
        converter_service = ConverterService(jsonConverter)
          
    elif output_format == 'yaml':
        logger.info('   Preparing to convert data to YAML format.')
        yamlConverter = YamlConverter()
        converter_service = ConverterService(yamlConverter)
    
    output_files = list()
    dic = {'valid': valid_list, 'invalid': invalid_list}
    for key, value in dic.items():
        filePathNameExt = utils.create_filepath(DATA_PATH, key + '_' + file_name, output_format, False)
        converter_service.convert(filePathNameExt, value)
        
        output_files.append(filePathNameExt)
    
    # 5. check whether or not created files.
    logger.info('Checking the results.')
    for file_path in output_files:
        if utils.check_file_exists(file_path):
            logger.info('   Create successfully the "%s" file.', file_path)
            if utils.check_file_size(file_path) < 1:
                logger.warn('   But, It would be empty.')
        else:
            logger.critical('   It failed to create the "%s" file.', file_path)
    
    logger.info('::: Finish Convert Data Format Module :::')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The objective of this program is to convert the data from one format to other formats.')
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
        "-i",
        "--input_file_name",
        required=True,
        type=str,
        default="",
        help="File name to read data. (tf.Example in 'trivago.csv')")
    parser.add_argument(
        "-sc",
        "--sort_columns",
        required=False,
        nargs='+',
        default=None, # name stars
        help="Target columns for sorting data. (tf.Example in 'name stars')")
    parser.add_argument(
        "-st",
        "--sort_types",
        required=False,
        nargs='+', 
        type="bool",
        default=None, # True, False
        help="Specify descending, ascending order for the columns specified in '--sort_columns'. True is ascending, False is descending (tf.Example in 'True False')")
    parser.add_argument(
        "-g",
        "--group_by_columns",
        required=False,
        nargs='+',
        default=None, # stars address
        help="Target columns for grouping data. (tf.Example in stars address)")
    parser.add_argument(
        "-o",
        "--output_file_format",
        required=True,
        type=str,
        default="json",
        help="Format to write data. (tf.Example in 'json')")
     
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)
    