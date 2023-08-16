# _\__o__ __o/    o__ __o      o         o  
#      v    |/   /v     v\    <|>       <|> 
#          /    />       <\   < >       < > 
#        o/    _\o____         |         |  
#       /v          \_\__o__   o__/_ _\__o  
#      />                 \    |         |  
#    o/         \         /   <o>       <o> 
#   /v           o       o     |         |  
#  />  _\o__/_   <\__ __/>    / \       / \ 
#                                           
#########################################################################################                                           

###
HISTFILE=~/.local/share/zsh/histfile
HISTSIZE=1000
SAVEHIST=1000

bindkey -v

zstyle :compinstall filename '~/.zshrc'

# Completion
autoload -U compinit
compinit

# Correction
setopt correctall

# Prompt
autoload -U promptinit
promptinit

autoload zcalc

#######################

##oh-my-zsh##
export ZSH=/usr/share/oh-my-zsh

ZSH_THEME="random"

plugins=(git fzf extract)

#######################

# User configuration

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Ignore commands that start with spaces and duplicates.

export HISTCONTROL=ignoreboth

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Don't add certain commands to the history file.

export HISTIGNORE="&:[bf]g:c:clear:history:exit:q:pwd:* --help"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Use custom `less` colors for `man` pages.

export LESS_TERMCAP_md="$(tput bold 2> /dev/null; tput setaf 2 2> /dev/null)"
export LESS_TERMCAP_me="$(tput sgr0 2> /dev/null)"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Make new shells get the history lines from all previous
# shells instead of the default "last window closed" history.

export PROMPT_COMMAND="history -a; $PROMPT_COMMAND"
source $ZSH/oh-my-zsh.sh

# Fish-like syntax highlighting and autosuggestions
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# Use history substring search
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh

# pkgfile "command not found" handler
source /usr/share/doc/pkgfile/command-not-found.zsh

export FZF_BASE=/usr/share/fzf

###########
###alias###
###########

##fstab
alias fstab="vim /etc/fstab"

# git
alias addup='git add -u'
alias addall='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias stat='git status'
alias tag='git tag'
alias newtag='git tag -a'

##pacman
alias update='doas pacman -Syyu'
alias upgrade='paru -Syyu'
alias cleanch="doas pacman -Scc"
alias depclean='doas pacman -Rsn $(pacman -Qdtq)'
alias fixpacman="doas rm /var/lib/pacman/db.lck"
alias install='doas pacman -Sy $1'
alias rip="expac --timefmt='%Y-%m-%d %T' '%l\t%n %v' | sort | tail -200 | nl"
alias tufupdate='repo-add /home/d4n13l/GitHub/tuf/tuf.db.tar.zst /home/d4n13l/GitHub/tuf/*.pkg.tar.zst'

##systemd
alias jctl="journalctl -p 3 -xb"

# processes########################################
## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'

## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
####################################################

# youtube-dl
alias yta-aac="youtube-dl --extract-audio --audio-format aac "
alias yta-best="yt-dlp -f 'bv*+ba' https://www.youtube.com/watch?v=1La4QzGeaaQ -o '%(id)s.%(ext)s'"
alias yta-flac="youtube-dl --extract-audio --audio-format flac "
alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
alias yta-opus="youtube-dl --extract-audio --audio-format opus "
alias yta-vorbis="youtube-dl --extract-audio --audio-format vorbis "
alias yta-wav="youtube-dl --extract-audio --audio-format wav "
alias ytv-best="yt-dlp -f 'bv*+ba'"

############
### PATH ###
############
if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/Applications" ] ;
  then PATH="$HOME/Applications:$PATH"
fi

