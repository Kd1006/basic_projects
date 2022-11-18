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
def get_mad_libs_from_command_line():
    parser = argparse.ArgumentParser(description='color, noun, celebrity')
    parser.add_argument('passed_info', type=str, nargs='+')
    args = parser.parse_args()
    return args.passed_info

if __name__ == '__main__':
    # color, plural_noun, celebrity = get_mad_libs_from_user()
    color, plural_noun, celebrity = get_mad_libs_from_command_line()
    print_mad_libs(color, plural_noun, celebrity)
