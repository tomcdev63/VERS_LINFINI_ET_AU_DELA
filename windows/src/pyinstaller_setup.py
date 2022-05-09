import PyInstaller.__main__

# pyinstaller.exe --onefile --runtime-tmpdir=. --hidden-import win32timezone --windowed --noconsole --icon=file_xml.ico myservice.py
# pyinstaller.exe --onefile --runtime-tmpdir=. --hidden-import win32timezone --icon=file_xml.ico serivce.py

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