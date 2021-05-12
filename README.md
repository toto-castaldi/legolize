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

### Greetings

[Lego Colors from Rebrickable](https://rebrickable.com/downloads/)