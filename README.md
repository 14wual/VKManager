# VKManager - Beta (V0.5.2)
<b>Vault Keys Manager</b> It is a password manager with interface programmed in python with the help of CustomTkinter (CTK) and MySQL.

```
888       888 888     888       d8888 888
888   o   888 888     888      d88888 888
888  d8b  888 888     888     d88P888 888        (code by WUAL)
888 d888b 888 888     888    d88P 888 888            twitter.com/codewual
888d88888b888 888     888   d88P  888 888     github.com/14wual
88888P Y88888 888     888  d88P   888 888            youtube: WualPK
8888P   Y8888 Y88b. .d88P d8888888888 888     
888P     Y888  "Y88888P" d88P     888 88888888
```

See commits updates (CHANGELOG) here: <a href="https://github.com/14wual/VKManager/blob/main/CHANGELOG.md"><b>Link</b></a>

## Install
Install && Conf Requerements

<b>Look out!</b> Be aware! Before configuring the script, please install MySQL Workbench or MySQL service.
```
git clone https://github.com/14wual/VKManager
cd VKManager
pip install requerements
python VKManager/other/mysql/mysql-setup.py
```

## Linux Command
Install && Conf the Command **"VKM"**

```
git clone https://github.com/14wual/VKManager
cd VKManagercd/setup/linux/
./linux-setup.sh --command
```

<details>
  <summary>Code</summary>
  
  ```bash
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
  ```
  
  <a href="https://github.com/14wual/VKManager/blob/main/setup/linux/linux-setup.sh"><b>See More (Full Code)</b></a>
  
</details>

### Linux Use
```
vkm
```

## Gallery
At V0.4.2 Release

![V0.4.2Image - SearchSection](https://user-images.githubusercontent.com/105047274/207924427-48209720-5cbb-42f9-8c8b-2d6ef4b1697e.png)


![V0.4.2Image - HomeSection](https://user-images.githubusercontent.com/105047274/207924253-bfb56fdc-a968-4c37-8378-d527e22e65ab.png)

## To do:
 
### Next Release (V0.6.2)
 - New GUI Widgets
 - More...
 
 <a href="https://github.com/14wual/VKManager/blob/main/CHANGELOG.md"><b>More</b></a>

<h3>🚀 Know me </h3>

<b>Linkeding</b> - https://www.linkedin.com/in/cpadilla10/ <br>
<b>Twitter</b> - https://twitter.com/codewual <br>
<b>YouTube</b> - https://www.youtube.com/channel/UC0B3mTwPPdKPEwLerauEtdg <br>
