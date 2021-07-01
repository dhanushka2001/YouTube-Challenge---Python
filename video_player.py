"""A video player class."""

from .video_library import VideoLibrary
from operator import itemgetter
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    current = None
    pause = False
    playlists = {}

    def __init__(self):
        self._video_library = VideoLibrary()

    def get_current(self):
        
        return self.current

    def video_exist(self,video_id):
        videoidlist = []
        #check if video even exists
        videos = self._video_library.get_all_videos()
        for i in videos:
            videoidlist.append(i.video_id)
        if video_id not in videoidlist:
            return False
        else:
            return True
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        #print(f"{num_videos} videos in the library")
        print(str(num_videos) + " videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")        
        videos = self._video_library.get_all_videos()
        videoslist = []
        for i in videos:
            videoslist.append([i.title,i.video_id,i.tags])
    
        x = sorted(videoslist, key=itemgetter(0))
        for i in x:
            print(i[0] + " (" + i[1] + ") [" + ' '.join(i[2]) +"]") 
        
        
    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        
        video = self._video_library.get_video(video_id)
        #use video ID to be specific about what video is playing

        
        #check if video even exists
        
        if self.video_exist(video_id) == False:
            print("Cannot play video: Video does not exist")
        else:
            self.pause = False
            if self.current == None:
                print("Playing video: " + video.title)
                self.current = video_id
                
            else:
                currentvideo = self._video_library.get_video(self.current)
                if self.current == video_id:
                    print("Stopping video: " + video.title)
                    print("Playing video: " + video.title)
                else:
                    print("Stopping video: " + currentvideo.title)
                    print("Playing video: " + video.title)
                    self.current = video_id
                    #replace current video id with new one

    def stop_video(self):
        """Stops the current video."""
        
        if self.current == None:
            print("Cannot stop video: No video is currently playing")
        else:
            currentvideo = self._video_library.get_video(self.current)
            print("Stopping video: " + currentvideo.title)
            self.current = None
            self.pause = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        num_videos = len(self._video_library.get_all_videos())
        n = random.randint(1,num_videos)
        valuelist = self._video_library.get_all_videos()
        self.play_video(valuelist[n-1].video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self.current == None:
            print("Cannot pause video: No video is currently playing")
        else:
            currentvideo = self._video_library.get_video(self.current)
            if self.pause == True:
                print("Video already paused: " + currentvideo.title)
            else:
                print("Pausing video: " + currentvideo.title)
                self.pause = True
            
            

    def continue_video(self):
        """Resumes playing the current video."""
        if self.current == None:
            print("Cannot continue video: No video is currently playing")
        else:
            if self.pause == False:
                print("Cannot continue video: Video is not paused")
            else:
                currentvideo = self._video_library.get_video(self.current)
                print("Continuing video: " + currentvideo.title)
                self.pause = False

    def show_playing(self):
        """Displays video currently playing."""
        if self.current == None:
            print("No video is currently playing")
        else:
            currentvideo = self._video_library.get_video(self.current)
            if self.pause == False:
                print("Currently playing: " + currentvideo.title + " (" + currentvideo.video_id + ") [" + ' '.join(currentvideo.tags) + "]")
            else:
                print("Currently playing: " + currentvideo.title + " (" + currentvideo.video_id + ") [" + ' '.join(currentvideo.tags) + "] - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        lower = playlist_name.lower()
        if lower not in list(self.playlists.keys()):
            self.playlists[lower] = []
            print("Successfully created new playlist: " + playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        lower = playlist_name.lower()
        if lower not in list(self.playlists.keys()):
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")
        else:
            if self.video_exist(video_id) == False:
                print("Cannot add video to " + playlist_name + ": Video does not exist")
            else:
                if video_id in self.playlists[lower]:
                    print("Cannot add video to " + playlist_name + ": Video already added")
                else:
                    video = self._video_library.get_video(video_id)
                    self.playlists[lower].append(video_id)
                    print("Added video to " + playlist_name + ": " + video.title)
            

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

