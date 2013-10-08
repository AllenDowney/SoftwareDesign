"""Test code for palindrome.py.

Author: Allen B. Downey
"""

def has_no_e(s):
    return True


def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        # only print palindromes
        if has_no_e(word):
            print word


if __name__ == '__main__':
    main()
