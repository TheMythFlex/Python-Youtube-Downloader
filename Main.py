import ctypes
import sys
import os

import keyboard
from pystyle import Colorate, Colors, Center, Write
from pytube import YouTube, Playlist
import colorama
from pytube.contrib import playlist
from pytube.request import stream
from termcolor import colored
from colorama import Fore, Back, Style
from youtubesearchpython import *
import time
import string
import pytube
import requests
import msvcrt as m
from pytube import Playlist

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

hide_cursor()

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    liveprogress = (int)(bytes_downloaded / total_size * 100)
    print("Downloading... [%{}]".format(liveprogress), end="\r")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def logo():
    text = (Colorate.Vertical(Colors.red_to_black, """



                              ██╗░░░██╗░█████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗
                              ╚██╗░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
                              ░╚████╔╝░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██████╦╝█████╗░░
                              ░░╚██╔╝░░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
                              ░░░██║░░░╚█████╔╝╚██████╔╝░░░██║░░░╚██████╔╝██████╦╝███████╗
                              ░░░╚═╝░░░░╚════╝░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝
                                   
          
            """, 1))
    print(Center.XCenter(text))

os.system("title YouTube Downloader - Made by Flex#8629")

def main():
    global youtube
    try:
        logo()

        print(Center.XCenter("""[1] Youtube Link | [2] Search Youtube

        """))

        useranswer = m.getch()
        useranswer = str(useranswer).replace("'", "")
        useranswer = str(useranswer).replace("b", "")

        if useranswer == "1":
            os.system("title YouTube Downloader - Youtube Link")
            clearConsole()
            logo()
            print(Center.XCenter("""[1] Single | [2] Playlist

            """))
            useranswer = m.getch()
            useranswer = str(useranswer).replace("'", "")
            useranswer = str(useranswer).replace("b", "")
            if useranswer == "1":
                os.system("title YouTube Downloader - Youtube Link/Single")
                clearConsole()
                logo()
                print(Center.XCenter("""[1] Audio | [2] Video

                """))
                useranswer = m.getch()
                useranswer = str(useranswer).replace("'", "")
                useranswer = str(useranswer).replace("b", "")
                if useranswer == "1":
                    os.system("title YouTube Downloader - Youtube Link/Single/Audio")
                    clearConsole()
                    logo()
                    url = str(input("\nYoutube video url: "))
                    clearConsole()
                    logo()
                    youtube = YouTube(url)
                    print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
                    youtube.streams.get_audio_only().download()
                    clearConsole()
                    logo()
                    print(colored("Download Finished.".format(youtube.title), "green"))
                    input("")
                else:
                    pass
                if useranswer == "2":
                    os.system("title YouTube Downloader - Youtube Link/Single/Video")
                    clearConsole()
                    logo()
                    url = str(input("\nYoutube video url: "))
                    clearConsole()
                    logo()
                    youtube = YouTube(url)
                    youtube.register_on_progress_callback(on_progress)
                    print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
                    youtube.streams.get_highest_resolution().download()
                    print(colored("Download Finished.".format(youtube.title), "green"))
                    input("")
            else:
                pass
            if useranswer == "2":
                os.system("title YouTube Downloader - Youtube Link/Playlist")
                clearConsole()
                logo()
                print(Center.XCenter("""[1] Audio | [2] Video

                        """))
                useranswer = m.getch()
                useranswer = str(useranswer).replace("'", "")
                useranswer = str(useranswer).replace("b", "")
                if useranswer == "1":
                    os.system("title YouTube Downloader - Youtube Link/Playlist/Audio")
                    clearConsole()
                    logo()
                    videoscounter = 0
                    p = Playlist(input("\nYoutube Playlist url: "))
                    clearConsole()
                    logo()
                    for videocount in p.videos:
                        videoscounter += 1
                    videoindex = 0
                    for video in p.videos:
                        video.register_on_progress_callback(on_progress)
                        videoindex += 1
                        print(
                            colored(
                                "Downloading: [{}/{}] | {} Videos Has Been Started.".format(videoindex, videoscounter,
                                                                                            video.title),
                                "red"))
                        video.streams.get_audio_only().download()
                    print(colored("Download Finished.".format(youtube.title), "green"))
                    input("")
                else:
                    pass
                if useranswer == "2":
                    os.system("title YouTube Downloader - Youtube Link/Playlist/Video")
                    clearConsole()
                    logo()
                    videoscounter = 0
                    p = Playlist(input("\nYoutube Playlist url : "))
                    clearConsole()
                    logo()
                    for videocount in p.videos:
                        videoscounter += 1
                    videoindex = 0
                    for video in p.videos:
                        video.register_on_progress_callback(on_progress)
                        videoindex += 1
                        print(
                            colored(
                                "Downloading: [{}/{}] | {} Videos Has Been Started.".format(videoindex, videoscounter,
                                                                                            video.title),
                                "red"))
                        video.streams.get_highest_resolution().download()
                    print(colored("Download Finished.".format(youtube.title), "green"))
                    input("")

        if useranswer == "2":
            os.system("title YouTube Downloader - Search Youtube")
            clearConsole()
            logo()
            print(Center.XCenter("""[1] Audio | [2] Video

                            """))
            useranswer = m.getch()
            useranswer = str(useranswer).replace("'", "")
            useranswer = str(useranswer).replace("b", "")
            if useranswer == "1":
                os.system("title YouTube Downloader - Search Youtube/Audio")
                clearConsole()
                logo()
                search = VideosSearch(input('\nSearch Youtube: '))
                clearConsole()
                logo()
                print(colored("\n[Use Ctrl+C / Ctrl+V, TO COPY AND PASTE URL]", 'red'))
                print("\n")
                link = 0
                for video in search.result()['result']:
                    link += 1
                    print(colored(video['title'], 'green'))
                    print(colored(video['link'], 'blue'))
                    print("-----------------------------------------------")
                    if link == 3:
                        break
                url = str(input("\nEnter video url : "))
                clearConsole()
                logo()
                print("\n")
                youtube = YouTube(url)
                print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
                youtube.streams.get_audio_only().download()
                clearConsole()
                logo()
                print("\n")
                print(colored("Download Finished.".format(youtube.title), "green"))
                input("")
            else:
                pass
            if useranswer == "2":
                os.system("title YouTube Downloader - Search Youtube/Video")
                clearConsole()
                logo()
                search = VideosSearch(input('\nSearch Youtube: '))
                clearConsole()
                logo()
                print(colored("\n[Use Ctrl+C / Ctrl+V, TO COPY AND PASTE URL]", 'red'))
                print("\n")
                link = 0
                for video in search.result()['result']:
                    link += 1
                    print(colored(video['title'], 'green'))
                    print(colored(video['link'], 'blue'))
                    print("-----------------------------------------------")
                    if link == 3:
                        break
                url = str(input("\nEnter video url : "))
                clearConsole()
                logo()
                print("\n")
                youtube = YouTube(url)
                print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
                youtube.streams.get_highest_resolution().download()
                clearConsole()
                logo()
                print("\n")
                print(colored("Download Finished.".format(youtube.title), "green"))
                input("")

        input("")
    except:
        print(Fore.RED + "[+] Error, Try again")

main()
