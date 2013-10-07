"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import time


def make_word_list1():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    return t


def make_word_list2():
    """Reads lines from a file and builds a list using list +.

    returns: list of strings
    """
    t = []
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'

