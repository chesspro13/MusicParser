import youtube_dl 

class Logger(object):
    def debug( self, msg):
        pass
    def warning( self, msg):
        pass
    def error( self, msg):
        print(msg)

songNames = []
songURLs = []
songCount = 0
count = 1
def updateStatus(obj):
    global count
    
#   print( obj )
    if obj['status'] == 'downloading':
        print("Downloading [" str(count) + "/" + str(songCount) "] [" + songNames[count] + "] status: " + obj['_percent_str'])
    if obj['status'] == 'finished':
        print( "Done downloading " + str(count) + "/" + str(songCount) )
        count = count + 1



downloadOptions = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': Logger(),
    'progress_hooks': [updateStatus],
}

ytdl = youtube_dl.YoutubeDL( downloadOptions )

phrase = '<h3 class="style-scope ytd-playlist-video-renderer" aria-label="'

playlist = open('playlist.html', 'r')
source = playlist.read()
playlist.close()

songs = source.split(phrase)
songCount = len(songs)
purgeList = ["(Official Video)", "[Official Video]", "(Official Music Video)", "(OFFICIAL MUSIC VIDEO)", "[OFFICIAL VIDEO]", "[Official Music Video]", "(Video)",
        "(Official HD Video)", "(HD)", "(4K)", "(HQ)", "[4K]", "[HD]", "(Official Lyric Video)", "(OFFICIAL)", "(Official Animated Video)", "(Official Audio",
        "(Lyric Video)", "[OFFICIAL MUSIC VIDEO]", "(lyrics)", "[Official video HD]"]

print( "Songs found:", len( songs ) )
#print( songs[0] )

a = 00

print( len( songs[0].split(phrase) ) )

def scrub( word ):
    for i in purgeList:
        word = word.replace(i," ")
    return word.strip()


def printAll():
    skip = True
    for i in songs:
        if skip:
            skip = False
            continue


        print( scrub(i.split("by")[0]) +"\n\t" + scrub(i.split('href="')[1].split(';')[0] ))
        songNames.append(scrub(i.split("by")[0]))
        songURLs.append(scrub(i.split('href="')[1].split(';')[0] ))
        print()
printAll()

for i in songURLs:
    print( i[:-4] )

for i in range(2):
    if i == 0:
        continue
    print("Downloading: " + songURLs[i][:-4])
    ytdl.download( [songURLs[i][:-4]] )

