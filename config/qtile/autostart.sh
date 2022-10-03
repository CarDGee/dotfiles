#!/bin/sh

# systray battery icon
#cbatticon -u 5 &
# systray volume
#volumeicon &

feh --randomize --bg-fill ~/Imagens/wallpapers/* &

#mpv --no-video ~/Música/startsound/panic-stricken-screaming.mp3

mpv --fullscreen --no-input-default-bindings --no-config --on-all-workspaces Videos/welcome/turntable.mp4 &

setxkbmap gb &

numlockx on &

/usr/libexec/polkit-mate-authentication-agent-1 &

##pipewire
#-gentoo-#
/usr/bin/gentoo-pipewire-launcher &
#-artix-#
#/usr/bin/pipewire &
#/usr/bin/pipewire-pulse &
#/usr/bin/wireplumber &

caja &
#nm-applet &

#blueman-applet &

# Keep screen on
xset -dpms     # Disable DPMS (Energy Star) features
xset s off     # Disable screensaver
xset s noblank # Don't blank video device
