import cv2
import numpy as np

capture = cv2.VideoCapture(0)

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']

gender_list = ['Male', 'Female']

def load_caffe_models():
    """ Load models for age and gender """
    age_net = cv2.dnn.readNetFromCaffe('deploy_age.proto.txt'
