# This script shoud take care of all the configuration needed for the EC2 instance
SCRIPT_DIR=$(pwd)

sudo yum update -y
sudo yum install -y git
cd ~
git clone https://github.com/luizzitol/habits.git


# Docker stuff
sudo yum install -y docker
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -a -G docker ec2-user

sudo yum install libxcrypt-compat
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

sudo cp ./docker-compose.service /etc/systemd/system/docker-compose.service
sudo systemctl daemon-reload
sudo systemctl enable docker-compose
sudo systemctl start docker-compose