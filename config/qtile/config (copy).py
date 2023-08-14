import os
import re
import socket
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder


mod = "mod4" #aka Windows key
terminal = "alacritty" #This is an example on how flexible Qtile is, you create variables then use them in a keybind for example (see below)
mod1 = "mod1" #alt key
filemanager = "nemo"

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod1, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "mod1"], "n", lazy.spawn(filemanager), desc="Launch filemanager"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod1], "Space", lazy.spawn("rofi -theme rounded-green-dark -show drun"), desc="Spawn a command using a prompt widget"),

###rofi###
#launcher
    Key([mod, "shift" ], "Return", lazy.spawn("/home/d4n13l/.config/rofi/launchers/type-2/launcher.sh"), desc="Spawn a command using a prompt widget"),

#powermenu
    Key([mod], "F12", lazy.spawn("/home/d4n13l/.config/rofi/powermenu/type-2/powermenu.sh"), desc="Spawn a command using a prompt widget"),

################
##Applications##

##Applications launched with mod + F keys


    Key([mod, "mod1"], "b", lazy.spawn("chromium"), desc="Launch ungoogled chromium browser"),
    Key([mod, "mod1"], "f", lazy.spawn("cachy-browser"), desc="Launch cachyos browser"),


##CUSTOM
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +1%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -1%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc='brightness Down'),
    
##Misc keybinds
    Key([], "Print", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key(["control"], "Print", lazy.spawn("flameshot full -c -p ~/Pictures/"), desc='Screenshot'),
    Key([mod], "e", lazy.spawn(filemanager), desc="Open file manager")

]   

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

group_names = [Group(" ", layout='matrix'),
          Group(" ", layout='monadwide'),
          Group(" ", layout='max'),
          Group(" ", layout='tile'),
          Group(" ", layout='monadwide'),
          Group(" ", layout='floating'),
          Group(" ", layout='floating'),
          Group(" ", layout='tile'),
          Group(" ", layout='tile'),
          Group(" ", layout='floating')]


#groups = [Group(f"{i+1}", label=" ") for i in range(9)] #Be careful modifying this, otherwise qtile config will break
dgroups_key_binder = simple_key_binder("mod4")


###𝙇𝙖𝙮𝙤𝙪𝙩###

layouts = [
    layout.Columns(
        margin = 0,
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E', 
        border_width = 3,
    ),
    
    layout.Max(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 0,
    ),
    
    layout.Floating(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
    # Try more layouts by unleashing below layouts
   #  layout.Stack(num_stacks=2),
   #  layout.Bsp(),
     layout.Matrix(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
     
    layout.MonadWide(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
    layout.Tile(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
   #  layout.TreeTab(),
   #  layout.VerticalTile(),
   #  layout.Zoomy(),
]


widget_defaults = dict(
    font = "sans",
    fontsize = 12,
    padding = 4,
)
extension_defaults = [ widget_defaults.copy()]


def open_launcher():
    qtile.cmd_spawn("rofi -theme rounded-green-dark -show drun")

def open_btop():
    qtile.cmd_spawn("alacritty --hold -e btop")

            
# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄
 
screens = [
    Screen(
        top = bar.Bar(
            [   
                widget.Spacer(
                    length = 18,
                    background = '#272e33',
                ),
                
                widget.Image(
                    filename = '~/.config/qtile/Assets/launch_Icon.png',
                    background = '#272e33',
                    mouse_callbacks = {'Button1': open_launcher},
                ),

                widget.Spacer(
                    length = 18,
                    background = '#272e33',
                ),
                #widget.Image(
                 #   filename = '~/.config/qtile/Assets/6.png',
                #),

                widget.GroupBox(
                    fontsize = 16,
                    borderwidth = 0,
                    highlight_method = 'block',
                    active = '#56D9C7', #Active workspaces circle color
                    block_highlight_text_color = "#00F076", #Current workspace circle color
                    highlight_color = '#4B427E',
                    inactive = '#052A25', #Empty workspace circle
                    foreground = '#046F5F',
                    background = '#272e33',
                    this_current_screen_border = '#00361A', #Circle background color
                    this_screen_border = '#52548D',
                    other_current_screen_border = '#52548D',
                    other_screen_border = '#52548D',
                    urgent_border = '#52548D',
                    rounded = True,
                    disable_drag = True,
                 ),

#                widget.Image(
 #                   filename = '~/.config/qtile/Assets/5.png',
  #              ),

                widget.Spacer(
                    length = 18,
                    background = '#272e33',
                ),

#                widget.Image(
#                    filename = '~/.config/qtile/Assets/2.png',
#                ),

                widget.CurrentLayoutIcon(
                    background = '#1e2326',
                    padding = 0,
                    scale = 0.5,
                ),

                widget.CurrentLayout(
                    background ='#1e2326',
                    font = 'IBM Plex Mono Medium',
                    fontsize = 15,
                    padding = 0,
                ),

#                widget.Image(
#                    filename = '~/.config/qtile/Assets/5.png',                
#                ),

                widget.Spacer(
                    length = 10,
                    background = '#272e33',
                ),

#                widget.Image(
#                    filename = '~/.config/qtile/Assets/2.png',
#                ),

                widget.Spacer(
                    length = 10,
                    background = '#272e33',
                ),

                widget.WindowName(
                    background = '#272e33',
                    format = "{name}",
                    font = 'IBM Plex Mono Medium',
                    fontsize = 14,
                    empty_group_string = 'Desktop',
                    padding = 0,
                ),

                widget.Spacer(
                    length = 10,
                    background = '#272e33',
                ),


#                widget.Image(
#                    filename = '~/.config/qtile/Assets/5.png',                
#                ),  

 #               widget.Image(
 #                   filename = '~/.config/qtile/Assets/1.png',                
 #                   background = '#52548D',
  #              ),

                widget.CPU(
                    font = "IBM Plex Mono Medium",
                    format='CPU:({load_percent:.1f}%/{freq_current}GHz)',
                    fontsize = 15,
                    margin = 0,
                    padding = 0,
                    background = '#1e2326',
                    mouse_callbacks = {'Button1': open_btop},
                ),

                widget.Spacer(
                    length = 10,
                    background = '#272e33',
                ),

#                widget.Image(
#                    filename = '~/.config/qtile/Assets/5.png',
#                ),

#                widget.Image(
#                    filename = '~/.config/qtile/Assets/2.png',                
#                    background = '#52548D',
#                ),  
  
                widget.Systray(
                    background = '#046F5F',
                    icon_size = 24,
                    padding = 3,
                ),

   #             widget.Image(
    #                filename = '~/.config/qtile/Assets/5.png',
     #           ),

      #          widget.Image(
       #             filename = '~/.config/qtile/Assets/2.png',                
        #            background = '#52548D',
         #       ),                    
                                                
                widget.Spacer(
                    length = 0,
                    background = '#046f5f',
                ),  
               
                widget.Memory(
                    format = 'RAM:({MemUsed:.0f}MB/{MemTotal:.0f}MB)',
                    font = "IBM Plex Mono Medium",
                    fontsize = 15,
                    padding = 0,
                    background = '#1e2326',
                    mouse_callbacks = {'Button1': open_btop},
                ),

                widget.Spacer(
                    length = 14,
                    background = '#272e33',
                ),  

                widget.Image(
                    filename = '~/.config/qtile/Assets/Bar-Icons/volume.svg',
                    background = '#1e2326',
                    margin_y = 3,
                    scale = True,
                    mouse_callbacks = {'Button1': open_btop},
                ),

                widget.Spacer(
                    length = 4,
                    background = '#1e2326',
                ), 
                
                widget.PulseVolume(
                    font= 'IBM Plex Mono Medium',
                    fontsize = 15,
                    padding = 0,
                    background = '#1e2326',
                    device = 'default',
                ),

                 widget.Spacer(
                    length = 14,
                    background = '#272e33',
                ),     

                widget.Image(
                    filename = '~/.config/qtile/Assets/Bar-Icons/calendar.svg',
                    background = '#272e33',
                    margin_y = 3,
                    scale = True,
                ),

                widget.Spacer(
                    length = 6,
                    background = '#272e33',
                ), 
        
                widget.Clock(
                    format = '%d/%m/%y ', #Here you can change between USA or another timezone
                    background = '#272e33',
                    font = "IBM Plex Mono Medium",
                    fontsize = 15,
                    padding = 0,
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/Bar-Icons/clock.svg',
                    background = '#272e33',
                    margin_y = 3,
                    margin_x = 5,
                    scale = True,
                ),

                widget.Clock(
                    format = '%H:%M', 
                    background = '#272e33',
                    font = "IBM Plex Mono Medium",
                    fontsize = 15,
                    padding = 0,
                ),

                widget.Spacer(
                    length = 18,
                    background = '#272e33',
                ),
            ],
            30,  # Bar size (all axis)
            margin = [0,8,6,8] # Bar margin (Top,Right,Bottom,Left)
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False #This basically puts your mouse in the center on the screen after you switch to another workspace
floating_layout = layout.Floating(
	border_focus='#00DC6C',
	border_normal='#1F1D2E',
	border_width=3,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

from libqtile import hook
# some other imports
import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh') # path to my script, under my user directory
    subprocess.call([home])

auto_fullscreen = True
focus_on_window_activation = "smart" #or focus
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
