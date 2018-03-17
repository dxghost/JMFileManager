import pyglet
import time
class mp3Player:
    def __init__(self,n=0,playList=[]):
        self.n = n
        self.playList = playList
        self.player = pyglet.media.Player()
        
    def addToPlayList(self,songDirectory):
        self.playList.append(songDirectory)

    def play(self):
        self.player.queue(pyglet.resource.media(self.playList[self.n]))
        self.player.play()

    def pause(self):
        self.player.pause()
        
    def stop(self):
        self.seek(0)
        self.pause()
    
    def previous(self):
        if self.n>0:
            self.pause()
            self.n-=1
            self.__init__(self.n,self.playList)
            self.play()

    def next(self):
        if self.n<len(self.playList)-1:
            self.pause()
            self.n+=1
            self.__init__(self.n,self.playList)
            self.play()
        
    def seek(self,second):
        self.player.seek(second)

