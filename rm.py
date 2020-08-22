'''
tp rm
'''

import sys
import tp


def main():
    '''main function'''
    port = tp.Tp()
    port.rm(sys.argv[1])


if __name__ == "__main__":
    main()
