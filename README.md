# VKManager - Beta (V0.8.2)
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

At V0.8.2 Release
![V0.8.2Image - Home Page](https://user-images.githubusercontent.com/105047274/209035118-a316f2d1-7223-47aa-ad3c-ea7a36f53458.png)

![V0.8.2Image - Generate Key](https://user-images.githubusercontent.com/105047274/209035179-df54d93d-3e96-4fdf-96a4-cb51a39f776a.png)

## Last Version BV0.8.2:

> Visual aspects (7) <br>
Easy switching between dark and light appearance mode <br>
A noticeable improvement in code readability <br>
Added About file (File showing the current version) <br>
Add a darling frame with buttons (for updating and for darling the repository) <br>
Informative banner (version number, time in use, copy and remaining time) <br>
Posted some test files (temporary) <br>
Programmed a more efficient code <br>
An easier (and cross-platform) way to install the repository

<a href="https://github.com/14wual/VKManager/blob/main/CHANGELOG.md#082---2022-12-23"><b>See More (all update)</b></a>

## To do:
 
### Next Release (V0.9.0)
 
 <a href="https://github.com/14wual/VKManager/blob/main/CHANGELOG.md"><b>See More</b></a>

<h3>🚀 Know me </h3>

<b>Linkeding</b> - https://www.linkedin.com/in/cpadilla10/ <br>
<b>Twitter</b> - https://twitter.com/codewual <br>
<b>YouTube</b> - https://www.youtube.com/channel/UC0B3mTwPPdKPEwLerauEtdg <br>
