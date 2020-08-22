'''
tp add
'''

import sys
import tp


def main():
    '''main function'''
    port = tp.Tp()
    port.add(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
