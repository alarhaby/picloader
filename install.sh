termux-setup-storage
chmod +x *
apt update && apt upgrade -y
pkg update -y
pkg upgrade -y
pkg install git curl wget -y
pkg install python -y
pkg install python3 -y
pkg install zip unzip -y
pkg install figlet cmatrix -y
clear
python start.py
