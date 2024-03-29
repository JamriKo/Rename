# Run rename.py after using AdobeBridge batch renaming.
# Set rename.py and media files in the same directory.

import os
import re

connector, count, startloop = '-', 0, 0
typelist = "".join(['.jpg', '.heic', '.png', '.mp4', '.mov'])
endloop = startloop + 1
while (startloop-endloop)!=0:
    startloop = count
    files = os.listdir('./')
    for item in files:
        filename, type = os.path.splitext(item)
        if bool(re.search(type, typelist, re.IGNORECASE)) and type != '' and filename[13] != connector:
            newname = filename[:13] + connector + filename[13:15] + connector + filename[15:]
            os.rename(item, newname + type)
            count += 1
            print((newname + type).ljust(30), str(count).rjust(6), 'Files Renamed Succesfully!')
            break
    endloop = count
