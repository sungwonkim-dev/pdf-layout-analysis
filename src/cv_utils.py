import cv2 as cv2
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler


def extract_metadata_from_img(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = resize_img(img)
    height, width = get_height_and_width(img)
    horizontal_projection = convert_img_to_projection(img)
    vertical_projection = get_vertical_projection(height, width, img)
    return height, width, horizontal_projection, vertical_projection


def resize_img(img):
    img = cv2.resize(img, dsize=(1000, 1618), interpolation=cv2.INTER_AREA)
    return img


def normalize_projection(projection):
    projection = projection.reshape(-1, 1)
    return MinMaxScaler().fit_transform(projection)


def get_height_and_width(img):
    height, width = img.shape[:2]
    return height, width


def convert_img_to_projection(img):
    projection = np.sum(img, 1, dtype=np.float32)
    return normalize_projection(projection)


def get_vertical_projection(height, width, img):
    projection = []
    for index in range(width):
        col = img[0:height, index: index + 1]
        projection.append(np.sum(col))

    projection = np.array(projection, dtype=np.float32)
    return normalize_projection(projection)
