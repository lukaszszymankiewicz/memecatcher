## memecatcher

To see site in full glory, please visit:

https://memecatcher.herokuapp.com/

WARNING: site is unreachable because heroku closed free tier! Implementation of new version in progres.

Script for scrapping memes from various sites wrapped in flask web-app.

No ads, no buttons, no additional links, no stupid headers taking
1/3 of screen, no logging, no comments - only pure fun.

## How it works?

Implementation is naive.
When app is asked to generate page number *2* of memes, chosen sites is 
scrapped from page *2* of its content, and then merged together on one screen.
Script is build using BeautifulSoup, request and flask packages.

## Disclaimer

This code is for personal and educational use only (and made purely for fun!),
I do not recommend to use it in ANY other way!

Please remember that most of these memes are owned by scrapped sites.

## Developing

To start developing, please create new virtual enviroment
and install requirements:

```
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

Run following command to start app:

```
python run.py
```

Visit localhost:5000 in your browser to see web-app
