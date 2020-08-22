'''
tp
'''

import sys
import tp


def main():
    '''main function'''
    port = tp.Tp()
    print(port.path(sys.argv[1]))


if __name__ == "__main__":
    main()
