# Concentrate.py
A simple Python script to block all distracting websites and also Telegram. Currently only supports `MacOS`

## To add your own websites to block: 
- Simply modify the `websites` array within the `concentrate.py` script by adding the websites you want to block. 

### To run
- Install [python3]([https://markdownlivepreview.com/](https://www.python.org/downloads/macos/)).
- Run using `sudo` by doing `sudo python3 concentrate.py` in the directory where the file is located.

### To run from anywhere
- Move the script to `/usr/local/bin`
- Make it executable by running `chmod +x /usr/local/bin/concentrate.py`
- Run using `sudo concentrate.py` from anywhere :) 


### Plans for the future: 
- Add a pomodoro timer, and do not allow to disable the script until the pomodoro finishes
  

# In plans: 
- Make it an application that can be pinned in the list in MacOs
- Super-focused mode - Blocks **ALL** websites - except those that are in the list.

Making it hard to disable the blocking: 
- Hold the disable button for 60 seconds to disable
- 5 minutes after disabling is pressed - the blocking is still in effect, and there is a button to "Disable the disabling" and return to blocking the websites. 
