import os
import sys

if __name__ == '__main__':

    file_name = os.path.join(sys.prefix, 'config/data.json')
    if not os.path.isfile(file_name):
        print(f"Unable to find file where expected: {file_name}")
    else:
        print("All is as expected!")