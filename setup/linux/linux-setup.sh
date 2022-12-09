banner() {
    echo """██╗    ██╗██╗   ██╗ █████╗ ██╗     
            ██║    ██║██║   ██║██╔══██╗██║     
            ██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)
            ██║███╗██║██║   ██║██╔══██║██║     
            ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
             ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝"""
}

pip() {
    pips = ("stdiomask","random","customtkinter","tkinter","os","datetime","mysql.connector")
    pipPIL = ("Image")

    for x in pips
    do
        pip install $x
        pip3 install $x

        python3 -m pip show $x
    done

    for x in pipPIL
    do
        pip install $x from PIL
    done
}

command() {
    sudo mkdir ~/.config/vkm
    sudo cp ../../main.py ~/.config
    sudo cp vkm /bin/
    sudo chmod +x /bin/vkm
}

mysql() {
    python3 ../other/mysql/mysql-setup.py
}

all() {
    banner()
    command()
    mysql()
    pip()

    vkm
}

if [[ "$1" == '--all' ]]; then 
        all ()
elif [[ "$1" == '--mysql' ]]; then 
        mysql ()
elif [[ "$1" == '--pip' ]]; then 
        pip()
elif [[ "$1" == '--command' ]]; then 
        command()
else 
        cat <<- EOF 
        Usage : ./linux-setup.sh --option 
                  
        Available Options : 
        --all       --mysql
        --command   --pip
        EOF 
fi
