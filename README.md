A very simple script to sign-in to the IIT Patna WiFi. 

**Caution: The file contains your password in plain text.**

**ProTip: If you use zsh or some other shell which support alias then you can put `alias go='python3 ~/sign-in.py'` or something similar and just run `go` in your terminal when you want to sign-in.**

### Run

`python sign-in.py` or `python3 sign-in.py`

### Requirements

1. Python3

1. Selenium

1. Chromedriver for Chrome or Geckodriver for Firefox

### Install Selenium

`pip install selenium` or `pip3 install selenium`

### Install Chromedriver using brew

Run `brew info chromedriver` and follow steps that it shows or download the chromedriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in /usr/local/bin/ directory.

If you are using Windows then the method to install chromedriver might be different, just google it or something.

If you use Firefox or some other browser then google for it specifically.