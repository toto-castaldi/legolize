LEGOLIZE
========

[![buddy pipeline](https://app.buddy.works/skillbill-bw/legolize/pipelines/pipeline/326415/badge.svg?token=107d3bbbb60ecabcdb08e0c4f842888977cc5d7b269e84936f8b8074747daf78 "buddy pipeline")](https://app.buddy.works/skillbill-bw/legolize/pipelines/pipeline/326415)

# WHAT ID DOES

[demo](http://legolize.skillbill.net)

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
DEBUG=True UPLOAD_FOLDER=`pwd`/UPLOAD_FOLDER HOST=127.0.0.1 LOG_LEVEL=DEBUG python src/server.py
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

## HTTPS

```
apt-get update
apt-get install nginx
snap install --classic certbot 
certbot --nginx 
vi /etc/nginx/sites-enabled/default 
#HTTPS CONF
nginx -t && nginx -s reload
```

### HTTPS CONF

```
location / {
    proxy_pass http://127.0.0.1:8080;
    add_header Cache-Control 'must-revalidate, proxy-revalidate, max-age=0';
}

location /api {
    rewrite ^/api/(.*)$ /$1 break;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://127.0.0.1:5000;
}

location /ws {
    rewrite ^/ws/(.*)$ /$1 break;
    proxy_pass http://127.0.0.1:5000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}

```

### Greetings

[Lego Colors from Rebrickable](https://rebrickable.com/downloads/)

[Fork me on Github](https://github.com/simonwhitaker/github-fork-ribbon-css)