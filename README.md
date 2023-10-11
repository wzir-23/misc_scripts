# misc_scripts
Random tools I've put together to simplify my life inside a terminal

### Tests
For running the tests, you need to install the "coverage" package, preferably with pip from venv and run the
tests by executing the following commands:
```
coverage run --source '.' -m unittest -v
coverage report -m
```


## copy_images_to_EXIF_date_structure.py
I use a photo management workflow outside the MacOS ecosystem where I first
copy all iPhone/iPad files to the file system using PhotoSync, then copy the
images to a date based file structure (i.e YYYY/MM/DD) using this script.

Dependencies:
- exiftool

Usage:
```
./copy_images_to_EXIF_date_structure.py <image_folder>
```

## futhark.py
Transliterate from the latin alphabet and som different futharks (runic
alohabets) and vice versa

Usage:
```
boran@amair:~/repos/git/public_wzir/misc_scripts> ./futhark.py
Enter text: Thorleif reste denna sten
```

## todo.py
A simple tool for managing a TODO list stored as .todo.txt in the home
directory. Create a link 't' in your bin directory for easier access to it.

```
usage: -h [-had] text
        a "text to add     # add task
        d <number>         # delete task
        l (or no argument  # list tasks
```

Example Usage:
```
t a "first entry"
Added: first entry

t a "second entry"
Added: second entry

t
1   first entry
2   second entry

d 2
Removed second entry
```
