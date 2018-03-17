from PIL import Image
import os
import subprocess as sp
from os import startfile
import glob

class openfile:
    def __init__(self, paths):
        self.paths = paths
    def openimage(self):
        img = Image.open(self.paths)
        img.show()

    def opentext(self):
        programName = "notepad.exe"
        sp.Popen([programName, self.paths])


    def video_music_player(self):
        startfile(self.paths)


    def openpdf(self):
        sp.Popen([self.paths],shell=True)


    def runfile(self):
        os.startfile(self.paths)

