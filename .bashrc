# ██████╗ █████╗ ██████╗ ██████╗  ██████╗ ███████╗███████╗
#██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝██╔════╝
#██║     ███████║██████╔╝██║  ██║██║  ███╗█████╗  █████╗  
#██║     ██╔══██║██╔══██╗██║  ██║██║   ██║██╔══╝  ██╔══╝  
#╚██████╗██║  ██║██║  ██║██████╔╝╚██████╔╝███████╗███████╗
# ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝
#                                                         
#   ██████╗  █████╗ ███████╗██╗  ██╗██████╗  ██████╗      
#   ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝      
#   ██████╔╝███████║███████╗███████║██████╔╝██║           
#   ██╔══██╗██╔══██║╚════██║██╔══██║██╔══██╗██║           
#██╗██████╔╝██║  ██║███████║██║  ██║██║  ██║╚██████╗  
########################################################################

# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi


# Put your fun stuff here.
if [ -f /usr/bin/neofetch ]; then neofetch --ascii_colors 1 --colors 1 7 1 1 7 3; fi

export PATH=$PATH:~/.bin
export PATH=$PATH:~/.local/bin
export HISTCONTROL=ignoreboth

##fancontrol
alias fanstart='sudo /opt/nbfc/nbfcservice.sh start'
alias fanmax='nbfc set -f 0 -s 100 && nbfc set -f 1 -s 100'
alias fanauto='nbfc set -f 0 -a && nbfc set -f 1 -a'

##firefox
alias firefox="firefox-bin"

##fstab
alias fstab="sudo vim /etc/fstab"

##grub update
alias boot="sudo mount /boot"
alias update-grub="sudo grub-mkconfig -o /boot/grub/grub.cfg"

##kernel
alias compile-kernel='sudo genkernel --kernel-config=/config all'

##list
alias ls='ls --color=auto'
alias la='ls -a'
alias ll='ls -la'
alias l='ls'
alias l.="ls -A | egrep '^\.'"



##portage
alias update='sudo eix-sync'
alias upgrade='sudo emerge -auDN @world'
alias depclean='sudo emerge --depclean'
alias install='sudo emerge $1'
alias keywords='sudo vim /etc/portage/package.accept_keywords'
alias rebuild='sudo emerge @preserved-rebuild'
alias ubase='sudo vim /etc/portage/package.use/base'
alias uboot='sudo vim /etc/portage/package.use/boot'
alias uclang='sudo vim /etc/portage/package.use/clang'
alias ukvm='sudo vim /etc/portage/package.use/kvm'
alias umedia='sudo vim /etc/portage/package.use/media'
alias umultilib='sudo vim /etc/portage/package.use/multilib'
alias uruby='sudo vim /etc/portage/package.use/ruby'
alias uwine='sudo vim /etc/portage/package.use/wine'
alias uwww='sudo vim /etc/portage/package.use/www'
alias uX='sudo vim /etc/portage/package.use/X'
alias env='sudo vim /etc/portage/package.env'
alias make.conf='sudo vim /etc/portage/make.conf'

##ssh
alias tota='ssh c4rl074@192.168.0.11'

##shutdown or reboot
alias ssn="loginctl poweroff"
alias sr="loginctl reboot"

##tools

# # ex = EXtractor for all kinds of archives
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;      
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}
