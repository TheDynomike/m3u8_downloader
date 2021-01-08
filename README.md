## Description

This tool will allow you to download the entire playlist of a given m3u8 file and merge into a single .ts file.

m3u8 files must contain a playlist, you'll know this if the m3u8 file has a response that looks like the example below

### Where to get a m3u8 file?

Example of Twitch:
Go to a Twitch stream profile
Go to the Popular clips section
(In chrome) Open your developer tools (F12 on windows)
Go to the Network tab
filter by "m3u8"
Search through the filtered requests until you find one whose Preview tab shows a list of .ts files
Example of a valid response:
```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:18
#ID3-EQUIV-TDTG:2019-09-22T17:17:40
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-TWITCH-ELAPSED-SECS:0.000
#EXT-X-TWITCH-TOTAL-SECS:18.0
#EXTINF:5.000,
485118384v0-517.ts
#EXT-X-DISCONTINUITY
#EXTINF:12.500,
518.ts
#EXT-X-DISCONTINUITY
#EXTINF:0.500,
485118384v2-519.ts
#EXT-X-ENDLIST
```

## How to

requires python 3.8.x

### run by double clicking the .py file
Download this repo
Right-click dl.py > Properties
General Tab > Change
Select Python 3.8.x
Click Apply
Click OK
Double click dl.py


### run via console

#install virtualenv

`pip install virtualenv`

#create virtualenv

`python -m virtualenv .`

#activate the virtualenv

`.\scripts\activate`

#install reqs

`pip install -r requirements.txt`

#run dl

`python .\dl.py`

#paste your m3u8 file in the url text box and hit download!