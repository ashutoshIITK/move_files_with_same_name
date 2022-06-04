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

- `annotations`: You can point to a folder containing annotations based on their file names to move the corresponding images with this flag.
- `ext_a`: This flag indicates the type of files (annotations) you intend to move. It could be XML, JSON, TXT, etc.
- `images` This is used for a folder containing several images from which you wish to filter out only those with annotations as specified by the `annotations` flag.
- `ext_i` Image extensions, such as PNG, JPG, JPEG, etc., are described here.
- `--move` (Optional) is used to move files from the original directory. The default behavior is copying files instead of moving unless specified otherwise.

