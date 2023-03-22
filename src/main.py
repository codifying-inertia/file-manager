from pathlib import Path

from file_loader import FileLoader

file_path = 'file1.txt'
base_path = Path(__file__).parent
full_path = f'{base_path}\\{file_path}'

file1_loader = FileLoader(full_path, True)
lines = file1_loader.get_contents()
print(lines)

file_path = 'file2.txt'
base_path = Path(__file__).parent
full_path = f'{base_path}\\{file_path}'

file2_loader = FileLoader(full_path, False)
lines = file2_loader.get_contents()
print(lines)