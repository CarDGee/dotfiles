# ██████╗ █████╗ ██████╗ ██████╗  ██████╗ ███████╗███████╗                                      
#██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝██╔════╝                                      
#██║     ███████║██████╔╝██║  ██║██║  ███╗█████╗  █████╗                                        
#██║     ██╔══██║██╔══██╗██║  ██║██║   ██║██╔══╝  ██╔══╝                                        
#╚██████╗██║  ██║██║  ██║██████╔╝╚██████╔╝███████╗███████╗                                      
# ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                      
#                                                                                               
#   ██████╗  █████╗ ███████╗██╗  ██╗        ██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗
#   ██╔══██╗██╔══██╗██╔════╝██║  ██║        ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝
#   ██████╔╝███████║███████╗███████║        ██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗  
#   ██╔══██╗██╔══██║╚════██║██╔══██║        ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝  
#██╗██████╔╝██║  ██║███████║██║  ██║███████╗██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████╗
#╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝
########################################################################                                                                                              

# This file is sourced by bash for login shells.  The following line
# runs your .bashrc and is recommended by the bash info pages.
if [[ -f ~/.bashrc ]] ; then
	. ~/.bashrc
fi
if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty7 ]]; then exec startx; fi