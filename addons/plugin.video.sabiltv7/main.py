# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urlparse import parse_qsl
import resources.lib.sabiltv7 as sabiltv
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
__url__ = sys.argv[0]
# Get the plugin handle as an integer number.
__handle__ = int(sys.argv[1])

import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","1","sabiltv")


def get_videos(category):
    """
    Get the list of videofiles/streams.
    Here you can insert some parsing code that retrieves
    the list of videostreams in a given category from some site or server.
    :param category: str
    :return: list
    """
    return VIDEOS[category]


def list_menus(menus):
    """
    Create the list of video categories in the Kodi interface.
    :return: None
    """

    # Create a list for our items.
    listing = []
    # Iterate through categories
    for menu in menus:

        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=menu['label'], thumbnailImage=menu['thumb'])
        # Set a fanart image for the list item.
        # Here we use the same image as the thumbnail for simplicity's sake.
        list_item.setProperty('fanart_image', menu['fanart'])
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': menu['label'], 'genre': menu['label']})
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = '{0}?action=listmenu&menu={1}'  .format(__url__, menu['label'])
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))
    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(__handle__)


def list_movies_list(menus):
    """
    Create the list of video categories in the Kodi interface.
    :return: None
    """

    # Create a list for our items.
    listing = []
    # Iterate through categories
    for menu in menus:

        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=menu['label'], thumbnailImage=menu['thumb'])
        # Set a fanart image for the list item.
        # Here we use the same image as the thumbnail for simplicity's sake.
        list_item.setProperty('fanart_image', menu['fanart'])
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': menu['label'], 'genre': menu['kod_nama']})
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = '{0}?action=listing&category={1}&muallim={2}'   .format(__url__, menu['label'], menu['muallim_id'])


        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))
    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(__handle__)



def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    :return: None
    """
    # Get video categories
    categories = get_categories()
    # Create a list for our items.
    listing = []
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category, thumbnailImage=VIDEOS[category][0]['thumb'])
        # Set a fanart image for the list item.
        # Here we use the same image as the thumbnail for simplicity's sake.
        list_item.setProperty('fanart_image', VIDEOS[category][0]['thumb'])
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = '{0}?action=listing&category={1}'.format(__url__, category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))
    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(__handle__)


def list_videos(videos):
    """
    Create the list of playable videos in the Kodi interface.
    :param category: str
    :return: None
    """
    # Get the list of videos in the category.
    # Create a list for our items.
    listing = []
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['label'], thumbnailImage=video['thumb'])
        # Set a fanart image for the list item.
        # Here we use the same image as the thumbnail for simplicity's sake.
        list_item.setProperty('fanart_image', video['thumb'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['label'], 'genre': ''})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
        url = '{0}?action=play&video={1}'.format(__url__, video['video_id'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))
    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(__handle__)


def play_video(video_id):
    """
    Play a video by the provided path.
    :param path: str
    :return: None
    """
    """
      Play a video via ID
      Syntax
      plugin://plugin.video.youtube/play/?video_id=[VID]
      Example
      https://www.youtube.com/watch?v=eWATHgcn2QE or https://youtu.be/eWATHgcn2QE
      plugin://plugin.video.youtube/play/?video_id=eWATHgcn2QE

      Playlists
      Show videos of a playlist
      plugin://plugin.video.youtube/playlist/[PID]/
      Default executing a playlist:
      plugin://plugin.video.youtube/play/?playlist_id=[PID]
      Play a playlist in a predetermined order
      plugin://plugin.video.youtube/play/?playlist_id=[PID]&order=[default|reverse|shuffle]
      Play a playlist with a starting video:
      plugin://plugin.video.youtube/play/?playlist_id=[PID]&video_id=[VID]

      Channels
      Navigate to a channel via ID:
      plugin://plugin.video.youtube/channel/[CID]/
      Navigate to a channel via username:
      plugin://plugin.video.youtube/user/[NAME]/

      Search
      plugin://plugin.video.youtube/search/?q=[URL_ENCODED_TEXT]

    """

    ################################ OK
    #CARA 1 - OK
    #path = "http://localhost/Dr_Zakir_Naik_YouTube.mp4"
#    path = "plugin://plugin.video.youtube/?action=play_video&videoid=oHg5SJYRHA0"
    #TGNA
    path = "plugin://plugin.video.youtube/?action=play_video&videoid=" + video_id
    #Listing
    #path = "plugin://plugin.video.youtube/playlist/PL_-neza6Rji6-LbT4pE5CPnuJvWl7ioEc/"
    #path = "plugin://plugin.video.youtube/play/?playlist_id=PL_-neza6Rji6-LbT4pE5CPnuJvWl7ioEc"
    print(path)
    
    #plugin://plugin.video.youtube/?action=play_video&videoid=oHg5SJYRHA0
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(__handle__, True, listitem=play_item)
    ################################ OK




     # Ini untuk PHP
     # CARA 1
     #xbmc.executebuiltin( 'Container.Update(plugin://plugin.video.discovery_com/?channelID=Discovery&channelThumb=%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.discovery_com%2fre​​sources%2fthumbs%2fdiscovery_channel.png&mode=listShows&type&url=http%3a%2f%2fdsc.discovery.com%2fvideos)' ) 
     # CARA 2
     #li = xbmcgui.ListItem('Folder of a different plugin')
     #url = 'plugin://plugin.video.discovery_com/?channelID=Discovery&channelThumb=%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.discovery_com%2fre​sources%2fthumbs%2fdiscovery_channel.png&mode=listShows&type&url=http%3a%2f%2fdsc.discovery.com%2fvideos'
     #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=true) 
     # CARA 3
     #xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/?action=play_video&videoid=<VIDEO-ID>)')

#      playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=JTZtWGmWXkk'
#      listItem = xbmcgui.ListItem(path=str(playback_url))
#      xbmcplugin.setResolvedUrl(__handle__, True, listItem)




def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring
    :param paramstring:
    :return:
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring[1:]))
    pgno = 1
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.


            videos = sabiltv.get_videos(pgno,params['category'],params['muallim'])
            list_videos(videos)
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        elif params['action'] == 'listmenu':
          if params['menu'] == 'Guru':
            gurus = sabiltv.get_muallims(pgno)
            #list_menus(gurus)
            list_movies_list(gurus)
          else:
            list_submenu(params['menu'])


    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        # list_categories()

        # Get video categories
        menus = sabiltv.get_menus(pgno)
        list_menus(menus)


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    router(sys.argv[2])
