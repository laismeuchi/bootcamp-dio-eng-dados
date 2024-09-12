from skimage.transform import resize

def resize_image(image, porportion):
    assert 0 <= porportion <=1, "Specify a valid proportion between 0 and 1"
    height = round(image.shape[0]*porportion)
    width= round(image.shape[1]*porportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized