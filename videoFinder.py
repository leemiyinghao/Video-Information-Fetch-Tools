from os import listdir
from os.path import isdir

videoSubFilenames = ['.mp4', '.mov', '.avi', '.wmv', '.mpg', '.vob', '.m2t', 'mpeg', 'mkv']

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