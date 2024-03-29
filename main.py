from os import system, name
from pytube import YouTube

videoMenuStr = """
[1]Download
[0]Exit
"""

menuStr = """
[1]Search video with url
[0]Exit
"""

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def iterateFormat(video, lenght, position):
    typeFormat = []

    clear()
    videoTitle(video.title)

    for idx in range(lenght):
        data = video.streams[idx].mime_type.split('/')
        typeFormat.append(data[position])
    typeFormat = list(set(typeFormat))
    
    print('Choose a type:')
    
    for idx in typeFormat:
        print(idx)
    typeFormat = input()

    return typeFormat

def mimeType(video, lenght):
    typeDown = iterateFormat(video, lenght, 0)

    if typeDown == 'audio':
        typeDown = True
    else:
        typeDown = False

    return typeDown


def download(video):
    clear()
    videoTitle(video.title)
    lenStreams = len(video.streams)
    try:
        audio = mimeType(video, lenStreams)
        clear()
        videoTitle(video.title)
        print('Downloading...')
        if audio == True:
            video.streams.get_audio_only().download()
        else:    
            video.streams.get_highest_resolution().download()
        input('Done!')
    except Exception as e:
        print(e)
    
    #input('algo')


def videoTitle(title):
    print('-'*100)
    print(title)
    print('-'*100)


def videoMenu(video):
    while True:
        clear()
        videoTitle(video.title)
        command = input(videoMenuStr)
        try:
            command = int(command)
            if command == 1:
                download(video)
            elif command == 0:
                break
            else:
                print('Invalid command')
        except:
            print('Input need to be a number')
            input()


def searchMenu():
    clear()
    url = str(input('Input url video from Youtube: '))
    yt = YouTube(url)
    videoMenu(yt)


def run():
    while True:
        clear()
        print('-'*30)
        print('Youtube Downloader')
        print('-'*30)
        command = input(menuStr)
        try:
            command = int(command)
            if command == 1:
                searchMenu()
            elif command == 0:
                break
            else:
                print('Invalid command')
        except:
            print('Input need to be a number')


if __name__ == "__main__":
    run()
    clear()