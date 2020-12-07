from scipy.io import loadmat
import numpy as np
import sys

from os.path import join
from classification.utils.utils import dense_to_one_hot

from classification.datasets.const import DATA_PATH


def load_svhn():
    svhn_train = loadmat(join(DATA_PATH, 'train_32x32.mat'))
    svhn_test = loadmat(join(DATA_PATH, 'test_32x32.mat'))
    svhn_train_im = svhn_train['X']
    svhn_train_im = svhn_train_im.transpose(3, 2, 0, 1).astype(np.float32)
    svhn_label = dense_to_one_hot(svhn_train['y'])
    svhn_test_im = svhn_test['X']
    svhn_test_im = svhn_test_im.transpose(3, 2, 0, 1).astype(np.float32)
    svhn_label_test = dense_to_one_hot(svhn_test['y'])

    return svhn_train_im, svhn_label, svhn_test_im, svhn_label_test
