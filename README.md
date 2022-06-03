# Move files with same names

This Python script allows you to copy/move files with same name but difference extension

## About

- While training neural networks, we require images and annotations that maybe present in the same/different folders unequally.
- For training, we ensure that for each image, its corresponding annotations are present.
- However, while labeling it is possible that several images do not contain their corresponding annotation files (say XML, TXT or JSON).
- This script separates images from the folder based on annotation files.

## Usage

```bash
 python3 move_file.py --annotations "/folder/containing/annotations/" --ext_a xml --images "folder/containing/images" --ext_i png      
```

- annotations flag is used to point to folder containing annotations based on their file names you want to move the corresponding images
- ext_a flag is used for the type of files you want to move. It could be xml, json, txt, etc.
- images flag is for the folder that contains several images from where you wish to filter only those that have their annotations
- ext_i indicates the extension type for images, which could be png, jpg, jpeg, etc.
- --move is used to move files from the original directory. Default behaviour is copy unless specified otherwise

