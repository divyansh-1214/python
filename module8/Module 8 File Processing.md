Module 8: File Processing

• Opening Files

• The os and os.path modules

• Reading files

• Writing into a file

• Appending data into a file

• Lab:

• Write a program to read and print the contents of a text file.

• Write a program to append a new line of text to an existing file.

• Use the os module to check if a file exists in a given directory.



###### Opening Files

syntax: file\_object = open("filename", "mode")

example: f = open("data.txt", "r")

| Mode | Description                                        |

| ---- | -------------------------------------------------- |

| `r`  | Open file for reading (file must exist)            |

| `w`  | Open file for writing (creates or overwrites file) |

| `a`  | Open file for appending                            |

| `x`  | Create a new file                                  |

| `r+` | Read and write                                     |

| `b`  | Binary mode (e.g., `rb`, `wb`)                     |



###### The os and os.path Modules (Python)



These modules are used to interact with the operating system and to work with file \& directory paths.

1. os → works with files, folders, and OS-level operations
2. os.path → works with paths (check existence, join paths, get size, etc.)



🔹 os.getcwd() – Get current directory

import os

print(os.getcwd())



🔹 os.chdir(path) – Change directory

import os

os.chdir("D:/")     # change to D drive

print(os.getcwd())



🔹 os.listdir(path) – List files and folders

import os

print(os.listdir("."))   # list current folder contents



🔹 os.mkdir(name) – Create one directory

import os

os.mkdir("MyFolder")



🔹 os.makedirs(path) – Create nested directories

import os

os.makedirs("A/B/C")



🔹 os.remove(file) – Delete a file

import os

os.remove("data.txt")



🔹 os.rmdir(dir) – Delete empty directory

import os

os.rmdir("MyFolder")





⚠ Folder must be empty



🔹 os.rename(old, new) – Rename file/folder

import os

os.rename("old.txt", "new.txt")



🔹 os.system(cmd) – Run system command

import os

os.system("notepad")   # opens Notepad (Windows)



🔹 os.path Functions with Examples

✔ os.path.exists(path)

import os

print(os.path.exists("data.txt"))



✔ os.path.isfile(path)

import os

print(os.path.isfile("data.txt"))



✔ os.path.isdir(path)

import os

print(os.path.isdir("MyFolder"))



✔ os.path.abspath(file)

import os

print(os.path.abspath("data.txt"))



✔ os.path.basename(path)

import os

print(os.path.basename("D:/code/data.txt"))



✔ os.path.dirname(path)

import os

print(os.path.dirname("D:/code/data.txt"))



✔ os.path.getsize(file)

import os

print(os.path.getsize("data.txt"), "bytes")



✔ os.path.join(p1, p2)

import os

path = os.path.join("D:/code", "data.txt")

print(path)

