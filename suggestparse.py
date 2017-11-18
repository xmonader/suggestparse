"""
suggestparse extends argparse.ArgumentParser from stdlib to allow suggestions based on the closest matches 

"""

import argparse
from difflib import get_close_matches
from gettext import gettext as _, ngettext


class SuggestingArgumentParser(argparse.ArgumentParser):

    def parse_args(self, args=None, namespace=None):
        allvalidopts = []
        for act in self._actions:
            allvalidopts.extend(act.option_strings)

        args_success, argv = self.parse_known_args(args, namespace)
        suggested_args = []
        for arg in argv:
            closest_matches = get_close_matches(arg, allvalidopts)
            if closest_matches:
                suggested_args.extend(closest_matches)

        if argv:
            if suggested_args:
                print("Did you mean: ", suggested_args)
            msg = _('unrecognized arguments: %s')
            self.error(msg % ' '.join(argv))
        return args_success


def test():
    parser = SuggestingArgumentParser()
    parser.add_argument('--add', '-a', help='add')
    parser.add_argument('--edit', '-e', help='edit')
    parser.add_argument('--delete', '-d', help='delete')
    parser.add_argument('--view', '-v', help='view')
    print(parser.parse_args())

if __name__ == '__main__':
    test()