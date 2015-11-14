#!/usr/bin/python3.4
import lxml, pprint
from pymediainfo import MediaInfo
from os import listdir
from os.path import isdir

videoSubFilenames = ['.mp4', '.mov', '.avi', '.wmv', '.mpg', '.vob', '.m2t', 'mpeg']

def findVideosRecursively(path):
    returnList = []
    for names in listdir(path):
        if path[-1] != "/":
            path += "/"
        if isdir(names):
            returnList.extend(findVideosRecursively(path + names))
        elif names[-4:] in videoSubFilenames:
            returnList.append(path + names)
    return returnList
for video in findVideosRecursively("."):
    media_info = MediaInfo.parse(video)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            print(video+","+track.other_duration[3])    
