"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

BUILD.
"""

import os
import sys

assert len(sys.argv) == 2, 'Argument is required, usage: build.py pyinstaller/pip/twine/gource'
mode = sys.argv[1].strip()
python = 'python3' if not sys.platform == 'win32' else 'py -3.7'

if mode == 'pip':
    if os.path.isdir('dist/pip'):
        for k in os.listdir('dist/pip'):
            if 'PyMultiDictionary-' in k:
                os.remove(f'dist/pip/{k}')
    if os.path.isdir('build'):
        for k in os.listdir('build'):
            if 'bdist.' in k or k == 'lib':
                os.system(f'rm -rf build/{k}')
    os.system(f'{python} setup.py sdist --dist-dir dist/pip bdist_wheel --dist-dir dist/pip')

elif mode == 'twine':
    if os.path.isdir('dist/pip'):
        os.system(f'{python} -m twine upload dist/pip/*')
    else:
        raise FileNotFoundError('Not distribution been found, execute build.py pip first')

elif mode == 'gource':
    os.system('gource -s 0.25 --title PyMultiDictionary --disable-auto-rotate --key '
              '--highlight-users --disable-bloom --multi-sampling -w --transparent --path ./')

else:
    raise ValueError(f'Unknown mode {mode}')
