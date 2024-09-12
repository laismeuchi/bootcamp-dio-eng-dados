import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histogramas
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shave, "Specify 2 images with the same shape"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, differece_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images:", score)
    normalized_diffference_image = (differece_image - np.min(differece_image))/(np.max(differece_image) - np.min(differece_image))
    return normalized_diffference_image

def tranfer_histogram(imag1, image2):
    matched_image = match_histogramas(imag1, image2, mutichanne=True)
    return matched_image

