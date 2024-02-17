#!/usr/bin/env python3

import PySimpleGUI as sg
import os
import subprocess
from themeconfig import *
from urllib.request import urlopen

def main():
    sg.theme_background_color(windowBackgroundColor)
    with open('builds.txt', 'r') as blist:
        builds = blist.readlines()

    url = "https://raw.githubusercontent.com/Bloxxel64/sm64pclauncher/main/repos.txt"
    newstext = urlopen(url).read().decode("utf-8")

    news=[
        [sg.Text('Repos', font=(1), background_color=windowBackgroundColor, text_color=textColor)],
        [sg.Multiline(newstext, disabled=True, size=(36, 16), background_color=boxColor, text_color=boxTextColor)]
        ]
    options=[
        [sg.Button('Play', size=(10, 2), button_color=("white", playButtonColor),font=(1),disabled=True)],
        [sg.Button('Build', size=(14, 1), button_color=('white', otherButtonColor))]
    ]
    buildselect=[[
        sg.Text('Select your sm64pc build:', background_color=windowBackgroundColor, text_color=textColor),

    ],
    [
        sg.Listbox(
            values=builds, enable_events=True,select_mode='single', size=(40, 20), key="buildlist", bind_return_key = True, background_color=boxColor, text_color=boxTextColor
        )
    ]
    ]
    
    layout = [
        [
            sg.Column(buildselect, size=(300, 300)),
            sg.VSeperator(),
            sg.Column(options,size=(140, 300)),
            sg.VSeparator(),
            sg.Column(news, size=(300, 300)),
        ]
    ]
        
    window = sg.Window('SM64LinuxLauncher', layout)
    while True:

        event, values = window.read()
        buildselected = os.path.join(
            values['buildlist'][0] # load the builds
        )

        if event == 'Build':
            import builder
            builder.build()
        if event == 'buildlist':
            buildselected = buildselected.rstrip("\n")
            if buildselected == "":
                window['Play'].update(disabled=True)
            if not buildselected == "":
                window["Play"].update(disabled=False)
        if event == "Play":
            buildfolder, sep, region = buildselected.partition(':')
            if os.name == 'posix':
                subprocess.run(f"cd {buildfolder}/build/{region}_pc/", shell=True)
                subprocess.run(f"/sm64.{region}.f3dex2e")       
        if event == sg.WIN_CLOSED:
            exit()

if __name__ == "__main__":
    try:
        main()
    except IndexError: # make it shut up about an empty build list
        import builder
        builder.build()
        pass

        
