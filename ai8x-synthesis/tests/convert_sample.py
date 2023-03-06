#!/usr/bin/env python3
###################################################################################################
# Copyright (C) 2021 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
###################################################################################################
"""
Convert sample input data to int64.  maybe try using ai8xnormalize
"""
import argparse

import numpy as np

parser = argparse.ArgumentParser(description='Convert sample input to int64')
parser.add_argument('input', help='path to the input sample data')
parser.add_argument('output', help='path to the output file (converted data)')
args = parser.parse_args()

d = np.int64(np.load(args.input))
print(np.amin(d))
print(np.amax(d))
# print(args.input)

test = np.load('/home/skim945/ECE189/ai8x-synthesis/tests/al2.npy')
print(test.shape)
np.save(args.output, d, allow_pickle=False, fix_imports=False)

