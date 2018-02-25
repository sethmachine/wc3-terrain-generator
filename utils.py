# -*- coding: utf-8 -*-

"""File system utility functions to simplify file manipulation.

.. moduleauthor:: Seth-David Donald Dworman <sdworman@brandeis.edu>

"""

import os
import re

def absolute_filepaths(directory, depth=0, file_pattern=r'.+'):
    """Lists all files joined to directory path.

    Args:
        depth (int): How many subdirectories to explore.
                    A depth of 0 only explores the first subdirectory,
                    while a depth of -1 explores all subdirectories.
        file_pattern (str): Valid regular expression denoting which
                            files to yield in directory exploration.

    """
    file_re = re.compile(file_pattern)
    for x in os.listdir(directory):
        path = os.path.join(directory, x)
        if os.path.isfile(path):
            if file_re.search(path):
                yield path
        elif depth != 0:
            for f in absolute_filepaths(path, depth - 1, file_pattern):
                yield f

def absolute_dirpaths(directory, depth=0, file_pattern=r'.+'):
    """Lists all files joined to directory path.

    Args:
        depth (int): How many subdirectories to explore.
                    A depth of 0 only explores the first subdirectory,
                    while a depth of -1 explores all subdirectories.
        file_pattern (str): Valid regular expression denoting which
                            files to yield in directory exploration.

    """
    file_re = re.compile(file_pattern)
    for x in os.listdir(directory):
        path = os.path.join(directory, x)
        if os.path.isdir(path):
            if file_re.search(path):
                yield path
            if depth != 0:
                for f in absolute_dirpaths(path, depth - 1, file_pattern):
                    yield f

def truncate(f, n):
    """Truncates/pads a float f to n decimal places without rounding

    """
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

if __name__ == '__main__':
    pass
    
    

