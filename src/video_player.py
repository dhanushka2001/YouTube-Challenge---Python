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
        self.playlists = {}

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

    def playlist_exist(self,playlist_name):
        #return OG playlist name if it does exist (not case-sensitive)
        #else return None
        playlistexist = False
        lower = playlist_name.lower()
        for key in self.playlists.keys():
            if key.lower() == lower:
                return key
                playlistexist = True
        if playlistexist == False:
            return None
        
        

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
        #list all videos in alphabetical order    
        x = sorted(videoslist, key=itemgetter(0))
        for i in x:
            print(i[0] + " (" + i[1] + ") [" + ' '.join(i[2]) +"]")

    def list_all_videos(self):
        """Returns LIST of all videos."""        
        videos = self._video_library.get_all_videos()
        videoslist = []
        for i in videos:
            videoslist.append([i.title,i.video_id,i.tags])
        #list all videos in alphabetical order    
        x = sorted(videoslist, key=itemgetter(0))
        return x

        
        
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
        if self.playlist_exist(playlist_name) == None:
            #cant put self.playlists = {} here, that would mean it would reset the list of playlists when u made a new playlist
            #still however want the playlists dict to reset for each different video player object, so put it in __init__ func
            self.playlists[playlist_name] = []
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
        key = self.playlist_exist(playlist_name)
        if key == None:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")
        else:
            if self.video_exist(video_id) == False:
                print("Cannot add video to " + playlist_name + ": Video does not exist")
            else:
                if video_id in self.playlists[key]:
                    print("Cannot add video to " + playlist_name + ": Video already added")
                else:
                    video = self._video_library.get_video(video_id)
                    self.playlists[key].append(video_id)
                    print("Added video to " + playlist_name + ": " + video.title)
            

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            #list playlists in alphabetical order
            for key in sorted(list(self.playlists.keys())):
                print(key)
        

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        key = self.playlist_exist(playlist_name)
        if key == None:
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")
        else:
            print("Showing playlist: " + playlist_name)
            #list videos same order they were added
            videosidlist = self.playlists[key]
            if len(videosidlist) == 0:
                print("No videos here yet")
            else:
                for videoid in videosidlist:
                    video = self._video_library.get_video(videoid)
                    print("Currently playing: " + video.title + " (" + video.video_id + ") [" + ' '.join(video.tags) + "]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        key = self.playlist_exist(playlist_name)
        if key == None:
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")
        else:
            if self.video_exist(video_id) == False:
                print("Cannot remove video from " + playlist_name + ": Video does not exist")
            else:
                if video_id not in self.playlists[key]:
                    print("Cannot remove video from " + playlist_name + ": Video is not in playlist")
                else:
                    self.playlists[key].remove(video_id)
                    video = self._video_library.get_video(video_id)
                    print("Removed video from " + playlist_name + ": " + video.title)
                    

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        key = self.playlist_exist(playlist_name)
        if key == None:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")
        else:
            #could check to see if already empty but assignment doesnt require it
            key = self.playlist_exist(playlist_name)
            self.playlists[key].clear()
            print("Successfully removed all videos from " + playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        key = self.playlist_exist(playlist_name)
        if key == None:
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")
        else:
            #should add a function to ask ARE YOU SURE?
            del self.playlists[key]
            print("Deleted playlist: " + playlist_name)


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        #list_all_videos() is list of lists where each list is
        #video broken into its components [title,url,tags]
        #videos in list are in alphabetical order
        videos = self.list_all_videos()
        search = []
        n = 1
        for i in videos:
            if search_term.lower() in i[0].lower():
                search.append(i)
                n+=1
        if n == 1:
            print("No search results for " + search_term)
        else:
            print("Here are the results for " + search_term + ":")
            for i in search:
                print(str(search.index(i)+1) + ") " + i[0] + " (" + i[1] + ") [" + ' '.join(i[2]) +"]")     
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            x = input()
            #pytest wont allow me to do x = input("If your...") -_-
            if x.isdigit() == False:
                pass
            elif not 0 < int(x) < n:
                pass
            else:
                print("Playing video: " + search[int(x)-1][0])
                    

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self.list_all_videos()
        search = []
        n = 1
        for i in videos:
            for j in i[2]:
                if video_tag.lower() in j.lower():
                    search.append(i)
                    n+=1
                    break
                    #need to add break otherwise if a video had the search
                    #tag twice it would put video in search list twice!
                
        if n ==1:
            print("No search results for " + video_tag)
        else:
            print("Here are the results for " + video_tag + ":")
            for i in search:
                print(str(search.index(i)+1) + ") " + i[0] + " (" + i[1] + ") [" + ' '.join(i[2]) +"]")     
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            x = input()
            if x.isdigit() == False:
                pass
            elif not 0 < int(x) < n:
                pass
            else:
                print("Playing video: " + search[int(x)-1][0])
            

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

