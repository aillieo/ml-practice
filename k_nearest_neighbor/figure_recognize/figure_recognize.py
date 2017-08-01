#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image
from k_nearest_neighbor.knn import *
import os


def img2vec(img):
    vec = zeros((1, 1024))
    im = Image.open(img)
    im.convert('1')
    pixel = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if pixel[i, j]:
                vec[0, 32 * j + i] = 1
    return vec


def classify_images():
    image_labels = []
    full_path = os.path.join('data', 'data_bmp', 'data4training')
    data_training_list = os.listdir(full_path)
    m = len(data_training_list)
    training_mat = zeros((m, 1024))
    for i in range(m):
        filename_str = data_training_list[i]
        label = int((filename_str.split('.')[0]).split('_')[0])
        image_labels.append(label)
        training_mat[i, :] = img2vec(os.path.join(full_path, filename_str))
    full_path = os.path.join('data', 'data_bmp', 'data4testing')
    data_testing_list = os.listdir(full_path)
    error_count = 0.0
    m_test = len(data_testing_list)
    for i in range(m_test):
        filename_str = data_testing_list[i]
        label = int((filename_str.split('.')[0]).split('_')[0])
        vector_under_test = img2vec(os.path.join(full_path, filename_str))
        classify_result = classify0(vector_under_test, training_mat, image_labels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classify_result, label))
        if classify_result != label:
            error_count += 1.0
    print("\nthe total number of errors is: %d" % error_count)
    print("\nthe total error rate is: %f" % (error_count / float(m_test)))


if __name__ == '__main__':
    classify_images()
