# LNX-02 Files and Directories
In this assignment, we are going to learn how to create files and navigate in linux.

## Key terminology
**ls**: a command that is used to list all files and directories.\
**pwd**: Print working directory, this command prints the directory you are currently in.\
**mkdir**:This command is used to create a directory.\
**Aboslute path**:The complete path from start of the file system.\
**Relative path**:The path related to the present working directory.

## Exercise
- Find out your current working directory.
- Make a listing of all files and directories in your home directory. You should see directories like ‘Desktop’, ‘Public’ and ‘Pictures’ among others.
- Within your home directory, create a new directory named ‘techgrounds’.
- Within the techgrounds directory, create a file containing some text.
- Move around your directory tree using both absolute and relative paths.


### Sources
Knowledge from school

### Overcome challenges
I had trouble creating a directory in the home directory. So I tried creating the techgrounds directory in the 'sait' directory which succeeded. I realized that I did not try to make the directory with the sudo command. 

Also the exercise tells us that we should see the directories like "Desktop", "Pictures". These were not present because we did not install ubuntu ourselves.

We needed to create a file in this directory. I couldnt create the file here either, the sudo command also didnt work. I figured I have no rights to do anything in the ''techgrounds'' directory. So I used ''chmod 777 techgrounds'' so that I can do anything in directory. 



### Results
Here, we show the contents of home directory\
![screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-01.png)

![screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX02-02.png)

![screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX02-03.png)

![screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX02-04.png)