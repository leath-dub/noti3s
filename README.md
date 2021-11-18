# noti3s
This repo shows you how I implemented a simple note taking system on i3.
_Disclaimer: please dont use this, this is probably the worst way to implement such a system_

---

### Dependencies

* Vim 
* i3( obviously )
* A terminal emulator of your choice
* python3
* git

--- 

### Installation(very manual)


Basically you need to add the following format of line in your .i3/config file

```
bindsym $mod+n exec (your terminal) -- vim "+normal G^0i_" "+normal $" "+normal a_" "+normal ko" "+normal ja" "+normal o    -  " +startinsert (directory to notes file); exec "zsh -c 'cd (notes directory); python3 removelines.py;date >> (directory to notes file); sleep 0.2s; i3-msg floating enable;'"
```
Below is an example of what I wrote in my i3 config( note that the brackets above were just for demonstration, and also make sure you link to directory of python script, before you run it ). If your cloning to home, this will mostly be the same(except for the terminal)

```
bindsym $mod+n exec st -- vim "+normal G^0i_" "+normal $" "+normal a_" "+normal ko" "+normal ja" "+normal o    -  " +startinsert ~/noti3s/notes.md; exec "zsh -c 'cd ~/noti3s; python3 removelines.py;date >> ~/noti3s/notes.md; sleep 0.2s; i3-msg floating enable;'"
```

By default the keybind is $mod+n, this can of course be changed

There is a python3 script can be found in this repo( the script as well as edit to i3 config is all you need ), to clone the repo use this command
```zsh
git clone https://github.com/leath-dub/noti3s.git
```
---

### Why this is terrible? ( funny enough this is also the "how to use" guide )

To exit and not save the "-" and other changes by the python3 script, you must exit the notes file with ```:q!```.
if you have made a note however, you can save that with ```:wq```









