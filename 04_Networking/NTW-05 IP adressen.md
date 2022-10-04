# NTW-05 IP adressen
nog adden niet vergeten

## Key terminology
**IPV4**:
**IPV6**:
**Public IP**:
**Private IP**: 
**Static IP**:
**Dyanmic IP**:

## Exercise
- Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.
Zijn de adressen hetzelfde of niet? Leg uit waarom.
- Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.
Zijn de adressen hetzelfde of niet? Leg uit waarom.
- Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?
- Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?


### Sources
https://www.howtogeek.com/247452/is-it-possible-for-different-people-to-have-the-same-public-ip-address/

### Overcome challenges
When I was working on the third question, I realized that I could elaborate a bit more than asked. Whilst explaining more about the subject is nice,  I am unsure whether the extra information I provide is neccessary/relevant. 

Later on I realized I read the question (where we have to change mobile's IP to that of your PC and vice versa) wrong, I had only changed the mobile phone's IP to that of the computer and left the computer with the same adress.

After asking my teammates if they were facing the same issue I realized I didn't read the question properly. 



### Results
- Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.
Zijn de adressen hetzelfde of niet? Leg uit waarom.

They are the same because they are connected to the same router, but you cannot have 2 devices with the same external IP adress (in different households). Unless your interprovider uses ipv4 and didn't upgrade/uses ipv6. 

- Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.
Zijn de adressen hetzelfde of niet? Leg uit waarom.

They are not the same, because each device connected to your **L**ocal **A**rea **N**etwork has a unique private IP address. These devices are connected to your router, so they would have the same public adress (in this case they are connected to the same router).

- Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan? 

So after manually configuring the ip adress page where we put in my PC's IP adress, the "connected to wifi" symbol at the top right dissappeared immediately. But on the wifi page it will show you as connected to the router. You just don't have internet access. This is assuming you read the question wrong and only change your Phone's adress to that of your computer only.

We have to change their respective IP's so that the computer would have the mobile's old IP and vice versa. After doing this, simply reboot your network and the devices will have access to the internet again. 

- Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?

I receive a network error. 
