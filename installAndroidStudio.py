#!/usr/bin/python3

## Importing modules
## ------------------

import os
import wget
import tarfile
import subprocess
import sys
import glob
import re

## -------------------


## Global variables
pwd = os.path.dirname(os.path.realpath(__file__))

androidVersion = "4.0.0.16"
url = "https://redirector.gvt1.com/edgedl/android/studio/ide-zips/" + androidVersion + "/android-studio-ide-193.6514223-linux.tar.gz"

installPath = "/usr/bin/"
androidStudio = ''


def downloadAndroidStudio():

    # Check if android studio already is downloaded
    grep = glob.glob('*.gz')
    androidStudio = ''.join(grep)

    # If not, download android studio
    if "android-studio" not in androidStudio:
        try:
            print("Starting to download Android Studio")
            download = wget.download(url, pwd)
            print("\n")

        except Exception as e:
            print(str(e))

    # When downloaded, run this extract function
    extractAndroidStudio()


def extractAndroidStudio():

    grep = glob.glob('*.gz')
    androidStudio = ''.join(grep)
    
    # Extract android studio to where ever the global variable "installPath" is pointing
    try:
        print("Extracting " + androidStudio)
        tar = tarfile.open(androidStudio, 'r:gz')
        tar.extractall(path=installPath)
        tar.close()

    except Exception as e:
        if "[Errno 13]" in str(e):
            print(str(e))
            print("Run this as root..")

    # When done, run and write the desktop entry for android studio
    writeDesktopEntry()

def writeDesktopEntry():

    # Desktop entry tells where to find android studio
    desktopEntry = """[Desktop Entry]
Encoding=UTF-8
Name=Android Studio
Comment=Android Studio - IDE for Android Development
Exec=/bin/sh "/usr/bin/android-studio/bin/studio.sh"
Icon=/usr/bin/android-studio/bin/studio.png
Category=Application;Java;IDE
Type=Application
Terminal=0 """

    # Try to write the desktop entry
    try:

        with open("/usr/share/applications/AndroidStudio.desktop", 'w') as out:
            out.write(desktopEntry + '\n')

    except Exception as fail:
        print(str(fail))

    
    print("All done!")


def main():

    print("Running in: " + pwd)
    downloadAndroidStudio()
    
    

if __name__ == "__main__":
    main()