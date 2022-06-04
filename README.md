# Move files with same names

Python script to copy/move files with the same name but different extensions.

## About

- The images and annotations needed for neural network training may unequally be in the same/different folders.
- During training, we ensure that the corresponding annotations are present for each image.
- During labeling, it is possible that some images will not contain their corresponding annotations (such as XML, TXT, or JSON).
- This script separates images (all formats such as PNG, JPG, etc.) from the folder based on annotation files (all formats TXT, JSON, etc.).

## Usage

```bash
 python3 move_file.py --annotations "/folder/containing/annotations/" --ext_a xml --images "folder/containing/images" --ext_i png      
```

- `annotations` flag is used to point to folder containing annotations based on their file names you want to move the corresponding images
- ext_a flag is used for the type of files you want to move. It could be xml, json, txt, etc.
- images flag is for the folder that contains several images from where you wish to filter only those that have their annotations
- ext_i indicates the extension type for images, which could be png, jpg, jpeg, etc.
- --move is used to move files from the original directory. Default behaviour is copy unless specified otherwise

