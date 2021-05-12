LEGOLIZE
========

# WHAT ID DOES

![source](byke-input.jpeg)
![dest](byke-output.png?ver=2)


# DEV

## Node

```
node --version 
v14.15.1
npm --version
7.5.4
```

## Python 

Developed with python version 3.8.7

### Fe

```
cd fe
npm install
npm run serve
```

### Api

```
cd application
pip install -r requirements.txt
UPLOAD_FOLDER=`pwd`/UPLOAD_FOLDER HOST=127.0.0.1 LOG_LEVEL=DEBUG python src/server.py
```

### Engine

```
cd application
pip install -r requirements.txt
UPLOAD_FOLDER=`pwd`/UPLOAD_FOLDER LOG_LEVEL=DEBUG python src/engine.py
```


# CLOUD SERVER

## INSTALLATION

The server is a Linux Ubuntu 20.04 (LTS) x64

```shell
apt-get update
apt upgrade
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io
apt install curl
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

### Greetings

[Lego Colors from Rebrickable](https://rebrickable.com/downloads/)