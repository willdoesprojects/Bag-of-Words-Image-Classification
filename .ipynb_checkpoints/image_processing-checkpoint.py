# image_processing.py
from PIL import Image
import numpy as np

def load_image(filepath):
    img = Image.open(filepath)
    img = img.resize((1024, 1024))
    return (np.asarray(img).astype(float) / 255)[:, :, :3]
