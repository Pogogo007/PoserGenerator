from asyncio import constants
from genericpath import exists
from pathlib import Path
import pprint as pp
import shutil
import subprocess
import sys
import os
from tempfile import mkdtemp, tempdir
import winreg
from pyunpack import Archive
import winreg

regPath = winreg.QueryValueEx(winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,
                                               "SOFTWARE\WOW6432Node\Bethesda Softworks\Skyrim Special Edition"), "installed path"
                              )
skyrimPath = regPath[0]
temp = mkdtemp()
tempdata = temp + "\\data"
os.mkdir(tempdata)
xEditPath = "Tools\\SSEEdit\\SSEEdit.exe"
poserDataGenPath = "Tools\\PoserDataGen\\PoserDataGen.exe"
requirements = ["Skyrim.esm", "Update.esm"]


def initialize():
    # os.rmdir(temp)
    # if not (os.path.exists("Tools\\SSEEdit")):
    #    Archive("Tools\\SSEEDIT.rar").extractall("Tools\\")
    if not (os.path.exists("Tools\\PoserDataGen")):
        Archive("Tools\\PoserDataGen.rar").extractall("Tools\\")
    for requirement in requirements:
        shutil.copy(skyrimPath + "data\\" + requirement, tempdata)
    files = Path("packs\\").glob("*")
    for file in files:
        Archive(file).extractall(tempdata)

    bruh = Path(tempdata).rglob('*.esp')
    for file in bruh:
        print(type(file))
        cut = Path(file).parent
        pp.pprint(cut)


initialize()

# Archive(file).extractall("tools\\")
# subprocess.call(xEditPath)
