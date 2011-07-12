# -*- coding: utf-8 -*-
# 

import xbmc,xbmcaddon
from trakt_cache import TraktCache

__author__ = "Ralph-Gordon Paul, Adrian Cowan"
__credits__ = ["Ralph-Gordon Paul", "Adrian Cowan", "Justin Nemeth",  "Sean Rudford"]
__license__ = "GPL"
__maintainer__ = "Ralph-Gordon Paul"
__email__ = "ralph-gordon.paul@uni-duesseldorf.de"
__status__ = "Production"

__settings__ = xbmcaddon.Addon( "script.TraktUtilities" )
__language__ = __settings__.getLocalizedString

# Caches all information between the add-on and the web based trakt api
class Movie:
    _remoteId
    _title
    _year
    _playcount
    _watchlistStatus
    _recommendedStatus
    _libraryStatus
    
    def __init__(self, remoteId):
        if remoteId is None:
            raise ValueError("Must provide the id for the movie")
        self._remoteId = remoteId
        
    def save(self):
        TraktCache.saveMovie(self)
        
    def scrobble(self):
        raise NotImplementedError("This function has not been written")
    def rate(self, rating):
        raise NotImplementedError("This function has not been written")
    def shout(self, text):
        raise NotImplementedError("This function has not been written")
        
    def setSeenStatus(self, value):
        raise NotImplementedError("This function has not been written")
    def getSeenStatus(self):
        raise NotImplementedError("This function has not been written")
        
    def setLibraryStatus(self, value):
        raise NotImplementedError("This function has not been written")
    def getLibraryStatus(self):
        raise NotImplementedError("This function has not been written")
        
    def setWatchingStatus(self, value):
        raise NotImplementedError("This function has not been written")
    def getWatchingStatus(self):
        raise NotImplementedError("This function has not been written")
        
    def setWatchlistStatus(self, value):
        raise NotImplementedError("This function has not been written")
    def getWatchlistStatus(self):
        raise NotImplementedError("This function has not been written")
        
    def traktise(self):
        movie = {}
        movie['title'] = _title
        movie['year'] = _year
        movie['plays'] = _playcount
        movie['in_watchlist'] = _watchlistStatus
        movie['in_collection'] = _libraryStatus
        if str(_remoteId).find('imbd=') == 0:
            movie['imdb_id'] = _remoteId[5:]
        if str(_remoteId).find('tmbd=') == 0:
            movie['tmdb_id'] = _remoteId[5:]
        return movie
        
    @staticmethod
    def fromTrakt(movie):
        if 'imdb_id' in movie:
            local = Movie("imdb="+movie['imdb_id'])
        else if 'tmdb_id' in movie:
            local = Movie("tmdb="+movie['tmdb_id'])
        else
            return None
        local._title = movie['title']
        local._year = movie['year']
        local._playcount = movie['plays']
        local._watchlistStatus = movie['in_watchlist']
        local._libraryStatus = movie['in_collection']
        return local
     
    @staticmethod
    def fromXbmc(movie):
        local = Movie("imdb="+)
        if 'imdbnumber' not in movie or movie['imdbnumber'].trim() == "":
            traktMovie = searchTraktForMovie(movie['title'], movie['year'])
            if traktMovie is None:
                return None
            if 'imdb_id' in traktMovie:
                local = Movie("imdb="+traktMovie['imdb_id'])
            else if 'tmdb_id' in traktMovie:
                local = Movie("tmdb="+traktMovie['tmdb_id'])
            else
                return None
        else:
            local = Movie("imdb="+movie['imdbnumber'].trim())
        local._title = movie['title']
        local._year = movie['year']
        local._playcount = movie['playcount']
        return local