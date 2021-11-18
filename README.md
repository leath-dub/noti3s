# noti3s
This repo shows you how I implemented a simple note taking system on i3.
_Disclaimer: please dont use this, this is probably the worst way to implement such a system_

### Dependencies

* Vim 
* i3( obviously )
* A terminal emulator of your choice
* python3
* git

### Installation(very manual)

Basically you need to add the following format of line in your .i3/config file

```c
bindsym $mod+n exec (your terminal) -- vim "+normal G^0i_" "+normal $" "+normal a_" "+normal ko" "+normal ja" "+normal o    - " +startinsert (directory to notes file); exec "zsh -c 'cd (notes directory); python3 removelines.py;date >> (directory to notes file); sleep 0.2s; i3-msg floating enable;'"
```
Example of what I wrote in my i3 config( note that the brackets above were just for demonstration, and also make sure you link to directory of python script, before you run it )

```c
bindsym $mod+n exec st -- vim "+normal G^0i_" "+normal $" "+normal a_" "+normal ko" "+normal ja" "+normal o    - " +startinsert ~/backups-linux-sd/notes/notes.md; exec "zsh -c 'cd ~/backups-linux-sd/notes; python3 removelines.py;date >> ~/backups-linux-sd/notes/notes.md; sleep 0.2s; i3-msg floating enable;'"
```

By default the keybind is $mod+n, this can of course be changed

There is a python3 script found in this repo, to clone the repo use this command
```zsh
git clone https://github.com/leath-dub/noti3s.git
```










