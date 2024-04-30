# Packages
import numpy as np
from skimage.io import imread
import napari
# Load image
image = imread("nuclei1_out_c00_dr90_image.tif")
# Open image in napari
viewer = napari.view_image(image)
napari.run()