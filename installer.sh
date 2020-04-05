sudo apt update
sudo apt upgrade
# Important utilities
sudo apt install gparted firefox okular libreoffice virtualbox

# DBMS
sudo apt install sqlite3

sudo apt install postgresql-10 psql pgadmin3

sudo apt install mongodb mongodb-clients mongo-tools
wget https://downloads.mongodb.com/compass/mongodb-compass_1.20.5_amd64.deb
sudo dpkg -i mongodb-compass_1.15.1_amd64.deb

# Latex installation
sudo apt install texlive-full

# Python installation starts below
sudo apt install python3.8
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.8 get-pip.py
pip install -U pip #Upgrade after install
python3.8 installations.py

# C/C++ Installation
sudo apt install build-essentials
sudo apt install libopencv-dev libopenmpi-dev libopencv-ml-dev

# Rust installation

sudo apt install cargo
