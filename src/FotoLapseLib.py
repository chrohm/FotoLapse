from PIL import Image, ImageDraw
from pathlib import Path
import moviepy.editor as mpy
import numpy
import os

def get_photos_paths_in_dir_as_list(photo_dir):
    paths = [photo_dir / Path(x) for x in os.listdir(photo_dir)]
    image_path_list = [(path.stat().st_ctime, path) for path in paths]
    image_path_list.sort()
    image_path_list = [path for time, path in image_path_list]
    return image_path_list

def photo_filename_to_numpy_arr(photo_path):
    pic = Image.open(photo_path)
    pic = numpy.asarray(pic)
    return pic
