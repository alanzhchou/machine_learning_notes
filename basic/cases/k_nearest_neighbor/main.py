#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       : main
@Author     : alanzhchou
@Create     : 19/8/7-2:04
@Python     : 3.62
@Version    : 1.0
@Email      : alanzhchou@gmail.com
@Copyright  : MIT License - Copyright (c) 2019 alanzhchou
@description:

@Change log :
19/8/7-2:04 created
"""

import numpy as np


def create_dataset() -> (np.ndarray, list):
    """
    create dataset of sample
    :return:
        group : the numpy array of two dismenion which discribe scene numbers
            => every row has two element,
            first => number of kiss scene
            second => number of fight scene
        labels : the label type string of every movie
    """
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    labels = ['爱情片', '爱情片', '动作片', '动作片']
    return group, labels


if __name__ == '__main__':
    group, labels = create_dataset()

    print(group)
    print(labels)


