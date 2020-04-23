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

def download(video):
    clear()
    videoTitle(video.title)
    try:
        for idx in range(len(video.streams)):
            print(video.streams[idx])
    except Exception as e:
        print(e)
    
    input('algo')

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
    #url = str(input('Input url video from Youtube: '))
    url = 'https://www.youtube.com/watch?v=KFUNJXRXSWE'
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