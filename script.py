from asyncio import constants
from genericpath import exists
from importlib.resources import path
import json
import pprint as pp
import subprocess
import sys
import os
from pyunpack import Archive
xEditPath = "Tools\\SSEEdit\\SSEEdit.exe"
poserDataGenPath = "Tools\\PoserDataGen\\PoserDataGen.exe"

def initialize():
    if not(os.path.exists("Tools\\SSEEdit")):
        Archive("Tools\\SSEEDIT.rar").extractall("Tools\\")
    if not(os.path.exists("Tools\\PoserDataGen")):
        Archive("Tools\\PoserDataGen.rar").extractall("Tools\\")

def loadJson():
    packsjson = json.load(open("packs.json", "r"))
    packs = packsjson["packs"]
    pp.pprint(packs)
    pp.pprint(type(packs))

initialize()
subprocess.call(xEditPath)