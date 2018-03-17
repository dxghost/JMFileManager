import pyglet
import time

class mp3Player:
    def __init__(self, n=0, playList=[]):
        self.n = n
        self.playList = playList
        self.player = pyglet.media.Player()
        self.playing = False

    def addToPlayList(self, songDirectory):
        self.playList.append(songDirectory)

    def clearPlayList(self):
        self.__init__(0, [])

    def jumpInPlayList(self, songDirectory):
        self.stop()
        self.indexOfMusic = self.playList.index(songDirectory)
        self.__init__(self.indexOfMusic, self.playList)
        self.play()

    def play(self):
        self.player.queue(pyglet.media.load(self.playList[self.n]))
        self.player.play()
        self.playing = True


    def pause(self):
        self.player.pause()
        self.playing = False

    def stop(self):
        self.seek(0)
        self.pause()
        self.playing = False

    def previous(self):
        if self.n > 0:
            self.pause()
            self.n -= 1
            self.__init__(self.n, self.playList)
            self.play()

    def next(self):
        if self.n < len(self.playList) - 1:
            self.pause()
            self.n += 1
            self.__init__(self.n, self.playList)
            self.play()

    def seek(self, second):
        self.player.seek(second)


