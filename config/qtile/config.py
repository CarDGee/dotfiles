#
#
# ██████╗ █████╗ ██████╗ ██████╗  ██████╗ ███████╗███████╗                               
#██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝██╔════╝                               
#██║     ███████║██████╔╝██║  ██║██║  ███╗█████╗  █████╗                                 
#██║     ██╔══██║██╔══██╗██║  ██║██║   ██║██╔══╝  ██╔══╝                                 
#╚██████╗██║  ██║██║  ██║██████╔╝╚██████╔╝███████╗███████╗                               
# ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝                               
#                                                                                        
# ██████╗ ████████╗██╗██╗     ███████╗     ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ 
#██╔═══██╗╚══██╔══╝██║██║     ██╔════╝    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ 
#██║   ██║   ██║   ██║██║     █████╗      ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
#██║▄▄ ██║   ██║   ██║██║     ██╔══╝      ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
#╚██████╔╝   ██║   ██║███████╗███████╗    ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
# ╚══▀▀═╝    ╚═╝   ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ 

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401
import arcobattery
from colorscheme import everforest

mod = "mod4"
myTerm = "alacritty"

#---------------#
#   KEYBINDINGS #
#---------------#

keys = [

    #---    Switch between windows  ---#
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "p", lazy.layout.next()),

    #---    Move windows    ---#
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    #---    Resize windows  ---#
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    #---    Get windows original size   ---#
    Key([mod], "n", lazy.layout.normalize()),

    #---    Toggle floating ---#
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    #---    Toggle fullscreen   ---#
    Key([mod], "f", lazy.window.toggle_fullscreen()),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),

    #---    Terminal    ---#
    Key([mod], "Return", lazy.spawn("alacritty")),

    #---    Launcher    ---#
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -fn 'UbuntuMono Nerd Font:size=16' -nb '#2d2a2e' -nf '#ffffff' -sb '#0A8A8A' -sf '#2d2a2e' -p 'dmenu:'")),

    #---    Toogle layout   ---#
    Key([mod], "Tab", lazy.next_layout()),

    #---    Kill window     ---#
    Key([mod], "q", lazy.window.kill()),

    #---    Reload Qtile    ---#
    Key([mod, "control"], "r", lazy.reload_config()),

    #---    Exit Qtile      ---#
    Key([mod, "control"], "e", lazy.shutdown()),

### Applications launched with SUPER + F ###

	Key([mod], "F1", lazy.spawn("/home/d4n13l/.local/share/dmenu-scripts/explorer")),

	Key([mod], "F2", lazy.spawn("/home/d4n13l/.local/share/dmenu-scripts/browseBox")),

	Key([mod], "F3", lazy.spawn("/home/d4n13l/.local/share/dmenu-scripts/bugzilla")),

	Key([mod], "F4", lazy.spawn("/home/d4n13l/.local/share/dmenu-scripts/torlook")),

	Key([mod], "F5", lazy.spawn("lxappearance")),

	Key([mod], "F6", lazy.spawn("pactl set-sink-volume 0 125%")),

	Key([mod], "F7", lazy.spawn("virt-manager")),

	Key([mod], "F8", lazy.spawn("/opt/piavpn/bin/pia-client")),

	Key([mod], "F9", lazy.spawn("scrot 'desktop-%Y%m%d%H%M.png' -e 'mv $f ~/Imagens/screenshots'")),

	Key([mod], "F10", lazy.spawn("librewolf-bin -no-remote -P 3v1l6006l3")),

	Key([mod], "F11", lazy.spawn("librewolf-bin -no-remote -P Incognito")),

	Key([mod], "F12", lazy.spawn("/home/d4n13l/.local/share/dmenu-scripts/dmpower")),

# SUPER + Alt KEYS

	Key([mod, "mod1"], "b", lazy.spawn("chromium-bin")),

	Key([mod, "mod1"], "c", lazy.spawn("caja")),

    Key([mod, "mod1"], "d", lazy.spawn("deluge")),

    Key([mod, "mod1"], "e", lazy.spawn("evolution")),

    Key([mod, "mod1"], "f", lazy.spawn("librewolf-bin")),

    Key([mod, "mod1"], "g", lazy.spawn("gimp")),

	Key([mod, "mod1"], "h", lazy.spawn(myTerm+" -e htop")),

	Key([mod, "mod1"], "k", lazy.spawn("pluma /home/d4n13l/.config/qtile/config.py")),

	Key([mod, "mod1"], "l", lazy.spawn("lutris")),

    Key([mod, "mod1"], "m", lazy.spawn("nuclear")),

    Key([mod, "mod1"], "n", lazy.spawn("flatpak run org.nicotine_plus.Nicotine")),

	Key([mod, "mod1"], "p", lazy.spawn("pavucontrol")),

	Key([mod, "mod1"], "r", lazy.spawn(myTerm+" -e mpv 'https://radio.streemlion.com:3715/stream'")),

	Key([mod, "mod1"], "s", lazy.spawn("steam")),

	Key([mod, "mod1"], "t", lazy.spawn("thunderbird-bin")),

	Key([mod, "mod1"], "v", lazy.spawn(myTerm+" -e vim")),


# SUPER + CTRL KEYS

	Key([mod, "control"], "a", lazy.spawn("flatpak run app.authpass.AuthPass")),
	
    Key([mod, "control"], "f", lazy.spawn("flatpak run org.freac.freac")),

	Key([mod, "control"], "n", lazy.spawn("flatpak run org.js.nuclear.Nuclear")),

	Key([mod, "control"], "o", lazy.spawn("flatpak run com.obsproject.Studio")),

	Key([mod, "control"], "s", lazy.spawn("flatpak run com.github.tchx84.Flatseal")),

	Key([mod, "control"], "t", lazy.spawn(myTerm+" -e tail -f /var/log/emerge-fetch.log")),

##########
#-volume-#
##########

Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
		 
Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),

Key([mod], "Up", lazy.spawn("pactl set-source-volume 0 +10%")),

Key([mod], "Down", lazy.spawn("pactl set-source-volume 0 -10%")),

]

group_names = [("  ", {'layout': 'bsp'}),
               ("  ", {'layout': 'monadtall'}),
               ("  ", {'layout': 'max'}),
               ("  ", {'layout': 'monadtall'}),
               ("  ", {'layout': 'floating'}),
               ("  ", {'layout': 'floating'}),
               ("  ", {'layout': 'max'}),
               ("  ", {'layout': 'floating'}),
               ("  ", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

#---------#
#-Layouts-#
#---------#

layout_conf = {
    'border_focus': everforest['text'],
    'border_width': 1,
    'margin': 3
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
    layout.Bsp(**layout_conf),
    layout.MonadWide(border_focus=everforest['text'],
                     border_normal=everforest['active'], border_width=1, margin=4),
    layout.RatioTile(border_focus=everforest['text'],
                     border_normal=everforest['active'], border_width=1, margin=4),
    layout.Floating(border_focus=everforest['text']),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=18,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.Image(
                    filename = "",
                    scale = "False"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    active=everforest['fg'],
                    inactive=everforest['color1'],
                    rounded=False,
                    highlight_color=everforest['text'],
                    highlight_method="line",
                    borderwidth=0
                ),

               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground=everforest['text']
                        ),
               widget.CurrentLayout(
                        foreground=everforest['light']
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground=everforest['text']
                        ),

                widget.WindowName(
                    fontsize=14,
                    foreground=everforest['text']
                ),



                widget.Systray(),

                widget.TextBox(
                    text='/',
                    foreground=everforest['color1'],
                    padding=-3,
                    fontsize=40
                ),
                widget.TextBox(
                    text=' ',
                    background=everforest['dark'],
                    foreground=everforest['color1'],
                    padding=3
                ),
                widget.Volume(
                    background=everforest['dark'],
                    foreground=everforest['color1'],
                ),
                widget.TextBox(
                    text='/',
                    background=everforest['dark'],
                    foreground=everforest['color2'],
                    padding=-3,
                    fontsize=40
                ),
                widget.Memory(
                    format="溜{MemUsed: .0f}Mb/{MemTotal: .0f}Mb",
                    background=everforest['dark'],
                    foreground=everforest['color2'],
                    interval=1.0
                ),
                widget.TextBox(
                    text='/',
                    background=everforest['dark'],
                    foreground=everforest['color3'],
                    padding=-3,
                    fontsize=40
                ),
                widget.TextBox(
                    text='',
                    background=everforest['dark'],
                    foreground=everforest['color3'],
                    padding=7
                ),
                widget.CPUGraph(
                    background=everforest['dark'],
                    graph_color=everforest['color3'],
					border_color=everforest['color3'],
                    border_width = 1,
                    line_width = 1,
                    core = "all",
                    type = "box"
                ),

                widget.TextBox(
                    text='/',
                    background=everforest['dark'],
                    foreground=everforest['color4'],
                    padding=-3,
                    fontsize=40
                ),
                widget.ThermalZone(
                    format=" {temp}°C",
                    fgcolor_normal=everforest['color4'],
                    background=everforest['dark'],
                    zone="/sys/class/thermal/thermal_zone0/temp"
                ),

                widget.TextBox(
                    text='/',
                    background=everforest['dark'],
                    foreground=everforest['color5'],
                    padding=-3,
                    fontsize=40
                ),
               arcobattery.BatteryIcon(
					padding=0,
					scale=0.7,
					y_poss=2,
					theme_path= "/home/d4n13l/.config/qtile/icons/battery_icons_horiz",
					update_interval = 5,
					background=everforest['dark'],
				),

                widget.TextBox(
                    text='/',
                    background=everforest['dark'],
                    foreground=everforest['color6'],
                    padding=-3,
                    fontsize=40
                ),
                widget.TextBox(
                    text='',
                    background=everforest['dark'],
                    foreground=everforest['color6'],
                    padding=7
                ),
                widget.Clock(
                    background=everforest['dark'],
                    foreground=everforest['color6'],
                    format="%d/%m/%Y @ %H:%M",
                    update_interval=60.0
                ),



            ],
            22,
            background=everforest['dark'],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus="#9ccfd8",
    border_normal="#31748f"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

#---------------#
#   AUTOSTART   #
#---------------#


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

