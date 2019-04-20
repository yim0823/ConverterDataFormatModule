# -*- coding: utf-8 -*-

'''
Created on 2019. 1. 1.

@author: Taehyoung Yim
'''
import logging as _logging
import threading
import pathlib

from datetime import datetime

_logger = None
_logger_lock = threading.Lock()

DATA_PATH = str(pathlib.Path(__file__).resolve().parents[3]) + '/data'
LOG_PATH = DATA_PATH + '/logs'

def get_logger():
    """Return TF logger instance."""
    global _logger
    
    # Use double-checked locking to avoid taking lock unnecessarily.
    if _logger:
        return _logger
    
    _logger_lock.acquire()
    
    try:
        if _logger:
            return _logger
        
        # Scope the Converter logger to not conflict with users' loggers.
        logger = _logging.getLogger('Converter')
        logger.setLevel(_logging.DEBUG)

        formatter = _logging.Formatter("%(asctime)s - %(levelname)s - %(processName)s - [%(name)s] - %(message)s")
        dev_formatter = _logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - [%(name)s] - %(message)s")

        # StreamHandler sends to stderr by default
        stream_hander = _logging.StreamHandler()
        stream_hander.setLevel(_logging.INFO)
        stream_hander.setFormatter(formatter)
        
        # FileHandler sends to a named file
        file_handler = _logging.FileHandler("{0}/{1}.log".format(LOG_PATH, datetime.now().strftime('%Y-%m-%d')))
        file_handler.setLevel(_logging.INFO)
        file_handler.setFormatter(formatter)
        
        # outputs *everything* to a seperate file, good for debugging during dev
        dev_file_handler = _logging.FileHandler("{0}/{1}.dev.log".format(LOG_PATH, datetime.now().strftime('%Y-%m-%d')))
        dev_file_handler.setLevel(_logging.DEBUG)
        dev_file_handler.setFormatter(dev_formatter)
        
        logger.addHandler(stream_hander)
        logger.addHandler(file_handler)
        logger.addHandler(dev_file_handler)
        
        _logger = logger
        logger.debug("configuration loaded")
        
        return _logger
    finally:
        _logger_lock.release()
