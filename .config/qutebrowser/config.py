### Load ui settings
config.load_autoconfig()


### Custom bindings
## Change scroll distance
config.bind("j", "scroll-px 0 300")
config.bind("k", "scroll-px 0 -300")

## Tab manager bindings
# Bring up tab manager "groups" command on cmd line with zg
config.bind("zg", "zg: cmd-set-text -s :groups")
# Open index with zz
config.bind("zz", "groups open -f index")
# Open specified session with zR
config.bind("zR", "cmd-set-text -s :groups restore -f")
# Overwrite with specified session with zr
config.bind("zr", "cmd-set-text -s :groups restore -c -f")
# Open specified session index with zo
config.bind("zo", "cmd-set-text -s :groups open -f")
# Save all tabs to specified session with za
config.bind("za", "cmd-set-text -s :groups save-all -o -f")
# Save and close all tabs to specified session with zA
config.bind("zA", "cmd-set-text -s :groups save-all -c -o -f")
# Save current tab to specified session with zs
config.bind("zs", "cmd-set-text -s :groups save -f")
# Remove tab from session with zd
config.bind("zd", "cmd-set-text -s :groups remove -t")
# Remove specified session with zD
config.bind("zD", "cmd-set-text -s :groups delete -f")
# Open help page with zh
config.bind("zh", "groups help")

## Bash readline bindings
# Delete character behind cursor
config.bind("<Ctrl-h>", "fake-key <Backspace>", "insert")
# Delete the previous word
config.bind("<Ctrl-w>", "fake-key <Ctrl-Backspace>", "insert")
# Delete character in front of cursor
config.bind("<Ctrl-d>", "fake-key <Delete>", "insert")
# Delete word in front of cursor
config.bind("<Mod1-d>", "fake-key <Ctrl-Delete>", "insert")
# Move to beginning
config.bind("<Ctrl-a>", "fake-key <Home>", "insert")
# Move to end
config.bind("<Ctrl-e>", "fake-key <End>", "insert")
# Move back one character
config.bind("<Ctrl-b>", "fake-key <Left>", "insert")
# Move back one word
config.bind("<Mod1-b>", "fake-key <Ctrl-Left>", "insert")
# Move forward one character
config.bind("<Ctrl-f>", "fake-key <Right>", "insert")
# Move forward one word
config.bind("<Mod1-f>", "fake-key <Ctrl-Right>", "insert")
# Previous command
config.bind("<Ctrl-p>", "fake-key <Up>", "insert")
# Next command
config.bind("<Ctrl-n>", "fake-key <Down>", "insert")
# Delete everything left of the cursor (not working)
config.bind("<Ctrl-u>", "fake-key <Shift-Home><Delete>", "insert")
# Delete everything right of the cursor (not working)
config.bind("<Ctrl-k>", "fake-key <Shift-End><Delete>", "insert")
# Edit text in text editor
config.bind("<Ctrl-x><Ctrl-e>", "open-editor", "insert")

## Configuration
# Open help page in new tab
config.bind("Sh", "open -t qute://help/configuring.html#configpy")
# Open config.py with SS
config.bind("SS", "config-edit")
# Reload config
config.bind(",r", "config-source")

## Misc
# Open history in new tab
config.bind("sh", "history -t")
# Prompt for help in new tab
config.bind(",h", "cmd-set-text -s :help -t") 
# Open bindings in a new tab
config.bind(",b", "bind")

## Aliases
config.set("aliases", {
    # open tab-manager with required paths using "groups"
    "groups": "spawn -u tab-manager/tab-manager.py /home/landond/.local/share/qutebrowser/userSessions/",
    # close qutebrowser with "q"
    "q": "close",
    # save session with "w"
    "w": "session-save",
    # close and save session with "wq" or "qw"
    "wq": "quit --save",
    "qw": "quit --save"
})


### Settings
## Tabs
# Open tab manager index file at startup
config.set("url.start_pages", "file:///home/landond/.local/share/qutebrowser/userSessions/index.html")
# Open tab manager index file when last tab closed
config.set("tabs.last_close", "startpage")
# New tabs default to blank
config.set("url.default_page", "about:blank")
# Disable switching tabs with scrollwheel
config.set("tabs.mousewheel_switching", False)
# Select Previous tab when current tab closed
config.set("tabs.select_on_remove", "prev")
# Unlimited undo tab closes
config.set("tabs.undo_stack_size", -1)

## Downloads
# Remove download bar after 15 seconds (15000ms)
config.set("downloads.remove_finished", 15000)
# Allow downloading or viewing downloads
config.set("downloads.location.suggestion", "both")

## Content
# Enable brave adblocker
config.set("content.blocking.method", "both")
# Disable autoplay
config.set("content.autoplay", False)
# Accept all cookies
config.set("content.cookies.accept", "all")
# Auto mute tabs
config.set("content.mute", True)
# Enable pdfjs pdf viewer
config.set("content.pdfjs", True)
# Allow local documents to link to external and local urls
config.set("content.local_content_can_access_remote_urls", True)
config.set("content.local_content_can_access_file_urls", True)

## Change editor command to neovim
host_editor_command = "foot $HOME/.local/bin/nvim '+call cursor({line}, {column})' {file}"
config.set("editor.command", ["distrobox-host-exec", "bash", "-c", host_editor_command])

## Appearance
# High DPI mode
config.set("qt.highdpi", True)
# Dark Mode
bg_threshold = 255
text_threshold = 256 - bg_threshold
config.set("colors.webpage.preferred_color_scheme", "light")
config.set("colors.webpage.darkmode.enabled", False)
config.set("colors.webpage.darkmode.threshold.foreground", text_threshold)
config.set("colors.webpage.darkmode.threshold.background", bg_threshold)
config.set("colors.webpage.darkmode.policy.images", "smart")

## Misc
# QT arguments
#config.set("qt.args", "null")
# Use heuristics to navigate with arrow keys
config.set("input.spatial_navigation", True)
# Enable smooth scrolling
config.set("scrolling.smooth", True)
# Save session on close
config.set("auto_save.session", True)
# Disable software rendering
config.set("qt.force_software_rendering", "none")
# Ignore casing when searching
config.set("search.ignore_case", "always")
# Hide window decorations since WM
config.set("window.hide_decoration", True)

### Theme
# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Scheme name: Gruvbox dark, hard
# Scheme author: Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)
# Template author: theova and Daniel Mulford
# Commentary: Tinted Theming: (https://github.com/tinted-theming)

base00 = "#1d2021"
base01 = "#3c3836"
base02 = "#504945"
base03 = "#665c54"
base04 = "#bdae93"
base05 = "#d5c4a1"
base06 = "#ebdbb2"
base07 = "#fbf1c7"
base08 = "#fb4934"
base09 = "#fe8019"
base0A = "#fabd2f"
base0B = "#b8bb26"
base0C = "#8ec07c"
base0D = "#83a598"
base0E = "#d3869b"
base0F = "#d65d0e"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base00

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0D

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base05

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base02

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base02

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base02

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base05

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base09

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = base01

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = base04

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base02

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base05

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base02

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = base05

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base05

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base0C

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base00

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base0A

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base00

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base0E

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base00

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base04

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base01

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base0E

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base01

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base0D

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base00

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base0D

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base00

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base09

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0B

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base00

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0B

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base00

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base00

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base02

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base05

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base02

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base05

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base05

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base02

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base05

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base02

# Background color for webpages if unset (or empty to use the theme's
# color).
#c.colors.webpage.bg = base00
