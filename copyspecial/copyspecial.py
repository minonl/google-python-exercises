#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    special_paths = []
    try:
        filenames = os.listdir(dir)
        for filename in filenames:
            match = re.search(r'\_\_[\w]+\_\_', filename)
            if match:
                special_paths.append(os.path.abspath(
                    os.path.join(dir, filename)))
    except IOError:
        sys.stderr.write('error reading: '+dir)
    else:
        #for path in special_paths:
        #    print path
        return special_paths


def copy_to(paths, dir):
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
    except IOError:
        sys.stderr.write('directory failure: '+dir)
    else:
        try:
            for path in paths:
                shutil.copy(path, os.path.join(dir, os.path.basename(path)))
        except IOError:
            sys.stderr.write('copy failure: [from]'+paths+'|[to]'+dir)


def zip_to(paths, zippath):
    command = 'zip -j '+zippath
    for path in paths:
          command += ' ' + os.path.abspath(path)
    print 'Command I\'m going to do:', command
    (status, output) = commands.getstatusoutput(command)
    if status:
        sys.stderr.write(output)
        sys.exit(status)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    paths = get_special_paths(args[0])
    if len(todir)>0:
        copy_to(paths,todir)
    if len(tozip)>0:
        zip_to(paths,tozip)


if __name__ == "__main__":
    main()
