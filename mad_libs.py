import argparse


def print_mad_libs(color, plural_noun, celebrity):
    print(f'Roses are {color}')
    print(f'{plural_noun} are blue')
    print(f'I love {celebrity}')


def get_mad_libs_from_user():
    color = input("Enter a color:")
    plural_noun = input("Enter a plural noun:")
    celebrity = input("Enter a celebrity:")
    return color, plural_noun, celebrity


def parse_args():
    # passed values from the command line are parsed and stored/returned in an object.
    # required = false allows users to be prompted if they want to
    parser = argparse.ArgumentParser(description='color, noun, celebrity')
    parser.add_argument('--color', type=str, required=False)
    parser.add_argument('--plural_noun', type=str, required=False)
    parser.add_argument('--celebrity', type=str, required=False)
    passed_args = parser.parse_args()
    return passed_args


def get_mad_libs_from_args(passed_args):
    return passed_args.color, passed_args.plural_noun, passed_args.celebrity


# there are two ways to call the code.
# >> python mad_lib.py
# It will require us to put values individually in the mad libs.
# >> python mad_libs.py --color <str> --plural noun <str> --celebrity <str>
# It will require you to put the values on command line.
if __name__ == '__main__':
    args = parse_args()

    color, plural_noun, celebrity = get_mad_libs_from_args(args)
    # if there is no value passed on command line, ask the users
    if color is None:
        color, plural_noun, celebrity = get_mad_libs_from_user()

    print_mad_libs(color, plural_noun, celebrity)
