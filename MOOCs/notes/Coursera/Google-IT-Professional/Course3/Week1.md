# Navigating the System (Week 1)

## Basic Commands

* This course deals with both a __GUI (graphical user interface)__ and a __CLI (command line interface/interpreter)__
    * With Windows, we'll be dealing with both the GUI and CLI
    * and with Linux, we'll just be dealing with the CLI
    
* The CLI in Linux is called a __shell__, and the language that we'll use to interact with this shell is called __Bash__.
* The course content for this week is broken down into two sections:
    * __Basic Operating System Navigation__
        * Navigating from one directory to another
        * Getting file information
        * Removing files and directories
    * __File and Text Manipulation__
        * Searching through your directories
        * Find a specific file
        * Copying and pasting
        * Chaining commands

* Here is a link to Microsoft's website providing information to their CLI: [https://docs.microsoft.com/en-us/powershell/scripting/powershell-scripting?view=powershell-5.1](https://docs.microsoft.com/en-us/powershell/scripting/powershell-scripting?view=powershell-5.1)
* Here is a link to GNU for a reference manual for Linux's CLI: [https://www.gnu.org/software/bash/manual/bash.html](https://www.gnu.org/software/bash/manual/bash.html)

### List Directories in a GUI

* A path in _Windows_ looks like _'C:\Users\<Username>\Desktop'_
* In Windows, filesystems are assigned to drive letters, which look like __C:__, or __D:__, or __X:__
    * Each drive letter references a filesystem
    * __REMEMBER:__ filesystems are used to keep track of files on a computer.
    
* Each filesystem has a root directory, which is the parent for all other directories on the filesystem
* In Windows, root directories are written like: __C:\\__ , __D:\\__, or __X:\\__
* In Windows, subdirectories are seperated with backslashes (\\), whereas in Linux, they are seperated with forward slashes (/)

* Discussion of "Size on Disk" vs. "Folder Size": [https://technet.microsoft.com/en-us/library/hh148159.aspx](https://technet.microsoft.com/en-us/library/hh148159.aspx)

### Windows: List Directories in CLI

* In Windows, there are two kind of command line interfaces:
    * Command Prompt: cmd.exe
    * PowerShell: powershell.exe
    
* PowerShell is something of an extension of Command Prompt, supporting all of its commands and offering extended scripting abilities.
* An __alias__ is something of a "nick name" for a command.
* A __parameter__ is a value that is input into a command to "fine tune" its behaviour

* The command for listing files on Windows Command Prompt/PowerShell is:

```powershell
ls [directory] <-Force>
```

... with the optional _-Force_ showing all (including system and hidden) files and folders in the directory in question.

* The __C:__ drive root folder is what is known as a __parent directory__ and the contents inside are considered __child directories.__
* __Parent__ and __child__ are terms in computing that describes a hierarchial relationship
    * In the case of file systems, given a folder __Fo__ and a file __Fi__ (with _Fi_ being inside _Fo_), we say that _Fo_ is the parent and that _Fi_ is the child of _Fo_

* The command to get information concerning a particular command (with -Full giving a more verbose description) is:

```powershell
Get-Help [command] <-Full>
```

### Linux: List Directories

* An example of a Linux path would be _'/home/\<username\>/Desktop'_

__Linux does have some key directories, like:__

|Folder Name|Purpose|
|-----------|-------|
|/bin|a folder that contains programs (or symlinks to programs) similar to the "Program Files" directory in Windows|
|/etc|this folder stores configurations for system and other programs|
|/home|the folder that contains other folders and files pertaining to users on the system|
|/proc|this folder contains information concerning currently running processes|
|/usr|doesn't contain user files, but rather user installed software|
|/var|stores system logs and other rapidly changing files|

* In Linux, a __flag__ is a way to specify additional options for a command, similar to the __parameters__ in Windows CLI/PowerShell
    * In Linux, you can add the _--help_ flag to get a verbose list of other flags to append to the command you're interested in
    * The manpages, which has the syntax of _man \[command\]_, usually gives a manual on how to use the command.
    
* In Linux, just as with Windows, the command to list a directory is:

```bash
ls <-la> [path]
```

where _-l_ lists the files with their information and _-a_ lists hidden files

### Windows: Changing Directories in the GUI

* An __absolute path__ is one that starts from the main directory, whilst a __relative path__ is the path starting from your current directory.

### Windows: Changing Directories in the CLI

* In Windows PowerShell, _pwd_, or __print working directory__ prints out the current working directory
* Again, in PowerShell, _cd_ or __change directory__ changes the working directory to
* __Tab Completion__ allows the user to use the \[tab\] key to "autocomplete" or guess the full name of the thing you're typing


## File and Text Manipulation

