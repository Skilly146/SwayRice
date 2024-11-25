# SwayRice

My sway config, including dotfiles and application configs.

- .config: If an entry in the repo isn't listed here then it is new and I haven't documented it yet
  
  - autostart: autostart apps
  
  - Thunar: Not really sure what the files in this one are
  - xfce4: Not sure but related to thunar
  
  - distrobox: config file for distrobox
  
  - gtk-3.0: Bookmarked folders for file explorer sidebar
  
  - htop: Not sure
  
  - joplin-desktop: settings.json file for joplin
  
  - nvim: init.vim config file for neovim
  
  - pulse: config for pulse text editor
  
  - qutebrowser: config.py and userscripts for qutebrowser
  
  - rofi: config.rasi for rofi dmenu
  
  - shikane: config.toml for display manager shikane
  
  - sway: sway config files. config includes all of the files in config.d, which is where all of my configs are. Not sure what environment and sddm-greeter.config are yet
  
  - swayidle: config file for swayidle, essentially just disables idle lock
  
  - swaylock: config file for swaylock, sets colors to match my wallpaper and disables some visual elements by giving them an rgba value of 00000000
  
  - Solaar: config to use the extra buttons on my MX Master 3 mouse
  
  - waybar: config.jsonc and style.css for waybar, not configured yet
  
  - mimeapps.list: default apps for different file types
  
  - user-dirs.dirs: Default xdg folder locatiopns, ex: XDG_CONFIG_HOME="$HOME/.config"
  
  - pavucontrol.ini: settings for the audio popup window connected to waybar

- .ssh: 
  
  - config: ssh config file that includes all of the files in config.d
  
  - config.d: config files for each ssh host including a shortened host name, the real hostname, username, and identity file stored in the not included .ssh/keys/ directory for obvious reasons
  
  - known_hosts and known_hosts.old: the automatically created known_hosts and known_hosts backup files

- .local/bin: Various self installed programs, usually just simple bash scripts

- Pictures/Wallpapers: My wallpapers

- .bashrc: my .bashrc config, including a PS1 prompt that changes if you are in a container and various aliases

- .gitconfig: My global git configs

- .gitignore: This repos gitignore file that excludes everything and then includes some top level files, the .ssh and .config directories minus specific folders, and my .local/bin
