# Users and groups
Summary here

## Key terminology
useradd 
usermod
getent

## Exercise
- Create a new user in your VM. 
    - The new user should be part of an admin group.
    - The new user should have a password.
    - The new user should be able to use ‘sudo’
- Locate the files that store users, passwords, and groups. See if you can find your newly created user’s data in there.



### Sources
https://www.cyberciti.biz/faq/howto-linux-add-user-to-group/
 
https://www.cyberciti.biz/faq/add-new-user-account-with-admin-access-on-linux/#:~:text=Open%20the%20terminal%20application,run%3A%20usermod%20%2DaG%20sudo%20marlena

https://askubuntu.com/questions/611584/how-could-i-list-all-super-users

https://linuxhint.com/getent-command/

### Overcome challenges
I realised that using cat/etc/passwd would show me more than needed. I love to keep my terminal clean so I looked up if it was possible to only show the newly created user's data from the same file. While doing this I learned about the getent command.

![screenshot_challenge]https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX04-extra1.png?raw=true

### Results

![screenshot_firstpart]https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-04-01.png?raw=true

![screenshot_secondpart]https://github.com/Techgrounds-Cloud-9/cloud-9-sait125/blob/main/00_includes/LNX/LNX-04-02.png?raw=true