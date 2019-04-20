# -*- coding: utf-8 -*-

'''
Created on 2019. 1. 1.

@author: Taehyoung Yim
'''
import src.package.utils.logger as my_logger

def test_logger():
    logger = my_logger.get_logger()
    
    logger.debug("program started")
    logger.info("Security is one of your major goals in life.")
    logger.warn("Some of your aspirations tend to be pretty unrealistic.")
    
    try:
        logger.debug("attempting to do something tricksy")
    except:
        logger.exception("caught unhandled exception.")
    finally:
        logger.info("program exiting, cleaning up")

if __name__ == '__main__':
    test_logger()