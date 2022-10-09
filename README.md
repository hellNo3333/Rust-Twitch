# twitch-drop-bot

a fork of a python selenium-based twitch drop bot.

# required libraries

you need selenium to use this script.
paste `py -m pip install selenium` in a cmd window (obviously you need to have [python](https://www.python.org/) installed too.)

# driver

chromedriver is required to use this script. although it can be easily changed to use Firefox or MS Edge instead of chrome, its cross-platform nature and ability to handle memory leaks more efficiently proves beneficial.

download here: https://chromedriver.chromium.org/

you must make sure that you have chrome installed and that the chromedriver version matches with your chrome installation.
create the `driver` directory and drop the chromedriver executable there.

# memory leaks

this script can be run in low memory environments (e.g. ubuntu virtual private server running xfce on 2gb of memory) but webdriver memory leaks will eventually crash your program. in my experience, chrome seems to handle memory leaks more efficiently than firefox, but will still crash after hours of usage. because of that, you may want to set the `anti_leak` variable in `API.py` to `True`. (this basically reopens the webdriver every 10 minutes)

# cookies

you must load your twitch cookies correctly. the original tutorial for the master branch seems to be good enough for this matter: https://www.youtube.com/watch?v=CQzE8ff-USo (0:00 - 1:45)

# username

you must update your username on line 50 of `API.py`. please make sure it is all lowercase

# minutes to watch

at the time of writing this readme, rust drops require 3 hours of watchtime per streamer. this value can be updated on line 23 of `API.py`

# game to watch

this script can be repurposed. you can change the name of the game on line 32 of `API.py`. please make sure it is all lowercase

# streamers.txt

this implementation uses a txt file to load in streamer data.
format example

```
streamer1 55.0
streamer2 180.0
streamer3 170.0
streamer4 21.0
streamer5 170.0
streamer6 44.0
```

replace the names (streamer1, streamer2, and so on) with the names of the streamers you want to watch. the numbers (can be float or int) are equivalent to minutes watched. 

you must create the streamers.txt file accordingly. it will update itself every 10 minutes.

# headlessness

by default, this script runs in headless mode, meaning that no visible browser window will be created. this might be counter-productive for debugging purposes: in order to disable it, comment line 9 in `main.py` and line 11 in `API.py`.

update: as of 2022/09/09, due to twitch detection updates, this script only works in non headless mode.

# desktop environments

as of 2022/08/11, this script performs as expected on servers without a desktop environment. please make sure to install chrome (or whatever other browser you choose to use) and remember to match versions with the driver.

# run

`py main.py`
