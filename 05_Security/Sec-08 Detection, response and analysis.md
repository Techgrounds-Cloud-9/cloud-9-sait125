# Detection, response and analysis
[Give a short summary of the subject matter.]

## Key terminology
**IDS**:

**IPS**:

**Hack response** 

**System hardening**:

**Disaster recovery options**:

## Exercise

- A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
- An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?

### Sources
https://www.varonis.com/blog/ids-vs-ips#ids-types

https://www.druva.com/blog/understanding-rpo-and-rto/#:~:text=Recovery%20Point%20Objective%20(RPO)%20describes,allowable%20threshold%20or%20%E2%80%9Ctolerance.%E2%80%9D


### Results
- Since we have no time given for the last detection the rpo is up to 24h (assuming the company creates a backup every 24h).

- It takes 8 minutes to recover all data. So the downtime is also 8 minutes. 