alias h='history 25'
alias j='jobs -l'
alias la='ls -a'
alias lf='ls -FA'
alias md='mkdir'
alias rd='rm -r'
alias edit='vi'
alias cls='clear'
alias ll='ls -la'

if [ -n "$PS1" ]; then PS1='\h:\w \u\$ '; fi
# Make bash check it's window size after a process completes
shopt -s checkwinsize

export CLICOLOR=1
export LSCOLORS=Gxhxxecxbxagaddxfxgxex

#RED="\[\033[0;31m\]"
RED="\[\033[0;36m\]" #(Cyan)
GREEN="\[\033[0;32m\]"
GOLD="\[\033[0;33m\]"
BLUE="\[\033[0;34m\]"
PURPLE="\[\033[0;35m\]"
CYAN="\[\033[0;36m\]"
GRAY="\[\033[0;37m\]"

NO_COLOUR="\[\033[0;0m\]"

export INPUTCHAR="\\$"$INPUTCHAR

export PS1='\n'$GOLD'[\t]'$CYAN' www.imeter24.com '$GREEN'\w'$GOLD'\n'$INPUTCHAR$NO_COLOUR' '
export PS2='\a> '
export SVN_EDITOR=vi


#LSCOLORS=Gxhxxecxbxagaddxfxgxex
LSCOLORS=GxhxxecxGxagaddxfxgxex
export LSCOLORS
