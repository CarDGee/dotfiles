#!/bin/bash

setxkbmap gb &

feh --randomize --bg-fill $HOME/Imagens/wallpapers/* &
picom --config $HOME/.config/qtile/scripts/picom.conf & 
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/wired &



# Keep screen on
xset -dpms     # Disable DPMS (Energy Star) features
xset s off     # Disable screensaver
xset s noblank # Don't blank video device
