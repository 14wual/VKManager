# VKManager - Beta (V2.5.0)
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

## Linux Install
```
git clone https://github.com/14wual/VKManager
cd VKManagercd/setup/linux/
./linux-setup.sh --all
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

## Windows Install
<b>Look out!</b> Be aware! Before configuring the script, please install MySQL Workbench or MySQL service.
```
git clone https://github.com/14wual/VKManager
cd VKManagercd/setup/windows/
python3 windows-setup.py
```


<details>
  <summary>Code</summary>
  
  ```python
  for x in pip_installers:
        try:
            os.system(f"pip install {x}")
        except:
            os.system(f"pip install {x}")
        finally:
            print(f"[ ✓ ] {x} installed correctly")
  ```
  
  ```python
  try:
        mlp = mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
            database = database
            )
    except:
        print("[ ✕ ] Manually create the database.")
        exit()
    finally:
        print("[ ✓ ] Created Correctly")
        mlp.execute("SHOW TABLES")
  ```
  
  <a href="https://github.com/14wual/VKManager/blob/main/setup/windows/windows-setup.py"><b>See More (Full Code)</b></a>
  
</details>

## To do:
 
### Next Release (V3.0.0)
 - Home >> Pinned Apps
 - Home >> Last Searchs
 - Section Modify Site
 
 <a href="https://github.com/14wual/VKManager/blob/main/CHANGELOG.md"><b>More</b></a>

<h3>🚀 Know me </h3>

<b>Linkeding</b> - https://www.linkedin.com/in/cpadilla10/ <br>
<b>Twitter</b> - https://twitter.com/codewual <br>
<b>YouTube</b> - https://www.youtube.com/channel/UC0B3mTwPPdKPEwLerauEtdg <br>
