
* A __standard user__ is one who is given access to a machine but has restricted access to do things like install software or change certain settings
* An __administrator (admin)__ is a user that has complete control over a machine
* Users segregate users into groups, group having their own default set of permissions for users
* __Computer Management__ is a tool in Windows that is used for system administrator tasks, like setting up users and groups
* A __Windows domain__ is a network of computers, users, files, etc. that are added to a central database

* Computer Management has various options in its menu:
    * __System Tools__ which has
        * __Task Scheduler:__ allows the admin to schedule programs and tasks to run at certain time (like automatically shutting off the computer at 11:00pm every night)
        * __Event Viewer:__ where the system stores the system logs
        * __Shared Folders:__ shows the folders that users on the machine share with each other
        * __Local Users and Groups__
        * __Performance:__ shows monitoring for the resources of our machine (like CPU and RAM)
        * __Device Manager:__ manages the internal and external hardware
    * __Storage__
        * __Disk management__
    * __Services and Applications:__ shows us the services and applications on the machine
    
* __User Access Control (UAC)__ is a feature in Windows that prevents unauthorized changes to a system

__Powershell Commands:__

* `Get-LocalUser` lists the current user as well as other accounts on the computer
* `Get-LocalGroup` will list the groups on the local machine
* `Get-LocalGroupMember <group>` will list the members of the local group

__Linux Users/Groups__

* The __root__ user is the first user installed on a Linux computer, it has all the privileges, it's a "superuser"
* The __sudoers__ file is a file located in `/etc/sudoers` that controls who has root privileges
* In Linux, the `sudo` command is used to run as root
* and in Linux, the `su` command allows you to "log in" to different user accounts from the shell
* Linux "Group IDs" are stored in `/etc/groupid`
* The file that contains user information is in `/etc/passwd`

__Windows Passwords__

* 
