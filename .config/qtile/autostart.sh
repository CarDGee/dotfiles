#!/bin/bash

#feh --randomize --bg-fill ~/Pictures/wallpapers/* &

setxkbmap gb &

numlockx on &

#picom -b --config /home/d4n13l/.config/qtile/picom.conf &

#/usr/libexec/polkit-gnome-authentication-agent-1 &

#nm-applet &

#blueman-applet &

# Keep screen on
xset -dpms     # Disable DPMS (Energy Star) features
xset s off     # Disable screensaver
xset s noblank # Don't blank video device
