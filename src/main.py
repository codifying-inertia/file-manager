import json

from pathlib import Path

from file_loader import FileLoader

file_path = 'file1.txt'
base_path = Path(__file__).parent
full_path = f'{base_path}\\{file_path}'

file1_loader = FileLoader(full_path, True)
lines = file1_loader.get_contents()
print(lines)

json_str = json.dumps(lines)
print(json_str)
with open("file1.json", "w") as json_output_file:
  json_output_file.write(json_str)