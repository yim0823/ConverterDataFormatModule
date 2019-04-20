# coding: utf-8

'''
Created on 2018. 12. 28.

@author: Taehyoung Yim
'''

import sys
import argparse

"""
py test_main.py \
  -- \
"""

def main(unused_args):
    print(FLAGS.type)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The objective of this program is to convert the data from one format to other formats.')
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
      "--training_data",
      type=str,
      default="",
      help="Path to training data (tf.Example in TFRecord format)")
    parser.add_argument(
      "--num_conv",
      type=str,
      default="[48, 64, 96]",
      help="Number of conv layers along with number of filters per layer.")
    parser.add_argument(
      "--num_nodes",
      type=int,
      default=128,
      help="Number of node per recurrent network layer.")
    
    
#     args = parser.parse_args()
#     if args.type:
#         print('type')
    
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)
    
    