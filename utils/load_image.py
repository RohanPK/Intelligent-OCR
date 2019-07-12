import numpy as np
import cv2

def crop_image(image, bb):
    ''' Helper function to crop the image by the bounding box (in percentages)
    '''
    (x, y, w, h) = bb
    x = x * image.shape[1]
    y = y * image.shape[0]
    w = w * image.shape[1]
    h = h * image.shape[0]
    (x1, y1, x2, y2) = (x, y, x + w, y + h)
    (x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
    return image[y1:y2, x1:x2]

def resize_image(image, desired_size):
    ''' Helper function to resize an image while keeping the aspect ratio.
    Parameter
    ---------
    
    image: np.array
        The image to be resized.

    desired_size: (int, int)
        The (height, width) of the resized image

    Return
    ------

    image: np.array
        The image of size = desired_size

    bounding box: (int, int, int, int)
        (x, y, w, h) in percentages of the resized image of the original
    '''
    size = image.shape[:2]
    if size[0] > desired_size[0] or size[1] > desired_size[1]:
        ratio_w = float(desired_size[0])/size[0]
        ratio_h = float(desired_size[1])/size[1]
        ratio = min(ratio_w, ratio_h)
        new_size = tuple([int(x*ratio) for x in size])
        image = cv2.resize(image, (new_size[1], new_size[0]))
        size = image.shape
            
    delta_w = max(0, desired_size[1] - size[1])
    delta_h = max(0, desired_size[0] - size[0])
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
            
    color = image[0][0]
    if color < 230:
        color = 230
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=float(color))
    crop_bb = (left/image.shape[1], top/image.shape[0], (image.shape[1] - right - left)/image.shape[1],
               (image.shape[0] - bottom - top)/image.shape[0])
    image[image > 230] = 255
    return image, crop_bb


def image_loader(file_names,box_locations):

    # From model params
    MAX_IMAGE_SIZE_LINE = (60, 800)

    form_images = []

    for file in file_names:
        image_array = []
        form = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

        if np.size(form) == 1:
            pass
        for each_box in box_locations:
            print(each_box)
            im = form[each_box[0][1]:each_box[1][1],each_box[0][0]:each_box[1][0]].copy()
            im, _ = resize_image(im, MAX_IMAGE_SIZE_LINE)
            image_array.append(im)
        form_images.append(image_array)

    return form_images