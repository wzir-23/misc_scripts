#!/usr/bin/env python3
''' Recursively searches for movies and images in a directory (including
    sub-directories and copies them to file structures on the format:

    images/YYYY/MM/DD
    movies/YYYY/MM/DD

    Usage:
    ./copy_images_to_EXIF_date_structure.py <image_folder>
'''

import shutil
import subprocess
import os
import sys

IMAGES = 1
MOVIES = 2


# Filmformat: .mov, .mp4, .3gp,
def find_image_files(filepath):
    ''' searches for images and movies in the supplied filepath based on file
        suffix
    '''
    img_files = []
    mov_files = []
    file_ext = ['.xmp', '.jpg', '.JPG', '.heic', '.HEIC',
                '.dng', '.DNG', '.PNG', '.RAF']
    mov_ext = ['.mov', '.MOV', '.mp4', '.3gp', '.MP4']
    for dirpath, _, filenames in os.walk(filepath):
        for fname in filenames:
            if fname.endswith(tuple(file_ext)):
                img_files.append(os.path.join(dirpath, fname))
            elif fname.endswith(tuple(mov_ext)):
                mov_files.append(os.path.join(dirpath, fname))
            elif fname.endswith('.exposurex5'):
                continue
            else:
                print(f'Not processed: {fname}')
    return (img_files, mov_files)


def new_file_path(img_files, FILE_TYPE):
    ''' set destination path for images/movies and supplies it to copy_file()
    '''
    if FILE_TYPE == IMAGES:
        prefix = 'images'
    else:
        prefix = 'movies'
    for fname in img_files:
        year, month, day = find_creation_date(fname, prefix)
        destination = f'{prefix}/{year}/{month}/{day}/'
        copy_file(fname, destination)


def find_creation_date(fname, prefix):
    ''' retrieves creation date for supplied object '''
    print(fname)
    process = subprocess.Popen(["exiftool", fname],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               encoding='utf8')
    exif_output = process.communicate()[0]
    exif_output = exif_output.split('\n')
    if 'images' in prefix:
        match_str = 'Date/Time Original'
    else:
        match_str = 'Creation Date'
    for exif in exif_output:
        if match_str in exif:
            # x = ['Date/Time Original              ', '2022:05:08 11:24:37']
            # date_time = '2022:05:08 11:24:37'
            date_time = exif.split(': ')[1]
            break
    if 'date_time' in locals():
        date_str = date_time.split(' ')[0]
    else:  # we have a picture that is not a photo
        for exif in exif_output:
            if 'File Modification Date/Time' in exif:
                date_time = exif.split(': ')[1]
                date_str = date_time.split(' ')[0]
                break
    return date_str.split(':')


def create_dir(directory):
    ''' creates new directory if needed '''
    new_dir = os.path.dirname(directory)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


def copy_file(fname, destination):
    ''' copies files '''
    create_dir(destination)
    shutil.copy2(fname, destination)
    copy_meta_file(fname, destination)


def copy_meta_file(fname, destination):
    ''' Handle metafiles from Exposure software X5. Should be updated to cover
        all later versions'''
    meta_path_prefix = 'Exposure Software/Exposure X5'
    meta_path = os.path.join(os.path.dirname(fname), meta_path_prefix) + '/'
    meta_file = meta_path + os.path.split(fname)[1] + '.exposurex5'
    if os.path.exists(meta_file):
        meta_dest = os.path.join(destination, meta_path_prefix) + '/'
        create_dir(meta_dest)
        shutil.copy2(meta_file, meta_dest)


def main():
    ''' Recursively search and copy image files to a date based file structure
    '''
    img_files, mov_files = find_image_files(sys.argv[1])
    if img_files:
        new_file_path(img_files, IMAGES)
    if mov_files:
        new_file_path(mov_files, MOVIES)


if __name__ == "__main__":
    main()
