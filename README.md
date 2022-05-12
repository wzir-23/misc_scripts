# misc_scripts
Random tools I've put together to simplyfy my life inside a terminal

## copy_images_to_EXIF_date_structure.py
I use a photo management workflow outside the MacOS ecosystem where I first
copy all iPhone/iPad files to the filesystem using PhotoSync, then copy the
images to a date based file structure (i.e YYYY/MM/DD) using this script.

Dependencies:
- exiftool

Usage:
```
./copy_images_to_EXIF_date_structure.py <image_folder>
```
