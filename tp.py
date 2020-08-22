'''
=======================
  tp: cd by reference
=======================

given {reference: path}, tp reference calls cd path
'''

from yaml import load, dump, Loader, Dumper


HINT = "usage: tp [<command>] <reference> [<path>]\n\n"\
        "positional argument:\n"\
        "  command:\n"\
        "    add:   add reference for current/given path\n"\
        "    rm:    remove reference"


class Tp:
    '''tp tool class'''

    def __init__(self):
        with open('/Users/alexchen/toolbox/tp/data.yml', 'r') as data:
            self.data = load(data, Loader=Loader)

    def write(self):
        '''write to data.yml'''
        with open('/Users/alexchen/toolbox/tp/data.yml', 'w') as data:
            dump(self.data, data, Dumper=Dumper)

    def add(self, reference, path):
        '''add reference: path pair to data'''
        if self.data is None:
            self.data = dict()
        self.data[reference] = path
        self.write()

    def rm(self, reference):
        '''remove reference'''
        del self.data[reference]
        self.write()

    def path(self, reference):
        '''return the corresponding path
        if path was not found, return the current dir .'''
        if self.data[reference] is not None:
            path = self.data[reference]
        else:
            path = '.'
        return path


if __name__ == "__main__":
    print(HINT)
