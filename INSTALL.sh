#!/bin/bash
#__str4vinsk__


function install()
{
	echo "Installing..."
        chmod +x hash.py
        cp hash.py /usr/bin/hashbreaker
	echo "Done! execute {hashbreaker} to use."
	exit
}

if [ "$EUID" -ne 0 ];then
	echo "[!!] Run the installer as root! [!!]"
  	exit
fi

if [[ -e "/usr/bin/hashbreaker" ]]; then
                echo "Hashbreaker is already installed!"
		read -p "Do you want to reinstall it (y/n) ? " yn
		if [[ "$yn" = "y" ]]; then
			rm /usr/bin/hashbreaker
                	install
		elif [ "$yn" = "n" ]; then
			echo "Okay"
			exit
		else
			echo "[!!] Invalid option!"
			exit
		fi
        else
		install
	fi
else
	install
fi
