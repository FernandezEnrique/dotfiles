from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from settings.path import qtile_path
from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

mod = "mod4"
terminal = guess_terminal()

#### START CHANGE BETWEEN SCREENS

### END CHANGE BETWEEN SCREENS

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # START MOVING BETWEEN SCREENS

    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
    # END MOVING

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Ventanas

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # Programas
    Key([mod], "n", lazy.spawn("firefox"), desc="Open browser"),

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),
    Key([mod], "e", lazy.spawn("thunar")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in [" "," "," "," "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    'border_focus': "#F07178",
    'border_width': 1,
    'margin': 4
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=17,
    padding=6,
)
extension_defaults = widget_defaults.copy()



screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff","#f1ffff"],
                    background=["#0f101a","#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff","#f1ffff"],
                    inactive=["#f1ffff","#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#F07178","#F07178"],
                    this_current_screen_border=["#a151d3","#a151d3"],
                    this_screen_border=["#353c4a","#353c4a"],
                    other_current_screen_border=["#0f101a","#0f101a"],
                    other_screen_border=["#0f101a","#0f101a"],
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground=["#a151d3","#a151d3"],
                    background=["#0f101a","#0f101a"],
                    fontsize=13,
                    font='UbuntuMono Nerd Font Bold',
                ),
                widget.Systray(),
                widget.Sep(
                    background=["#0f101a","#0f101a"],
                    linewidth=0,
                    padding=5
                ),
                widget.Image(
                    filename=path.join(qtile_path, 'img', 'bar2.png'),
                ),
                widget.TextBox(
                    text=" ",
                    background=["#FFD208","#FFD208"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Net(
                    background=["#FFD208","#FFD208"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Image(
                    filename=path.join(qtile_path, 'img', 'bar3.png'),
                ),
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=["#F07178","#F07178"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.CurrentLayout(
                    background=["#F07178","#F07178"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Sep(
                    background=["#F07178","#F07178"],
                    linewidth=0,
                    padding=5
                ),
                widget.Image(
                    filename=path.join(qtile_path, 'img', 'bar1.png'),
                ),
                widget.TextBox(
                    text=" ",
                    background=['#a151d3',"#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Clock(
                    background=['#a151d3',"#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                    format='%d/%m/%Y - %H:%M:%S',
                ),
            ],
            30,
            opacity=0.95,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff","#f1ffff"],
                    background=["#0f101a","#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff","#f1ffff"],
                    inactive=["#f1ffff","#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#F07178","#F07178"],
                    this_current_screen_border=["#a151d3","#a151d3"],
                    this_screen_border=["#353c4a","#353c4a"],
                    other_current_screen_border=["#0f101a","#0f101a"],
                    other_screen_border=["#0f101a","#0f101a"],
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground=["#a151d3","#a151d3"],
                    background=["#0f101a","#0f101a"],
                    fontsize=13,
                    font='UbuntuMono Nerd Font Bold',
                ),
                widget.Sep(
                    background=["#0f101a","#0f101a"],
                    linewidth=0,
                    padding=5
                ),
                widget.Image(
                    filename=path.join(qtile_path, 'img', 'bar2.png'),
                ),
                widget.TextBox(
                    text=" ",
                    background=["#FFD208","#FFD208"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Net(
                    background=["#FFD208","#FFD208"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Image(
                    filename=path.join(qtile_path, 'img', 'bar3.png'),
                ),
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=["#F07178","#F07178"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.CurrentLayout(
                    background=["#F07178","#F07178"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Sep(
                    background=["#F07178","#F07178"],
                    linewidth=0,
                    padding=5
                ),
                widget.Image(
                    filename=path.join(qtile_path, 'img', 'bar1.png'),
                ),
                widget.TextBox(
                    text=" ",
                    background=['#a151d3',"#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                ),
                widget.Clock(
                    background=['#a151d3',"#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                    format='%d/%m/%Y - %H:%M:%S',
                ),
            ],
            30,
            opacity=0.95,
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
    ], border_focus="#F07178"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
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
