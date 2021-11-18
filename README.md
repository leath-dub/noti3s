# noti3s
This repo shows you how I implemented a simple note taking system on i3.
_Disclaimer: please dont use this, this is probably the worst way to implement such a system_

### Installation(very manual)

Basically you need to add the following format of line in your .i3/config file
```
bindsym $mod+n exec st -- vim "+normal G^0i_" "+normal $" "+normal a_" "+normal ko" "+normal ja" "+normal o    - " +startinsert ~/backups-linux-sd/notes/notes.md; exec "zsh -c 'cd ~/backups-linux-sd/notes; python3 removelines.py;date >> ~/backups-linux-sd/notes/notes.md; sleep 0.2s; i3-msg floating enable;'"

```




