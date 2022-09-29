# LNX-07 Bash scripting 
The default CLI in Linux is called Bash shell. We have already used some commands in this sell. A bash script is basically a series of those commands in a text file. 

## Key terminology
**bin**:

**bash**:

**variable**:

**parameter**:

**scripts**:


## Exercise
- Create a directory called ‘scripts’.
 Place all the scripts you make in this directory.
- Add the scripts directory to the PATH variable.
- Create a script that appends a line of text to a text file whenever it is executed.
- Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

### Sources
https://linuxize.com/post/how-to-add-directory-to-path-in-linux/ 

https://www.howtogeek.com/808593/bash-script-examples/

https://www.cyberciti.biz/faq/linux-append-text-to-end-of-file/

https://linuxhint.com/30_bash_script_examples/

https://www.youtube.com/watch?v=7qd5sqazD7k

https://www.computerhope.com/jargon/p/positional-parameter.htm
### Overcome challenges
I realised some of my scripts weren't working because I did not have the permission. This is because I saved my folders not in my home folder but in the "home" folder. We can fix this with using sudo. The actual fix is to put the scripts in the correct folder.
### Results
#### Excerise 1
Here we create our scripts directory.

![vraag1](../00_includes/LNX-07-01.png)

We add the scripts directory to the PATH variable with this command, make sure there is no spaces before and after the quotation mark.

![vraag1.2](../00_includes/LNX-07-02.png)

This is our script that appends a line of text to a text file whenever it is executed.

![vraag1.3](../00_includes/LNX-07-03.png)

When executed it should result in:

![vraag1.3](../00_includes/LNX-07-04.png)

Here we create a script that installs the httpd (apache2) package, activates httpd, and enables httpd. The script also prints the status of httpd in the terminal.

![vraag1.4](../00_includes/LNX-07-05.png)

Running the script will give you:

![vraag1.4](../00_includes/LNX-07-06.png)

