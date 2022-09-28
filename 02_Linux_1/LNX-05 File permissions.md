# LNX-05 File permissions
Every file in Linux contains a set of permissions. There are separate permissions for reading, writing, and executing files (rwx). There’s also three types of entities that can have different permissions: the owner of the file, a group, and everyone else. Root does not need permissions to read, write or execute a file.


## Key terminology

**touch**: command used to create an empty file.

**chmod**: Change mode, a command used for managing file system permissions (rwx). 

**chgroup**: Change group, command used to change the group associated with a file system object (file, even directory).


## Exercise
- Create a text file.
- Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?
- Make the file executable by adding the execute permission (x).
- Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?
- Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.
- Change the group ownership of the file to a different group.

### Sources
https://stackoverflow.com/questions/9381463/how-to-create-a-file-in-linux-from-terminal-window

https://www.pluralsight.com/blog/it-ops/linux-file-permissions

https://linuxize.com/post/linux-chown-command/



### Overcome challenges
none

### Results
Here we create our text file and use the ls command to confirm the file is created.
![vraag1](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-05-01.png?raw=true)

I made a list to show the file's  permissions. 
![vraag2](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-05-02.png?raw=true)

The file was not executable, so we changed by adding the execute permission (x).
![vraag3](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-05-03.png?raw=true)

With the same command we used previously (ls -l "filename".txt) we can confirm that the file's permissions have changed.
![vraag4](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-05-04.png?raw=true)

We can remove the read and write permissions (rw) from the file for everyone else but not for the owner with "chmod o-rw permission.txt". If you try to open the file (cat permission.txt), you will see a "Permission denied" message.
![vraag5](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-05-05.png?raw=true)

Here we change the group ownership of the file to a different group. 
![vraag6](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-05-06.png?raw=true)


