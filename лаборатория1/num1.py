"""Вывести информацию в консоль о логических дисках,
именах, метке тома, размере типе файловой системы.
"""

import win32api
import win32file

import string
from ctypes import windll


print("      Диски >>> ", win32api.GetLogicalDriveStrings())
driveTypes = ['DRIVE_UNKNOWN', 'DRIVE_NO_ROOT_DIR', 'DRIVE_REMOVABLE', 'DRIVE_FIXED', 'DRIVE_REMOTE', 'DRIVE_CDROM', 'DRIVE_RAMDISK']

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


for drive in get_drives():
    if not drive:
        continue
    print("Диск:", drive)
    try:
        typeIndex = windll.kernel32.GetDriveTypeW(u"%s:\\"%drive)
        print("Тип:",driveTypes[typeIndex])
        print("Свободных байт на диске >>> ", win32file.GetDiskFreeSpaceEx(u"%s:\\"%drive)[2])
    except Exception:
        print( "error:")
