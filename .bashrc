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

# Git add+commit+push shortcut
git_cmd="git add ~; git commit; git push"
if [[ -z $CONTAINER_ID ]]; then
  alias config-update="$git_cmd"
else
  alias config-update='distrobox-host-exec -- bash -c "$git_cmd"'
fi

# Check if the current env contains DISTROBOX
if (env | grep -Fq 'DISTROBOX'); then
    # Customize PS1 as green with container name instead of host
    PS1="\[$(tput setaf 2)\][\u@${CONTAINER_ID} \w]# \[\e[m\]"
    alias less=bat
else
    # Keep the default PS1 for other environments
    PS1="\[$(tput setaf 3)\][\u@\h \w]# \[\e[m\]"
fi

# Foot Configuration, allows new windows to open in same directory
osc7_cwd() {
    local strlen=${#PWD}
    local encoded=""
    local pos c o
    for (( pos=0; pos<strlen; pos++ )); do
        c=${PWD:$pos:1}
        case "$c" in
            [-/:_.!\'\(\)~[:alnum:]] ) o="${c}" ;;
            * ) printf -v o '%%%02X' "'${c}" ;;
        esac
        encoded+="${o}"
    done
    printf '\e]7;file://%s%s\e\\' "${HOSTNAME}" "${encoded}"
}
PROMPT_COMMAND=${PROMPT_COMMAND:+${PROMPT_COMMAND%;}; }osc7_cwd

# Allow jumping between prompts
prompt_marker() {
    printf '\e]133;A\e\\'
}
PROMPT_COMMAND=${PROMPT_COMMAND:+$PROMPT_COMMAND; }prompt_marker

# Allow piping previous command
PS0+='\e]133;C\e\\'
command_done() {
    printf '\e]133;D\e\\'
}
PROMPT_COMMAND=${PROMPT_COMMAND:+$PROMPT_COMMAND; }command_done

unset rc

