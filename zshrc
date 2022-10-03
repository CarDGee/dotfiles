# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/d4n13l/.zshrc'

# Completion
#autoload -U compinit
#compinit

# Correction
setopt correctall

# Prompt
autoload -U promptinit
promptinit
prompt gentoo

autoload zcalc

########################################
#
#
# Path to your oh-my-zsh installation.
export ZSH=/usr/share/zsh/site-contrib/oh-my-zsh
#export ZSH=/usr/share/oh-my-zsh

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="random"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# Caution: this setting can cause issues with multiline prompts (zsh 5.7.1 and newer seem to work)
# See https://github.com/ohmyzsh/ohmyzsh/issues/5765
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
#ZSH_CUSTOM=~/.local/share/zsh/plugins

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
        git
        zsh-autosuggestions
        zsh-autocomplete)

bindkey '^X' create_completion

source $ZSH/oh-my-zsh.sh

      #####################
      # User configuration#
      #####################
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='vim'
fi

#########
##alias##
#########
##doas
#alias sudo='doas'

##fancontrol
alias fanstart='doas /opt/nbfc/nbfcservice.sh start'
alias fanmax='nbfc set -f 0 -s 100 && nbfc set -f 1 -s 100'
alias fanauto='nbfc set -f 0 -a && nbfc set -f 1 -a'

##firefox
alias firefox="firefox-bin"

##fstab
alias fstab="doas vim /etc/fstab"

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
alias stat='git status'  # 'status' is protected name so using 'stat' instead
alias tag='git tag'
alias newtag='git tag -a'

##grub update
alias boot="doas mount /boot"
alias update-grub="doas grub-mkconfig -o /boot/grub/grub.cfg"

##kernel
alias compile-kernel='doas genkernel --kernel-config=/config all'

##pacman
#alias update='doas pacman -Syyu'
#alias upgrade='paru -Syyu'
#alias depclean='doas pacman -Rsn $(pacman -Qdtq)'
#alias install='doas pacman -Sy $1'
#alias tufupdate='doas repo-add /usr/local/repos/tuf/tuf.db.tar.zst /usr/local/repos/tuf/*.pkg.tar.zst'
#alias archupdate='doas repo-add /usr/local/repos/arch/arch.db.tar.zst /usr/local/repos/arch/*.pkg.tar.zst'

##portage
alias update='doas eix-sync'
alias upgrade='doas emerge -auDN @world'
alias depclean='doas emerge --depclean'
alias install='doas emerge $1'
alias keywords='vim /etc/portage/package.accept_keywords'
alias rebuild='doas emerge @preserved-rebuild'
alias ubase='vim /etc/portage/package.use/base'
alias uboot='vim /etc/portage/package.use/cleanup'
alias uclang='vim /etc/portage/package.use/clang'
alias udesktop='vim /etc/portage/package.use/desktop'
alias ukvm='vim /etc/portage/package.use/kvm'
alias umedia='vim /etc/portage/package.use/media'
alias umultilib='vim /etc/portage/package.use/multilib'
alias uruby='vim /etc/portage/package.use/ruby'
alias uwine='vim /etc/portage/package.use/wine'
alias uwww='vim /etc/portage/package.use/www'
alias uX='vim /etc/portage/package.use/X'
alias env='vim /etc/portage/package.env'
alias make.conf='vim /etc/portage/make.conf'

# processes########################################
## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'

## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
####################################################

##rickroll
# the terminal rickroll
alias rr='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'


##shutdown or reboot
alias ssn="loginctl poweroff"
alias sr="loginctl reboot"

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

#######
##Ola##
#######
ola

###############
##colorscript##
###############
#colorscript random

############
##neofetch##
############
#if [ -f /usr/bin/neofetch ]; then neofetch --ascii_colors 1 --colors 1 7 1 1 7 3; fi

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

