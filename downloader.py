from pytube import YouTube

"""
Downloader is used to download video and provides functions to handle video properties
"""


class Downloader:
    def __init__(self, url):
        self.url = url
        self.videos = None
        self.video_data = None
        self.youTube = YouTube(url)
        self.createYoutube(self.url)

    # createYoutube(url) creates YouTube object using url so that videos can be
    # downloaded
    # createYoutube: self, String -> void
    def createYoutube(self, url):
        self.youTube = YouTube(url)

    # downloadVideos() download videos and store them in a list. If it fails to
    # download, it returns False otherwise it returns True
    # downloadVideos: self -> Bool
    def downloadVideos(self):
        # download videos and store them
        try:
            self.videos = self.youTube.get_videos()
            return True
        except BufferError:
            return False

    # getVideoData() gathers important data for the video and stores in dictionary.
    # It returns true if data gathered successfully and false otherwise
    # getVideoData: self -> Bool
    def getVideoData(self):
        # name: author
        # length: length_seconds
        # views: view_count
        # rating: avg_rating

        try:
            data = self.youTube.get_video_data()
            args = data["args"]

            self.video_data = {"author": args["author"],
                               "length": args["length_seconds"],
                               "views": args["view_count"],
                               "rating": args["avg_rating"]}
            return True
        except BufferError:
            return False

    # setUrl(url) updates the youTube url for the downloader
    # setUrl: self, String - > void
    def setUrl(self, url):
        self.url = url
        self.createYoutube(self.url)

    # getTime() returns the time in hours, minutes and seconds
    # getTime: self -> string
    def getTime(self):
        time_sec = self.video_data["time"]
        seconds = time_sec % 60
        minutes = time_sec / 60
        hours = time_sec / 3600

        if hours != 0:
            return "{}:{}:{}".format(hours, minutes, seconds)
        else:
            return "{}:{}".format(minutes, seconds)

    # getAuthor() returns the name of the author of the video
    # getAuthor: self -> string
    def getAuthor(self):
        return self.video_data["author"]

    # getViews() returns the view count of the video
    # getViews: self -> int
    def getViews(self):
        return self.video_data["views"]

    # getRating() returns the the rating of the video
    # getRating: self -> float
    def getRating(self):
        return self.video_data["rating"]