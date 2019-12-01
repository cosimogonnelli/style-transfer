import sys
import matplotlib.pyplot as plt
import numpy as np
from keras import backend as K
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import load_img, img_to_array

# get keras image array from file
def get_img_arr(filepath, out_dims):
    image = load_img(path=filepath, target_size=out_dims)
    img_arr = img_to_array(image)
    return image, K.variable(preprocess_input(np.expand_dims(img_arr, axis=0)), dtype='float32')

# define paths to content, style, output images
C_PATH = 'rhodes.jpg'       # content image
S_PATH = 'kandinsky.jpg'    # style image
O_PATH = 'results/out.jpg'  # output image

# optionally get content img, style img from command line
if len(sys.argv) == 3:
    C_PATH = argv[1]
    S_PATH = argv[2]

# Output image dimensions
OUT_HEIGHT = 512
OUT_WIDTH = 512
OUT_DIMS = (OUT_HEIGHT, OUT_WIDTH)

# load images from file
c_img, c_img_arr = get_img_arr(C_PATH, OUT_DIMS)
s_img, s_img_arr = get_img_arr(S_PATH, OUT_DIMS)

# generate random rgb image for inital output
o_img_arr = np.random.randint(256, size=(OUT_WIDTH, OUT_HEIGHT, 3)).astype('float64')
o_img_arr = preprocess_input(np.expand_dims(o_img_arr, axis=0))
o_img0 = K.placeholder(shape=(1, OUT_WIDTH, OUT_HEIGHT, 3))

