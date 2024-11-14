#!/usr/bin/env python3
""" program that scans specified directory for snppet files containing
    proven programming constructs in different languages. Each snippet
    file should have a header in the first line on the format:
    language: keyword1 [keyword2] ...
"""

import os
import subprocess
import sys

snippet_files_dir = '~/.snippets/'


def print_usage():
    """ print usage """
    this_program = sys.argv[0]
    print(f'\n{this_program}: keep track of program snippets')
    print('Usage:')
    print(f'/t{this_program} <language> <keyword>\n')


def scan_snippet_dir(snippet_dir):
    """ get a list of all files in the snippet directory """
    snippet_dir = os.path.expanduser(snippet_files_dir)
    if not os.path.isdir(snippet_dir):
        return False
    # get a full path list of actual files in snippet_dir
    file_list = [file for file in os.listdir(snippet_dir)
                    if os.path.isfile(os.path.join(snippet_dir, file))]
    file_index = []
    for file in file_list:
        with open(os.path.join(snippet_dir, file), encoding="utf-8") as fhandle:
            first_line = fhandle.readline().strip('\n')
            file_index.append(f'{file}:{first_line}')
    return file_index


def pick_alternative(file_index, language, keyword):
    """ find matching snippet files """
    if not file_index:
        return False
    matching_files = []
    for file in file_index:
        _, lang_str, keyword_str = file.lower().split(':')
        if language in lang_str and keyword in keyword_str:
            matching_files.append(file)
    return matching_files


def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)
    snippet_dir = os.path.expanduser(snippet_files_dir)
    language = sys.argv[1]
    keyword = sys.argv[2]
    file_index = scan_snippet_dir(snippet_dir)
    matching_files = pick_alternative(file_index, language, keyword)
    if len(matching_files) > 1:
        print("Pick a file to view:")
        for index, entry in enumerate(matching_files):
            print(str(index) + '. ' + entry)
        pick = int(input("? "))
        print(pick)
        picked_filename = os.path.expanduser(snippet_dir) \
                + '/' \
                + matching_files[pick].split(':')[0]
    else:
        picked_filename = os.path.expanduser(snippet_files_dir) \
                            + '/' \
                            + matching_files[0].split(':')[0]
    subprocess.run(['cat', picked_filename], check = False)
    print()

if __name__ == "__main__":
    main()
