import subprocess
import sys
from pathlib import Path


def convert_files_in_directory(directory_path):
    python_files = Path(directory_path).glob('*.py')
    for python_file in python_files:
        conversion_command = ['/home/hung/.local/share/virtualenvs/stock_investing-VnnxBpBf/bin/p2j', str(python_file)]
        subprocess.run(conversion_command, check=True)
        print(f"Converted {python_file}")
        python_file.unlink()
        print(f"Deleted {python_file}")

if __name__ == '__main__':
    folder_name = sys.argv[1]
    directory_path = f'/home/hung/Documents/make_color/AI/applying-math-with-python/materials/{folder_name}'
    convert_files_in_directory(directory_path)