## Introduction

`alphaTouch` is a smarter way to launch the applications based on the patterns drawn on the touch-pad. Currently it identifies all alphabets. (You can see in the `applications` file to the patterns it identifies)


It uses [synclient](https://wiki.archlinux.org/index.php/Touchpad_Synaptics#Synclient) utility to get the information from the touch-pad.

## Installation

Clone the repo:
`git clone https://github.com/sagarrakshe/alphaTouch.git`

Run `install.sh`:
`$ ./install.sh`

Inorder to use `synclient` you will need to Enable `SHMConfig` (Shared Memory) option. 

For `Ubuntu` users, edit file:
`/usr/s^Cre/X11/xorg.conf.d/50-synaptics.conf`

For `Debian` users, edit file:
`/etc/X11/xorg.conf.d/50-synaptics.conf`

Paste this into the document:


    Section "InputClass"
    Identifier "enable synaptics SHMConfig"
    MatchIsTouchpad "on"
    MatchDevicePath "/dev/input/event*"
    Option "SHMConfig" "on"
    EndSection

(Here's my  [file](http://paste.ubuntu.com/5747634/) for reference.)

You need to reboot machine in order to take place the effect. 
