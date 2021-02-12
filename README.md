# Bingus Rich Presence
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A small Python program to show off your love for Bingus, and invite people to "The House of Bingus" discord.

## Installation
### Perquisites
* Make sure Discord is installed on the system and is running.


* Download and install the latest version of Python.
    * [Windows downloads](https://www.python.org/downloads/windows/)
    * On Linux, use your package manager. Many distros already come with Python pre-installed.
    

* Install the required modules
    * Windows
      * Open the start menu, type `cmd`, and hit enter. Then input `pip install pypresence`, and hit enter again.
    * Linux
      * Open your terminal, then run `pip install pypresence`, use `sudo` if needed.
   
 
* Create a developer application
    * Go to the Discord developer portal [here](https://discord.com/developers/).
    * Create a new application, name it Bingus.
    * Click Rich Presence -> Art assets, then upload the image you'd like to show in the RP.
        * The image may take about 20 minutes to actually show up.
    
### Installation
* Get the repository
    * Download it as a .zip file. then extract it.
    * Clone it using the `git` CLI.
    
## Usage
* Change directory into the one containing the repository:
    * `cd /path/to/bingus-richpresence-master`
* Copy your Client ID and Image Key from your application in the discord dev portal.
    * The client ID is visible on the main page, but for the Image Key go to Rich Presence -> Art assets.
    
* Run the code
    * In your command prompt or terminal, type `python main.py CLIENT-ID-HERE IMAGE-KEY-HERE`.
        * A completed command would look like `python main.py 80934327152361522 upload_2021_04_20`.
    
Done! If everything was successful, once someone looks at your status, it will appear like this!
Keep the terminal open, or run it as a daemon.

<img src="https://i.imgur.com/tEvL4u1.png" width="200">

## Need support/want to suggest something?
Feel free to do so! Send me a friend request on discord, `Gustav#6035`, and I'll try to answer as best I can.