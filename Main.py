import ctypes
import sys
import os
from pytube import YouTube, Playlist
import colorama
from pytube.contrib import playlist
from pytube.request import stream
from termcolor import colored
from colorama import Fore, Back, Style
from youtubesearchpython import *
import easygui
import time
import string
import pytube
import PyQt5
import requests
from pytube import Playlist
colorama.init()


def logo():
    print(colored('███████╗██╗     ███████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗', 'red'))
    print(colored('██╔════╝██║     ██╔════╝╚██╗██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝', 'red'))
    print(colored('█████╗  ██║     █████╗   ╚███╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗', 'red'))
    print(colored('██╔══╝  ██║     ██╔══╝   ██╔██╗        ██║   ██║   ██║██║   ██║██║     ╚════██║', 'red'))
    print(colored('██║     ███████╗███████╗██ ╔╝██╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║', 'red'))
    print(colored('╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝', 'red'))

ctypes.windll.kernel32.SetConsoleTitleW("YouTube Downloader - Made by Flex#8888")
time.sleep(0.5)
print("\n")

logo()


print(colored('\nselect [1] OR [2]', 'cyan'))
print(colored('\n[1] YOUTUBE LINK', 'magenta'))
print(colored('[2] SEARCH YOUTUBE', 'magenta'))

useanswer = input("\nENTER TYPE : ").upper()


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    liveprogress = (int)(bytes_downloaded / total_size * 100)
    print("Downloading... [%{}]".format(liveprogress), end="\r")


if useanswer == "1":
    print(colored('\nSELECTED [1]', 'cyan'))
    print(colored('\n[S] SINGLE VIDEO', 'magenta'))
    print(colored('[P] PLAYLIST', 'magenta'))
    useanswer = input("\nPLAYLIST OR SINGLE : ").upper()


if useanswer == "S":
    print(colored('\nSELECTED [S]', 'cyan'))
    print(colored('\n[A] Audio', 'magenta'))
    print(colored('[v] VIDEO', 'magenta'))
    useanswer = input("\nENTER TYPE : ").upper()



try:
    if useanswer == "A":
        url = str(input("\nYoutube video url : "))
        youtube = YouTube(url)
        youtube.register_on_progress_callback(on_progress)
        print("\n")
        print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
        print("\n")
        youtube.streams.get_audio_only().download()

except Exception as e:
    print(e)
    input("")


try:
    if useanswer == "V":
        url = str(input("\nYoutube video url : "))
        youtube = YouTube(url)
        youtube.register_on_progress_callback(on_progress)
        print("\n")
        print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
        print("\n")
        youtube.streams.get_highest_resolution().download()

except Exception as e:
    print(e)
    input("")

if useanswer == "P":
    print(colored('\nSELECTED [P]', 'cyan'))
    print(colored('\n[A] Audio', 'magenta'))
    print(colored('[v] VIDEO', 'magenta'))
    useanswer = input("\nENTER TYPE : ").upper()
    if useanswer == "V":
        videoscounter = 0
        p = Playlist(input("\nYoutube Playlist url : "))
        for videocount in p.videos:
            videoscounter += 1
        videoindex = 0
        for video in p.videos:
            video.register_on_progress_callback(on_progress)
            print("\n")
            videoindex += 1
            print(
                colored(
                    "Downloading: [{}/{}] | {} Videos Has Been Started.".format(videoindex, videoscounter, video.title),
                    "red"))
            print("\n")
            video.streams.get_highest_resolution().download()

    if useanswer == "A":

        videoscounter = 0
        p = Playlist(input("\nYoutube Playlist url : "))
        for videocount in p.videos:
            videoscounter += 1
        videoindex = 0
        for video in p.videos:
            video.register_on_progress_callback(on_progress)
            print("\n")
            videoindex += 1
            print(
                colored(
                    "Downloading: [{}/{}] | {} Videos Has Been Started.".format(videoindex, videoscounter, video.title),
                    "red"))
            print("\n")
            video.streams.get_audio_only().download()





if useanswer == "2":
    print(colored('\nSELECTED [2]', 'cyan'))
    print(colored('\n[A] Audio', 'magenta'))
    print(colored('[F] VIDEO', 'magenta'))
    useanswer = input("\nENTER TYPE : ").upper()
    if useanswer == "A":

        search = VideosSearch(input('\nSEARCH YOUTUBE : '))

        print(colored("\n[Use Ctrl+c / Ctrl+v to COPY AND PASTE URL]", 'red'))

        time.sleep(1.5)
        print("\n")
        for video in search.result()['result']:

            print(colored(video['title'], 'green'))
            print(colored(video['link'], 'cyan'))
        else:
            print(colored('\n[Use Ctrl+c / Ctrl+v to COPY AND PASTE URL]', 'red'))
            url = str(input("\nYoutube video url : "))  # have to include in if or it shows up in other downloads
            youtube = YouTube(url)
            youtube.register_on_progress_callback(on_progress)
            print("\n")
            print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
            print("\n")
            youtube.streams.get_audio_only().download()

    if useanswer == "F":

        search = VideosSearch(input('\nSEARCH YOUTUBE : '))

        print(colored("\n[Use Ctrl+c / Ctrl+v to COPY AND PASTE URL]", 'red'))
        time.sleep(1.5)

        for video in search.result()['result']:
            print("\n")
            print(colored(video['title'], 'green'))
            print(colored(video['link'], 'cyan'))
        else:
            print(colored('\n[Use Ctrl+c / Ctrl+v to COPY AND PASTE URL]', 'red'))

            url = str(input("\nYoutube video url : "))  # have to include in if or it shows up in other downloads
            youtube = YouTube(url)
            youtube.register_on_progress_callback(on_progress)
            print("\n")
            print(colored("Downloading : {} Has Started.".format(youtube.title), "red"))
            print("\n")
            youtube.streams.get_highest_resolution().download()




print("\n")
print(colored('DOWNLOAD COMPLETED', 'green'))
print("\n")
input("Press Enter To Exit : ")
