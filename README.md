# fastapi+mariadb

## setup
```
sudo apt update
sudo apt install mariadb-server mariadb-client -y
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo mysql_secure_installation
# do config
# ...

# check 
mysql -u root -p
```