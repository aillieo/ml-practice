#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import os

path_in = 'testDigits'


def txt2mat(txt_file):
    mat = np.zeros((32, 32))
    txt = open(txt_file)
    for i in range(32):
        line_str = txt.readline()
        for j in range(32):
            mat[i, j] = int(line_str[j])
    return mat


def mat2img(mat, txt_file):
    im = Image.new('1', (32, 32))
    im.load()
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            if mat[x, y]:
                im.putpixel((y, x), 1)
    filename = os.path.split(txt_file)
    name = filename[-1].split('.')[0]
    bmp_name = format("%s.bmp" % name)
    im.save(os.path.join('output',bmp_name))


def txt2img(txt_file):
    return mat2img(txt2mat(txt_file), txt_file)


if __name__ == "__main__":

    txt_files = os.listdir(path_in)
    if not os.path.exists(os.path.join(path_in,'output')):
        os.makedirs('output')
    for txt_file in txt_files:
        if txt_file[0] != '.':
            txt2img(os.path.join(path_in, txt_file))
