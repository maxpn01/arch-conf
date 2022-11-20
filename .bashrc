# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='exa'
alias ll='exa -lah'
alias upgrade='sudo pacman -Syu'
alias update='sudo pacman -Sy'
alias install='sudo pacman -S'
alias uninstall='sudo pacman -Rns'
alias vim="nvim"

PS1='\[\e[0;1;38;5;46m\]\w\[\e[0m\] \[\e[0m\]'
