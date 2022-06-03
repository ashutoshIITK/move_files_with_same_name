import os
import shutil

try:
    import argparse
except ImportError:
    os.system("pip3 install "+ "argparse")

parser = argparse.ArgumentParser()
parser.add_argument('--annotations', type=str, help='annotations path')
parser.add_argument('--ext_a',  type=str, default="xml", help='annotation extension')
parser.add_argument('--images', type=str, help='images path')
parser.add_argument('--ext_i',  type=str, default="png", help='image extension')
parser.add_argument('--move',  action='store_true')
parser.set_defaults(move=False)
opt = vars(parser.parse_args())

ANNOTATIONS_FOLDER_PATH = opt["annotations"]
ANNOTATIONS_EXTENSION = opt["ext_a"]
IMAGES_FOLDER_PATH = opt["images"]
IMAGES_EXTENSION = opt["ext_i"]
MOVE = opt["move"]

_, _, annotations = next(os.walk(ANNOTATIONS_FOLDER_PATH))
annotations = [annotation for annotation in annotations if annotation.endswith(f".{ANNOTATIONS_EXTENSION}")]

for annotation in annotations:
    BASE_FILE_NAME = annotation.split(f".{ANNOTATIONS_EXTENSION}")[0]
    print(BASE_FILE_NAME)
    os.makedirs(f"{ANNOTATIONS_EXTENSION}", exist_ok=True)
    os.makedirs(f"{IMAGES_EXTENSION}", exist_ok=True)

    if MOVE:
        # Move annotation files
        shutil.move(f"{ANNOTATIONS_FOLDER_PATH}/{annotation}", f"./{ANNOTATIONS_EXTENSION}/{annotation}")
        # Move image files
        shutil.move(f"{IMAGES_FOLDER_PATH}/{BASE_FILE_NAME}.{IMAGES_EXTENSION}", f"./{IMAGES_EXTENSION}/{BASE_FILE_NAME}.{IMAGES_EXTENSION}")

    else:
        # Copy annotation files
        shutil.copyfile(f"{ANNOTATIONS_FOLDER_PATH}/{annotation}", f"./{ANNOTATIONS_EXTENSION}/{annotation}")
        # Copy image files
        shutil.copyfile(f"{IMAGES_FOLDER_PATH}/{BASE_FILE_NAME}.{IMAGES_EXTENSION}", f"./{IMAGES_EXTENSION}/{BASE_FILE_NAME}.{IMAGES_EXTENSION}")



