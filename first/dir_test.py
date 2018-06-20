import os

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.exists('\\IdeaResource'))
print(os.path.isfile('.\\dir_test.py'))
print(os.path.join('\\first', '\\www'))

from pathlib import Path

Path.mkdir()

