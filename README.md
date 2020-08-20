<h1 align="center">Discord RPC</h1>
<h5 align="center"> Readme is still updating please wait 1-2 days</h5>
<h5 align="center">Discord RPC is a library for interfacing your game with a locally running Discord desktop client</h5>
<img align="right" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/intro.gif' width="150">

### Status:
<a href="https://img.shields.io/youtube/views/udY540zICDY?style=social"><img src="https://img.shields.io/youtube/views/udY540zICDY?style=social" alt="Stars Badge"/></a>
<a href="https://github.com/niveshbirangal/discord-rpc/stargazers"><img src="https://img.shields.io/github/stars/niveshbirangal/discord-rpc" alt="Stars Badge"/></a>
<a href="https://github.com/niveshbirangal/discord-rpc/network/members"><img src="https://img.shields.io/github/forks/niveshbirangal/discord-rpc" alt="Forks Badge"/></a>
<a href="https://github.com/niveshbirangal/discord-rpc/issues"><img src="https://img.shields.io/github/issues/niveshbirangal/discord-rpc" alt="Issues Badge"/></a>
### Requirements:
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
### Setup:
clone this to your local device
```bash
git clone git@github.com:niveshbirangal/discord-rpc.git
```
Go to the developer portal and create an application
```bash
https://discord.com/developers/applications
```
<img align="center" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/createapp.gif'>
<br><br />
Add assets(image) to your application
<br><br>
<img align="center" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/selectimage.png'>
<br><br />
Select images and clear all fields except PARTY ID and join secret
<br><br>
<img align="center" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/fileds.png'>
<br><br />
Now go to example.py, put your client id, and change the activity code according to your best fit

```bash
 activity = {
            "state": "Adobe",  # anything you like
            "details": "Editing",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Adobe",  # anything you like
                "small_image": "adobe",  # must match the image key
                "large_text": "Illustrator",  # anything you like
                "large_image": "illustrator"  # must match the image key
            }
        }
```
Make sure your desktop app is running and then run the example.py
```bash
python3 example.py
```
<img align="center" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/activity.png'>



