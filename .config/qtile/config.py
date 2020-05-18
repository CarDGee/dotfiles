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
#############################################################################################################
##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
import arcobattery

##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                                    # My terminal of choice
myConfig = "/home/d4n13l/.config/qtile/config.py"    # The Qtile config file location

##### KEYBINDINGS #####
keys = [
         ### The essentials
         Key(
             [mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches Terminal'
             ),
         Key(
             [mod, "shift"], "Return",
             lazy.spawn("dmenu_run -fn 'UbuntuMono Nerd Font:size=10' -nb '#282a36' -nf '#ffffff' -sb '#bd93f9' -sf '#282a36' -p 'dmenu:'"),
             desc='Dmenu Run Launcher'
             ),
         Key(
             [mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key(
             [mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key(
             [mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key(
             [mod, "shift"], "x",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key(
             [mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key(
             [mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key(
             [mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key(
             [mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key(
             [mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key(
             [mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key(
             [mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key(
             [mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key(
             [mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         ### Stack controls
         Key(
             [mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key(
             [mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key(
             [mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),

         ### Applications launched with SUPER + F
         Key(
             [mod], "F1",
             lazy.spawn("spacefm"),
             desc='spacefm file manager'
             ),
         Key(
             [mod], "F2",
             lazy.spawn("firefox-bin"),
             desc='firefox web browser'
             ),
         Key(
             [mod], "F3",
             lazy.spawn("brave-bin"),
             desc='brave web browser'
             ),
         Key(
             [mod], "F4",
             lazy.spawn("thunderbird-bin"),
             desc='mozilla thunderbird email client'
             ),
         Key(
             [mod], "F5",
             lazy.spawn("lxappearance"),
             desc='lxappearance'
             ),
         Key(
             [mod], "F6",
             lazy.spawn("gimp"),
             desc='gimp'
             ),
         Key(
             [mod], "F7",
             lazy.spawn("virt-manager"),
             desc='virt-manager machine emulator'
             ),
         Key(
             [mod], "F8",
             lazy.spawn("/opt/piavpn/bin/pia-client"),
             desc='pia vpn app'
             ),
         Key(
             [mod], "F9",
             lazy.spawn("firefox-bin -no-remote -P Incognito"),
             desc='incognito browser'
             ),
         Key(
             [mod], "F10",
             lazy.spawn("geany"),
             desc='geany editor'
             ),                                                    
         ### Applications launched with SUPER + ALT + KEY
         Key(
             [mod, "mod1"], "a",
             lazy.spawn(myTerm+" -e mpv 'https://radio.streemlion.com:2905/stream'"),
             desc='launches artic outpost radio'
             ),
         Key(
             [mod, "mod1"], "b",
             lazy.spawn("blueman-manager"),
             desc='launches bluetooth manager'
             ),
         Key(
             [mod, "mod1"], "e",
             lazy.spawn("flatpak run org.libretro.RetroArch"),
             desc='launches retroarch'
             ),
         Key(
             [mod, "mod1"], "f",
             lazy.spawn("/opt/brave/brave --profile-directory=Default --app-id=celnaknmndcdcjcagffhbhciignkeokb"),
             desc='facebook webapp'
             ),
         Key(
             [mod, "mod1"], "g",
             lazy.spawn(myTerm+" -e glances"),
             desc='launches glances'
             ),
         Key(
             [mod, "mod1"], "j",
             lazy.spawn(myTerm+" -e joplin"),
             desc='joplin'
             ),
         Key(
             [mod, "mod1"], "l",
             lazy.spawn("flatpak run org.libreoffice.LibreOffice"),
             desc='libreoffice'
             ),
         Key(
             [mod, "mod1"], "n",
             lazy.spawn(myTerm+" -e newsboat"),
             desc='newsboat'
             ),
         Key(
             [mod, "mod1"], "o",
             lazy.spawn("flatpak run com.obsproject.Studio"),
             desc='obs studio'
             ),
         Key(
             [mod, "mod1"], "p",
             lazy.spawn("pulseeffects"),
             desc='launches pulseeffects'
             ),
         Key(
             [mod, "mod1"], "q",
             lazy.spawn('geany -i /home/d4n13l/.config/qtile/config.py'),
             desc='qtile config file'
             ),
         Key(
             [mod, "mod1"], "r",
             lazy.spawn("flatpak run im.riot.Riot"),
             desc='launches riot'
             ),
         Key(
             [mod, "mod1"], "s",
             lazy.spawn("flatpak run com.valvesoftware.Steam"),
             desc='steam'
             ),
         Key(
             [mod, "mod1"], "z",
             lazy.spawn("/opt/brave/brave --profile-directory=Default --app-id=njeegidhkgpheoodgenaapfclailfhlp"),
             desc='zugaina webapp'
             ),
             
         ### Flatpaks launched with SUPER + CONTROL + KEY
         
         Key(
             [mod, "control"], "j",
             lazy.spawn(myTerm+" -e joplin"),
             desc='joplin'
             ),
         
         # INCREASE/DECREASE BRIGHTNESS
		 Key(
			[], "XF86MonBrightnessUp", 
			lazy.spawn("xbacklight -inc 5"),
			desc='decreases brightness'
			),
		 Key(
			[], "XF86MonBrightnessDown", 
			lazy.spawn("xbacklight -dec 5"),
			desc='decreases brightness'
			),
             
         ## INCREASE/DECREASE/MUTE VOLUME
		 Key(
			[], "XF86AudioMute", 
			lazy.spawn("amixer -q set Master toggle"),
			desc='mutes sound'
			),
		 Key(
			[], "XF86AudioLowerVolume", 
			lazy.spawn("amixer -q set Master 5%-"),
			desc='decreases volume'
			),
		 Key(
			[], "XF86AudioRaiseVolume", 
			lazy.spawn("amixer -q set Master 5%+"),
			desc='increases volume'
			),
]

##### GROUPS #####
group_names = [("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'max'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'floating'}),
               ("", {'layout': 'floating'}),
               ("", {'layout': 'max'}),
               ("", {'layout': 'floating'}),
               ("", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

##### THE LAYOUTS #####
layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
     layout.Floating(**layout_theme)
]

##### COLORS #####
colors = [["#282a36", "#282a36"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####

def init_widgets_list():
    widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Ubuntu Bold",
                        fontsize = 9,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[4],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Prompt(
                        prompt=prompt,
                        font="Ubuntu Mono",
                        padding=10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[4],
                        background = colors[0]
                        ),         
               widget.CurrentLayout(
                        font = "Ubuntu Mono",
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[4],
                        background = colors[0]
                        ),                  
              widget.WindowName(
                        foreground = colors[6],
                        background = colors[0],
                        padding = 0
                        ),
              widget.CPUGraph(
                        border_color = colors[0],
                        fill_color = colors[4],
                        graph_color = colors[4],
                        background=colors[0],
                        border_width = 1,
                        line_width = 1,
                        core = "all",
                        type = "box"
                        ),
              widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[0]
                        ),
               widget.TextBox(
                        text="",
                        foreground=colors[4],
                        background=colors[0],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Memory(
                        foreground = colors[2],
                        background = colors[0],
                        padding = 5
                        ),
               arcobattery.BatteryIcon(
                         padding=0,
                         scale=0.7,
                         y_poss=2,
                         theme_path= "/home/d4n13l/.config/qtile/icons/battery_icons_horiz",
                         update_interval = 5,
                         background = colors[0]
                         ),
               widget.TextBox(
                        text=" 🔊",
                        foreground=colors[2],
                        background=colors[0],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Volume(
                        foreground = colors[2],
                        background = colors[0],
                        padding = 5
                        ),
              widget.TextBox(
                        font="Ubuntu Mono",
                        text=" 🕒 ",
                        foreground=colors[3],
                        background=colors[0],
                        padding = 0,
                        fontsize=16
                        ),
              widget.Clock(
                        foreground = colors[2],
                        background = colors[0],
                        fontsize = 12,
                        format="%Y-%m-%d %H:%M"
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[0]
                        ),
               widget.Systray(
                        background=colors[0],
                        padding = 5
                        ),
              ]
    return widgets_list
 
##### SCREENS ##### (TRIPLE MONITOR SETUP)

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
