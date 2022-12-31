# VKManager - V1.3.8
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

## Gallery

At V0.8.2 Release

![V0.8.2Image - Home Page](https://user-images.githubusercontent.com/105047274/209035118-a316f2d1-7223-47aa-ad3c-ea7a36f53458.png)

![V0.8.2Image - Generate Key](https://user-images.githubusercontent.com/105047274/209035179-df54d93d-3e96-4fdf-96a4-cb51a39f776a.png)

## Last Versión: VKM V1.3.8 | Search Panel

 1. Added a new box, in the search bar.
 1.2 This box is displayed when writing to the "search_entry" of the main.
 1.3 This box adds search buttons with:
  1.3.1 | Top 3 Daily Searches + Total Number of Searches
  1.3.2 | Last 5 searches + The time that has passed since the search was performed
  1.3.3 |  Search button with the text written in the entry in real time

 2. Visual aspects
 2.1 Changing the password will close the dialog box.
 2.2 When adding the password you will get a label with a confirmation message
 2.3.1 | On the search page, a frame has been added that skips if there is no result
 2.3.2 | On the modify password page, a frame has been added that jumps if there is no result

3. Improved the search script, now it asks you for the search instead of looking for it in the History, this solves several bugs, with the search popup panel
4. Checking for blanks in results, password modifications and adding key
5. Added two new columns to the history csv, datetime ``("%d/%m/%Y %H:%M:%S")`` and date ``("%d/%m/%Y").`` These are to improve the search box
6. Added the images (icons) for the light theme option
7. Bug Fixed
7.1 Fix a gub where the login password was not getting correctly from the temporary files on the Add Key page
7.2 Remove line break in the gui banner, where the version looked wrong due to the vers check. script

**Full Changelog**: https://github.com/14wual/VKManager/compare/modify_key...search-panel

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

 ## License

Copyright © 2023 Carlos Padilla.

This project is [GPL](https://github.com/14wual/VKManager/blob/main/LICENSE) licensed.

<h3>🚀 Know me </h3>

<b>Linkeding</b> - https://www.linkedin.com/in/cpadilla10/ <br>
<b>Twitter</b> - https://twitter.com/codewual <br>
<b>YouTube</b> - https://www.youtube.com/channel/UC0B3mTwPPdKPEwLerauEtdg <br>
