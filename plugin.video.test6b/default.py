# Import modules - this is from - Python Koding 6: Creating a dir structure
# These import modules are required to run this addon
# had this on week 4 epsicode etc - url = 'http://localhost/some_video.mkv'
# revised on 2017-07-09 - try to use the xbmc.log(text,2) method now etc

import xbmc, xbmcgui, xbmcplugin
import os, urllib, re
import sys, urlparse

# Global variables
# variables assign different values to different items

player  = xbmc.Player()
video1  = "https://archive.org/download/babies_and_breadwinners_2/babies_and_breadwinners_2_512kb.mp4"
video2  = "https://archive.org/download/house_on_haunted_hill_ipod/house_on_haunted_hill_512kb.mp4"
video3  = "https://archive.org/download/night_of_the_living_dead/night_of_the_living_dead_512kb.mp4"
icon1   = "http://jonohunt.design/work/candy-apple-icon.png"
icon2   = "http://icons.iconarchive.com/icons/social-media-icons/glossy-social/512/Android-icon.png"
icon3   = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI4NzczMjA1Nl5BMl5BanBnXkFtZTcwNzk1Mzg0MQ@@._V1_.jpg"


#######################################################################
# initalize plugin directory structure
addon_handle = int(sys.argv[1])
#######################################################################

def addDir(dir_type, mode, url, name, iconimage, fanart):
    base_url  = sys.argv[0]
    base_url += "?url="             +urllib.quote_plus(url)
    base_url += "&mode="            +str(mode)
    base_url += "&name="            +urllib.quote_plus(name)
    base_url += "&iconimage="       +urllib.quote_plus(iconimage)
    base_url += "&fanart="          +urllib.quote_plus(fanart)

    li = xbmcgui.ListItem(name, iconImage=iconimage)

    li.setInfo( type="Video", infoLabels={ "Title": name} )
    li.setProperty( "Fanart_Image", fanart )
    
    if dir_type != '':
        link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=base_url,listitem=li,isFolder=True)
        
    else:
        link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=url,listitem=li,isFolder=False)
    
    return link

def TV_List():
    addDir('', '', video1, 'Example 1', icon1, icon3)
    addDir('', '', video2, 'Example 2', icon2, icon1)

def Movie_List():
    addDir('', '', video1, 'Babies and Breadwinners', icon1, icon3)
    addDir('', '', video2, 'House on Haunted Hill', icon2, icon1)
    addDir('', '', video3, 'Night of the Living Dead', icon3, icon2)

def Trailer_List():
    addDir('', '', video1, 'Babies and Breadwinners (TRAILER)', icon1, icon3)
    addDir('', '', video2, 'House on Haunted Hill (TRAILER)', icon2, icon1)
    addDir('', '', video3, 'Night of the Living Dead (TRAILER)', icon3, icon2)
    addDir('folder', 'tv_list',   "", 'TV',   icon1, icon2)

def Main_Menu():
    addDir('folder', 'movie_list',   "", 'Movies',   icon1, icon2)
    addDir('folder', 'trailer_list', "", 'Trailers', icon2, icon3)

mode = None

args = sys.argv[2]

if len(args) > 0:
    mode = args.split('mode=')
    xbmc.log('####### THE MODE NOW 01 CONTAINS: %s' % mode,2)
    mode = mode[1].split('&')
    xbmc.log('####### THE MODE NOW 02 CONTAINS: %s' % mode,2)
    mode = mode[0]
    xbmc.log('####### THE MODE NOW 03 CONTAINS: %s' % mode,2)


if   mode == None               : Main_Menu()
elif mode == 'movie_list'       : Movie_List()
elif mode == 'trailer_list'     : Trailer_List()
elif mode == 'tv_list'          : TV_List()






#############################################
# close directory structure
xbmcplugin.endOfDirectory(addon_handle)
#############################################

