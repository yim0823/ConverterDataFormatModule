# -*- coding: utf-8 -*-

'''
Created on 2019. 1. 2.

@author: gtrus
'''
import unittest

class Test(unittest.TestCase):

    def test_install(self):
        package = 'Requests'
        import pip
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            # As of pip version >= 10.0.0,
            from pip._internal import main as pipmain 
            pipmain (['install', '--user', package])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_install_and_import_packages']
    unittest.main()