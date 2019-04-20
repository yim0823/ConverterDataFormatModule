# -*- coding: utf-8 -*-

'''
Created on 2019. 1. 2.

@author: Taehyoung Yim
'''

def install_packages(package):
    import pip
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        # As of pip version >= 10.0.0,
        from pip._internal import main as pipmain 
        pipmain (['install', '--user', package])
    
if __name__ == '__main__':
    install_packages('argh')