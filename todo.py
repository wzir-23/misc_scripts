#!/usr/bin/env python3

import os
import sys


def print_usage(todo_script):
    print('\nusage: %s [-had] text' % todo_script)
    print('\ta "text to add     # add task')
    print('\td <number>         # delete task')
    print('\tl (or no argument  # list tasks\n')


def handle_arguments(args):
    if len(args) == 1:          # no args, all
        read_file()
        return
    if args[1] == '-h' or args[1] == '--help' or len(args) > 3:
        print_usage(args[1])
        return
    if args[1] == 'l':          # list all
        read_file()
    if args[1] == 'a':          # add entry
        add_entry(args[2])
    if args[1] == 'd':          # remove entry
        delete_entry(args[2])
    return


def read_file():
    fname = '~/.todo.txt'
    fname = os.path.expanduser(fname)
    if os.path.isfile(fname):
        with open(fname,'r') as fhandle:
            entries = fhandle.read().splitlines()
        for count, msg in enumerate(entries, start=1):
            print(f'{count:<3} {msg}')


def add_entry(msg):
    fname = '~/.todo.txt'
    fname = os.path.expanduser(fname)
    os.path.isfile(fname)
    fhandle = open(fname,'a')
    fhandle.write(msg + '\n')
    fhandle.close()
    print(f'Added: {msg}')


def delete_entry(number):
    fname = '~/.todo.txt'
    fname = os.path.expanduser(fname)
    new_todos = []
    if not number.isnumeric():
        return False
    number = int(number)
    if os.path.isfile(fname):
        with open(fname,'r') as fhandle:
            entries = fhandle.read().splitlines()
        for count, msg in enumerate(entries, start=1):
            if count == number:
                print(f'Removed {msg}')
            else:
                new_todos.append(msg)
    if new_todos:
        with open(fname, 'w') as fhandle:
            for msg in new_todos:
                fhandle.write(msg + '\n')
    else:
        os.remove(fname)


def main():
    handle_arguments(sys.argv)


if __name__ == "__main__":
    main()
