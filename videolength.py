#!/usr/bin/python3.4
import lxml, pprint
from pymediainfo import MediaInfo
from videoFinder import findVideosRecursively

for video in findVideosRecursively("."):
    media_info = MediaInfo.parse(video)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            print(video+","+track.other_duration[3])    
