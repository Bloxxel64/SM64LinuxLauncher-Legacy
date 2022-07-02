# SM64LinuxLauncher
A launcher for super mario 64 pc port. works on linux apt/pacman based distros.
![screenshot](https://cdn.discordapp.com/attachments/886701656488697878/919333674229583923/Zrzut_ekranu_z_2021-12-11_22-02-23.png)

## Linux installation
1.download latest release and unpack it  
2.Double-click setup and click "run in terminal"

## Windows installation
This repo is focused on Linux. yould be better off using SM64Builder2 or SM64NXBuilder, you can also use the original sm64pclauncher, but it's not recommended.

## Usage
### Running on Linux

type in terminal `python3 launcher.py` (you must be in launcher directory)  
or  
doubleclick  on `launcher.py`

### Using it

To build sm64, press "Build"  
To play, select existing build and click "Play"  

## How to build

In the drop down menu, select a repo. and in the box next to it type the branch.  

In the second box, type any name you want for your repo folder. it will display like that in the launcher build selection.  

In the other two boxes you can specify modelpack and texture pack folder. Note: when you browse for the folder, you have to be in this folder to select it.  

Click "Ok". it will freeze for a while this is because it is downloading the repo. 

Click "Browse" and find your Super Mario 64 rom. Click "Ok"  

Specify the build flags, you can find which build flags are avaible for your repo by checking the makefile or checking your repo's wiki if it exists. Remember to add "-j4" for faster building speed.  

Click "Build". Now wait patiently for the build to finish. When it finishes, game should lauch shortly after. If you see a text box and the game does not launch for like 2 minutes, it means that your build failed. delete the repo folder and try to build again. If the game launches, it is ok. When you restart the launcher, it should show the new build on the list.

### Tip
if you want a shortcut to the laucher, on ubuntu, you can do this by making a file called `sm64launcher.desktop` in `$HOME/.local/share/applications/` containing the following:  
`[Desktop Entry]`  
`Name=SM64 launcher`  
`Type=Application`  
`Exec=bash -c "cd path/into/sm64pclauncher ; ./launcher.py"`  
`Icon=/whatever/icon/you/like`  
`Categories=Game;`  
