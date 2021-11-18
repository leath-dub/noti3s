#!/usr/bin/env python3

file_name = "/home/cathal/backups-linux-sd/notes/notes.md"
with open(file_name, "r") as r:
    ar_lines = r.readlines()
    if ar_lines[len(ar_lines) - 1][0] != " " and ar_lines[len(ar_lines) - 1][0] != "#" and ar_lines[len(ar_lines) - 1][0] != "\n":
        ar_lines.pop()
with open(file_name, "w") as w:
    ar_lines = "".join(ar_lines)
    w.write(ar_lines)


