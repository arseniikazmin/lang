#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

if [[ $1 = install ]] || [[ $1 = uninstall ]]
	then
	if [[ $1 = install ]]
	then
		if [[ $2 =~ "" ]]
		then
			confirmation=""
			echo "The script will install lang on the system."
			echo "The installation directories are:"
			echo " ADD  the bash command - /usr/bin/lang"
			echo " ADD  program files - ~/.lang/"
			echo
			mkdir "/home/$2/.lang"
			cp -r ../** "/home/$2/.lang"
			touch /usr/bin/lang
			printf "#!/bin/bash\npython3 /home/$2/.lang/main.py" >> /usr/bin/lang
			chmod +x /usr/bin/lang
			chown $2 /home/$2/.lang/**
			chgrp $2 /home/$2/.lang/**
			echo "Installation completed."
			echo "You can now use the program by typing lang in the terminal."
		else
			echo "Usage: sudo ./install.sh install $USER"
		fi
	fi
	if [[ $1 = uninstall ]]
	then
		echo "The script will uninstall lang from the system."
		echo "The directories that will be deleted are:"
		echo " REMOVE the bash command -/usr/bin/lang"
		echo " REMOVE program files - ~/.lang/"
		rm -r "/home/$2/.lang"
		rm /usr/bin/lang
		echo "Uninstallation completed."
	fi
else
	echo "lang: bad usage"
	echo "example: sudo ./install.sh install \$USER"
	echo "example: sudo ./install.sh uninstall \$USER"
	printf "i, install\t\tinstall\n"
	printf "u, uninstall\t\tuninstall\n"
fi
