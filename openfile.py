from PIL import Image
import os
import subprocess as sp
from os import startfile
import glob

class openfile:
    def __init__(self, paths):
        self.paths = paths
    def openimage(paths):
        img = Image.open(paths)
        img.show()

    def opentext(paths):
        programName = "notepad.exe"
        sp.Popen([programName, paths])


    def video_music_player(paths):
        startfile(paths)


    def openpdf(paths):
        sp.Popen([paths],shell=True)


    def runfile(paths):
        os.startfile(paths)

