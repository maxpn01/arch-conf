from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal



mod = "mod4"
terminal = guess_terminal()
myBrowser = "brave"



keys = [
    # Move focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle Layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Base
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "t", lazy.window.toggle_floating()),

    # Dmenu
    Key([mod], "p", lazy.spawn("dmenu_run -nb '#000000' -nf '#ababab' -sb '#000000' -sf '#D0D0D0' -fn 'JetBrainsMono:bold:pixelsize=17'"), desc="launch dmenu"),

]



groups = [
    Group('1'),
    Group('2'),
    Group('3'),
    Group('4'),
    Group('5'),
    Group('6')
]

for i, grp in enumerate(groups):

    keys.extend([
        # Switch to group
        Key([mod], str(i+1), lazy.group[grp.name].toscreen()),

        # Switch to & move focused window to group
        Key([mod, "shift"], str(i+1), lazy.window.togroup(grp.name,
            switch_group=True)),

])



layouts = [
    layout.Columns(
        border_focus='#151515',
        border_normal='#151515',
        margin=2,
    ),
    layout.Max(),
]



widget_defaults = dict(
    foreground = '#ffffff',
    background = '#000000',
    font = 'JetBrains Mono Bold',
    fontsize = 14,
    padding = 3,
)
extension_defaults = widget_defaults.copy()



screens = [
    Screen(
        bottom = bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                ),
                widget.GroupBox(
                    this_current_screen_border = '#f9f9f9',
                    disable_drag = 'true',
                    highlight_method = "line",
                ),
                widget.Spacer(),
                widget.Systray(),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),
                widget.Clock(
                    padding = 10,
                    format = '%d/%m/%y'
                ),
                widget.Clock(
                    padding = 10,
                    format = '%H:%M'
                ),
                widget.Battery(
                    low_percentage = 0.20,
                    notify_below = 0.20,
                    padding = 10,
                    format='{percent:2.0%}'
                ),
                widget.KeyboardLayout(
                    configured_keyboards = ['us', 'ru'],
                    padding = 10,
                ),
            ],
            25,
        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
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
    ]
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
