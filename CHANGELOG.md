# Changelog
## Current version - 1.1.1
All notable changes to this project will be documented in this file!

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),

## [1.1.1] - 2022-12-28

### Added (  Modify Key Page )

 - Fixed Modify Key Page >> Now it can be modified correctly
 - Encryption added to modified keys
 - Updated the update script

## [1.1.1] - 2022-12-27

### Added ( Update Script )

 - New script that checks the current version with the one you have running.
 - Now a pop-up window will appear warning that you must update in case the versions are not the same

## [1.0.0] - 2022-12-27

### Added ( Encryption Release )

In this (Encryption Release) version, the program officially stops being beta and becomes a complete program. All the functionality that was planned from the beginning has already been implemented, and now the only thing left is the resolution of bugs, visual improvements and functionality that is imagined along the way.

- Password encryption

## [0.9.7] - 2022-12-27

### Added ( Clipboard Fixed Bug )

 - The bug that only allows copying the last password of each site has been resolved. Now they can all be copied correctly.
 - Removed the main.py file and changed the path of the __init__.py file to the main folder because (main.py) was an unnecessary file that only hindered the execution of the program.
 - Modified all files with internal imports due to __init__.py file path change

 - License published
 - Posted the requirements.txt file to be able to do "_pip install requirements_"
 - Posted project python setup file

<details>

## This has been the solution that I have carried out to fix the clipboard bug

### Before

```python
self.generate_copy_button_1 =customtkinter.CTkButton(self.generate_result_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
self.generate_copy_button_1.grid(row=2, column=0, pady=10, padx=5, sticky="n")
```

### After

```python
self.generate_copy_button_1 =customtkinter.CTkButton(self.generate_result_frame,text="Copy to Clipboard",
                            command=lambda password=x[1]: clipboard.copy(password))
self.generate_copy_button_1.grid(row=2, column=0, pady=10, padx=5, sticky="n")
```
</details>

## [0.9.5] - 2022-12-26

### Added ((PRE) Modify Key Release)

 - Established the bases of the "Modify Password" page
 - Visual improvements on the "Add Key" page
 - Removal of "junk" lines in scripts
 - All scripts Signed

### ⚠︎ ALERT
**Program error: in the generation of the frames with the passwords, when you press copy, only the last one taught is copied.**

Work is already underway to resolve this problem, but it is not promised that this will be resolved soon.

<details>

 <summary>Example of "junk" line</summary>

 <br> _And then not use the bilbiotec (in this example)_
```python
import tkinter as tk
```

_Example of unnecessary line in most scripts_
```python
with open('conf/appearance.conf','r') as appearance_file:
    conf_appearance_mode = appearance_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)
```

</details>

## [0.9.3] - 2022-12-24

### Added (Code (2) Release)

 - Again, some new extreme code cleanup, for cleaner, more efficient code.
 - Divided the script into different files, for a cleaner treatment and more efficient use of resources by the application
 - Now, the script will work with temporary files, which will be deleted at the end of this activity.****

## [0.8.6] - 2022-12-24

### Added (Installation (2) Release)

 - Fixed installation bugs
 - Added setup file for a flawless pip installation

<details>
 
 <summary>New Installation</summary>
 
 ```
git clone https://github.com/14wual/VKManager
cd VKManager
pip install requerements
python3 VKManager/other/mysql/mysql-setup.py
```


</details>

## [0.8.5] - 2022-12-23

### Added (Banner Release)

 - Added a Chronometer
 - Added a Date 
 - A key Count (total)

## [0.8.2] - 2022-12-22
 
### Added (Big Release)
 - Visual aspects (7)
 - Easy switching between dark and light appearance mode
 - A noticeable improvement in code readability [See Code](https://github.com/14wual/VKManager/blob/main/main.py)
 - Added About file (File showing the current version) - [See Version](https://github.com/14wual/VKManager/blob/main/about/version)
 - Add a darling frame with buttons (for updating and for darling the repository)
 - Informative banner (version number, time in use, copy and remaining time)
 - Posted some test files (temporary) - [See Temps](https://github.com/14wual/VKManager/tree/main/test)
 - Programmed a more efficient code - [See Code](https://github.com/14wual/VKManager/blob/main/main.py)
 - An easier (and cross-platform) way to install the repository

<details>
<summary>See Visual Changes Aspects </summary> 

 - [Page Links Section] The buttons lower their opacity depending on the page where it is to inform the user where they are
 - [Page Links Section] Icons have been added
 - [Search Button] Added Icons
 - Added two different types of icons (for dark systems and light systems)
 - Posted icons
 - Added the informative banner (version, remaining time, ...)
 - A new (completely different) interface for the password generator
 
 ### Gallery 
 
 Before:
 
 ![Image - V0.4.2 Search Page](https://user-images.githubusercontent.com/105047274/209036705-80bb06fa-44e7-401c-b674-a307f9cd3f7b.png)
 
 ![Image - V0.4.2 - Home Page](https://user-images.githubusercontent.com/105047274/209036710-302f4939-de8c-47ad-a897-cb642598ec68.png)
 
 After:
 
 ![V0.8.2Image - Home Page](https://user-images.githubusercontent.com/105047274/209035118-a316f2d1-7223-47aa-ad3c-ea7a36f53458.png)

 ![V0.8.2Image - Generate Key](https://user-images.githubusercontent.com/105047274/209035179-df54d93d-3e96-4fdf-96a4-cb51a39f776a.png)
 
</details>
 
## [0.5.2] - 2022-12-19
 
### Added (Filters Release)
 - Fixed Login History (Login Authorization).
 - Added Search filters (User Filter)

<details>
Fixed Login History (Login Authorization). <br>
[ ] Before: <br>
2022-12-18 12:15:25.660903, example, <class 'main.log'> <br>
[ ] After: <br>
2022-12-18 12:37:27.714245, example, True <br>
2022-12-18 12:37:27.714245, example, False <br>
<br>
Addd Search filters (User Filter) <br>
New Feature!: Search filters. Now look up your password by username, instead of by site. <br>
</details> 

## [0.4.7] - 2022-12-18

<details>
 
 <summary>[0.4.8] - Post Release</summary>
 
### [0.4.8] - 2022-12-18
### Added (Post Release of V0.4.7) 
 - Fixed the bug that only show a content of the total. It is fixed as follows >> https://github.com/14wual/VKManager/wiki/Pinned-Keys#label-above-label
 - Changing the writing mode in the search history
</details>
 
### Added (Post Release)
 - Created Wiki Pages
 - Pinned Keys Fixed Bug
 - <a href='https://github.com/14wual/VKManager/wiki/Pinned-Keys#configuration-file-and-the-n'>Configuration file and the "\n"</a>
 - <a href='https://github.com/14wual/VKManager/wiki/Pinned-Keys#infinite-requests'>Infinite Requests of Pinned Keys</a>
 - Create (in teh script) the **pre** Section Modify Site

## [0.4.2] - 2022-12-15
 
### Added (Home Release)
 - Upgrade Home >> Pinned Apps
 - Upgrade Home >> Last Searchs
 - Upload 'Search log File'
 - Fix the bug that only show me a single key (in the pinned section), now it can show infinite keys

## [0.3.7] - 2022-12-11
 
### Added (Installation Release)
 - Windows Setup (bat) Upgrade
 - Fixed Looping Bugs
 - Upload alternative Installation (py)

## [0.3.6] - 2022-12-9
 
### Added (Installation Release)
 - Linux Setup (sh)
 - Windows Setup (py or bat)
 - MySQL Setup (py)
 - Linux Comand (sh)
 - Pip Setup Install (py)

## [0.2.8] - 2022-12-07
### Added
 - Publication of the files
 - Published Requerments
 - Added Search Bar
 - Added Results Section
 - Added Search Filters
 - Added Section >> Home
 - Added Section >> Add Key To Vault
 - Added Section >> Password Generator

## [0.0.0] - 2022-12-3
### Added
- Created Script
