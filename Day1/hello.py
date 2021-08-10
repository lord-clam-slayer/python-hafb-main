print("Hello Waldo")
"""
Author: me
"""
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()
def main():
    """
    This is where the action is
    :return: None
    """
    args = get_args()
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
    main()
print(__name__)