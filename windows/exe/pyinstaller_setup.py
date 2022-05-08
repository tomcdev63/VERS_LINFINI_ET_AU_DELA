import PyInstaller.__main__


PyInstaller.__main__.run([
    'VIEAD.py',
    '--onefile',
    '--runtime-tmpdir=.',
    '--hidden-import',
    'win32timezone',
    '--windowed',
    '--icon=buzz.ico',
    '--noconsole'
])