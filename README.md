# SM64LinuxLauncher-Legacy
A launcher for the Super Mario 64 PC Port. Based off of sm64pclauncher.

# NOTICE!
As of 4/18/24, this repo is reaching it's end-of life. The codebase for the launcher has gotten too out of hand, and tk/tkinter + PySimpleGUI, the window and GUI libraries, are just not very great. I will hopefully be starting work on a full remake coded in Python or C++ using qt instead of tkinter and PySGUI. In the meantime, i will try to resolve any misc issues that have arisen. Please understand, Hai.

![screenshot](https://cdn.discordapp.com/attachments/775908791417700363/996196405708329030/Screenshot_from_2022-07-11_18-28-18.png?size=4096)

also the script will mostly not work due to "externally-managed-environment" error, this can be fixed by either installing the native packages of the libraries used, or by using virtual environment (require some extra work)

## GNU/Linux installation
### Using the Install Script
1. Install git if you have not already:
 * `sudo apt-get install git` on Debian/Ubuntu based systems,
 * `sudo pacman -S git` on arch based systems, or

2. Clone the repo using this command:
`git clone https://github.com/Bloxxel64/SM64LinuxLauncher`.

3. Run this command to ensure the file can be executed: `chmod +x setup.py`.

4. Run the setup.sh file by double-clicking it or running `python3 setup.py` in your terminal. Enter your password, and the script will install depedencies for both SM64LL and SM64 PC Port, and finall place the SM64LinuxLauncher directory in your `home/username` folder.

5. Open the directory in the terminal or file explorer, if you open it in terminal run `python3 launcher.py`. If you run it from your file explorer, just double-click it.

### Manually Installing Dependencies
If you should encounter errors while using the application, there may be an uninstalled dependency. Use the following commands to install all depends:

Debian-Based Distros:  
`sudo apt install python3 python3-pip python3-tk libsdl2-dev gcc-mips-linux-gnu make`  
`pip3 install pysimplegui`  
`pip3 install tk`  

Arch-Based Distros/SteamOS:

TBW, i know nothing about arch nor steamos 😿.

## Supported Distros

* `apt` Based Distros (Ubuntu, Debian, Mint, etc.)
* `pacman` Based Distros (EndeavourOS, Arch, Artix, Arco, Manjaro, etc.)

## Windows installation
This repo is focused on Linux. yould be better off using SM64Builder2 or SM64NXBuilder, you can also use the original sm64pclauncher, but it's not recommended.

## Usage
### Running on Linux

Type `python3 launcher.py` into your terminal (you must be in the root launcher directory), or doubleclick `launcher.py`.

### Using it

To build a new instance of sm64pc, press "Build".
To play an existing build, select a build from the buildlist and click "Play".

## How to build

* In the drop down menu, select a repo. and in the box next to it type the branch.  
* In the second box, type any name you want for your repo folder. it will display like that in the launcher build selection.  
* In the other two boxes you can specify modelpack and texture pack folder. Note: when you browse for the folder, you have to be in this folder to select it.  
* Click "Ok". it will freeze for a while this is because it is downloading the repo. 
* Click "Browse" and find your Super Mario 64 rom. Click "Ok"  
* Specify the build flags, you can find which build flags are avaible for your repo by checking the makefile or checking your repo's wiki if it exists. Optionally, you can add a `-j` argument to set how many simoultaneous build jobs can be done at one time. The guideline is one job for one core and 2GB of ram. Example: `-j4` for a quad-core processor with 8GB of RAM.
* Click "Build". Now wait patiently for the build to finish. When it finishes, game should lauch shortly after. If you see a text box and the game does not launch for like 2 minutes, it means that your build failed. delete the repo folder and try to build again. If the game launches, it is ok. When you restart the launcher, it should show the new build on the list.

### Launcher Shortcut
If you want a shortcut to the laucher, you can do this by making a file called `sm64launcher.desktop` in `/home/username/.local/share/applications/` containing the following:  

```
[Desktop Entry]
Name=SM64LinuxLauncher  
Type=Application
Exec=path/into/sm64linuxlauncher/launcher.py
Categories=Game;  
```
