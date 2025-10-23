# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.cargo/bin:$HOME/.local/bin:$HOME/bin:" ]]; then
    PATH="$HOME/.cargo/bin:$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Set default editor to neovim
export EDITOR=nvim
export VISUAL=$EDITOR

# Aliases
alias ls='ls -F --color=auto'
alias lh='ls -a'
alias ll='lh -lh'
alias grep='grep --color=auto'
alias ip='ip -color=auto'
alias vim='nvim'
alias enter='distrobox enter'
# Codium container alias
#alias codium="/usr/bin/distrobox-enter -n development -- /usr/bin/codium"

# Check if the current env contains DISTROBOX
if (env | grep -Fq 'DISTROBOX'); then
    # Customize PS1 as green with container name instead of host
    PS1="\[$(tput setaf 2)\][\u@${CONTAINER_ID} \w]# \[\e[m\]"
    alias less=bat
else
    # Keep the default PS1 for other environments
    PS1="\[$(tput setaf 3)\][\u@\h \w]# \[\e[m\]"
fi

unset rc

