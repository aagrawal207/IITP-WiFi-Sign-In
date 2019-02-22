A very simple script to sign-in to the IIT Patna WiFi. 

The script takes around ~0.7s if already signed-in and around ~5s if not signed-in.

**Caution: The file contains your password in plain text.**

### Run

`python3 sign-in.py`

**ProTip: If you use zsh or some other shell which support aliases then you can put `alias go='python3 ~/sign-in.py'` or something similar in your `~/.zshrc` file and just run `go` in your terminal when you want to sign-in.**

### Requirements

1. Python3

1. Selenium (Python Library)

1. wireless (Python Library)

1. requests (Python Library)

1. Chromedriver for Chrome or Geckodriver for Firefox

### Install Selenium

`pip3 install selenium`

### Install wireless

`pip3 install wireless`

### Install requests

`pip3 install requests`

### Install Chromedriver using brew

Run `brew info chromedriver` and follow steps that it shows or download the chromedriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in /usr/local/bin/ directory.

If you are using Windows then the method to install chromedriver might be different, just google it or something.

If you use Firefox or some other browser then google for it specifically.
