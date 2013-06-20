#!/bin/bash

#Install Requirements
echo -e "Installing Touch-pad driver.\n"
sudo apt-get install xserver-xorg-input-synaptics
echo -e "\nInstallation complete."

echo -e "\nReboot required.\nRestart your machine [Y/N]: "
read option
