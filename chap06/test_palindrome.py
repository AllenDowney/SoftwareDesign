"""Test code for palindrome.py.

Author: Allen B. Downey
"""

from palindrome import is_palindrome


def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        # only print palindromes
        if is_palindrome(word):
            print word


if __name__ == '__main__':
    main()
