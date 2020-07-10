"""
Design a jukebox

"""

class JukeBox:
    _user=None
    _cdPlayer=None
    _cdCollection=[]
    _ts=None #track selector


    def __init__(self,user,cdPlayer,cdCollection,ts):
        self._user=user
        self._cdPlayer=cdPlayer
        self._cdCollection=cdCollection
        self._ts=ts

    def getCurrentTrack(self):
        return self._ts.getCurrentSong()

    def processOneUser(self,user):
        self._user=user

class Playlist:
    _track=None
    _queue=[]

    def __init__(self, track, queue):
        self._track=track
        self._queue=queue

    def getNextTrackToPlay(self):
        if len(self._queue)>0:
            return self._queue[0]
        else:
            return None

    def queueUpTrack(self,song):
        self._queue.appen(song)

class Song:
    pass

class TrackSelector:
    _currentSong=None

    def __init__(self,song):
        self._currentSong=song

    def setTrack(self, song):
        self._currentSong = song

    def getCurrentSong(self):
        return self._currentSong

class User:
    _name=""

    def getName(self):
        return self._name

    def setName(self,name):
        self._name=name
    
    def getuser(self):
        return self
        
