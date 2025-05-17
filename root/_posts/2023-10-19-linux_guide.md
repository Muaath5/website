---
title: "Linux Basic Guide (Ubuntu/Kali)"
description: "Commands, concepts, and programs tutorial"
lang: en
tags: ["tutorial", "linux"]
---
## Installing WSL
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
After restart:
```
wsl --install
```
After restart, go to Microsoft Store, pick whatever distribution you like & install it.


## General knowledge
- First word of any command is the _program_ name, and anything that comes after it are the _parameters_, Examples:
  - `curl google.com`: Program `curl`, Paramaters: `google.com`
  - `g++ file.cpp -o ahmad -O2`: Program `g++`, Paramaters: `file.cpp`, `-o`, `ahmad`, `-O2`
- Every program has its own way to handle parameters
- Usually every program will response to `--version` and `--help`, but sometimes they won't so you must read manual
- Program `help` might show you some commands, mostly useless
- Manual `man {command}`, will give you a full manual
- If a program run infinitly, you can shut it down using `Ctrl + C`
- Don't enter `vim` without minimum 2 years of experience, because you won't be able to get out of it.

## Working Directory (WD)
- To check the working directory use `pwd`
#### `cd` (Change Directory)
Usage: `cd {PATH}`
- To get to parent folder use `cd ..`
- To get to grandparent folder use `cd ../..`
- To get to root `cd /`
- To get to home `cd ~`
- To get to a child directory `cd ./child/childofchild`
- The concept here is about **Relative** and **Static** paths:
  - Relative: describing a path based on the working directory
  - Static: describing a path fully, it must start with `/` which indicates the root, like `/usr/bin/g++`

## Root Permissions
- Append `sudo` before any command to run as root
- To login as root use `sudo su -`
- Usually running with `sudo` solves any "Permission Denied" problem

## Files/Directories
- **Related commands**: `touch`, `mv`, `cp`, `rm`, `mkdir`, `ls`
- Creating file: `touch file.txt`
- Creating directory: `mkdir dir`
- Moving file: `mv file.txt /path/to/anothername.txt`
- Renaming file: `mv file.txt another.txt`
- Removing file: `rm file.txt`
- Removing directory: `rm -d somedirectory`
- Removing directory and removing contents recursively: `rm -d -r somedirectory`
- Listing all contents of WD: `ls`
- Listing all contents of WD with extra details: `ls -la`
- Copying a file: `cp old_code.cpp new_code.cpp`

## Editing text files
- To append to a file: `echo "Added this text" >> file.txt`
- To overwrite a file: `echo "Added this text" > file.txt`
- To write to a file: `cat >file.txt` and when you finish just interrupt it with Ctrl+C
- To output a file: `cat file.txt`
- To output first 5 lines of a file: `head -n 5 file.txt`
- To edit a file: `sudo nano file.txt` 

## Running executables

### About `$PATH`
- There is an environment variable called `PATH`, you can see it by `echo $PATH`
- This have a list of directory paths seperated by a colon (`:`)
- If you run a command, without specifing a path for it (either static or relative) it will search on these directories by their order
- If not found you will get `command not found` with error `127`

### Running
- Running a local executable (in your directory): `./app`
- Running a global executable: `app`
- Running a global executable that matchs some command in `help` list: `\app`

## Multiple commands
- `mkdir child; cd child` - Using `;` it will run these two commands
- `mkdir child && cd child`- Using `&&` it will run the second command if the first have a zero exit code

## File Input/Output pipe redirection
- Every program have 3 pipes (file descriptors):
  - 0: stdin
  - 1: stdout
  - 2: stderr
- stderr/stdout will be shown togother in the same terminal
- Redirecting stdin to a file: `./app < file.in`
- Redirecting stdout to a file: `./app 1> file.in`
- Redirecting stderr to a file: `./app 2> file.in`
- Run without output (redirect to empty): `./app >/dev/null`
- Read from random input: `./app </dev/urandom`
- Append to a file: `./app >> append.txt`
- `./code | ./checker` - Using `|` it will run first app and redirect its output to second app input

## Environment Variables
The system has some variables with assigned values, so programs can use it
- Checking environment variables: `env`
- Writing an environment variable in current session: `export VAR="value"`
- Writing a permanent environment variable: `echo 'export VAR="value"' >> ~/.bashrc`
- Outputting an environment variable: `echo $VAR`
- Outputting last command exit code: `echo $?`

## Processes management
- Every process have a Process ID (PID)
- Check current processes: `ps`, for all use `ps -a`
- Kill a process by PID: `kill 7522`, force kill `kill -9 7522`

## File Permissions
When doing `ls -la`, here is an expected output:
```
drwxrwxrwx root root somedir
lrwxr-xr-- root root somelnk
-rw-rw-r-- user user somefile
```
- First character: file type `d`=directory, `l`=link, `-`=file
- Next 3 characters: Permissions of owner
- Next 3 characters: Permissions of group
- Next 3 characters: Permissions of others
- Permissions `rwx` means **r**ead, **w**rite, e**x**ecute.
- After it the owner
- After it the group

- Changing owner: `chown`
- Changing group: `chgrp`
- Changing permissions: `chmod`

For more, check [this page](https://help.ubuntu.com/community/FilePermissions)

## About shells
- There are multiple shell prgrams
- Most common ones are `bash`, `sh`, `zsh`
- Each one might have slight differences
- To know which shell are you using: run `echo $0`

### Shell execuatables
- If you had a text file that is executable, it will run it based on first line of it
- Usually it's on this format `#!/bin/bash`, After `#!` is the static path of running this file
- Using this you might write any interpreter programs as executables\
- It could be `#!/usr/bin/env python3` and the script is a Python code

#### Example

```sh
#!/bin/bash

g++ --version > script_temp.txt
head -n 1 script_temp.txt
rm script_temp.txt
```

This script will show you the first line of `g++ --version` output

#### Example 2

## Helping Programs
- `time {COMMAND}` - Measures execution time of a command
- `which {PROGRAM_NAME}` - Shows you the path of the program
- `timeout {SECONDS} {COMMAND}` - Exits with error code 127 in case it exceeds time
- `curl` - Client for sending web requests

## Package Manager 
- Almost every linux-based system has a package manager
- The package manager installs programs/compilers/tools easily

### Different Systems Package Manager
- Debian: `dpkg`
- Ubuntu: `apt`
- Arch: `pacman`
- Alpine: `apk`
- MacOS: `homebrew` (Not installed by default in MacOS)

### `apt`
- Installing: `sudo apt install {package}`
- Updating: `sudo apt update`
- Upgrading `sudo apt upgrade`
- Removing `sudo apt remove {package}`
