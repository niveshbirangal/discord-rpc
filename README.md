<h1 align="center">Discord RPC</h1>
<h5 align="center">"Discord RPC is a library for interfacing your game with a locally running Discord desktop client"</h5>
<!--<img align="right" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/intro.gif' width="150">-->

### Status:
<a href="https://img.shields.io/youtube/views/udY540zICDY?style=social"><img src="https://img.shields.io/youtube/views/udY540zICDY?style=social" alt="Stars Badge"/></a>
<a href="https://github.com/niveshbirangal/discord-rpc/stargazers"><img src="https://img.shields.io/github/stars/niveshbirangal/discord-rpc" alt="Stars Badge"/></a>
<a href="https://github.com/niveshbirangal/discord-rpc/network/members"><img src="https://img.shields.io/github/forks/niveshbirangal/discord-rpc" alt="Forks Badge"/></a>
<a href="https://github.com/niveshbirangal/discord-rpc/issues"><img src="https://img.shields.io/github/issues/niveshbirangal/discord-rpc" alt="Issues Badge"/></a>
### Requirements:
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)<br>3.0 and above
### Setup:
clone this to your local device
```bash
git clone https://github.com/niveshbirangal/discord-rpc.git
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
Select images and clear all fields except <code>PARTY ID</code> and <code>JOIN SECRET</code>
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

<!-- ROADMAP -->
## Roadmap
See the [open issues](https://github.com/niveshbirangal/discord-rpc/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Connect with me:
[<img align="left" alt="niveshb.com" width="32px" src="https://raw.githubusercontent.com/niveshbirangal/niveshbirangal/master/source/website.svg"/>][website]
[<img align="left" alt="niveshbirangal | LinkedIn" width="32px" src="https://raw.githubusercontent.com/niveshbirangal/niveshbirangal/master/source/linkedin.svg"/>][linkedin]
[<img align="left" alt="niveshbirangal | Instagram" width="32px" src="https://raw.githubusercontent.com/niveshbirangal/niveshbirangal/master/source/instagram.svg"/>][instagram]
[<img align="left" alt="niveshbirangal | YouTube" width="32px" src="https://raw.githubusercontent.com/niveshbirangal/niveshbirangal/master/source/youtube.svg"/>][youtube]



[website]: https://niveshb.com
[youtube]: https://www.youtube.com/channel/UCpwUP_HiOyG_GHluWpQK59g?view_as=subscriber
[instagram]: https://instagram.com/niveshbirangal
[linkedin]: https://linkedin.com/in/niveshbirangal
