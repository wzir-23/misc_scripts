#!/usr/bin/env python3
''' Command line TODO tool that stores a list of tasks in ~/.todo.txt that
    is manipulated via a(dd), d(elete) and l(ist) arguments. Supply -h or
    --help for usage information
'''
import os
import sys


def print_usage(todo_script):
    ''' print usage information '''
    print(f'\nusage: {todo_script} [-had] text')
    print('\ta "text to add     # add task')
    print('\td <number>         # delete task')
    print('\tl (or no argument  # list tasks\n')


def handle_arguments(fname, args):
    ''' simple argument handling '''
    if len(args) == 1:          # no args, all
        read_file(fname)
        return
    if args[1] == '-h' or args[1] == '--help' or len(args) > 3:
        print_usage(args[1])
        return
    if args[1] == 'l':          # list all
        read_file(fname)
    if args[1] == 'a':          # add entry
        add_entry(fname, args[2])
    if args[1] == 'd':          # remove entry
        delete_entry(fname, args[2])
    return


def read_file(fname):
    ''' read TODO file and print contents '''
    if os.path.isfile(fname):
        with open(fname,'r', encoding='UTF-8') as fhandle:
            entries = fhandle.read().splitlines()
        for count, msg in enumerate(entries, start=1):
            print(f'{count:<3} {msg}')


def add_entry(fname, msg):
    ''' add a new item to TODO list '''
    mode = 'w'
    if os.path.isfile(fname):
        mode = 'a'
    with open(fname, mode, encoding='UTF-8') as fhandle:
        fhandle.write(msg + '\n')
    print(f'Added: {msg}')


def delete_entry(fname, number):
    ''' remove item from TODO list '''
    new_todos = []
    if number.isnumeric():
        number = int(number)
        if os.path.isfile(fname):
            with open(fname, 'r', encoding='UTF-8') as fhandle:
                entries = fhandle.read().splitlines()
            for count, msg in enumerate(entries, start=1):
                if count == number:
                    print(f'Removed {msg}')
                else:
                    new_todos.append(msg)
        if new_todos:
            with open(fname, 'w', encoding='UTF-8') as fhandle:
                for msg in new_todos:
                    fhandle.write(msg + '\n')
        else:
            os.remove(fname)


def main():
    ''' program main function '''
    fname = '~/.todo.txt'
    fname = os.path.expanduser(fname)
    handle_arguments(fname, sys.argv)


if __name__ == "__main__":
    main()
