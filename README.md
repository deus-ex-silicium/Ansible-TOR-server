# Ansible playbook / roles for setting up a TOR server
 - **setup_ufw** role installs and configures Uncomplicated Firewall
 - **tor_apache** role installs and configures Apache server instance
 - **tor_conn** role installs tor and connects Apache server to Tor network
 - check **vars.yaml** to customize role configuration
 - after running playbook server hostname is in **/var/lib/tor/onion_service/hostname**
---
### Useful commands
```ansible all -m ping -u <user> -i <vps-ip>,```
- pings vps server without the need to set up inventory

```ansible-playbook main.yaml --private-key <path> -u <user> -b -i <vps-ip>,```
- requires that main.yaml has hosts: all (be carefull if you have inventory set up)
- key needs proper perms ```chmod 0400 key.pem```
- (b)ecome using sudo by default for all tasks
---
[Based on tutorial from niebezpiecznik.pl](https://niebezpiecznik.pl/post/jak-uruchomic-wlasny-serwer-www-w-sieci-tor/)
