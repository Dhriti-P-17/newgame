## This file contains options that can be changed to customize your game.
## Lines beginning with two '#' marks are comments.

## Basics ######################################################################

## Game name (used in window title and error reports).
define config.name = _("NewGame")

## Show the title on the main menu.
define gui.show_name = True

## Game version.
define config.version = "1.0"

## Default typewriter speed (characters per second).
define config.default_text_cps = 30

## About screen text.
define gui.about = _p("""
""")

## Short name for executables and build directories.
define build.name = "NewGame"

## Sounds and music ############################################################
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

# define config.main_menu_music = "main-menu-theme.ogg"

## Transitions #################################################################
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## Window management ###########################################################
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preference defaults #########################################################

## Default text speed. 0 = instant. Set to 30 for typewriter effect.
default preferences.text_cps = 30

## Default auto-forward delay (0–30).
default preferences.afm_time = 15

## Save directory ##############################################################
define config.save_directory = "NewGame-1758993894"

## Icon ########################################################################
define config.window_icon = "gui/window_icon.png"

## Build configuration #########################################################
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')

# define build.google_play_key = "..."
# define build.itch_project = "renpytom/test-project"
