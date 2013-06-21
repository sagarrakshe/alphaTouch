
## Introduction

Isn't it cool to open calculator by drawing '+' sign on the touch-pad? or Reboot your machine by drawing 'O' and Shutdown by drawing 'X' on touch-pad? `alphaTouch` is a smarter way to execute the applications or programs based on the patterns drawn on the touch-pad. Currently it identifies all alphabets. (You can see in the `applications` file for the patterns it identifies.)


It uses [synclient](https://wiki.archlinux.org/index.php/Touchpad_Synaptics#Synclient) utility to get the information from the touch-pad.

## Installation

Clone the repo:
    
    $ git clone https://github.com/sagarrakshe/alphaTouch.git

Run `install.sh`:
    
    $ ./install.sh

After successful installation of the package, inorder to use `synclient` you will need to Enable `SHMConfig` (Shared Memory) option. 

For `Ubuntu` users, open file:
   
    /usr/share/X11/xorg.conf.d/50-synaptics.conf

For `Debian` users, open file:
   
    /etc/X11/xorg.conf.d/50-synaptics.conf

Add the **SHMConfig** option into the document as shown below:


    Section "InputClass"
    Identifier "enable synaptics SHMConfig"
    MatchIsTouchpad "on"
    MatchDevicePath "/dev/input/event*"
    Option "SHMConfig" "on"
    EndSection

(Here's my  [file](http://paste.ubuntu.com/5747634/) for reference.)

You need to reboot your machine in order to take place the effect. 

## Configuration

To configure your touch-pad for this utility, run `config.py`

    $ python config.py

Follow the instructions and after succesful execution you will get a file - `CONFIGURATION`.
You can configure as many times you need it or you can manually edit the `CONFIGURATION` file provided it's protocol is followed.

##Usage

The program forms a grid on touch-pad as shown below. 
Each intersection is numbered from 1 to 25. A pattern is defined by the order of this numbers.

![touch-pad image](https://raw.github.com/sagarrakshe/alphaTouch/master/_assets/touch-pad.png)

Files:

`CONFIGURATION` - 
    This file contains the co-ordinates of the **four corners** of your touch-pad and the **time-limit** to draw the pattern. 

`mapPattern` - 
    This file contain the records of pattern and the corresponding alphabet. For    example consider this record, `[[[3, 8, 13, 18, 23], [3, 4, 5], [13, 14]], 3, 'F']`.The first arguemnt(list) denotes the pattern, the second one denotes the no. of lines(3) in the pattern and the last one denotes the corresponding alphabet(F).

`applications` - 
    This file contains the list applications corresponding to the particular alphabet
    . For example, `'F':'firefox'` on identifying letter 'F', 'firefox' applications will be opened. Edit this file to your own fit. 

The `time-limit` to draw pattern is by default 8 seconds. You can set it in the `CONFIGURATION` file.

Run `main.py`:

    `$ python main.py`

Let say you want to open **firefox**. Imagine the 5X5 grid on your touch-pad and draw the pattern as follows. After drawing one line lift your hand and then draw the second line. 


## Comments, Suggestion

If you have any suggestions or some problem regarding `alphaTouch` feel free to ping me at `sagarrakshe2@gmail.com`